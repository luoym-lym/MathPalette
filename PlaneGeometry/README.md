# PlaneGeometry锛氬钩闈㈠嚑浣?

鏈垎鏀彁渚涘钩闈㈠嚑浣曢噸缁樺崗璁€佹満鍣ㄦ牱寮忛厤缃笌鍏叡缁樺浘鍣ㄣ€傚畠涓?Analytics 鐨勫嚱鏁板浘娴佺▼鍒嗗埆缁存姢銆?

Protocol 1.2.0: diagrams are centered, occupy about 86% of the 768x768 canvas on the long side, and retain at least 5% margins. Vertex labels are 18 pt; values and other text are 16 pt; strokes remain 1 pt. Fitted square viewports preserve geometry proportions. Plane01-Plane40 were originally redrawn; Plane03 was later deleted at the user request. Plane01 approved edits remain in effect. See the [layout comparison](../imports/mathverse_vision_dominant/layout_upgrade_20261010/layout_review.html) and [layout validation](../imports/mathverse_vision_dominant/layout_upgrade_20261010/validation.json).

鏁板瓧銆佸瓧姣嶅拰缂栧彿瑙掓爣鍧囬厤涓€鏉¤寮э紝鍚屼竴涓嚑浣曡鐨勫涓爣璇嗗叡鐢ㄤ竴鏉″姬銆傛棤瑙掓爣鐨勭洿瑙掍繚鐣欐柟妗嗭紱娓叉煋鍣ㄤ細鎷掔粷婕忕粦銆侀敊缁戝拰鍚岃閲嶅寮с€?

姝ゅ墠 1.1.0 杩佺Щ琛ュ厖 26 鏉¤寮э紝40 涓鏍囧搴?39 涓嚑浣曡锛涘彟淇濈暀涓や釜鏃犳爣绛剧殑瑙掑钩鍒嗗叧绯诲崟寮с€傚綋鏃?25 棰樺儚绱犲彂鐢熷彉鍖栵紝鍘嗗彶妫€鏌ヨ [瑙掑姬杩佺Щ璁板綍](dataset_generator/angle_arc_review/validation.json)锛涘悓鐩綍鐨?`review_01.png`锝瀈review_10.png` 淇濈暀褰撴椂鐨勫鐓у浘銆傝寮ц縼绉诲墠鍦烘櫙鍦?`archive/angle_arcs_1_1_0/`锛屾湰娆℃瀯鍥捐皟鏁村墠鐨勫畬鏁存枃浠跺湪 `imports/mathverse_vision_dominant/layout_upgrade_20261010/before/`銆?

- [REDRAW_PROTOCOL.md](REDRAW_PROTOCOL.md)锛氬埗浣滃拰楠屾敹瑙勫垯銆?
- [dataset_generator/protocol.json](dataset_generator/protocol.json)锛氱敾甯冦€佺嚎瀹姐€佸瓧浣撱€佹爣璁颁笌鏁板€煎宸€?
- [dataset_generator/common_renderer.py](dataset_generator/common_renderer.py)锛氫粠鍐荤粨鍦烘櫙鐢熸垚 PNG / SVG锛屾鏌ユ敮鎸佺殑鍑犱綍绾︽潫鍜屾爣娉ㄣ€?
- [dataset_generator/test_renderer.py](dataset_generator/test_renderer.py)锛氫娇鐢ㄧ嫭绔嬫瀯閫犵殑鍑犱綍鍦烘櫙鏍稿閲嶇粯鍣ㄣ€?

鍦?MathPalette 鐩綍鎵ц锛?

```powershell
python -B PlaneGeometry/dataset_generator/test_renderer.py
```

The renderer provides `draw(scene_path, output_path=None)` for frozen scenes. It now has 39 active MathVerse candidates (Plane01-Plane40, excluding deleted Plane03). User-approved items enter `dataset.jsonl`; the rest stay in `pending_dataset.jsonl`. Source images are in `originals/`, redraws in `image/`, and scenes, per-question classes, and reports in `dataset_generator/`. See the [question review progress](../imports/mathverse_vision_dominant/geometry_review_progress.json). Agent review is separate from user approval; editing an approved drawing requires a fresh review.

鍦ㄩ」鐩牴鐩綍鎵ц `python -B dataset_tools/geometry_dataset.py PlaneGeometry Plane01` 鍙噸鏂扮敓鎴愭寚瀹氶鐩苟鏍稿纭畾鎬с€傛瘡棰樼被涔熸彁渚?`draw(output_path=None)`銆傛潵婧愰骞插拰 GT 鍘熸牱淇濈暀锛涚瓟妗堝啿绐併€佺己灏戞潯浠舵垨瑙ｉ噴姝т箟鍙﹀瓨 `answer_verification`锛屼笉鍥犵枒鐐瑰垹棰樸€傚叏鎵硅 [鍘熷浘 / 閲嶇粯瀵圭収椤礭(../imports/mathverse_vision_dominant/redraw_review.html) 涓?[鏍搁獙鐤戠偣](../imports/mathverse_vision_dominant/issues.md)銆?

Base 鎿嶄綔銆佷汉宸?Special 宸ヤ綔鍙板拰璇勬祴鎺ュ叆灏氭湭鍒跺畾銆傜幇鏈?Analytics 宸ヤ綔鍙板彧鏈嶅姟 Ana 绯诲垪銆?

