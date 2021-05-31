---
title: ブログをオレオレCMSからHugoに移行した
date: 2018-05-15T09:54:53+09:00
tags:
  - 日記
  - お知らせ
archives:
  - 2018
  - 2018-05
---

### 移行の経緯

前回の記事から半年経っていますね。何でこんなに間が空いたかを説明できるような納得感のある理由があるかといえば、ないです。

しいて言えば(やっぱりある)、3年前に作って使っていたシェルスクリプトなCMS、[site.sh](https://github.com/knokmki612/sitesh)でブログを管理していましたが、

1. データと処理がごちゃごちゃでつらい
2. 記事執筆用のオレオレフォーマットを拡張したくても面倒くさい
3. シェルスクリプトで全部やろうとするのが良くないのでは？
4. 他の言語だとかなり良さげなのが既にあるので作り直すのもな…

という堂々巡りを2年くらい前からやっており、微妙なsite.shの使い勝手の悪さで、記事を書くモチベーションが下がっていました。それで、この度ようやく[Hugo](https://gohugo.io)に移行する決心がついたというわけです。


### Hugoを選んだ理由

* site.shが完成しようかという時に初めて知った静的サイトジェネレータがHugoだった
* 生成が早そう

という2点がメインです。Go言語が好きと言えるほど使ったことはないです。が、テンプレート処理が[標準パッケージ](https://golang.org/pkg/text/template/)なところとか、ありものを組み合わせている感じがして好きです。[^小言]

Hugoでサイトを組んでみた印象としては、色々なやり方があって、ベストプラクティスっぽいものはなさそうだなあということです。それだけ作り方に幅があるのは良いことだと思いますが、どこから手を付けたら良いか迷いましたので、ポイントかなというのをいくつか紹介したいと思います。

### Hugoでサイトを組んでいた時の気づき

#### [Archetypes](https://gohugo.io/content-management/archetypes/)と[Section Templates](https://gohugo.io/templates/section-templates/)の関係性

* contentディレクトリ下の構成でSectionが定まる
* `archetypes/<section>.md`を作るとhugo newでSectionにあわせた雛形を作ってくれる
* mdに`type: <section>`で明示的に指定することもできる。(省略しても良い)

#### [Base(Block)](https://gohugo.io/templates/base/)/[Partial](https://gohugo.io/templates/partials/)/[Internal](https://gohugo.io/templates/internal/) Templatesと[Shortcodes](https://gohugo.io/content-management/shortcodes/)の関係性

* Base Templatesは`{{ block }}`にしたところを`{{ define }}`で書き換えられる
* Partial Templatesは`layouts/partials/**.html`を`{{ partial }}`で使いまわせる
* Internal Templatesはあらかじめ用意されたPartial Templatesみたいなもん
* Internal Templatesをカスタムする場合は[ここ](https://github.com/gohugoio/hugo/tree/master/tpl/tplimpl/embedded/templates)をみてPartial Templatesにすればいい
* 個人的には`{{ block }}`と`{{ define }}`と`{{ partial }}`はPugの[extendsとblock](https://pugjs.org/language/inheritance.html)と[includes](https://pugjs.org/language/includes.html)に似ていると思った
* Shortcodesは記事の中で凝ったマークアップ構造を使いたい時に使う
    * 画像とか動画とか
    * [あらかじめ用意された](https://gohugo.io/content-management/shortcodes/#use-hugo-s-built-in-shortcodes)Shortcodesもある
* [Lookup Order](https://gohugo.io/templates/lookup-order/)を見ながらテンプレートを配置すると良い

#### configの細かいところ

* [preserveTaxonomyNames](https://gohugo.io/content-management/taxonomies/#preserve-taxonomy-values)を`true`にしとかないと、タグの文字列が[urlize](https://gohugo.io/functions/urlize/)される
* [hasCJKLanguage](https://gohugo.io/getting-started/configuration/#all-configuration-settings)を`true`にしとかないと、`.Summary`がスペース区切りの単語数でカウントされて、RSSフィードの`description`とかめちゃ長くなる[^関連リンク1]
* [BlackfridayのplainIDAnchors](https://gohugo.io/getting-started/configuration/#blackfriday)を`false`にしとかないと、同じ文字列の見出しが2つあるとidが重複する

#### 最近のHugo(0.32〜)は便利

* 画像や動画を`static`に置かないといけなかったのが、`<記事のディレクトリ>/index.md`で一緒に置けるようになった[^関連リンク2]
    * これは活用してる
* [画像の最適化](https://gohugo.io/news/0.32-relnotes/)もしてくれるようになった
    * これは活用してない

### Hugoに移行した結果

Markdownで記事が書けるようになったのは、前と比較したら良くなったかなと思います。勘違いしてほしくないのは、私はそんなにMarkdownが好きではないということです(面倒くさい人だ)。それでも、リストのネストが簡単に書けるようになったのは良かったですね。

それと同じくらい、Shortcodeが使えるようになったのも良かったです。site.shで記法を拡張したかったのは、任意のHTMLコードを使いまわせるようなところだったので。

今回移行するに当たってHugoのテーマも作成したので、参考になればさいわいです。

https://github.com/knokmki612/hugo-pencil-and-ruler

これで記事を書くペースが上がるといいなぁ…

[^小言]:シェルスクリプトで頑張っていたからそう感じるのかねぇ…いや、シェルスクリプト的にはコマンドを活用すれば良くて、自分がそういう風にうまく書けなかっただけだな…
[^関連リンク1]:[Hugo のサマリーが大きすぎる件 - awm-Tech](https://blog.awm.jp/2016/01/02/hugo/)
[^関連リンク2]:[Hugo 0.32から記事と同じ場所に画像を置けるようになった - blog.ton-up.net](https://blog.ton-up.net/2018/01/13/hugo-032/)
