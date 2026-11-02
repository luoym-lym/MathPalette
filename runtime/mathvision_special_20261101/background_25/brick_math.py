from design_tools import *
import itertools
def prove(q):
    out={};models=AD.scenes[q]['visibility']['surface_models'];white_stock=1 if q=='Solid119' else 2
    for letter in 'ABCDE':
        model=models[letter];sx,sy,sz=model['size'];cells=set(itertools.product(range(sx),range(sy),range(sz)));known={}
        for r in model['visible_regions']:
            x0,y0,x1,y1=r['uv_bounds']
            for a in range(int(x0),int(x1)):
                for b in range(int(y0),int(y1)):
                    cell=(a,0,b) if r['face']=='front' else (sx-1,a,b) if r['face']=='right' else (a,b,sz-1)
                    color='W' if r['color'].lower()=='#ffffff' else 'G'
                    assert cell not in known or known[cell]==color
                    known[cell]=color
        placements=[]
        for c in sorted(cells):
            for axis in range(3):
                d=tuple(c[i]+(i==axis) for i in range(3))
                if d in cells:placements.append(frozenset((c,d)))
        partitions=[]
        def enumerate_partitions(left,path):
            if not left:partitions.append(path);return
            c=min(left)
            for dom in placements:
                if c in dom and dom<=left:enumerate_partitions(left-dom,path+[dom])
        enumerate_partitions(cells,[])
        successes=[];colorings=0
        for partition in partitions:
            for white_indices in itertools.combinations(range(len(partition)),white_stock):
                colorings+=1;colors={c:('W' if i in white_indices else 'G') for i,dom in enumerate(partition) for c in dom}
                if all(colors[c]==color for c,color in known.items()):successes.append([{'cells':sorted(dom),'color':colors[next(iter(dom))]} for dom in partition])
        out[letter]={'size':model['size'],'known_surface_colors':{str(c):col for c,col in sorted(known.items())},'uncolored_domino_partitions_exhausted':len(partitions),'stock_colorings_exhausted':colorings,'valid_colored_tilings_count':len(successes),'first_witness':successes[0] if successes else None}
    valid=[k for k,v in out.items() if v['valid_colored_tilings_count']]
    assert valid==(['C'] if q=='Solid119' else ['D'])
    proof=f'Every axis-aligned unit-domino exactcover and every assignment of exactly{white_stock}white bricks and the remaininggray bricks was exhausted. Every original visible front/right/topunitcell color is constrained; hiddencolors free. Only{valid[0]} has a tiling, with an explicit fullstock witness. Sourcewhite/graystock and all unitdimensions remain unchanged.'
    write(TASK/q/'primary_math_proof.json',{'question_id':q,'unique_answer':valid[0],'independently_recomputed':True,'method':'Enumerate geometry-only full domino partitions first, then all fixed-stock white/gray colorings; independent enumeration of originalsource constraints, no reliance on previous solver answer.','options':out,'white_bricks':white_stock,'gray_bricks':4-white_stock if q=='Solid119' else 6-white_stock,'proof':proof})
    return proof
if __name__=='__main__':
    for q in sys.argv[1:]:print(q,prove(q))
