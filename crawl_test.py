#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from icrawler.builtin import GoogleImageCrawler
import sys
import os
import os.path
from datetime import datetime

# http://icrawler.readthedocs.io/en/latest/
#sys.exit()

args = sys.argv
target = ""
dir_name = "images/"
default_word = "hoge"
revenue = 100 #画像の収集数
head_date = (2018, 1, 1) #開始年月日
#fin_date = (2018, 1, 3)
fin_date = datetime.now().date() #現在年月日

# 引数があれば定義（コマンド実行時） なければ初期文字を設定
target = args[1] if len(args) > 1 and args[1] else default_word

# 画像用ディレクトリがなければ作成
if not os.path.isdir(dir_name):
    os.mkdir(dir_name)
new_dir = dir_name + target

# keywordのディレクトリがなければ作成
if not os.path.isdir(new_dir):
    os.mkdir(new_dir)

#sys.exit()

google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=2,
    downloader_threads=4,
    storage={'root_dir': new_dir})
filters = dict(
    size='large',
    color='orange',
    license='commercial,modify',
    date=(head_date, fin_date))

google_crawler.crawl(keyword=target, filters=filters, max_num=revenue, file_idx_offset=0)
