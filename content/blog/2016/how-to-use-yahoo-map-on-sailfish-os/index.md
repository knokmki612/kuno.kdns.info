---
title: Sailfish OSでY!地図が使えました
date: 2016-04-13T17:40:45+09:00
tags:
  - Jolla
  - Sailfish OS
  - Tips
archives:
  - 2016
  - 2016/04
---

Jolla Phone/TabletにはAlien DalvikというAndroidランタイムをインストールすることが出来ますが、使えないAndroidアプリも多いです。

中でもGoogle Play Servicesの機能を使っているアプリなんかは、動くものも少なくないのにムラハチされてる感が凄いんですよね。
Yahoo\!地図という地図アプリも、例外なくGoogle Play Servicesの機能を使って位置情報の精度を上げているので、起動するとこのように怒られます。

{{% image src="Screenshot-16-04-13-17-30-34.png" caption="Yahoo\!地図アプリに怒られた画面" %}}

Jolla Phoneをメイン端末にしようと思うと使える地図アプリの重要性も高くなるわけですが、ネイティブの地図アプリもいくつかあるものの、日本国内での住所や地名検索には弱く、常用するには厳しいところがあります。かと言ってAndroidの地図アプリも上記のありさまで、グーグル・サンにドゲザしないと良い選択肢がない...かのように思っていました！！！！

{{% image src="スクリーンショット_2016-04-13_18-45-02.png" caption="microG Project" %}}

実はGoogle Play Services互換の機能を提供することを目指す[microG Project](https://microg.org)というものがありまして、これを使えばGoogle Play Servicesをゴニョゴニョして導入することなく、Yahoo\!地図アプリの機能がフルで使えるようになるんですよ！というわけで手順を書きますね。

<br>

### 1、F-Droidをインストールする

{{% image src="Screenshot-16-04-13-18-07-14.png" caption="JollaストアのF-Droid" %}}

Jollaストアから入ります。

### 2、F-Droidにリポジトリを追加する

{{% image src="Screenshot-16-04-13-18-10-28.png" caption="F-Droidの起動画面" %}}

F-Droidを起動したら、右上の詳細ボタンをタップし、"リポジトリ"をタップします。

{{% image src="Screenshot-16-04-13-17-33-11.png" caption="リポジトリの追加作業中" %}}

{{% image src="Screenshot-16-04-13-17-33-36.png" caption="リポジトリが追加できた" %}}

リポジトリ一覧で右上の"+"ボタンをタップし、ポップアップの"リポジトリのアドレス"に"https\://microg.org/fdroid/repo"を入力してから、"追加"をタップします。しばらくするとカタログファイルのダウンロード等され、"microG F-Droid repo"という項目にチェックが入ります。

### 3、microG Services Coreをインストールする

{{% image src="Screenshot-16-04-13-17-34-09.png" caption="microG Services Coreを見つけた" %}}

{{% image src="Screenshot-16-04-13-17-34-21.png" caption="インストール中" %}}

起動画面まで戻り、虫眼鏡をタップしてから"Gms"などで検索すると、micfoG Services
Coreというアプリがヒットするので、あとは流れに沿ってポチポチします。

<br>

この状態でもう一度Yahoo\!地図アプリを起動すると、何も怒られず現在位置が表示されるようになりました！

{{% image src="Screenshot-16-04-13-17-34-40.png" caption="Yahoo\!地図アプリに怒られなくなった" %}}

ルート検索や住所検索もできるし、雨雲レーダーも見れるみたいだし、かなり良さげなのではないでしょうか。

microGをインストールすることで使えるアプリを増やすことができるのは、非常に素晴らしいことですね！
