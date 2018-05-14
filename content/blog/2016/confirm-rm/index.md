Title: 意図しないrmを回避するためのbashrc
Label: Tips
Permalink: confirm-rm
Write from next line:
皆さん、楽しいターミナルライフしてますか？

先日、私は不注意なrmを実行したことで、フォルダのPicturesとDocumentsがあべししました。写真はバックアップをとってありますし、Documentsに入っていたものも消えても問題ないかバックアップをしてあったので被害は少なかったのですが、それにしたってちょっと雑過ぎるダンシャリ過ぎました。ショックです。
もうこんな過ちを犯すのはごめんなので、rmを実行したら確認のワンクッションを置けるaliasをbashrcに書いてみました。
<pre><code>confirm_rm() {
	echo "rm $@"
	echo "are you sure you want to remove these files?"
	while true; do
		echo -n '(y/n): '
		read res
		if echo "$res" | grep '^[yn]$' 2>&1 >/dev/null; then
			break
		fi
	done
	if [ "$res" = y ]; then
		\rm "$@"
	else
		echo 'these files were saved!'
	fi
}

alias rm="confirm_rm"
</code></pre>
rmを実行しようとしたら、もう一度実行内容を確認します。ワイルドカードを使っていたら展開されて消される対象のファイルやフォルダがずらっと出てきます。
<pre><code>$ ls 消したくないフォルダ/
消したくないファイル1  消したくないファイル3  消したくないファイル5
消したくないファイル2  消したくないファイル4
$
</code></pre>
<pre><code>$ rm 消したくないフォルダ/*
rm 消したくないフォルダ/消したくないファイル1 消したくないフォルダ/消したくないファイル2 消したくないフォルダ/消したくないファイル3 消したくないフォルダ/消したくないファイル4 消したくないフォルダ/消したくないファイル5
are you sure you want to remove these files?
(y/n): n
these files were saved!
$
</code></pre>
本当に消してよい覚悟があるならy、ないならnを入力して、本来なら消えるはずだったものを救済しましょう！
<pre><code>$ rm -rf /*
rm -rf /bin /boot /dev /etc /home /lib /lib32 /lib64 /lost+found /media /mnt /opt /portage-latest.tar.bz2 /proc /root /run /sbin /srv /stage3-amd64-20151203.tar.bz2 /sys /tmp /usr /var
are you sure you want to remove these files?
(y/n): n
these files were saved!
$
</code></pre>
あくまで実行する前に確認するだけなので、ないものを消そうとしたり権限が足りなくて消せないはずでも確認します。だるいでしょうけど仕方ないですね。
ぶっちゃけこんなダイアログ的にしなくても、もっと簡単に同じことが出来ますけどね。aliasはコマンドの頭にバックスラッシュを書けば一時的に無効化されるそうです。最初に紹介したやつもこれを利用しています。(参考にしたもの:<a href="http://www.atmarkit.co.jp/flinux/rensai/linuxtips/214dsblalas.html">エイリアスを一時的に無効にするには</a>)
<pre><code>$ alias rm="echo rm"
$ rm 消したくないフォルダ/*
rm 消したくないフォルダ/消したくないファイル1 消したくないフォルダ/消したくないファイル2 消したくないフォルダ/消したくないファイル3 消したくないフォルダ/消したくないファイル4 消したくないフォルダ/消したくないファイル5
$ \rm 消したくないフォルダ/*
$
</code></pre>

確認メッセージの英語おかしかったらツッコんで下さい。新幹線で書いてるんですけど、広島行ってきます！では！