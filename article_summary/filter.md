# Benchmark of filter methods for feature selection in high-dimensional gene expression survival data

#### 摘要

We compare 14 filter methods for feature selection based on 11 high-dimensional gene expression survival data sets.

此外，我们还考虑了运行时间、用于拟合具有高预测精度的模型的所选特征的数量以及特征选择的稳定性。
我们得出的结论是，**简单方差滤波器优于所有其他考虑的滤波器方法**。 

该过滤器选择具有最大方差的特征，并且不考虑生存结果。

 此外，我们将相关性调整回归分数过滤器视为一种更精细的替代方案，允许以类似的预测精度拟合模型。
此外，我们还研究了基于特征排名的过滤方法，找到相似过滤器的组。

#### 简介

For many filter methods, the score calculation can be done in
parallel, thus resulting in increased computational efficiency.

An extensive overview of existing filter methods is given in [2].
Wrapper methods [3] consider subsets of the set of all features.

别人的文章

In [22], filter methods are compared based on two
gene expression data sets, counting the number of misclassified
samples. In [23], the classification accuracy of different filter,
wrapper, and embedded methods on several artificial data sets
is analyzed. In [24, 25], filter methods are compared with respect
to classification accuracy based on microarray data sets. In [26,
27], extensive comparisons based on text classification data sets
are conducted. The authors analyze filter and wrapper methods,
respectively. In [28], filter methods are compared with respect
to classification accuracy on malware detection data. In [29,
30], filter methods are studied on large data sets, analyzing the
predictive accuracy with respect to the number of features to
select. In [31, 32], small artificial data sets are used to assess
whether the correct features are selected. In [31], different fea-
ture selection methods are compared while in [32], only filter
methods are considered. In [33], filter and wrapper methods
are compared on large simulated data sets with respect to the
correctness of the selected features. Additionally, the authors
conduct comparisons with respect to classification accuracy on
real data sets. In [34], filter and wrapper methods are compared
comprehensively with respect to classification accuracy and run
time, considering each of the two objectives separately. Most
of the data sets on which the comparison is based contain a
small or medium number of features. In [35, 36], several filter
methods that are based on mutual information are compared. In
[35], the accuracy and the run time of the methods are analyzed
separately. Additionally, the authors take into account theoret-
ical properties and look at the proportions of correctly identi-
fied features on artificial data. In [36], the authors analyze the
classification accuracy with respect to the number of selected
features and search for Pareto optimal methods considering the
accuracy and feature selection stability. In [37], an extensive
study of correlation-based feature selection is conducted. The
author analyzes the classification accuracy based on real data
sets as well as the choice of relevant or irrelevant features
based on artificial data sets. In [38], an extensive comparison of
22 filter methods on 16 large or high-dimensional data sets is
conducted with respect to both classification accuracy and run
time jointly. Also, the empirical similarity of the filter methods
based on the rankings of all features of all considered data sets
is analyzed. In [39], the authors perform hyper parameter tuning
of predictive models on survival data sets. They use combined
methods consisting of a filter and a survival prediction method
and consider the choice of filter method as a hyper parameter.
This way, they find out which filter methods yield good results
on many data sets.

#### 方法

#### 实验

#### 结论

#### 数据获取

