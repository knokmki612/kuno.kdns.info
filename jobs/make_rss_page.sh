#!/bin/sh

. ./site.conf

labels=$(
	find $POSTS -name label  |
	xargs cat                |
	LANG=ja_JP.UTF-8 sort -f |
	uniq                     |
	sed 's/^ *//g')

cat << HEADER > cache/choose
cat << +
<article>
<h2>購読のオプション</h2>
<p>除外したいラベルを選択して、あなたに合わせたRSSフィードを生成することができます。選択せずに、全ての記事を購読することもできます。</p>
<form action="rss/" method="GET">
<ul>
HEADER

BACKUP_IFS=$IFS
IFS='
'
for label in $labels; do
	echo "<li><label for=\"$label\">$label</label> <input type=\"checkbox\" name=\"label\" id=\"$label\" value=\"$label\"></li>" >> cache/choose
done
IFS=$BACKUP_IFS

cat << FOOTER >> cache/choose
</ul>
<input type="submit" value="生成する">
</form>
</article>
+
FOOTER
