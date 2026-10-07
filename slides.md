---
theme: none
title: 紙飛行機の翼幅と飛距離の関係
author: ''
info: false
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
fonts:
  provider: none
  sans: 'Arial, BIZ UDPGothic'
  mono: Consolas
transition: none
mdc: true
drawings:
  enabled: false
themeConfig:
  pageNumbers: true
layout: cover
bodyClass: paper-example paper-cover
affiliation: ［所属］
presenter: ［発表者名］
subtitle: 翼幅6・9・12 cmの3条件を比較
exportFilename: paper-airplane-example
coverImage: /media/cover-airplane.svg
coverImageAlt: 紙飛行機を上から見た図
---
紙飛行機の翼幅と<br>飛距離の関係

<!--
研究発表の構成を示す、表紙を含む11枚の例です。実験条件・寸法・測定値は完成見本用の架空の設定です。
所属と発表者名は差し替えてください。
構成・配置の参考：https://student.tsutawarudesign.com/powerpoint_slide/
各本文ページは、具体的な見出し・図表や短い説明・研究内容に即した締めの一文で構成しています。
-->
---
layout: split
section: 背景・目的
title: 翼幅を広げると、遠くまで飛ぶのか
bodyClass: paper-example paper-purpose
page: 1
---
<MediaBox src="/media/wing-shapes.svg" alt="翼幅が小さい紙飛行機と大きい紙飛行機の比較" />

::right::

<section class="paper-text-block">

## 仮説を立てた理由

翼を広げると、空気に<br>支えられやすいと考えた。

</section>

<section class="paper-text-block">

## 仮説

翼幅が広いほど、<br>平均飛距離が長くなる。

</section>

::takeaway::

3つの翼幅で**平均飛距離**を比較する

<!--
紙飛行機は、折り方も投げ方も変えられます。飛距離に関係しそうな条件は複数あるため、
今回は翼幅に絞って比べます。翼幅は上から見た左右の翼端間の幅です。
この導入図は形の違いを示すもので、寸法や性能は表していません。
ここで身近な題材から具体的な研究の問いにつなぎます。目安は40秒程度です。
-->

<!--
タイトルに研究の問いを置き、本文では仮説を立てた理由を示します。
「空気に支えられやすい」は、この例で実験前に考えた理由です。飛距離が伸びると確認できた事実ではありません。
翼幅を変えると翼面積や形状も変わります。翼幅と飛距離が単純に比例するとは限りません。
物理の参考：https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/lift-to-drag-ratio/
以降は、比較する機体、測定方法、結果の順に説明します。
この仮説への答えは、考察と最後のまとめで示します。目安は35秒程度です。
-->
---
layout: split
section: 方法
title: 翼幅6・9・12 cmの機体を用意
bodyClass: paper-example paper-conditions paper-two-blocks
page: 2
---
<MediaBox src="/media/paper-airplanes.svg" alt="胴体長18 cmの機体を上から見た図。翼幅はAが6 cm、Bが9 cm、Cが12 cm" />

::right::

<section class="paper-text-block">
  <h2>そろえた条件</h2>
  <dl class="paper-specs">
    <div><dt>用紙</dt><dd>A4コピー用紙</dd></div>
    <div><dt>胴体長</dt><dd>18 cm</dd></div>
  </dl>
</section>

<section class="paper-text-block">

## 翼幅の変え方

翼を折る位置で<br>6・9・12 cmに調整。

</section>

::takeaway::

翼幅6・9・12 cmの3条件を、**各3機**で比較

<!--
翼幅6・9・12 cm、胴体長18 cm、A4コピー用紙は完成見本用の設定です。
図の左右方向と胴体方向は寸法の比率をそろえています。詳細な折り手順を示す図ではありません。
上から見た図で、寸法矢印は左右の翼端間の幅を示しています。この説明は口頭で補います。
紙を切らず、胴体の折り方と長さを共通にし、翼を折る位置で翼幅を変える想定です。
この操作では翼面積・形状も変わります。重心や硬さも変わる可能性があり、考察で扱います。
実際の研究に置き換えるときは寸法と折り手順を実測値に差し替えます。目安は45秒程度です。
-->
---
layout: split
section: 方法
title: 最初に床に触れるまでの距離を測る
bodyClass: paper-example paper-three-blocks
page: 3
ratio: 1.1fr 1fr
---
<MediaBox src="/media/flight-measurement.svg" alt="投げた位置の真下から最初に床に触れた位置までの水平距離を測る" />

::right::

<section class="paper-text-block">

## 測定環境

風の影響が少ない屋内

</section>

<section class="paper-text-block">

## そろえる条件

投げる人・位置・高さ

</section>

<section class="paper-text-block">

## 測定の終点

最初に床に触れた位置

</section>

::takeaway::

飛距離は、最初に床に触れるまでの**水平距離**

<!--
飛んだ軌道の長さではなく、床に沿った水平距離を測ります。
着地後に滑った距離は含めません。
起点は投げた位置の真下です。手で投げるため速さ・角度の統一には限界があります。
目安は45秒程度です。
-->
---
layout: split
section: 方法
title: 9機を5回ずつ測り、平均で比較する
bodyClass: paper-example paper-three-blocks paper-trials
page: 4
---
<MediaBox src="/media/flight-averaging.svg" alt="各機体の5試行を平均し、3機分の平均から条件ごとの平均飛距離を求める" />

::right::

<section class="paper-text-block">

## 比較する機体

3条件 × 各3機

</section>

<section class="paper-text-block">

## 繰り返し回数

各機体を5回測定

</section>

<section class="paper-text-block">

## 条件の順番を入れ替える

A・B・C → B・C・A → C・A・B

</section>

::takeaway::

**計45試行**の結果を、条件ごとの平均で比べる

<!--
A→B→C、B→C→A、C→A→Bなどと順番を入れ替えます。
慣れや疲れが特定の条件に偏らないようにします。各機体の測定回数は5回で統一します。
目安は45秒程度です。
-->
---
layout: figure
section: 結果
title: 翼幅9 cmの平均飛距離が最長
bodyClass: paper-example
page: 5
---
<MediaBox src="/media/flight-results.svg" alt="翼幅6 cmのAは平均4.2 m、9 cmのBは6.3 m、12 cmのCは5.0 m" />

::takeaway::

翼幅12 cmのCは、<strong>9 cmのBより短かった</strong>

<!--
説明用の架空データ。各条件3機、各機体5試行。
棒は各条件3機の平均値です。Bが最も高いことに着目します。
統計的有意差や一般的な最適条件を示すものではありません。目安は30秒程度です。
元データは public/media/flight-distance.csv にあります。
-->
---
layout: figure
section: 結果
title: 機体ごとの平均でもBが最長
bodyClass: paper-example
page: 6
---
<MediaBox src="/media/aircraft-results.svg" alt="1点は1機の5試行平均。翼幅6 cmのAは3.8、4.2、4.6 m、9 cmのBは5.9、6.3、6.7 m、12 cmのCは4.5、5.0、5.5 m。Bの3点はAとCの全点より大きい" />

::takeaway::

Bの全3機が、**A・Cの全機体を上回った**

<!--
説明用の架空データ。点は個々の試行の記録ではなく、機体ごとの平均値。
表の数字を一つずつ追う代わりに、3機の平均値を点で比較します。
色が見分けにくくても条件は行ラベルで識別できます。線で点をつながず、時系列や対応関係を示唆しません。
各条件3機という範囲での結果です。目安は40秒程度です。
-->
---
layout: split
section: 考察
title: 仮説と測定結果の照合
bodyClass: paper-example paper-hypothesis-check
page: 7
---
<MediaBox src="/media/flight-comparison.svg" alt="翼幅9 cmのBは平均6.3 m、翼幅12 cmのCは5.0 mで、予想とは逆にCのほうが短かった" />

::right::

<section class="paper-comparison-block">
  <h2>予想：Cの方が長い</h2>
  <div class="paper-relation" aria-label="仮説ではBの平均飛距離がCより短いと予想">
    <div><strong>B</strong><span>翼幅9 cm</span></div>
    <span class="paper-relation-sign" aria-hidden="true">&lt;</span>
    <div><strong>C</strong><span>翼幅12 cm</span></div>
  </div>
</section>

<section class="paper-comparison-block paper-observation">
  <h2>結果：Bの方が長い</h2>
  <div class="paper-relation" aria-label="実測した平均飛距離はBが6.3メートル、Cが5.0メートルで、Bの方が長かった">
    <div><strong>B</strong><span>6.3 m</span></div>
    <span class="paper-relation-sign" aria-hidden="true">&gt;</span>
    <div><strong>C</strong><span>5.0 m</span></div>
  </div>
</section>

::takeaway::

今回の3条件では、**仮説は支持されなかった**

<!--
グラフは説明用の架空データ。
BとCの2条件に着目して、最初の仮説と結果を照合します。軸は結果のグラフと同じ0〜8 mです。
右側の不等号は平均飛距離の大小を表します。上下とも左がB、右がCで、予想と実測結果の逆転を示します。
このスライドでは仮説への答えを示し、原因の検討は次のスライドで扱います。目安は40秒程度です。
-->
---
layout: split
section: 考察
title: 飛距離の差を生んだ原因は未確定
bodyClass: paper-example paper-causes
page: 8
---
<section class="paper-factor-block">

## 機体の違い

<MediaBox src="/media/aircraft-factors.svg" alt="翼幅を変えると折り方も変わる。翼、重心、折り目の位置を示した模式図" />

重心・機体の硬さは未測定

</section>

::right::

<section class="paper-factor-block">

## 投げ方の違い

<MediaBox src="/media/throw-variation.svg" alt="同じ位置から異なる速さと角度で投げる可能性を示した模式図。実際の記録ではない" />

投げる速さ・角度は未統一

</section>

::takeaway::

翼幅以外の影響が残り、**原因は特定できない**

<!--
ここでは今回そろえきれなかった条件を示します。重心・機体の硬さの違いは未確認です。
手で投げたため速さ・角度の統一には限界があり、これらも記録していません。
いずれかが原因だったと断定せず、次に条件をそろえて再比較する理由につなぎます。
図の重心位置は説明のための模式的な位置です。目安は45秒程度です。
-->
---
layout: split
section: 今後
title: 条件をそろえて、3つの翼幅を再比較
bodyClass: paper-example paper-future paper-two-blocks
page: 9
---
<MediaBox src="/media/controlled-retest.svg" alt="翼幅6、9、12 cmの機体で重心を胴体の同じ位置に調整し、再比較する計画" />

::right::

<section class="paper-text-block">

## 発射装置で統一

速さ・角度・高さを<br>そろえる。

</section>

<section class="paper-text-block">

## 機体の条件を調整

重心の位置・総重量を統一。<br>同じ3条件を再比較する。

</section>

::takeaway::

発射条件・重心をそろえ、**3条件を再比較する**

<!--
追加実験の計画です。図の点は重心を同じ位置に調整する意図を示し、具体的な重心位置を指定するものではありません。
同じ総量のおもりの配置を変えるなどして、重心の位置と総重量をそろえる想定です。
最初に投げ方と重心の影響を減らし、同じ3条件の飛距離の差が再現するかを調べます。
調整後も翼面積・形状や硬さの影響は残り得ます。翼幅だけの効果を完全に分離したと主張しません。
折りのずれ・機体の硬さも確認する必要があります。目安は45秒程度です。
-->
---
layout: summary
section: まとめ
title: 翼幅と飛距離の関係
bodyClass: paper-example paper-summary
page: 10
---
<section>

## 比べた条件

3条件・9機・45試行

</section>

<section>

## 今回の結果

翼幅9 cmのBが最長

</section>

<section>

## 次に確かめること

同じ傾向が再現するか

</section>

::figure::

<MediaBox src="/media/flight-summary.svg" alt="3条件の平均飛距離。翼幅6 cmは4.2 m、9 cmは6.3 m、12 cmは5.0 m" />

::takeaway::

今回の3条件では、<strong>翼幅9 cmが最長（平均6.3 m）</strong>

<!--
最初の問いに戻って答えを述べます。翼幅9 cmのBが最長だったという結論は、今回比べた3条件の範囲です。
別の寸法や別の折り方でも最適だという一般化はしません。目安は40秒程度です。
-->
