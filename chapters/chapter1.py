# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 1章 データについて

import pandas as pd

# データをインポート
df = pd.read_csv("../python_stat_sample/data/ch1_sport_test.csv", index_col="生徒番号")
df

df["握力"] # 握力だけを抽出

df.shape # データの形を出力 (行, 列)
