#!/usr/bin/python
# encoding: utf-8

"""
回归涉及的概念
一.定义
1.回归：指研究一组随机变量(Y1 ,Y2 ,…,Yi)和另一组(X1,X2,…,Xk)变量之间关系的统计分析方法,又称多重回归分析
2.线性回归：线性回归是利用数理统计中回归分析,来确定两种或两种以上变量间相互依赖的定量关系的一种统计分析方法,运用十分广泛。
其表达形式为 y = w'x+e,e为误差服从均值为0的正态分布
3.逻辑回归：logistic回归是一种广义线性回归（generalized linear model）,因此与多重线性回归分析有很多相同之处。它们的模型形式基本上相同,
都具有 w‘x+b,其中w和b是待求参数,其区别在于他们的因变量不同,多重线性回归直接将w‘x+b作为因变量,即y =w‘x+b,
而logistic回归则通过函数L将w‘x+b对应一个隐状态p,p =L(w‘x+b),然后根据p 与1-p的大小决定因变量的值。如果L是logistic函数,
就是logistic回归,如果L是多项式函数就是多项式回归,机器学习的 l 一般为  sigmod函数 L=1/(1+e^(-y)),y=w‘x+b
4.梯度下降：梯度下降法(gradient descent)是一个最优化算法,通常也称为最速下降法。常用于机器学习和人工智能当中用来递归性地逼近最小偏差模型

二.难点
1.用梯度下降问题解决回归问题


三.算法相关数学知识
* 排列组合
 https://jingyan.baidu.com/article/63acb44ac60d4e61fcc17e2e.html
* 二项式分布
https://baike.baidu.com/item/%E4%BA%8C%E9%A1%B9%E5%88%86%E5%B8%83/1442377?fr=aladdin&fromid=3565421&fromtitle=%E4%BA%8C%E9%A1%B9%E5%BC%8F%E5%88%86%E5%B8%83
* 正态分布
https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83&rsv_spt=1&oq=%25E6%2599%25BA%25E8%2581%2594&rsv_pq=d208ecf600049ed1&rsv_t=e900CBzvOlNi08HwZYqwb%2Bz%2BKObaP3wvIVvLbtfgqW3T22p1%2BE7STpfsK9x4sw%2Bf4yEO&rqlang=cn&rsv_enter=1&inputT=7892&rsv_sug3=19&rsv_sug1=18&rsv_sug7=101&rsv_sug2=0&rsv_sug4=9506&rsv_sug=1
* sigmod函数
 https://baike.baidu.com/item/Sigmoid%E5%87%BD%E6%95%B0/7981407?fr=aladdin


"""