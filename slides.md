---
theme: none
title: Plain Slidev Template
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
affiliation: ［所属］
group: ［部署・グループ］
presenter: ［発表者名］
subtitle: ［サブタイトル］
exportFilename: plain-template-preview
---

［発表タイトル］

---
layout: agenda
title: 目次
numbered: false
---

1. ［セクション1］
2. **［セクション2］**
3. ［セクション3］
4. ［まとめ］

---
layout: default
title: ［スライドタイトル］
page: 1
---

## ［小見出し］

- ［説明したいこと］
- ［その理由や背景］
- ［具体例や補足］

::takeaway::

［このスライドで伝えたいことを1文で記入］

---
layout: split
title: ［図と説明］
ratio: 1fr 1.1fr
page: 2
---

<MediaBox alt="図・写真を配置" caption="［図の説明］" />

::right::

## ［説明の見出し］

- ［注目してほしい点］
- ［背景・理由］
- ［補足情報］

::takeaway::

［図と説明から伝えたいこと］

---
layout: compare
title: ［2つの対象の比較］
page: 3
---

<h2 class="red">［対象A］</h2>

<MediaBox alt="対象Aの図を配置" height="250px" />

<p class="spaced">［対象Aの特徴］</p>

::right::

<h2 class="blue">［対象B］</h2>

<MediaBox alt="対象Bの図を配置" height="250px" />

<p class="spaced">［対象Bの特徴］</p>

::takeaway::

［比較から分かる違いや共通点］

---
layout: equation
title: ［数式と説明］
page: 4
---

［数式の意味や、扱う関係を説明］

$$
y = ax + b
$$

<p class="center small">［各記号の意味・単位を記入］</p>

<p class="center spaced">［式から分かること］</p>

::takeaway::

［数式に関する要点］

---
layout: figure
title: ［大きな図・写真］
page: 5
---

<MediaBox alt="図・グラフ・写真を配置" />

::takeaway::

［図から読み取れることを1文で記入］

---
layout: split
title: ［結果と考察］
lead: ［評価条件や、見るべきポイントを短く記入］
ratio: 1.5fr 1fr
page: 6
---

<MediaBox alt="結果のグラフ・表を配置" />

::right::

## ［観察したこと］

［図から確認できる事実］

<h2 class="spaced">［考えられる理由］</h2>

［結果に対する解釈］

::takeaway::

［結果から言えること］

---
layout: compare
title: ［動画の比較］
page: 7
---

## ［条件A］

<VideoBox label="動画Aを配置" caption="［動画Aの説明］" />

::right::

## ［条件B］

<VideoBox label="動画Bを配置" caption="［動画Bの説明］" />

::takeaway::

［動画で確認してほしい違い］

---
layout: default
title: ［表による整理］
page: 8
---

| 比較項目 | 対象A | 対象B |
| :--- | :---: | :---: |
| ［項目1］ | ［内容］ | ［内容］ |
| ［項目2］ | ［内容］ | ［内容］ |
| ［項目3］ | ［内容］ | ［内容］ |

::takeaway::

［表から分かること］

::note::

［必要に応じて、出典や条件を記入］

---
layout: summary
title: まとめ
page: 9
---

<section>

## ［要点1］

［1つ目の要点を簡潔に記入］

</section>

<section>

## ［要点2］

［2つ目の要点を簡潔に記入］

</section>

<section>

## ［次のアクション］

［今後の方針や、相手に求めること］

</section>

---
layout: default
title: ［補足・参考情報］
page: 10
---

## ［補足事項］

- ［説明を補う情報］
- ［対象範囲や前提条件］

<h2 class="spaced">［参考文献・資料］</h2>

<p class="small">［著者・資料名・発行年・URLなど］</p>
