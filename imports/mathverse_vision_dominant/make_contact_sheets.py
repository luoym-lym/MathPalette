"""Build source/redraw comparison sheets without modifying drawing assets."""
from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont, ImageOps

IMPORT = Path(__file__).resolve().parent
ROOT = IMPORT.parents[1]
sources = {r['source_key']: r for r in json.loads((IMPORT/'source_manifest.json').read_text(encoding='utf-8'))}
assignments = json.loads((IMPORT/'assignments.json').read_text(encoding='utf-8'))
font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 21)
(IMPORT/'qa').mkdir(exist_ok=True)
for start in range(0, len(assignments), 8):
    sheet = Image.new('RGB', (1600, 2000), 'white')
    draw = ImageDraw.Draw(sheet)
    for i, row in enumerate(assignments[start:start+8]):
        source = sources[row['source_key']]
        x, y = (i % 2)*800, (i//2)*500
        answer = str(source['source_answer'])
        draw.text((x+10, y+5), f"{row['id']} / {row['source_key']} GT: {answer[:45]}", font=font, fill='black')
        draw.text((x+10,y+32), 'SOURCE                              REDRAW', font=font, fill='black')
        redraw = ROOT/row['branch']/('fine_grained_dataset' if row['branch']=='Analytics' else '')/'image'/f"{row['id']}.png"
        if not redraw.exists():
            redraw = IMPORT/'results'/'analytics'/f"{row['id']}.png"
        for j, path in enumerate((IMPORT/source['source_image'], redraw)):
            if path.exists():
                with Image.open(path) as im:
                    im = ImageOps.contain(im.convert('RGB'), (390,430))
                    sheet.paste(im, (x+j*400+(400-im.width)//2, y+65+(430-im.height)//2))
    target = IMPORT/'qa'/f'overview_{start//8+1:02d}.png'
    sheet.save(target)
    print(target.name)
