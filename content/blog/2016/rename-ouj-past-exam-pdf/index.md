Title: 単位認定試験pdfのファイル名をちょっと料理しました
Label: Tips,放送大学
Permalink: rename-ouj-past-exam-pdf
Write from next line:
放送大学って色々学習支援をネットから受けられるわけですが、微妙に使い勝手が悪い気がします。放送授業の時間割とかGoogleカレンダーと連携させたいけど手作業で打ち込むしかなかったり、資料室のインターネット配信は埋め込み再生のほうが良さそうとかですね。
で、単位認定試験が迫っていて遅まきながら、過去問を落とそうと思ったら、ファイル名が"科目番号-年度+学期+問題か解説.pdf"という規則だったので、科目名が分かりにくいと思いました。
それで、こんな感じのシェルスクリプトを書きました。
<pre><code>#!/bin/sh
if [ ! -f "$1" ]; then
	echo "no such file"
	exit 1
fi
html="$1"

for sbjnum in $(grep -oE '[0-9]{7}' "$html" | uniq); do
	for pdf in $(ls -f | grep -E "$sbjnum-[0-9]{4}[aq]\.pdf"); do
		sbjname=$(
			grep "$sbjnum" "$html" |
			sed 's;.*nowrap="">\([^<]\+\)</td>.*;\1;g')
		echo "found: $sbjname"
		mv "$pdf" $(echo "$pdf" | sed "s;[0-9]\{7\};$sbjname;")
	done
done

exit
</code></pre>
"単位認定試験問題・解答・解説一覧"のhtmlそのものと任意の科目のpdfをダウンロードし、引数にhtmlを指定して実行すると、カレントディレクトリ内にある過去問pdfの、ファイル名に含まれる科目番号が科目名に置き換わります。
スクリーンショット_2016-07-09_01-12-31.png: 置き換え中
スクリーンショット_2016-07-09_01-13-15.png: 置き換え後
分かりにくいですがこんな感じです。
わりと雑に書いたので、すぐ使い物にならなくなりそうな気がしますが、まあいいかなぁ
