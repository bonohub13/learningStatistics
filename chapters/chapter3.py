# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 3章 2次元データの整理

# +
import numpy as np
import pandas as pd

# %precision 3
pd.set_option("precision", 3)
# -

df = pd.read_csv("../python_stat_sample/data/ch2_scores_em.csv", index_col="生徒番号")
en_scores = np.array(df["英語"])[:10]
ma_scores = np.array(df["数学"])[:10]

scores_df = pd.DataFrame({"英語": en_scores, "数学": ma_scores}, 
                         index=pd.Index([chr(ord('A')+i) for i in range(10)]))
scores_df

# - - -
#
# ## 2つのデータの関係性の指標
#
# - 正の相関
#     - 片方のデータが上下に変動した際に, もう片方のデータも似たように上下に変動する関係性をもつこと
# - 負の相関
#     - 片方のデータが上下に変動した際に, もう片方のデータは逆に変動する関係性をもつこと
# - 無相関
#     - 片方のデータが上下に変動しても, もう片方のデータに影響を及ぼさない関係性をもつこと
#     
# - - -
#
# ### 共分散
# 2つのデータが互いにどのような関係性 (相関) をもっているかを表す際に用いられる

summary_df = scores_df.copy()
summary_df["英語の偏差"] = summary_df["英語"] - summary_df["英語"].mean()
summary_df["数学の偏差"] = summary_df["数学"] - summary_df["数学"].mean()
summary_df["偏差同士の積"] = summary_df["英語の偏差"] * summary_df["数学の偏差"]
summary_df

summary_df["偏差同士の積"].mean()

# これらから英語の点数と数学の点数は正の相関をもっているといえる。
#
# 共分散の式: 
#
# \begin{align*}
# S_{xy} = \frac{1}{n}\sum^{n}_{i=1}(x_i - \bar{x})(y_i - \bar{y}) \\
#        = \frac{1}{n}{(x_1 - \bar{x})(y_1 - \bar{y}) + (x_2 - \bar{x})(y_2 - \bar{y})+ \dots +(x_n - \bar{x})(y_n - \bar{y})}
# \end{align*}
#
# Numpyの場合, 共分散はcov関数を用いることで求められる。しかし, 返り値は共分散ではなく__共分散行列 (covariance matrix)__または__分散共分散行列 (variance-covariance matrix)__という行列になってしまうことを留意する必要がある。

cov_mat = np.cov(en_scores, ma_scores, ddof=0)
cov_mat

np.var(en_scores, ddof=0), np.var(ma_scores, ddof=0)

# - - -
#
# ### 相関係数
#
# 単位に依存しない相関を表す指標。
# - 相関係数 (correlation coefficient)
#     - 必ず-1から1の間をとる
#     - データが正の相関をもつほど1に近づく
#     - 逆に負の相関をもつほど-1に近づく
#     - 無相関であれば0になる
#     - また, -1か1であれば完全に直線上のデータになる
#
# \begin{align*}
# r_{xy} = \frac{S_{xy}}{S_xS_y} \\
# = \frac{1}{n}\sum^{n}_{i=1} (\frac{x_i - \bar{x}}{S_x})({\frac{y_i - \bar{y}}{S_y}})
# \end{align*}

np.cov(en_scores, ma_scores, ddof=0)[0, 1] / (np.std(en_scores) * np.std(ma_scores))

np.corrcoef(en_scores, ma_scores)

scores_df.corr()


