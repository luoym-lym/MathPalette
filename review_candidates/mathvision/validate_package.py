"""Read-only validation and isolated pixel reproduction of MathVision candidates."""
from pathlib import Path
import argparse
import concurrent.futures
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import time

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
sys.path.insert(0, str(ROOT))
from dataset_tools.answer_schema import validate_answer
from dataset_tools.catalog import validate_formal_row


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec); spec.loader.exec_module(value)
    return value


def pixel_equal(reference, output):
    from PIL import Image
    with Image.open(reference) as a, Image.open(output) as b:
        return a.size == b.size == (768, 768) and a.convert('RGBA').tobytes() == b.convert('RGBA').tobytes()


def validate_one(row, formal=False, twice=False):
    started = time.perf_counter()
    result = {'id': row['id'], 'source_key': row['source_key'], 'branch': row['subject']}
    try:
        validate_answer(row)
        assert row['source_dataset'] == 'MathVision' and row['user_approved'] is False
        assert json.loads((ROOT / row['candidate_path']).read_text(encoding='utf-8')) == row
        reference = ROOT / row['image']
        runtime = module('_mathvision_validation_runtime', PACKAGE / 'shared/runtime.py')
        item = (ROOT / row['candidate_path']).parent
        with tempfile.TemporaryDirectory(prefix='mathvision-validate-') as temporary:
            temporary = Path(temporary)
            first = temporary / 'first.png'
            runtime.draw(item, PACKAGE / 'shared/native', first)
            result['candidate_pixels_equal'] = pixel_equal(reference, first)
            result['candidate_bytes_equal'] = reference.read_bytes() == first.read_bytes()
            if twice:
                second = temporary / 'second.png'
                runtime.draw(item, PACKAGE / 'shared/native', second)
                result['second_pixels_equal'] = pixel_equal(reference, second)
                result['twice_bytes_equal'] = first.read_bytes() == second.read_bytes()
            if formal:
                promotion = module('_mathvision_validation_promotion', PACKAGE / 'promotion.py')
                prefix = 'Solid' if row['subject'] == 'SolidGeometry' else 'Plane'
                formal_row, writes, notes = promotion.prepare(ROOT, row, prefix + '9999')
                staged = temporary / 'formal'
                for name, data in writes.items():
                    target = staged / name; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(data)
                validate_formal_row(staged, row['subject'], formal_row)
                output = temporary / 'formal.png'
                environment = os.environ.copy()
                environment.update(PYTHONDONTWRITEBYTECODE='1', MPLBACKEND='Agg', MPLCONFIGDIR=str(temporary / 'mpl'))
                process = subprocess.run([sys.executable, '-B', str(staged / row['subject'] / formal_row['script']), str(output)], cwd=staged,
                                         env=environment, capture_output=True, text=True, timeout=60)
                if process.returncode:
                    raise RuntimeError(process.stderr[-1800:])
                result['formal_pixels_equal'] = pixel_equal(reference, output)
                result['formal_bytes_equal'] = reference.read_bytes() == output.read_bytes()
        result['passed'] = all(v for k,v in result.items() if k.endswith('_equal'))
    except Exception as error:
        result.update(passed=False, error=f'{type(error).__name__}: {error}')
    result['seconds'] = round(time.perf_counter() - started, 3)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--formal', action='store_true')
    parser.add_argument('--twice', action='store_true')
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--ids', nargs='*')
    parser.add_argument('--output', type=Path, default=ROOT / '.runtime/mathvision_package_validation.json')
    args = parser.parse_args()
    rows = [json.loads(l) for l in (PACKAGE / 'index.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
    exclusions = json.loads((PACKAGE / 'excluded.json').read_text(encoding='utf-8'))
    assert len({r['id'] for r in rows}) == len(rows)
    assert not {r['source_key'] for r in rows} & {r['source_key'] for r in exclusions}
    if args.ids:
        rows = [r for r in rows if r['id'] in set(args.ids)]
        assert len(rows) == len(set(args.ids)), 'Some requested IDs are absent'
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(validate_one, row, args.formal, args.twice): row['id'] for row in rows}
        for future in concurrent.futures.as_completed(futures):
            result = future.result(); results.append(result)
            if not result['passed'] or len(results) % 25 == 0:
                print(json.dumps({'completed': len(results), 'total': len(rows), 'last': result}, ensure_ascii=False), flush=True)
    report = {'candidate_count': len(rows), 'excluded_count': len(exclusions), 'formal_preparation_tested': args.formal,
              'twice_tested': args.twice, 'passed': all(r['passed'] for r in results), 'results': sorted(results, key=lambda r:r['id'])}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k != 'results'}, ensure_ascii=False), flush=True)
    return 0 if report['passed'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
