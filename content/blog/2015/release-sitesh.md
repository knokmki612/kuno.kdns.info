---
title: 分散型？ブロギングツール、siteshを作りました
date: 2015-12-03T14:57:21+09:00
tags:
  - Tips
archives:
  - 2015
  - 2015-12
---

こんなものを作ろうと思ったのはなんでかというと、[「フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門」という本を読んでしまった](http://www.amazon.co.jp/dp/4048660683)からなんですが。

本では機能ごとにファイル分けたり、[Tukubai](https://uec.usp-lab.com/TUKUBAI/CGI/TUKUBAI.CGI?POMPA=ABOUT)というコマンド群を使って華麗なテキスト処理をやっていて、対する私のスクリプトはゴチャゴチャにコード突っ込んで泥臭くsedのオンパレードかましているので、「本当にこの本を読んだのかな？」という感じになっています。

とりあえずこのサイトは題名の通り命名したsiteshで執筆、運用しています。[GitHub](https://github.com/knokmki612/sitesh)にソースを公開しているので、興味あったら見てください。

コミットメッセージが適当とかきたねえコードだとかプルリクとはなんぞとかライセンス何が良いんだとか分からないことだらけなので、興味持ったような人が万が一いたら教えてください。

### 特徴

既存のブログ管理ツールというと、動的なものとと静的なものがあると思うんですが、動的なものはサーバー側で常に起動する必要があったり、ツールそのものやDBの更新が大変だったりするし、はたまた静的なものはサーバ側はWebサーバさえ動かせばいい反面、ローカルでサイト全体のファイルを持つ必要があったり、修正を加えるたびにサイト全体をビルドする必要があったりするみたいじゃないですか。

なので、

- ローカルで扱うデータの最小単位を1記事にする
- サイトの機能や見た目を気軽に変更できるようにcgiで動かす

ことを念頭に置いて作りました。記事側はあらかじめテンプレートを適用して生成していますが、サイトと記事はcgiで連結して表示するという感じの、動的なものと静的なものの中間なものみたいになっています。

### 動作する環境

#### ローカル側の動作環境

Mac、Linux、msys2での動作を確認しました。

#### ローカル側で必要なもの

- GNU sed
- GNU date
- OpenSSH
- rsync
- nkf
- sudo
- ImageMagick

#### リモート側の動作環境

後述するテンプレートをどう書くかでどうとでもなってしまいますが、自分が作ったテンプレートはDebian GNU/Linuxで動かすことを前提に作りました。

#### リモート側で必要なもの(テンプレート"kuno"の場合)

- GNU sed
- GNU date
- nkf
- sudo
- git

### 導入のしかた

githubから持ってきて、setup.shを実行します。デフォルトでは/usr/local下にインストールされますが、prefixを指定すれば任意のパスにインストールできます。2回目以降のinstallはパスが維持されるので、指定しなくて大丈夫です。

```
$ git clone https://github.com/knokmki612/sitesh.git
Cloning into 'sitesh'...
remote: Counting objects: 533, done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 533 (delta 0), reused 0 (delta 0), pack-reused 525
Receiving objects: 100% (533/533), 98.18 KiB | 0 bytes/s, done.
Resolving deltas: 100% (220/220), done.
Checking connectivity... done.
$ cd sitesh
$ prefix=/usr ./setup.sh install
```

### 使い方

siteshはsiteコマンドとpostコマンドがあります。siteコマンドはサイトのリモート操作に必要な設定をするためのコマンドで、複数のサイトの管理ができます。postコマンドは記事の作成やリモートとの記事の送受信・削除とかするコマンドです。

例として、サイトを開設する流れを書きます。

まず最初に、記事をやりとりするためのSSHホストとか設定します。すでにsite makeで作成されたサイトを設定する場合、site addだけで完了です。

```
$ site add
url: http://hoge
ssh host: fuga@hoge
ssh key: ~/.ssh/id_rsa
server path: /var/www/site/
posts dir: /var/www/site/post_files
template: kuno

current selected site: http://hoge/
$ 
```

テンプレート名を入力するところは、/usr/local/share/sitesh/templatesにあるフォルダから選べます。~/.sitesh/templatesにテンプレートを置いたら、そちらが優先して使用されるようになっています。

次にサイトを作成します。ブログに必要な情報を入力した後、テンプレートフォルダに用意されたファイルを配置します。

リモートに指定したディレクトリが無い場合、sudo権限を要求してmkdirするという強引な挙動なので注意して下さい。

```
$ site make
no.  url           hostname
1    http://hoge/  fuga@hoge

select make site of number (q for quit): 1

owner: fuga
name: ブログのタイトル
description: ブログの説明文
Agent pid 3527
Enter passphrase for /home/fuga/.ssh/id_rsa: 
Identity added: /home/fuga/.ssh/id_rsa(/home/fuga/.ssh/id_rsa)
Connection to hoge closed.
sending incremental file list
./
.gitignore
favicon.ico
index.cgi
kuno.ttf
normalize.css
style.css
template-article.html.sh
template-site.html.sh
cache/
jobs/
jobs/make_archives.sh
jobs/make_labels.sh
jobs/make_rss_page.sh
jobs/make_search_cache.sh
post_files/
preview/
rss/
rss/index.cgi
rss/template.rss.sh

sent 13,719 bytes  received 309 bytes  28,056.00 bytes/sec
total size is 32,253  speedup is 2.30
Initialized empty Git repository in /var/www/site/.git/
[master (root-commit) 77bc2a1] skeleton site is opened
 16 files changed, 1441 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 apache-2.4.conf.example
 create mode 100644 favicon.ico
 create mode 100755 index.cgi
 create mode 100755 jobs/make_archives.sh
 create mode 100755 jobs/make_labels.sh
 create mode 100755 jobs/make_rss_page.sh
 create mode 100755 jobs/make_search_cache.sh
 create mode 100644 kuno.ttf
 create mode 100644 normalize.css
 create mode 100755 rss/index.cgi
 create mode 100644 rss/template.rss.sh
 create mode 100644 site.conf
 create mode 100644 style.css
 create mode 100755 template-article.html.sh
 create mode 100755 template-site.html.sh
Agent pid 3527 killed
$
```

サイトにファイルを配置するとともにgitのローカルリポジトリを作成し、"skelton site is opened"というメッセージで最初のコミットがされます。

今のところ、apache-2.4.conf.exampleというファイルも一緒に配置されるようになっているので、rewriteとかの参考にしてwebサーバの設定を行なって下さい。

site addやsite makeで入力した設定を変更したい場合、ローカルでの設定はsite editで、リモートでの設定はディレクトリ直下のsite.confを直接いじって下さい。

次はpostコマンドです。

とりあえず、post newと実行して下さい。すると、拡張子がdraftの、数字が14文字並んでいるファイルが作成されたと思います。これは実行した時点での秒単位の時刻です。

あとdraftファイルをcatしてみると、すでに何か書いてあると思います。

```
$ post new
$ ls *.draft
20151207230833.draft
$ cat 20151207230833.draft
Title: 
Label: 
Permalink: 
Write from next line: 
$
```

これは上から順番にタイトルの記事、記事につけるラベル、記事のurlの一部となるパーマリンク、最後のものは次行から本文を入力しろというだけのメッセージです。コロンの右側に入力して下さい。ラベルはカンマで複数指定できます。

それで本文を書いていくわけですが、仮にdraftファイルがこんな感じだったとします。

```
Title: 最初の投稿
Label: 日記,テスト
Permalink: first-post
Write from next line:
あーあーあー
こんにちは

最初の投稿です
hello.jpg: 最初の写真
http://fugafuga.net/seeyou.jpg: 2枚目の写真
<strong>おわりです!</strong>
```

このdraftファイルを変換するには、こう入力します。

```
$ post make 20151207230833.draft
```

すると、こんな感じのフォルダとファイルが生成されます。

```
$ tree 20151207230833-first-post/
20151207230833-first-post/
├── draft
├── hello-s.jpg
├── hello.jpg
├── html
├── label
├── rss
├── seeyou-s.jpg
├── seeyou.jpg
└── title

0 directories, 7 files
```

中のhtmlファイルは、こんな感じにテンプレートが適用されて、各所変換されています。

```
<article>
<aside class="clearfix">
<div class="social-icon">
  <a href="http://twitter.com/share?url=${URL}post/20151207230833-first-post&text=%E6%9C%80%E5%88%9D%E3%81%AE%E6%8A%95%E7%A8%BF$TITLE_TAIL_ENCODED"><span class="icon-">twitter</span></a>
  <a href="http://www.facebook.com/sharer.php?u=${URL}post/20151207230833-first-post"><span class="icon-">facebook</span></a>
  <a href="https://plusone.google.com/_/+1/confirm?hl=ja&url=${URL}post/20151207230833-first-post"><span class="icon-">google+</span></a>
</div>
<div class="date">
  <time datetime="2015-12-07T23:08+09:00">2015/12/07</time>
</div>
<div class="labels">
  <a href="$URL?label=%E6%97%A5%E8%A8%98">日記</a>,<a href="$URL?label=%E3%83%86%E3%82%B9%E3%83%88">テスト</a>
</div>
</aside>
<h2><a href="${URL}post/20151207230833-first-post">最初の投稿</a></h2>
<p>あーあーあー</p>
<p>こんにちは</p>
<br>
<p>最初の投稿です</p>
<p class="image">
<a href="$URL${POSTS}20151207230833-first-post/hello.jpg"><img class="landscape" src="$URL${POSTS}20151207230833-first-post/hello-s.jpg" alt="最初の写真"></a>
<a href="http://fugafuga.net/seeyou.jpg"><img class="landscape" src="$URL${POSTS}20151207230833-first-post/seeyou-s.jpg" alt="2枚目の写真"></a>
</p>
<strong>おわりです!</strong>
</article>
```

本文の変換について、要点をおさえておくと、

- ただの文字列はpタグで囲まれる
- 改行すれば別々にpタグで囲まれる
- 空行はbrタグになる
- "写真のファイル名、もしくは写真を指すurl: 任意の文字列"は、縮小画像をローカルで作ったり、任意の文字列をaltに格納する
- タグで始まる文字列は、何も変換しない

という感じになっています。

次はこの記事をリモートに送ります。送るにはこうです。

```
$ post send

     1 20151207230833-first-post

(? for help, q for quit): 1

Agent pid 4492
Enter passphrase for /home/fuga/.ssh/id_rsa: 
Identity added: /home/fuga/.ssh/id_rsa (/home/fuga/.ssh/id_rsa)
sending incremental file list
20151207230833-first-post/
20151207230833-first-post/draft
20151207230833-first-post/html
20151207230833-first-post/hello-s.jpg
20151207230833-first-post/hello.jpg
20151207230833-first-post/label
20151207230833-first-post/rss
20151207230833-first-post/seeyou-s.jpg
20151207230833-first-post/seeyou.jpg
20151207230833-first-post/title

sent 2,499,574 bytes  received 153 bytes  999,890.80 bytes/sec
total size is 2,559,383  speedup is 1.02
[master f30fbb7] deployed: 20151207230833-first-post
 7 files changed, 58 insertions(+)
 create mode 100644 post_files/20151207230833-first-post/draft
 create mode 100644 post_files/20151207230833-first-post/hello-s.jpg
 create mode 100644 post_files/20151207230833-first-post/hello.jpg
 create mode 100644 post_files/20151207230833-first-post/html
 create mode 100644 post_files/20151207230833-first-post/label
 create mode 100644 post_files/20151207230833-first-post/rss
 create mode 100644 post_files/20151207230833-first-post/seeyou-s.jpg
 create mode 100644 post_files/20151207230833-first-post/seeyou.jpg
 create mode 100644 post_files/20151207230833-first-post/title
Agent pid 4492 killed
$
```

無事にリモートに送られ、"deployed: 20151207230833-first-post"というメッセージでコミットされています。例にあわせると、http://hoge/post/20151207230833-first-postというURLで記事が公開されています。

送った記事は、post receiveを実行すればどこからでもローカルで持ってこれます。それでフォルダ内のdraftファイルを編集し、post sendすれば編集が反映されます。

ついでに言うと、post sendで記事を送ったとき、リモートのjobsフォルダに置かれたスクリプトが自動実行されるようになっています。これで記事を追加した際のサイトの情報を変化させるのに対応しています。

<br>

あとは補足みたいなやつですけど、post newするときに第二引数にパーマリンクを指定すると、固定記事用のフォーマットで記事が作れます。

gitでスナップショットをとっているので編集履歴が残りますし、post removeで記事を削除しても復元することができます。

siteコマンドは複数のサイトを管理し、記事を投稿することができるようになっています。別のサイトに記事を送りたいときは、post
makeの前にpost switchを実行してサイトを切り換えます。

疲れたのでここら辺にしておきたいんですが、これくらいで十分でしょうか...？

### 今後について

今後はこういうことをやろうかと思っています。多分しばらくやらないけど。

- 記事のテンプレートを変えた際、記事に一斉にテンプレートを適用するような実装
- zenityかなんかでGUIを作って、もっとやさしくする

冒頭にも書いたように、さっきのような使い方でこのサイトは運用しています。私以外にも「使ってみよう」という変な人がいたら幸いです。~~ソースコード改善してほしいし、色々まだ整備が必要な部分があるし、とにかく誰かKAIZENに参加して欲しいです。本文がオレオレフォーマットで変換してますけど、ぶっちゃけおとなしくマークアップのほうがいいと思うならそうしていただいていいですし。~~

というかそういう人が本当にいたとしてもどう対応していいのか分からない程度には本当に色々分かってません。まあよろしくお願いします。
