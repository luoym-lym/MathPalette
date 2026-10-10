# MathVerse 重绘题核验疑点

MathVerse source has 107 questions; 106 retained and 1 deleted. 45 retained candidates have QA concerns.

原图、重绘图、完整题干和逐题推导可在 [对照页](redraw_review.html) 查看。`needs_review` 不表示已经证明题目错误。

## Plane04（s244）

- 来源答案：D
- 核验候选：95 degrees
- 疑点：按圆周角关系推出 ∠B=95°；来源选项和 GT 给的是 100°。
- 推导：In cyclic order A-E-D-C-B, angle AED=115 gives arc AED=130. Angle CAD=30 gives arc CD=60. Angle ABC intercepts arc AEDC=190, so B=95 degrees. This conflicts with the source GT D/100.

## Plane08（s449）

- 来源答案：C
- 核验候选：B
- 疑点：中心角 AOB=50°，相应圆周角 ACB=25°（B）；来源 GT 为 100°（C）。
- 推导：The source marks central angle AOB=50 degrees. Independently, the requested inscribed angle is half the intercepted arc, 25 degrees (choice B). Source GT C/100 conflicts.

## Plane09（s454）

- 来源答案：B
- 核验候选：C
- 疑点：半圆内由 ∠BAC=30°、弧 AD=DC 推出 ∠DAC=30°（C）；来源 GT 为45°（B）。
- 推导：The upper semicircle is 180 degrees. Angle BAC=30 gives arc BC=60. Equal arcs AD and DC are each 60, so angle DAC=30 degrees, choice C; this differs from source GT B/45.

## Plane11（s584）

- 来源答案：B
- 核验候选：6 sqrt(2) cm (not among choices)
- 疑点：按图中底面半径3与120°扇形推得圆锥高6√2 cm，不在选项中；需核查原尺寸线含义及遗漏题干。
- 推导：The sector angle is 120 degrees and the cone base radius is marked 3. The sector arc length equals the cone base circumference: (1/3)(2 pi l)=2 pi(3), so slant height l=9. Then h=sqrt(9^2-3^2)=6 sqrt(2) cm, absent from the choices. The 3 label is preserved on the cone radius from center K to the right rim.

## Plane12（s704）

- 来源答案：A
- 核验候选：12 m
- 疑点：两段水平距离3和15、参照高2推得楼高12 m；来源 GT 为10 m。
- 推导：The sightline passes through a 2 m reference at A, with CA=3 and AB=15. Similar triangles give building height 2*(18/3)=12 m, differing from source GT 10 m.

## Plane13（s719）

- 来源答案：D
- 核验候选：4/3 m
- 疑点：按图示6 m与4 m距离比例，击球高为4/3 m；来源 GT 为8/15 m。
- 推导：The 0.8 m reference is 6 m from the start and h is 4 m farther along the same line. Similar triangles give h=0.8*(10/6)=4/3 m, choice B, differing from source GT 8/15.

## Plane14（s724）

- 来源答案：B
- 核验候选：D
- 疑点：由两个等腰三角形的30°和40°推出中心角 BOC=140°；来源 GT 为70°。
- 推导：Radii OA=OB make angle AOB=120 from base angles 30. Radii OA=OC make angle AOC=100 from base angles 40. Therefore BOC=140 degrees, choice D, differing from source GT B/70.

## Plane15（s874）

- 来源答案：C
- 核验候选：A
- 疑点：题目直接询问图中已标的中心角 AOB=40°，来源 GT 却为80°。
- 推导：The marked central angle AOB is 40 degrees, the requested angle and choice A. This differs from source GT C/80.

## Plane16（s964）

- 来源答案：C
- 核验候选：现有条件未能确定
- 疑点：题干在切线条件后结束，没有求解目标或选项，无法验证来源答案 C。
- 推导：The source question ends before stating the requested quantity or choices. Redraw the stated tangent configuration only; answer is unresolved.

## Plane20（s1379）

- 来源答案：C
- 核验候选：C (67 degrees)
- 疑点：半径13、弦长24对应中心角约134.76°，与图示134°有舍入差；目标弧约67°仍对应选项 C。
- 推导：OB is perpendicular to chord CD at X, so CX=12. In right triangle OCX, OC=13 and CX=12, so angle COX=arcsin(12/13), about 67 degrees. Since OX lies on OB, arc CB is about 67 degrees (choice C).

## Plane21（s1644）

- 来源答案：2191.7 metres
- 核验候选：现有条件未能确定
- 疑点：已知返程直线916 m及一处方位角，但缺少另一距离/角度，不能唯一求总路程。
- 推导：The text gives BP=916 m and the diagram gives a 145 degree bearing from north at S to SP. This fixes the direction of SP (and angle P), but does not fix S or BS; infinitely many triangles satisfy those givens with different BS+SP. Retain source GT 2191.7 m for review without calling it a proven source error.

## Plane24（s1754）

- 来源答案：4.4 m
- 核验候选：现有条件未能确定
- 疑点：只有两根杆高8/25 m及一处57°标注，缺少独立条件来确定两根杆的水平间距。
- 推导：The source has heights 8 m and 25 m, with 57 degrees marked from the ground baseline to the upper sightline to Pole 2. No angle or distance is given for the sightline to Pole 1, so AB and BC cannot be determined uniquely. Retain GT 4.4 m for review; no GT conflict is asserted.

## Plane25（s1774）

- 来源答案：93.31
- 核验候选：现有条件未能确定
- 疑点：由左边58与57°计算的高约48.64，右边72与31°计算的高约37.08，两组给定条件不相容。
- 推导：The source shows AB=58, BD=72, base angles 57 and 31 degrees, and an altitude at C. These lengths and angles are mutually inconsistent, so the intended geometry cannot be verified; the drawing preserves all source givens as visible annotations.

## Plane29（s1839）

- 来源答案：777
- 核验候选：768.77 GBP
- 疑点：按所标尺寸，周长约20.7703 m，费用约£768.77；来源 GT £777可能采用未说明的整米舍入。
- 推导：The shown perimeter is 1+sqrt(29)+2+sqrt(29)+7, about 20.7703 m. At GBP 37 per metre, cost is about GBP 768.77, differing from source GT 777.

## Plane32（s2054）

- 来源答案：Perimeter $=257.73 \mathrm{~m}$
- 核验候选：现有条件未能确定
- 疑点：扇形只标半径32.2 m，未给出可读角度/弧长，不能唯一计算周长。
- 推导：Radius 32.2 m is legible but the sector angle or arc measure is not. The perimeter cannot be uniquely computed.

## Plane34（s2099）

- 来源答案：$5=s$
- 核验候选：现有条件未能确定
- 疑点：题干称梯形，图示近似平行四边形且未标待求边 s；10与6两数不足以推出来源 s=5。
- 推导：Recreated the given parallelogram-like outline, side BC=10 cm, extended parallel side through D to E, and perpendicular EC=6 cm. Kept the source GT for review without assigning s to a vertex or asserting a derivation.

## Ana21（s2164）

- 来源答案：(2,-2)
- 核验候选：(2, 2)
- 疑点：矩形顶点的中点为 (2,2)，来源 GT 写成 (2,-2)。
- 推导：Diagonal midpoint: ((-6+10)/2,(5+(-1))/2)=(2,2); both diagonals share it.

## Ana33（s2404）

- 来源答案：domain: [-4, 0) and range: (-3, 1]
- 核验候选：domain (-3,1]; range [-4,0]
- 疑点：图中定义域为 (-3,1]、值域为 [-4,0]；来源答案混淆了两者及端点。
- 推导：Graph has open (-3,0), closed (1,-4), interior extrema (-2,-4),(0,0).

## Ana36（s2429）

- 来源答案：\[domain: [-6,-\frac{1}{6}] \cup[\frac{1}{6}, 6] and range: [-6,-\frac{1}{6}\right] \cup[\frac{1}{6}, 6]\]
- 核验候选：domain [-6,-1/6] U [1/6,6]; range [-6,-1/6] U [1/6,6]
- 疑点：数学区间与图相符，但来源答案的 LaTeX 括号不完整，需清理格式后再用于自动判分。
- 推导：y=1/x is restricted to the two shown closed branches; four marked endpoint coordinates are (-6,-1/6),(-1/6,-6),(1/6,6),(6,1/6). The red dashed auxiliary line is x=0.

## Ana38（s2449）

- 来源答案：\[\text { local maximum: }(-3,60) \text {, local minimum: }(3, -60)\]
- 核验候选：local maximum approximately (-3,54); local minimum approximately (3,-54)
- 疑点：原图极值约在 (-3,54)、(3,-54)，来源答案估计为 ±60；属于粗刻度读图的精度疑点。
- 推导：The source curve is exactly consistent with y=x^3-27x: derivative 3x^2-27=0 at x=?3, giving y(-3)=54 and y(3)=-54. The graph uses 20-unit vertical ticks, so sourceGT ?60 is a coarse visual estimate; retain it verbatim and flag estimate precision.

## Ana39（s2454）

- 来源答案：\[\text { Local minimum at }(-2,-2) \text {, decreasing on }(-3,-2) \text {, increasing on }(-2, \infty)\]
- 核验候选：local maximum approximately (-3,50); local minimum approximately (3,-50)
- 疑点：来源答案描述的极小值和单调区间与图中有限曲线不相符，疑似配错答案。
- 推导：Frozen piecewise cubic Hermite curve through source landmarks, domain [-8,7], with solid endpoints (-8,-225),(7,150) and horizontal tangents at (-3,50),(3,-50).

## Ana40（s2469）

- 来源答案：When x<=-3 $f(x) = -x-5$, when x>3, $f(x)=x+1$
- 核验候选：V-shaped graph with vertex (-3,-2), rays continue both directions
- 疑点：右支应从 x>-3 开始，来源答案却写 x>3，遗漏了一段定义域。
- 推导：The source graph is y=|x+3|-2; both visible arms carry continuation arrows.

## Ana41（s2509）

- 来源答案：(-1.8,10)
- 核验候选：No absolute maximum; the local maximum is approximately (-1.8,10).
- 疑点：题目问绝对最大值，但箭头表示三次曲线继续上升；来源答案给的是局部极大点。
- 推导：The graph has a local peak near (-1.8,10), then a local minimum, and the right tail continues upward with an arrow. Thus the function is unbounded above and has no absolute maximum.

## Ana43（s2614）

- 来源答案：(B)
- 核验候选：B; D is also a valid interpretation of the intersections
- 疑点：选项 B 和 D 都描述交点的正确含义，来源 GT 只列出 B，需核查单选/多选设定。
- 推导：At each intersection f(t)=g(t), and both heights are 10,000 m; labels f and g sit by the matching solid and dashed polylines.

## Ana47（s2689）

- 来源答案：\[{8}{5} \pi\]
- 核验候选：period 8pi/5
- 疑点：周期应为 8π/5，与图相符；来源答案把分数写为 {8}{5}π，可能影响公式解析或判分。
- 推导：Marked midline crossings are (3pi/5,8) descending and (7pi/5,8) ascending; opposite crossing directions imply half-period 4pi/5, hence period 8pi/5. Curve has midline 8 and amplitude 2.

## Ana50（s2779）

- 来源答案：-4.9
-4.9
- 核验候选：undetermined
- 疑点：题干没有列出需要计算的表达式；来源答案为重复两行 -4.9，无法核实求解目标。
- 推导：Question text has no expression list; the image alone does not specify what to evaluate.

## Ana52（s2789）

- 来源答案：C
- 核验候选：B: -5<=x<=4
- 疑点：图中右端点为 x=4，应选 B；来源 GT 选 C，对应 x=5。
- 推导：Closed graph endpoints have x=-5 and x=4.

## Ana58（s2899）

- 来源答案：$13 \%$
- 核验候选：approximately 13% forgotten each day
- 疑点：图缺少横轴数值标注，13% 可作曲线估读；重绘冻结的 0.87 衰减率参考了来源答案，不能作为独立精确证明。
- 推导：The question has no numerical day ticks. The black Lucy curve retains about 87% over the first daily interval; its relative loss is therefore approximately 13%. The frozen exponential model is GT-supported, but the low-resolution image itself only supports an estimate.

## Ana65（s3109）

- 来源答案：C
- 核验候选：C and F
- 疑点：题目要求多选，可读选项 C 和 F 均正确；来源 GT 仅 C，且选项 B、E 文本缺失。
- 推导：The displayed function is f(x)=-1.25 ln(1/x)=1.25 ln x. Its intersection with y=4 solves the equation in C and identifies the starting amount that remains for four hours in F (x=e^3.2?24.53 mg).

## Ana66（s3144）

- 来源答案：Bugs Bunny
- 核验候选：360 liters
- 疑点：初始水量为纵截距 360 升，来源答案却是 Bugs Bunny，明显与题目无关。
- 推导：The line has y-intercept 360 at t=0 and crosses at (5,0); complete axis titles Time (minutes) and Water (liters) are visible.

## Solid05（s3389）

- 来源答案：68.34
- 核验候选：68.34 degrees (using rounded AW=8.49 cm); exact dimensions give 68.35 degrees
- 疑点：使用精确长度得68.35°；若上一问先把 AW 舍入到8.49，则得来源68.34°，存在前序计算依赖。
- 推导：cos(theta)=AW/VA. With prior-part rounding: arccos(8.49/23)=68.34 degrees. Without intermediate rounding, arccos((12/sqrt(2))/23)=68.35 degrees. This is a rounding-dependence issue.

## Solid06（s3404）

- 来源答案：\[75.15 \mathrm{m}^2\]
- 核验候选：75.15 cm^2
- 疑点：图中长度单位均为cm，面积数值75.15对应cm²；来源答案写m²。
- 推导：The divider is triangle ACD. CD=7 cm and AC is a base diagonal sqrt(19^2+10^2)=sqrt(461); area=(1/2)*7*sqrt(461)=75.15 cm^2.

## Solid08（s3419）

- 来源答案：\[94.59 \mathrm{m}^2\]
- 核验候选：94.59 cm^2
- 疑点：图中长度单位均为cm，面积数值94.59对应cm²；来源答案写m²。
- 推导：Divider triangle ACD has CD=9 cm and AC=sqrt(19^2+9^2)=sqrt(442); area=(1/2)*9*sqrt(442)=94.59 cm^2.

## Solid09（s3424）

- 来源答案：14
- 核验候选：14.32 cm
- 疑点：按直线空间弦计算 L≈14.32 cm；来源14可能是取整，但题干未要求舍入。若理解为曲面路径则另有不同结果。
- 推导：The 3 cm mark is the radius. The depicted straight segment joins opposite sides, so L=sqrt(13^2+6^2)=14.32 cm.

## Solid10（s3449）

- 来源答案：Volume $=502.65 \mathrm{~cm}^{3}$
- 核验候选：2010.62 cm^3
- 疑点：图上8 cm从圆心到圆周，按半径计算体积2010.62 cm³；来源502.65相当于把8当直径。
- 推导：Preserved source radius8cm and length20cm; did not reinterpret as diameter.

## Solid12（s3514）

- 来源答案：\[338 \mathrm{cm}^2\]
- 核验候选：388 cm^2
- 疑点：梯形底面及纵深8推得表面积388 cm²，来源 GT 为338 cm²。
- 推导：Trapezoid area=(18+10)*3/2=42 cm^2 and perimeter=18+10+5+5=38 cm. Prism SA=2*42+38*8=388 cm^2. Raw GT 338 is an arithmetic error.

## Solid13（s3524）

- 来源答案：\[577.0 \mathrm{cm}^2\]
- 核验候选：576.6 cm^2
- 疑点：精确表面积576.648…取一位小数为576.6；来源577.0可能先将斜边舍入14.8再计算。
- 推导：Front trapezoid area=(10+3)*13/2=84.5 cm^2; slant side y=sqrt(218). Prism SA=2*84.5+10*(10+3+13+sqrt(218))=576.648... cm^2.

## Solid15（s3544）

- 来源答案：\[256.2 \mathrm{m}^2\]
- 核验候选：256.2 cm^2
- 疑点：数值256.2与计算相符，但图示单位cm、来源答案单位m²不相符。
- 推导：Square base side 10 cm and vertical height 6 cm. Face slant height sqrt(6^2+5^2)=sqrt(61). SA=100+4*(1/2*10*sqrt(61))=100+20*sqrt(61)=256.2 cm^2.

## Solid16（s3559）

- 来源答案：\[288.6 \mathrm{m}^2\]
- 核验候选：288.68 mm^2
- 疑点：应为288.68 mm²；来源288.6 m²同时存在单位和小数精度问题。
- 推导：For side 10 mm and perpendicular height 8 mm, base area is 100 mm^2 and each triangular face has slant height sqrt(8^2+5^2). Total=100+4*(1/2*10*sqrt(89))=288.679... mm^2, or 288.68 mm^2.

## Solid18（s3589）

- 来源答案：\[36\pi \mathrm{cm}^3\]
- 核验候选：4.5*pi cm^3
- 疑点：球A图上3看起来标的是直径，体积应4.5π；来源36π相当于把3作为半径，需核查尺寸含义。
- 推导：If A diameter is 3 cm, r=1.5 cm and V=(4/3)*pi*(1.5^3)=4.5*pi cm^3. Raw GT retained in answer.

## Solid19（s3599）

- 来源答案：100
- 核验候选：64:1
- 疑点：已标体积5760与90，比例直接为64:1；来源 GT 100与题面不符。
- 推导：The volume ratio is 5760/90=64. For similar cylinders, the linear scale factor is cube_root(64)=4, so the larger height is c=4*20=80 cm.

## Solid20（s3634）

- 来源答案：$1690cm^2$
- 核验候选：1690 cm^3
- 疑点：体积数值1690正确，单位应cm³；来源答案写cm²。
- 推导：Rectangular prism volume=13*13*10=1690 cm^3. Raw GT gives cm^2, a unit error.

## Solid21（s3639）

- 来源答案：$144cm^3$
- 核验候选：1728 cm^3
- 疑点：立方体边长12 cm，体积为1728 cm³；来源 GT 144 cm³误用了平方。
- 推导：All side lengths are 12 cm, so cube volume=12^3=1728 cm^3. Raw GT 144 is inconsistent.

## Plane36（s3824）

- 来源答案：23
- 核验候选：70/3
- 疑点：矩形精确面积为70/3≈23.333；来源 GT 23，但题干未说明取整。
- 推导：Triangle RST has base TS=PS-PT=3/5 PS and height equal to rectangle height h. Its area is (1/2)(3/5 PS)h=3/10 area(PQRS)=7, hence area(PQRS)=70/3. The 7 and PT=2/5 PS are formal question conditions, not labels in the source figure.

## Plane37（s3834）

- 来源答案：0
- 核验候选：5/8
- 疑点：阴影比例为5/8，来源 GT 为0，需核查答案编码或题目配对。
- 推导：The two unshaded triangles occupy 1/4 and 1/8 of the rectangle. The shaded fraction is 5/8, differing from source GT 0.
