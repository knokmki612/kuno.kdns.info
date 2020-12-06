---
title: sfos-jaチームでフリックキーボードのパッケージを公開した
date: 2019-04-14T23:08:34+09:00
tags:
  - 日記
  - Sailfish OS
archives:
  - 2019
  - 2019/04
---

日本語フリックキーボードのパッケージ、jolla-kbd-flick-jpをsfos-jaとして[OpenRepos.netで公開した](https://openrepos.net/content/sfosja/japanese-flick-keyboard)よ。

### sfos-jaができた経緯

私がこのフリックキーボードの存在を知ったのは、Jolla端末のオフの集まりに参加した時だったと思う。なにやら[sleepsounds](https://github.com/sleepsounds/)という方がフリックキーボードを開発されていて[^tmoのスレ]、しかもその方は日本人らしいって話を聞いて、はぇ〜すごい人がいるもんだな〜と思ったのを覚えている。

それからしばらくして、オフでつながっていた[helicalgear](https://github.com/helicalgear)さんがsleepsoundsさんとつながっていて、sleepsoundsさんの[リポジトリ](https://github.com/sleepsounds/jolla-kbd-flick-jp)をフォークしてrpmパッケージが作れるようになる[プルリクエスト](https://github.com/sleepsounds/jolla-kbd-flick-jp/pull/5)が作られていたみたいだった。

そのことに数ヶ月おくれで気づいた自分は、「自分の環境でもフリックキーボードのrpmパッケージをビルドして使いたい〜」と思って自分の環境でビルドできる別の方法を[プルリクエスト](https://github.com/helicalgear/jolla-kbd-flick-jp/pull/1)でhelicalgearさん宛てに出した。

その1年後に、Jollaの地元であるフィンランドの方らしい[topiasv](https://github.com/topiasv)さんが、私のプルリクエストをベースにsleepsoundsさん宛てに[プルリクエスト](https://github.com/sleepsounds/jolla-kbd-flick-jp/pull/7)を出していて、これをみた自分は「海外の人もフリックキーボードに興味あるんだな…これは色んな人がインストールしやすいようにしたほうが良いかもしれないな…」と思った。

と、ここまでの時点で3つプルリクエストが出ていて、それぞれ反応がないという奇妙な四角関係が完成してさらに1年が経過した…。1年間で日本語入力関係のパッケージをメンテする覚悟が決まり、フリックキーボードは色んな人のコード寄せ集めてブランチを整えたり、フリックキーボードに必要なAnthy関係のパッケージもフォークして[OpenRepos.netで公開](https://openrepos.net/content/knokmki612/japanese-flick-keyboard-patch-fork)したりした。

ただ根本的な問題があって、sleepsoundsさんはjolla-kbd-flick-jpにこの時点ではライセンスを設定しておらず、GitHubに置いてあろうともsleepsoundsさんの著作物なので、二次配布する時点で許諾をとる必要があったけどしていなかった。そういう問題があることを自分は認識していたものの、連絡がとれる自信がなかったので放置してしまった。

で、私がOpenRepos.netに公開したものはtopiasvさんにもバッチリ気づいてもらえたみたいで、去年の11月に直接メールで連絡をもらった。それをきっかけに[奇妙な四角関係について話し合う機会](https://github.com/sleepsounds/jolla-kbd-flick-jp/pull/7#issuecomment-435059563)が持てて、「みんなで開発しようよ！」という流れになった。

そこから奇跡的に4人のTwitterのグループDMができて、どこのjolla-kbd-flick-jpのリポジトリがアップストリームか迷わなくてすむようにっていうのと、自分がフォークして触ってきた日本語入力関係のパッケージをまとめられるように[sfos-ja](https://github.com/sfos-ja/)というorganizationができた。

### sfos-jaができてから

各々がコードの一方的なマージ以外ではまったく連携せずにやってきたので、DMで話せるのはめっちゃありがたい。topiasvさんはとくに機能開発へのモチベーションが高くて、今回のリリースに2つオプション機能が追加された。自分もレイアウトの調整に少しだけqmlを触ったりした。

{{% image src="Screenshot_20190415_002.png" caption="オプションをオフにした状態でキーボードを表示した様子" %}}

{{% image src="Screenshot_20190415_001.png" caption="オプションをオンにした状態でキーボードを表示した様子" %}}

あと、主にtopiasvさんとsleepsoundsさんがコードレビューしながらコードが良くなっているのを眺めている身としては、本当にsfos-jaできてよかったな〜と思った。

ちなみに、OpenRepos.netはGitHubのorganizationに対応する機能がないのでアカウントの情報を共有する必要があって、OSS Gateで自分が体験した[gpgでやり取りする方法](https://github.com/oss-gate/resources/tree/master/account)を[そのまま使わせてもらった](https://github.com/sfos-ja/resources/)

### sfos-jaの今後について個人的に思っていること

今いる人たちで、今後のSailfish OSのアップデートに追従していくのも楽しくできそうだなと思っている。細かいissueも立っているし、やることが色々ある。

個人的には、日本語リソースを使ってUIが日本語表示できるようにするパッチとか、日本語関係がまとめて入るメタパッケージもsfos-jaでそのうち作りたいなと。まあのんびりやっていけたらなと思う。

{{% tweet 1035113698929467393 %}}

### ついでにSailfish OS関係で書いときたいこと

#### Wiki的なもの

実は[@kenya888](https://twitter.com/kenya888)さんが中心になって作った[Jolla/Sailfish OS情報まとめ](https://sites.google.com/site/jollausersjp/home)っていうWiki的なものがあるよ！色々まとまっているからSFOS端末で遊ぶ時に参考にしてね！

#### Storeman

OpenRepos.netのパッケージを簡単に入れられるストアアプリがいくつかあって、最近は[Storeman](https://openrepos.net/content/osetr/storeman)が良いよ！

#### Patchmanager

SFOSにはパッチを当ててシステムをカスタマイズするPatchmanagerというツールがあるんだけど、活発に開発されていて、最新の[Patchmanager 3 Beta](https://openrepos.net/content/patchmanager3beta/patchmanager-3-beta)はオリジナルのファイルにパッチを当てずにfakerootでパッチ済みの環境を作るみたいだよ！Betaみたいだけど自分は使ってて快適なのでおすすめ！

[^tmoのスレ]:[talk.maemo.orgのスレッド](https://talk.maemo.org/showthread.php?p=1472394#post1472394)に当時の様子が残っている
