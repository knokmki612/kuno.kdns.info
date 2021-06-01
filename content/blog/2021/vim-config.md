---
title: 自分のエディタ事情と(Neo)Vim使ってますという話
date: 2021-06-01T22:13:07+09:00
tags:
  - Tips
  - Vim
archives:
  - 2021
  - 2021-06
---

Vimの設定は[ここ](https://github.com/knokmki612/vim-config)に置いていて、気づけば4か月ほど設定を変えておらず安定してるんだなあと思ったので、記事のネタにすることにした。

### なぜVimを使うのかとか設定の好みの話

お仕事で[VSCode](https://code.visualstudio.com/)のプロジェクトごとの設定をおいたり、[Live Share](https://visualstudio.microsoft.com/ja/services/live-share/)でコミュニケーションをとりながらコードを触ったりするので、VSCodeは入れるようにしている。が、Vimのモードを切り替える感覚から逃れがたいのでVimを使っている。

VSCodeにもVim風のキーバインドを設定できるかもしれないけど、似せるくらいならVimでいいじゃんと思う。基本的に設定しないですむなら設定は書きたくなくて、書くにしても書く量は少なくしたい。

プラグインも設定と同じでなるべく少ないほうがよいと思うし、プラグインの管理のために書く設定も少なくしたい。あまりプラグイン管理まわりのプラグインのことは熱心に調べてはいないものの、[2016年にNeoBundleからdein.vimに切り替えて](https://github.com/knokmki612/vim-config/commit/27e0c06e2b086d3c29e584f81d37fc89cca8cdfa)今に至るらしい。

ここ最近の設定の大きな変更としては、[去年にdein.vimのプラグインはvimrcからdein.tomlに移動したり、aleの代わりにcoc.nvimを入れたりした](https://github.com/knokmki612/vim-config/commit/24662af694801eb9f4b2b5520204f39121a494a1)。

tomlにしたのもcoc.nvimを導入したのも、設定の記述量がそんなに減ったわけではないけども、Vim scriptを書く量が減っているのは嬉しかったかもしれない。つらつら `dein#add` を書いていた箇所がtomlを読むだけになったし、coc.nvimはaleのlinterとかの設定にあたるものは `settings.json` に書くようになった。書きながら思ったけど、もしかして自分はVim scriptが嫌いなのか…？いや多分嫌いではないし好きでもない…

### Neo vimの設定

coc.nvimを入れたときに、Vim対応でありつつもプラグイン名からしてNeo vimのプラグインであることを主張しているので、なんとなく「Neo vimも使えるように準備しておくか…」と思ってNeo vimも使えるようにした。

ただ、Neo vim用の設定を書いてVimとの設定の差異が出てくると、設定に頭を悩ませることになるので、Neo vimの設定は書かないですむようにしたくて[シェルスクリプト](https://github.com/knokmki612/dotfiles/blob/master/local/bin/setup-nvim.sh)を書いた。Vimの設定とカラースキームのシンボリックリンクを張っているだけで、問題なく使えている。[^実は少し設定を調整した]

### (主にcoc.nvimのおかげで)私の用途では問題なさそう

coc.nvimのおかげで[LSP](https://microsoft.github.io/language-server-protocol/)の恩恵が得られたりVSCodeっぽくcocの設定が書けたりlinterとかの連携もできていたりするので、とりあえずnode.jsとかTypeScriptを書くならVSCodeがおすすめされるであろうこのご時世に、心穏やかに過ごせている。

[^実は少し設定を調整した]: ヤンクしたものをクリップボードに入れる設定だけNeo vimと互換性がなかったので[取り除いた](https://github.com/knokmki612/vim-config/commit/cd6c43b40cbbe39e57e40ae678c55e54387c74dd)
