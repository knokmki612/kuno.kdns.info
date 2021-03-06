---
title: Vivaldiと私の1年をふりかえりました
date: 2017-02-08T23:28:20+09:00
tags:
  - 日記
archives:
  - 2017
  - 2017-02
---

### ユーザーミートアップへの参加

私は元々Operaユーザーだったのですが、Vivaldiを普段使いしだしたのは、4月にあったVivladiの[ユーザーミートアップイベント](http://vivaldimeetup01.peatix.com)に参加してからです。それ以前はVivaldiを触りつつOperaをメインにしていました。

{{% image src="cover-gBCp1zTJthkq6mhPjx7oNqGlYLP8jr4l.jpg" caption="peatixに掲載されている1.0ローンチの画像" %}}

イベントの様子は[togetter](https://togetter.com/li/967261)に[Kyu3](http://kyu3.blog.jp/profile.html)さんがまとめてくださっています。

イベントでは、ライトニングトークでVivaldiの触って気に入っているところをテーマにしたのですが、思ったより他の人の発表内容が多岐にわたっていて被らなかったのが意外でした。

他にも冨田氏やテッツナー氏がどのようにVivaldiブラウザの開発に取り組んでいるのか、Vivaldiのファンがどんな人たちなのかを直接見て聞くことができたのはとても良いイベントだったと思います。

それからは毎日Vivaldiを使っていた…はずなんですけど、[Twitterで検索](https://twitter.com/search?q=vivaldi%20OR%20ビバルディ%20OR%20タイリング%20OR%20タブスタッキング%20from%3Aknokmki612%20since%3A2016-04-26%20until%3A2016-11-01&src=typd)してみてもそんなに使ってる感じしないですね…

### ソプラノチームへの参加

それはそれとして、ユーザーミートアップイベントに参加してからしばらくして、6月にソプラノメンバー募集の知らせが来ていました。"ソプラノ"というのはつまるところ、ボランティアでテスターやる人のことらしいです。活動内容には

- バグ管理システムへのバグの登録
- ソーシャルメディア等で報告される不具合の検証と報告
- 他のテスターや開発者とのやりとり
- それらを英語で行う

と書いてありました。これに応募するかどうかは迷いつつ、半年後の12月にはなんだかんだで応募することにしました。

応募したきっかけには2つありまして、1つは3年前くらいから知り合いの[NEAR](http://libreproducts.info)さんから「やりませんか？」と言われていたことですね。この方は何かと積極的な方で、ミートアップイベントも勧めていただいたり、早い時期にソプラノとして活動なさっていました。

もう1つは、迷っている半年間に[OSS Gate](http://oss-gate.github.io)という取り組みへの継続的な参加を通して、テスターとしての活動内容に不安が薄らいできた、ということですね。

なかでもOSS Gateのワークショップでは、「OSS開発未経験者がOSS開発経験者になる」ことを目的としているのですが、

- 対象のOSSへのフィードバック(バグ報告やパッチ作成)をする
- フィードバックする過程では大抵英語でフィードバックする

という2点で、はからずもソプラノでの活動に必要な下地が整っていた感があります。もちろんVivaldiはプロプライエタリなソフトウェアで、自分でコードを弄るという選択肢が与えられていないのがやきもきするところではありますが。まあChromiumの由来のバグなら可能(厳しそう)ですし、あとそもそもReactとか分からないですけど。

それで、ソプラノへの応募にあたって志望動機書いたりNDAとかあったりして、参加が決まった後はテキストチャットでチームに挨拶しました。あとオスロでコミュニティマネージャなるものをやっている[Gaëlle](https://forum.vivaldi.net/user/gaelle)さんにバグ管理システムの説明を受けたりしました。まさかオスロの人とビデオチャットする日が来るとは思わなかった。

### ソプラノとして活動していたらモデレータになった

ソプラノとして具体的にどういう活動をしていこうか考えた時に、以下のことを考えました。

- すでに報告されているバグをテストしていく
- 自分でバグを発見して報告する
- SNSやフォーラムで話題にあがっているバグをテストして報告する

1つ目は作業として楽しめる自信がない、2つ目は自分だと見つけようとして見つかるものではない、ということで、3つ目を中心にすえて頑張ろうと1ヶ月やってみました。

やってみると、フォーラムのユーザーさんがあげているバグは「よく気づくなあ」というものも含んでいて、かなり洗い出しができると思いました。集合知すげーという感じです。

また、フォーラムやTwitterを見ている限り、バグ報告以外にも「翻訳したい！」とか「こんな機能がほしい！」という人など、Vivaldiというソフトウェアを改善したい欲求を持っているユーザーが思ったより多いなあと思いました。どうしたらその欲求をみたせるだろうか？とか考えていました。ここらへんもOSS Gateの「詰まったらOSS開発参加のチャンス！」という考えが多分に影響している気がします。

そんな中、Gaëlleさんが「調子はどうですか？」とチャットで声を掛けてきて下さったんで、1ヶ月で思ったことを伝えたら、「モデレータやりませんか？」と突然言われましたね。それでやることになりました。

{{% tweet 823879110996828161 %}}

### 今思っていること

フォーラムで確認できたバグを報告するところはルーチン化しつつありますが、報告したバグが修正されるところまで持っていくのに、自分ができることを探している段階です。

そのためには、私はもっとVivaldiの開発者やソプラノチームと連携する必要があるでしょうし、誰を引っ張ればいいかよく観察したいと思います。うーん、なんかここらへんも最近OSSへのコントリビューションする際の話としてどこかで読んだような…

また、特に日本語話者のソプラノメンバーや、Vivaldiの人とはもっと意思疎通をしたいと思っています。今のところ、なかなか作業をしていても相手が何を考えているのか分からない場面が多いです。

[Vivaldiの国別ユーザーは日本が1位](http://news.mynavi.jp/articles/2017/01/07/vivaldi_tomita_2016/)というニュースもありましたし(今はどうなんだろう)、CJK関連のバグを潰せるように活動を注力したいなあと私も思っています。

Vivaldiでも、最近オスロで日本人のテストエンジニアである[Takaaki](https://forum.vivaldi.net/user/takaaki)さんに来てもらったりと、日本人ユーザを意識しているようです。ただ、やっぱりIME関連のバグは中々手強いみたいですね。

あと、今のところ私って

- ソプラノメンバーとしての活動
- フォーラムのモデレーターとしての活動
- 翻訳とそのレビュアーとしての活動

という役割をもっていて、全てフル稼働しているわけじゃない(何を期待されているのかさえよく分かっていない)んですけど、これからも続けていく上ではボランティアでつらいなあとも思っています。時間はあるんですけど。

なので、なるべく他のソプラノメンバーやVivaldiの人と役割を共有・分担して、最悪私がサボっても同じようにまわりそうな感じにしたいなあと思っています。

…たかだかまだ3ヶ月くらいしか活動していなくて何様なのかな？と自分でも思いますが、大事なのは「誰もつらくならず続くこと」だと思うので、そういう意味でもちゃんと意思疎通がしたいです。

-----

そんなわけで、またユーザーミートアップイベントやりましょうよ！「ソプラノメンバーって何してんの？」というのは私が分かっている範囲でちゃんと話しますので！知りたい人いるのか知りませんけど！

ついでに[OSS Gateワークショップは今現在、東京、札幌、大阪で開催している](https://oss-gate.doorkeeper.jp)ことをお知らせしておきます！

まあ、そんなVivaldiと私の1年でした。これからもよろしくお願いします。
