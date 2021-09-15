# Index
- [LOCAL CASE-CONTROL SAMPLING: EFFICIENT SUBSAMPLING](#local-case-control-sampling-efficient-subsampling)
- [Diversity creation methods: a survey and categorisation](#diversity-creation-methods-a-survey-and-categorisation)
- [Selection via Proxy: Efficient Data Selection for Deep Learning](#selection-via-proxy-efficient-data-selection-for-deep-learning)

## LOCAL CASE-CONTROL SAMPLING: EFFICIENT SUBSAMPLING
##### Authors: William Fithian, Trevor Hastie
###### Published: 2014
Available: https://arxiv.org/pdf/1306.3706.pdf\
Added By: Samuel Atkins\
Recommendation: A great read to learn about a relatively modern sampling technique that combats marginal and conditional imbalance by factoring in the importance of the data points

> For classification problems with significant class imbalance, subsampling can reduce computational costs at the price of inflated variance in estimating model parameters. We propose a method for subsampling efficiently for logistic regression by adjusting the class balance locally in feature space via an accept–reject scheme. Our method generalizes standard case-control sampling, using a pilot estimate to preferentially select examples whose responses are conditionally rare given their features. The biased subsampling is corrected by a post-hoc analytic adjustment to the parameters. The method is simple and requires one parallelizable scan over the full data set. 
\
Standard case-control sampling is inconsistent under model misspecification for the population risk-minimizing coefficients 
θ∗. By contrast, our estimator is consistent for θ∗ provided that the pilot estimate is. Moreover, under correct specification and with a consistent, independent pilot estimate, our estimator has exactly twice the asymptotic variance of the full-sample MLE—even if the selected subsample comprises a miniscule fraction of the full data set, as happens when the original data are severely imbalanced. The factor of two improves to 1 + 1/c if we multiply the baseline acceptance probabilities by c > 1 (and weight points with acceptance probability greater than 1), taking roughly (1 + c)/2 times as many data points into the subsample. Experiments on simulated and real data show that our method can substantially outperform standard case-control 

### Summary:
Method:
- Marginal and conditional imbalance plague many classification and regression problems
- By sampling in a more efficient way, the size of the dataset can be significantly reduced and more complex models and methods can be utilized
Contribution:
- "local case-control sampling"
- We create a pilot model (a model that is a good estimate of the true parameters)
- We use this pilot model to compute p(x_i)
- We accept (x_i, y_i) with probability |y_i - p(x_i)|
- This means that if the difference between the target and the value predicted by the pilot model is large, then we will likely keep this point because it is "surprising"

Results:
- This process yields a dataset that is significantly smaller than the original dataset as data points that are predicatble by the pilot model have a low sampling probability


<br />

*Insights:*
- Perhaps most of the computational load that is faced during a validation/ML pipeline is redundant
    - If most of the points are predictable and don't actually improve the ability of the model, why are we spending hours analyzing them?


## Diversity creation methods: a survey and categorisation
##### Authors: Gavin Brown, Jeremy L Wyatt, Rachel Harris, Xin Yao
###### Published: 2005

<br />

Available: https://www.researchgate.net/publication/222530052_Diversity_Creation_Methods_A_Survey_And_Categorisation<br />

Summary:  
- IPR

<br />

> Ensemble approaches to classification and regression have attracted a great deal
of interest in recent years. These methods can be shown both theoretically and
empirically to outperform single predictors on a wide range of tasks. One of the
elements required for accurate prediction when using an ensemble is recognised to
be error “diversity”. However, the exact meaning of this concept is not clear from
the literature, particularly for classification tasks. In this paper we first review the
varied attempts to provide a formal explanation of error diversity, including several
heuristic and qualitative explanations in the literature. For completeness of discussion we include not only the classification literature but also some excerpts of the
rather more mature regression literature, which we believe can still provide some
insights. We proceed to survey the various techniques used for creating diverse ensembles, and categorise them, forming a preliminary taxonomy of diversity creation
methods. As part of this taxonomy we introduce the idea of implicit and explicit
diversity creation methods, and three dimensions along which these may be applied.
Finally we propose some new directions that may prove fruitful in understanding
classification error diversity.


### Summary
- "Error diversity" is key to creating successful classifiers
*How do ensembles encourage better performance?*
- Each memeber of an ensemble is a realisation of the random variable defined by the distribution over all possible training datasets and weight initializations
    - By increasing the number of members in an ensemble we are reducing the variance of our estimate and bringing our estimate closer to the true estimate (assuming we are dealing with an un-biased estimator)



<br />

*Insights:*
- IPR

## Selection via Proxy: Efficient Data Selection for Deep Learning
##### Authors: Cody Coleman, Christopher Yeh, Stephen Mussmann, Baharan Mirzasoleiman, Peter Bailis, Percy Liang, Jure Leskovec, Matei Zaharia
###### Published: 2019

<br />

Available: https://arxiv.org/pdf/1906.11829.pdf<br />

Summary:  
- "Selection via proxy" (SVP) is a technique that shrinks the size of the original dataset using active learning/core-set selection
    - This method boasts up to 41.9x run-time improvements when compared to the existing data selection techniques

<br />

> Data selection methods, such as active learning and core-set selection, are useful tools for machine learning on large datasets. However, they can be prohibitively expensive to apply in deep learning because they depend on feature representations that need to be learned. In this work, we show that we can greatly improve the computational efficiency by using a small proxy model to perform data selection (e.g., selecting data points to label for active learning). By removing hidden layers from the target model, using smaller architectures, and training for fewer epochs, we create proxies that are an order of magnitude faster to train. Although these small proxy models have higher error rates, we find that they empirically provide useful signals for data selection. We evaluate this "selection via proxy" (SVP) approach on several data selection tasks across five datasets: CIFAR10, CIFAR100, ImageNet, Amazon Review Polarity, and Amazon Review Full. For active learning, applying SVP can give an order of magnitude improvement in data selection runtime (i.e., the time it takes to repeatedly train and select points) without significantly increasing the final error (often within 0.1%). For core-set selection on CIFAR10, proxies that are over 10x faster to train than their larger, more accurate targets can remove up to 50% of the data without harming the final accuracy of the target, leading to a 1.6x end-to-end training time improvement.

### Summary
*"Active learning" (https://www.datacamp.com/community/tutorials/active-learning):*
- The main hypothesis is that if a learning algorithm is able to choose the data that it learns from it will beform much better than traditional methods
- When a model is given a large amount of data randomly sampled from the underlying distrubtion it is "passively learning"
    - Conversely, when the model is given a smaller number of more expressive points it is "actively learning"


Method:
- Selection via proxy (SVP) uses the feature representation from a less computationally intensive proxy model to select points to label for a much more computationally expensive classifier
- To make these proxy models, we scale down deep learning models by removing layers, using smaller model architectures, and training them for fewer epochs
- For their active learning improvement, they followed the traditional iterative procedure of training and selecting points to label but replaced the target model with a cheaper-to-compute proxy model
- For core-set selection, they learned a feature representation over the data using a proxy model and then used it to select points that were passed to a much larger model

Results:
- For the active learning and core-set techniques, their method achieved similar or higher accuracy and up to a 41.9x improvement in data selection runtime

<br />

*Insights:*
- By incorporating a method like this into our validation work, we could experience extreme run-time improvements and potentially stronger model performance
