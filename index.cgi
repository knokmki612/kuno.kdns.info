#!/bin/sh

. ./site.conf

archives=$(. ./cache/archives)
labels=$(. ./cache/labels)

echo 'Content-Type: text/html'
echo ''
# listクエリに必須のpageクエリをかならず頭に持ってくる

queries=$(
	echo $QUERY_STRING                            |
	sed 's/\(.*\)&\(listview\)\(.*\)/\2\&\1\3/'   |
	sed 's/\(.*\)&\(page=[^&]*\)\(.*\)/\2\&\1\3/' |
	tr '&' '\n')

for query in $queries; do
	request_key=$(echo $query | cut -d '=' -f 1)
	request_param=$(echo $query | cut -d '=' -f 2)

	case $request_key in
		history)
			post=$(echo $request_param | sed 's;^;'$POSTS';g')
			article=$(
				cat <<- +
					<pre>
					$(
						git log --pretty=format:"%cd" -p $post/draft |
						sed \
							-e 's/&/\&amp;/g' -e 's/</\&lt;/g' \
							-e 's/>/\&gt;/g' -e 's/"/\&quot;/g' \
							-e 's/&amp;\(lt;\|gt;\|quot;\)/\&\1/g'
					)
					</pre>
					<p class="edit-history"><a href="${URL}post/$request_param">記事に戻る</a></p>
				+
			)
			title="\"$(cat $post/title)\"の編集履歴$TITLE_TAIL"
		;;
		feeds)
			article=$(. ./cache/choose)
			title="購読 $TITLE_TAIL"
		;;
		preview)
			POSTS='preview/'
			post=$(echo $request_param | sed 's;^;'$POSTS';g')
			article=$(. ./$post/html; . ./template-article.html.sh)
			title="$(cat $post/title)$TITLE_TAIL"
			break
		;;
		post)
			post=$(echo $request_param | sed 's;^;'$POSTS';g')
			article=$(
				cat <<- +
					$(. ./$post/html; . ./template-article.html.sh)
					<p class="edit-history"><a href="${URL}?history=$request_param">編集履歴</a></p>
				+
			)
			title="$(cat $post/title)$TITLE_TAIL"
			break
		;;
		listview)
			listview='&amp;listview'
		;;
		page)
			if [ -n "$page" ]; then
				continue
			fi
			echo $request_param | grep -sq -e '[a-z|A-Z]' || page=$request_param
		;;
		archive|label|search)

			if [ -z "$page" ]; then
				page=1
			fi

			pager() {
				case $1 in
					older)
						class='pager-older'
						text='Older »'
						;;
					newer)
						class='pager-newer'
						text='« Newer'
						;;
					next)
						class='pager-older'
						text='Next »'
						;;
					prev)
						class='pager-newer'
						text='« Previous'
						;;
					*)
						echo 'please set 1st argument older or newer' 2>&1
						exit 1
						;;
				esac

				case $2 in
					increase) page_next=$(( $page + 1 )) ;;
					decrease) page_next=$(( $page - 1 )) ;;
					*)
						echo 'please set 2nd argument increase or decrease' 2>&1
						exit 1
						;;
				esac

				echo "<a class=\"$class\" href=\"$URL?$request_key=$request_param&amp;page=$page_next$listview\">$text</a>"
			}

			case $request_key in
				archive)
					if [ $request_param = 'latest' ]; then
						pager_next=$(pager older increase)
						pager_prev=$(pager newer decrease)

						# 最新記事から順番にリストアップする
						title="$SITE_NAME"
						list=$(
							find $POSTS -name html |
							grep -E '[0-9]{14}'    |
							sort -r)
					else
						pager_next=$(pager newer increase)
						pager_prev=$(pager older decrease)

						# 任意の年月日をリストアップする
						year=$(echo $request_param | cut -c 1-4)
						month=$(echo $request_param | cut -c 5-)
						if [ -z "$month" ]; then
							title="${year}年の記事$TITLE_TAIL"
						else
							title="${year}年${month}月の記事$TITLE_TAIL"
						fi
						list=$(
							find $POSTS -name html          |
							grep -e "^$POSTS$request_param" |
							sort)
					fi
					;;
				label)
					pager_next=$(pager older increase)
					pager_prev=$(pager newer decrease)

					# 特定のラベルの記事をリストアップする
					request_param=$(echo $request_param | nkf --url-input)
					title="\"${request_param}\"の記事$TITLE_TAIL"
					list=$(
						find $POSTS -name label        |
						xargs grep -l "$request_param" |
						sed 's/\/label$/\/html/'       |
						sort -r)
					;;
				search)
					pager_next=$(pager next increase)
					pager_prev=$(pager prev decrease)

					request_param=$(
						echo $request_param |
						nkf --url-input     |
						sed \
							-e 's/　\+/ /g' \
							-e 's/+\+/ /g' \
							-e 's/&/\&amp;/g' \
							-e 's/</\&lt;/g' \
							-e 's/>/\&gt;/g')
					title="\"$request_param\"の検索結果$TITLE_TAIL"
					request_param=$(
						echo $request_param |
						sed 's/ /\\|/g')
					hit_pages=$(
						grep -nie $request_param cache/search.sentence |
						cut -d ':' -f 1                                |
						sed 's/^.*$/-e &p /'                           |
						tr -d '\n')
					list=$(
						sed -n $hit_pages cache/search.postname |
						uniq -c                                 |
						sort -nr                                |
						sed -e 's/^ *//' -e 's/$/\/html/'       |
						cut -d ' ' -f 2)
					if [ -z $list ]; then
						article="<p>""\"$request_param\"が含まれる記事はありませんでした。</p>"
						break
					fi
					;;
			esac

			if [ -n "$listview" ]; then
				numofdisplay=20
				xargsdo="list={} ; . ./template-list.html.sh"
				listview_select="<div class=\"list-view\"><a href=\"$URL?$request_key=$request_param\">記事表示</a></div>"
			else
				numofdisplay=3
				xargsdo=". ./{}; . ./template-article.html.sh"
				listview_select="<div class=\"list-view\"><a href=\"$URL?$request_key=$request_param&amp;listview\">リスト表示</a></div>"
			fi
			listcount=$(echo "$list" | wc -l | cut -d ' ' -f 1)
			displaycount=$(( $page * $numofdisplay ))
			# ここの判定はリストの始まりと終わりの挙動を変えるためのもの
			if [ $page -eq 1 ] && [ $listcount -le $displaycount ]; then
				#echo "1ページ目から表示する記事が${numofdisplay}つ以下の場合はこちら"
				article=$(
					echo "$list"                                      |
					head -n $(( $listcount % $numofdisplay > 0 \
						? $listcount % $numofdisplay : $numofdisplay )) |
					xargs -I {} sh -c "$xargsdo")
				pager=$(
					cat <<- PAGER
					<aside id="pager" class="clearfix">
						$listview_select
					</aside>
					PAGER
				)
		elif [ $page -eq 1 ]; then
				#echo "表示する記事が${numofdisplay}つより多いけど1ページ目の場合はこちら"
				article=$(
					echo "$list"          |
					head -n $displaycount |
					xargs -I {} sh -c "$xargsdo")
				pager=$(
					cat <<- PAGER
					<aside id="pager" class="clearfix">
						$pager_next
						$listview_select
					</aside>
					PAGER
				)
			elif [ $listcount -le $displaycount ]; then
				#echo '最後以降のページはこちら'
				article=$(
					echo "$list"                                      |
					tail -n $(( $listcount % $numofdisplay > 0 \
						? $listcount % $numofdisplay : $numofdisplay )) |
					xargs -I {} sh -c "$xargsdo")
				pager=$(
					cat <<- PAGER
					<aside id="pager" class="clearfix">
						$pager_prev
						$listview_select
					</aside>
					PAGER
				)
			else
				#echo '表示するページが2ページ以上あって、その中間のページの場合はこちら'
				article=$(
					echo "$list"          |
					head -n $displaycount |
					tail -n $numofdisplay |
					xargs -I {} sh -c "$xargsdo")
				pager=$(
					cat <<- PAGER
					<aside id="pager" class="clearfix">
						$pager_next
						$pager_prev
						$listview_select
					</aside>
					PAGER
				)
			fi
			break
			;;
		*)
			continue
			;;
	esac

done

. ./template-site.html.sh
