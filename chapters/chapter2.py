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

# # 2章 1次元データの整理

# +
import numpy as np
import pandas as pd

pd.set_option("precision", 3)
# -

df = pd.read_csv("../python_stat_sample/data/ch2_scores_em.csv", index_col="生徒番号")
df.head()

# +
# 英語の点数の最初の１０個を取得
scores = np.array(df["英語"])[:10]

scores

# +
index = [chr(i+ord("A")) for i in range(10)]
scores_df = pd.DataFrame({"点数":scores},
                index=pd.Index(index, name="生徒"))

scores_df
# -

# ## 平均値
#
# \begin{align*}
#     \bar{x} = \frac{1}{N} \sum_{i=0}^{N} x_i
# \end{align*}
#     
# - $\bar{x}: \text{average}$
# - $N: \text{length of data}$
# - $x_i: \text{each data in }x$

sum(scores)/len(scores)

# numpyを使った方法
np.mean(scores)

# pandasを使った方法
scores_df.mean()

# ## 中央値

# 中央値を導出するためにデータを順番に置き直す
scores_sorted = np.sort(scores)
scores_sorted

# +
n = len(scores_sorted)
if n%2 == 0:
    median = (scores_sorted[n//2 - 1] + scores_sorted[n//2])/2
else:
    median = scores_sorted[n//2+1]

median
# -

# numpy
np.median(scores)

# pandas
scores_df.median()

# ## 最頻値

tmp_list = [1, 1, 1, 2, 2, 3]
pd.Series(tmp_list).mode()

# multiple modes in list
tmp_list = [i+1 for i in range(5)]
pd.Series(tmp_list).mode()

# ## 偏差

mean = np.mean(scores)
deviation = scores - mean
deviation

# keep copy of scores_df
summary_df = scores_df.copy()
summary_df["偏差"] = deviation
summary_df

scores_ = [50, 60, 58, 54, 51, 56, 57, 53, 52, 59]
mean_ = np.mean(scores_)
deviation_ = scores_ - mean_
deviation_

# +
# mean of deviation_
mean_deviation = np.mean(deviation_)

mean_deviation
# -

# ### 偏差の平均が0になる理由
#
# \begin{align*}
# \frac{1}{n} \sum_{i=1}^{n}(x_i - \bar{x}) = \frac{1}{n} \sum_{i=1}^{n}x_i - \frac{1}{n} \sum_{i=1}^{n} \bar{x}\\
# = \bar{x} - \bar{x}\\
# = 0
# \end{align*}

# ## 分散

var = np.mean(deviation ** 2)
var_np = np.var(scores) # defaults to sample variance
var_pd = scores_df.var() # defaults to unbiased variance
print(f"variance: {var}")
print(f"variance thru numpy: {var_np}")
print(f"variance thru pandas: {var_pd}")

summary_df["偏差二乗"] = np.square(deviation)
summary_df

# ### 標本分散
# \begin{align*}
# S^2 = \frac{1}{n} \sum_{i=1}^{n}(x_i - \bar{x})^2 \\
# (n > 0)
# \end{align*}
#
# ### 不偏分散
# \begin{align*}
# \sigma^2 = \frac{1}{n-1} \sum_{i=1}^{n}(x_i - \bar{x})^2 \\
# (n > 1)
# \end{align*}
#
# よって標準偏差は以下のようになる
# \begin{align*}
# S = \sqrt{S^2} = \sqrt{\frac{1}{n} \sum_{i=1}^{n}(x_i - \bar{x})^2} \\
# (n > 0)
# \end{align*}

# 標準偏差
np.sqrt(np.var(scores, ddof=0)) # 標本分散を使用
np.std(scores, ddof=0) # 上と同様

# ## 範囲
# \begin{align*}
# \it{Rg} = x_{max} - x_{min}
# \end{align*}

# 範囲
np.max(scores) - np.min(scores)

# ただし, これだと一つでも大きい値または, 小さい値があると範囲が極端になってしまう
# そのため, データの上位数%と下位数%の範囲を用いる場合がある
# これを<b>四分位範囲</b> (interquartile range) という
#
# \begin{align*}
# IQR = Q3 - Q1
# \end{align*}

# 四分位範囲
scores_Q1 = np.percentile(scores, 25)
scores_Q3 = np.percentile(scores, 75)
scores_IQR = scores_Q3 - scores_Q1
scores_IQR

# pandas
pd.Series(scores).describe()
