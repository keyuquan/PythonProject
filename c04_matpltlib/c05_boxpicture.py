#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import pandas as pd

# 盒子图
reviews = pd.read_csv('fandango_scores.csv')
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[num_cols]

fig, ax = plt.subplots()
ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_ylim(0,5)
plt.show()


