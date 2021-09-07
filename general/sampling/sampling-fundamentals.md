## LOCAL CASE-CONTROL SAMPLING: EFFICIENT SUBSAMPLING
Available: https://arxiv.org/pdf/1306.3706.pdf\
Added By: Samuel Atkins\
Recommendation: A great read to learn about a relatively modern sampling technique that combats marginal and conditional imbalance by factoring in the importance of the data points
> For classification problems with significant class imbalance, subsampling can reduce computational costs at the price of inflated variance in estimating model parameters. We propose a method for subsampling efficiently for logistic regression by adjusting the class balance locally in feature space via an accept–reject scheme. Our method generalizes standard case-control sampling, using a pilot estimate to preferentially select examples whose responses are conditionally rare given their features. The biased subsampling is corrected by a post-hoc analytic adjustment to the parameters. The method is simple and requires one parallelizable scan over the full data set. 
\
Standard case-control sampling is inconsistent under model misspecification for the population risk-minimizing coefficients 
θ∗. By contrast, our estimator is consistent for θ∗ provided that the pilot estimate is. Moreover, under correct specification and with a consistent, independent pilot estimate, our estimator has exactly twice the asymptotic variance of the full-sample MLE—even if the selected subsample comprises a miniscule fraction of the full data set, as happens when the original data are severely imbalanced. The factor of two improves to 1 + 1/c if we multiply the baseline acceptance probabilities by c > 1 (and weight points with acceptance probability greater than 1), taking roughly (1 + c)/2 times as many data points into the subsample. Experiments on simulated and real data show that our method can substantially outperform standard case-control subsampling.
Motivation:
- Marginal and conditional imbalance plague many classification and regression problems
- By sampling in a more efficient way, the size of the dataset can be significantly reduced and more complex models and methods can be utilized
Contribution:
- "local case-control sampling"
- We create a pilot model (a model that is a good estimate of the true parameters)
- We use this pilot model to compute p(x_i)
- We accept (x_i, y_i) with probability |y_i - p(x_i)|
- This means that if the difference between the target and the value predicted by the pilot model is large, then we will likely keep this point because it is "surprising"
- This process yields a dataset that is significantly smaller than the original dataset as data points that are predicatble by the pilot model have a low sampling probability
## Diversity Creation Methods: A Survey and Categorization
Available: https://researchgate.net/publication/222530052_Diversity_Creation_Methods_A_Survey_And_Categorisation\
Added By: Samuel Atkins\
Recommendation:
>Ensemble approaches to classification and regression have attracted a great deal
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
classification error diversity
Insights:
## Exploratory Undersampling for Class-Imbalance Learning
Available: https://ieeexplore.ieee.org/document/4717268\
Added By: Samuel Atkins\
Recommendation:
>Undersampling is a popular method in dealing with class-imbalance problems, which uses only a subset of the majority class and thus is very efficient. The main deficiency is that many majority class examples are ignored. We propose two algorithms to overcome this deficiency. EasyEnsemble samples several subsets from the majority class, trains a learner using each of them, and combines the outputs of those learners. BalanceCascade trains the learners sequentially, where in each step, the majority class examples that are correctly classified by the current trained learners are removed from further consideration. Experimental results show that both methods have higher Area Under the ROC Curve, F-measure, and G-mean values than many existing class-imbalance learning methods. Moreover, they have approximately the same training time as that of undersampling when the same number of weak classifiers is used, which is significantly faster than other methods.
Insights: