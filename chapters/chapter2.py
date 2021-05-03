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
#
# \begin{align*}
# S^2 = \frac{1}{n} \sum_{i=1}^{n}(x_i - \bar{x})^2 \\
# (n > 0)
# \end{align*}
#
# ### 不偏分散
#
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
#
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

# ## データの正規化

# データから平均を引き, 標準偏差で割る操作を__標準化 (standardization)__という<br/>
# また, 標準化されたデータを__標準化変量 (standardization data)__や__Zスコア (z-score)__という<br/>
#
# \begin{align*}
# z_i = \frac{x_i - x}{S}
# \end{align*}

z = (scores - np.mean(scores))/np.std(scores)
z

np.mean(z), np.std(z, ddof=0)

# ### 標準化されたデータの特徴
#
# - 標準化されたデータの平均は0で標準偏差は1になる
#     - (上記のものではそうなっていないように見えるが, 平均の値が極めて0に近いことから無視できる誤差であると言える)
# - データと同じ単位をもつ標準偏差で除算していることから, 標準化されたデータは単位を持たない

# ### 偏差値
#
# 偏差値は平均が50, 標準偏差が10になるように正規化したデータのことをいう<br/>
# 数式では以下のように表す
#
# \begin{align*}
# z_i = 50 + 10 \times \frac{x_i - \bar{x}}{S}
# \end{align*}

z = 50 + 10 * (scores - np.mean(scores))/np.std(scores)
z

np.mean(z), np.std(z, ddof=0)

scores_df["偏差値"] = z
scores_df

# ### 1次元データの視覚化

# +
# 50人分の英語のテストの点数
english_scores = np.array(df["英語"])

pd.Series(english_scores).describe()
# -

# #### 度数分布表
# 分割した区間とデータ数を表にまとめたものを__度数分布表__という
# - 階級 (class)
#     - 区間
# - 階級幅
#     - 階級の幅
# - 階級数
#     - 階級の数
# - 階級値
#     - 各階級の中央値
# - 度数 (frequency)
#     - 各階級に属しているデータの数

freq, _ = np.histogram(english_scores, bins=10, range=(0, 100))
freq

freq_class = [f'{i}~{i+10}' for i in range(0, 100, 10)]
freq_dist_df = pd.DataFrame({"度数":freq}, index=pd.Index(freq_class, name="階級"))
freq_dist_df

# 階級値
class_value = [(i+(i+10))//2 for i in range(0, 100, 10)]
class_value

# ##### 相対度数
# __相対度数__は全データ数に対してその階級のデータが占めている割合の度数を示す

rel_freq = freq/freq.sum()
rel_freq

# #### 累積相対度数
# __累積相対度数__はその階級までの総体度数の和を示す

cum_rel_freq = np.cumsum(rel_freq)
cum_rel_freq

freq_dist_df["階級値"] = class_value
freq_dist_df["相対度数"] = rel_freq
freq_dist_df["累積相対度数"] = cum_rel_freq
freq_dist_df = freq_dist_df[["階級値", "度数", "相対度数", "累積相対度数"]]
freq_dist_df

# 度数分布表から再瀕値を求めることで最も度数の高い階級値を求めることができる<br/>
# _なお, 再瀕値は度数分布表の作り方に大きく依存することを留意する必要がある_

freq_dist_df.loc[freq_dist_df["度数"].idxmax(), "階級値"]

# ### ヒストグラム
# __ヒストグラム (histogram)__は度数分布表を棒グラフで表したもの

import matplotlib.pyplot as plt
# %matplotlib inline

# +
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

freq, _, _ = ax.hist(english_scores, bins=10, range=(0, 100))
ax.set_xlabel("点数", )
ax.set_ylabel("人数")
ax.set_xticks(np.linspace(0, 100, 10+1))
ax.set_yticks(np.arange(0, freq.max()+1))
plt.show()
# -
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
freq, _, _ = ax.hist(english_scores, bins=25, range=(0, 100))
ax.set_xlabel("点数", )
ax.set_ylabel("人数")
ax.set_xticks(np.linspace(0, 100, 25+1))
ax.set_yticks(np.arange(0, freq.max()+1))
plt.show()

# +
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

weights = np.ones_like(english_scores)/len(english_scores)
rel_freq, _, _ = ax1.hist(english_scores, bins=25, range=(0, 100), weights=weights)
cum_rel_freq = np.cumsum(rel_freq)
class_value = [(i+(i+4))//2 for i in range(0, 100, 4)]
ax2.plot(class_value, cum_rel_freq, ls='--', marker='o', color='gray')
ax2.grid(visible=False)
ax1.set_xlabel("点数")
ax1.set_ylabel("累積相対度数")
ax2.set_ylabel("相対度数")
ax2.set_xticks(np.linspace(0, 100, 25+1))

plt.show()
