---
title: {{ replace .Name "-" " " | title }}
date: {{ .Date }}
tags:
  - 日記
archives:
  - {{ now.Format "2006" }}
  - {{ now.Format "2006/01" }}
draft: true
---

