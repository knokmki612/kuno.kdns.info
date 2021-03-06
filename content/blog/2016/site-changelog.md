---
title: サイトの手入れでやったこと
date: 2016-06-06T20:13:10+09:00
tags:
  - 日記
  - お知らせ
archives:
  - 2016
  - 2016-06
---

このサイトを開設してから半年が経ちました。

ちょくちょくサイトの見た目を弄ったり、記事で動画の埋め込み等するたびにCSSの調整をしています。あと、多分パフォーマンスに影響がありそうなところもやっています。いつもTwitterで独り言のように変更したらつぶやいていますが、変化が分かりやすいところについて、gitの記録を遡りながら記事に記録しておこうかと思います。

### 編集履歴ページを追加した

{{% image src="スクリーンショット_2016-06-06_22-54-14.png" caption="編集履歴が見えるところ" %}}

11月29日に追加しました。これが何をやっているかというと`git log -p`の結果をそのまま流しています。あと、数日前に変更箇所に色がつくようにしてみました。

何故これをしようと思ったかというと、記事を黙って書き換えても誰にでも分かるようにしたかったからです。自分から「追記しました」と書くより良さそうかなと。

### 記事一覧のリスト表示ができるようにした

{{% image src="スクリーンショット_2016-06-06_22-55-09.png" caption="リスト表示しているところ" %}}

これは4月4日にやったようですね。記事の数がもっと増えないと意味がない気もしますが、通常は全文表示の記事3つ文が1ページであるところを、リスト表示では20記事くらい見ることが出来ます。記事を探すのには便利かも知れません。

### 大画面時に右カラムの本文が中央に来るようにした

{{% image src="スクリーンショット_2016-04-24_23-09-26.png" caption="右カラム修正前" %}}

{{% image src="スクリーンショット_2016-04-24_23-08-34.png" caption="右カラム修正後" %}}

これは見た目の話ですね。4月24日にやっているようです。見ての通り、私のサイトは2カラムのデザインを採用しています。ウィンドウに表示している分には満足していたのですが、大きなディスプレイのフルスクリーンで表示すると、どうにも気持ち悪さがあったんです。

どうしてかなあとずっと考えていたのですが、左カラムの固定幅であるぶん、本文の位置が右寄りなのが目立ってくるんです。私が持っている中では24インチのFHDが一番広いディスプレイなのですが、さらに大画面でQHDや4Kのディスプレイでは、より右寄りのずれが顕著になるであろうと思います。

それで、マージンをcalc()でうまくやって真ん中に来てくれるようにしました。私としてはスッキリしたと思うのですが、いかがでしょうか？

### 共有ボタンのG+をはてブに入れ替えた

{{% image src="スクリーンショット_2016-06-06_23-18-03.png" caption="はてブの共有ボタン" %}}

5月10日にやりました。ツイッターとフェイスブックは日常的に私が使っているので良いのですが、G+は手付かず。かといって、3つ並べることにしていたので補欠ポジション的にそこにありました。はてブが1軍入りしたきっかけは、[OSS Gateの記事]({{% relref "/blog/2016/impression-oss-gate" %}})を書いたら、どなたかがはてブでコメントをつけて下さっているのを発見したことでしたね。

根本的にボタンの数を3つに制限しているのがイマイチな気もしますし、さらに追加する際のデザインもなんとなく考えていますが、今のところ必要性を感じないのでそのままです。

### Vivaldiのバナーを追加した

{{% image src="スクリーンショット_2016-06-06_23-04-07.png" caption="バナー追加前" %}}

{{% image src="スクリーンショット_2016-06-06_23-04-43.png" caption="バナー追加後" %}}

6月1日に入ってからやってました。

{{% tweet 734771593600225280 %}}

たまたまツイートを見てみたら一番小さいバナーの幅が230pxで、左カラムの250pxにピッタリ。ただ、見出しと子要素の字下げのルールがバナーを入れると崩れてしまうので、字下げをせず揃えるように修正を入れました。今見たらバナーだけじゃなくてボタンも公開されてますね！

### CSSのお掃除

これは6月3日です。急に思い立ったんだと思いますけど、idとクラスの入り混じったセレクタ祭りだったのを、ここで綺麗にしています。3つくらいセレクタくっつけてた状態から、最高でも1つだけになりました。パフォーマンス的には変わったんですかね？

### CSSファイルを連結して出力するようにした

{{% image src="スクリーンショット_2016-06-06_23-58-31.png" caption="CSSファイル連結前" %}}

{{% image src="スクリーンショット_2016-06-06_23-59-19.png" caption="CSSファイル連結後" %}}

同日の6月3日。グーグル神がサイトの体験を評価してくれる[PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)は、私も気が向いたら試すようにしています。画像の最適化とかは去年やって、速度のスコアは79/100まではあげられたものの、もうちょっとスコア上げたいなあと思っていました。そしたら、

[javascriptとcssを全自動で連結&圧縮する | jamadam weblog](http://blog2.jamadam.com?p=18)

という記事を見つけまして、「あー！linkのhrefにcgiを指定しても良かったのかー！」と思いまして、シェルでcssファイルをcatするだけのcgiを書きました。

```
#!/bin/sh
echo 'Content-Type: text/css'
echo ''
cat normalize.css style.css
```

そしたら速度のスコアが90/100でオレンジから緑色になって、結構な効果ですよこれは。まあスコアが上がって満足したって話ですね。

ちなみにcssファイルの圧縮もしろと言われていますが、人間が読める状態にしておきたいので、それはパスです。

### バナーやアバターの画像を、サーバ側にキャッシュするようにした

翌日6月4日の昼。こっちはPageSpeed Insightsのスコアに影響を与えませんが、個人的に効果があるなあと思いました。前述のVivaldiのバナーはvivaldi.comから、[概要のページ](/about)で表示しているアバターはgravater.comから持ってきています。なんかキャッシュ有効のはずなのに読みこんで時間が伸びている気が…ということなので、サーバ側で画像をwgetで持ってきて、それを表示させています。

wgetするタイミングは私が自作した[sitesh](https://github.com/knokmki612/sitesh)の挙動で、記事を投稿したり更新すると専用のフォルダの中に置かれたスクリプトを実行するようになっており、そこでやってます。検索キャッシュの生成とか左カラムのラベルやアーカイブの更新のスクリプトも置いています。

なんか書きながら自分の言っていることに対して、セキュリティ的に不安になってきましたけど大丈夫だよね…？大丈夫だよね…？

と、半年のあいだ、他にも細かくいじっているのですが、我ながらよく続くなあという感じです。自分で全部作った愛着からなんでしょうか。これからも使いやすいサイトを目指していきたいと思います。
