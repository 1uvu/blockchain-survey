#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   analyzer.py
@Desc    :   
@Project :   src
@Contact :   1uvu.zhang@gmail.com
@License :   (C)Copyright 2018-2020, 1UVU.COM
@WebSite :   1uvu.com
@Modify Time           @Author        @Version
------------           -------        --------
2020/08/14 20:14       1uvu           1.0         
"""
import pandas as pd
import numpy as np
import re

""" 手工
1.
时间格式化->year mouth：all
合并
2.
publisher，cite，factor 忽略
3.
topics 处理 **
"""
# format
# df = pd.read_excel("./out/new/springer.xlsx")
# date = df["date"]
# dd = []
# for d in date:
#     if d != None:
#         dd.append(re.split("-", str(d))[0])
#     else:
#         dd.append("")
# df["date"] = dd
#
# df.to_excel("./out/new/springer-tf.xlsx", index=False)

# merge
# utils

# remove blank
df = pd.read_excel("./out/all-filtered.xlsx")
print(df.isnull().any())
d = df.dropna(axis=0, subset=["topics"])
print(d.isnull().any())
d.to_excel("./out/all-filtered-has_topics.xlsx", index=False)

# rank
df = pd.read_excel("./out/all-filtered-has_topics.xlsx")
topic_items = df["topics"]
topics = []
for t_item in topic_items:
    ts = re.split(",", str(t_item))
    for t in ts:
        if t != "":
            topics.append(t.replace("\xa0", ""))
from collections import Counter

topics_rank = dict(Counter(topics))

f = open("./out/topics_simple_rank.txt", "w", encoding="utf-8")
i = 1
for topic in sorted(topics_rank.items(), key=lambda x: x[1], reverse=True):
    f.write(f"({i}) {topic[0]}: {topic[1]} \n")
    print(f"({i}) {topic[0]}: {topic[1]}")
    i += 1
f.close()

# # rm titles
#
# """
# B/blockchain-B/based
# B/blockchain B/based
# B/based on
# """
# ts = []
# with open("./out/titles-6.txt", "r", encoding="utf-8") as f:
#     for t in f.readlines():
#         if "based" not in t:
#             ts.append(t)
#
# f.close()
# with open("./out/titles-7.txt", "w", encoding="utf-8") as f:
#     for t in ts:
#         f.write(t)
#
# df = pd.read_excel("./out/all-filtered.xlsx")
# f = open("./out/titles.txt", "r", encoding="utf-8")
# titles = [s.strip() for s in f.readlines()]
#
# # i=0
# # for t in df["title"]:
# #     print(t + ": " + titles[i])
# #     print(t in titles)
# #     i+=1
# df1 = df[df['title'].isin(titles)]
#
# df1.to_excel("./out/all-filter_by_title.xlsx", index=False)