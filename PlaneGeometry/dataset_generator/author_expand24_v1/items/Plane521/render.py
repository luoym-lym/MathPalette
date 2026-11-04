from pathlib import Path
import argparse, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    scene=json.loads(Path(__file__).with_name("scene.json").read_text(encoding="utf-8"))
    plt.rcParams.update({"font.family":"DejaVu Sans", "svg.fonttype":"path"})
    fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor="white")
    ax=fig.add_axes([.05,.05,.9,.9]); ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(scene["view"]["xlim"]); ax.set_ylim(scene["view"]["ylim"]); ax.set_autoscale_on(False)
    for obj in scene["objects"]:
        a,b=obj["points"]
        line,=ax.plot([a[0],b[0]],[a[1],b[1]],color="black",linewidth=1,solid_capstyle="round",antialiased=True)
        if obj["role"]=="cut": line.set_dashes([4,3])
    for label in scene["labels"]:
        ax.annotate(label["text"],xy=scene["points"][label["point"]],xytext=label["offset_pt"],textcoords="offset points",fontsize=18,fontstyle="italic",ha=label["ha"],va=label["va"],color="black")
    fig.savefig(args.output,dpi=100,facecolor="white")
    plt.close(fig)
if __name__=="__main__": main()
