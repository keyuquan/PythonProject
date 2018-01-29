#!/usr/bin/python
# encoding: utf-8

"""
拼写检查器:在输入某个字符串后 预测后面可能输入的字符串

"""
import re, collections

# 把语料中的单词全部抽取出来, 转成小写, 并且去除单词中间的特殊符号
def words(text): return re.findall('[a-z]+', text.lower())

# 统计各个词语出现的次数
def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

def edits1(word):
    n = len(word)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return set([word[0:i] + word[i + 1:] for i in range(n)] +  # deletion
               [word[0:i] + word[i + 1] + word[i] + word[i + 2:] for i in range(n - 1)] +  # transposition
               [word[0:i] + c + word[i + 1:] for i in range(n) for c in alphabet] +  # alteration
               [word[0:i] + c + word[i:] for i in range(n + 1) for c in alphabet])  # insertion


# 找出 抽取 的词语中 包含已输入字符串 的词语
def known(words,NWORDS): return set(w for w in words if w in NWORDS)


# 如果known(set)非空, candidate 就会选取这个集合, 而不继续计算后面的
def correct(word,NWORDS):
    candidates = known([word],NWORDS) or known(edits1(word),NWORDS)
    # 找出抽取词语中 出现次数最多的 词语
    return max(candidates, key=lambda w: NWORDS[w])

def main():
    NWORDS = train(words(open('big.txt').read()))
    print(correct("chan",NWORDS))


if __name__ == "__main__":
    main()
