---
title: Let's Encryptを使ってサイトをhttpsな感じにした
date: 2015-12-22T14:23:12+09:00
tags:
  - Tips
  - お知らせ
archives:
  - 2015
  - 2015/12
---

サーバー証明書の取得がこんな簡単にできるとは思わなかった...

参考にしたページ

- [Let's EncryptでValidなSSL/TLS証明書を取得する ｜ Developers.IO](http://dev.classmethod.jp/server-side/lets-encrypt-beta/)
- [Apache 2.4系でHTTP2対応サーバを構築してみるテスト。［Let's Encrypt編］](https://http2.try-and-test.net/letsencrypt.html)

お勧められていない`letsencrypt-auto --apache`を使ってみましたが、勝手にApacheでの証明書の指定もやってくれましたし良かったです。
