# Index
- [Efficient Logistic Regression on Large Encrypted Data](#efficient-logistic-regression-on-large-encrypted-data)
- [Logistic Regression Model Training based on the Approximate Homomorphic Encryption](#logistic-regression-model-training-based-on-the-approximate-homomorphic-encryption)
- [Logistic regression over encrypted data from fully homomorphic encryption](#logistic-regression-over-encrypted-data-from-fully-homomorphic-encryption)
- [Secure Logistic Regression Based on Homomorphic Encryption: Design and Evaluation](#secure-logistic-regression-based-on-homomorphic-encryption-design-and-evaluation)

## Efficient Logistic Regression on Large Encrypted Data
##### Authors: Kyoohyung Han, Seungwan Hong, Jung Hee Cheon, and Daejun Park
###### Published: 2018

<br />

Available: https://eprint.iacr.org/2018/662.pdf<br />
Summary:
- HEAAN/CKKS encryption scheme
- Method shows "practical" logistic regression model that utilizes "approximate HE", the CKKS packing method in conjunction with SIMD operations, parallelized bootstrapping, clever training data packing, polynomial approximations for non-polynomial functions, mini-batch gradient descent, and NAG
- The model takes 17 hours to train and achieves an accuracy of 96.4%

> Machine learning on encrypted data is a cryptographic method
for analyzing private and/or sensitive data while keeping privacy. In the
training phase, it takes as input an encrypted training data and outputs
an encrypted model without using the decryption key. In the prediction
phase, it uses the encrypted model to predict results on new encrypted
data. In each phase, no decryption key is needed, and thus the privacy of
data is guaranteed while the underlying encryption is secure. It has many
applications in various areas such as finance, education, genomics, and
medical field that have sensitive private data. While several studies have
been reported on the prediction phase, few studies have been conducted
on the training phase due to the inefficiency of homomorphic encryption
(HE), leaving the machine learning training on encrypted data only as a
long-term goal.
In this paper, we propose an efficient algorithm for logistic regression on
encrypted data, and evaluate our algorithm on real financial data consisting of 422,108 samples over 200 features. Our experiment shows that
an encrypted model with a sufficient Kolmogorov Smirnow statistic value
can be obtained in ∼17 hours in a single machine. We also evaluate our
algorithm on the public MNIST dataset, and it takes ∼2 hours to learn
an encrypted model with 96.4% accuracy. Considering the inefficiency of
HEs, our result is encouraging and demonstrates the practical feasibility
of the logistic regression training on large encrypted data, for the first
time to the best of our knowledge.

Method:
- HEAAN/CKKS encryption scheme
- Fully-encrypted training and inference (no decryption key for either phase)
- "Approximate HE" (HEAAN)
    - Reduces computational overheads
    - Adds additional noise for each computation step that may affect the overall ML performance (unclear how significant this is)
- Utilizes the "packing method" ("Homomorphic encryption for arithmetic of approximate numbers" - CKKS paper) in conjunction with "SIMD" operations
    - SIMD = Single Instruction/Multiple Data
        - It only takes one instruction to multiply a batch of data together
        - This results in fewer instructions to process data
- Parallelized bootstrapping (because bootstrapping is the most computationally intensive operation)
- Clever training data packing (the training data is partitioned into m' x n' partitions where m' x n' is the maximum size of the ciphertexts)
- All non-polynomial functions are approximated as polynomial functions
    - Sigmoid is approximated
- Mini-batch gradient descent because SGD does not utilize the maximum capacity of each ciphertext and GD requires ciphertexts that are too large
- "Nesterov Accelerated Gradient Optimizer" because it is fast and doesn't use division


Results:
- Takes ~17 hours to train a model on a dataset of size 422,108 x 200
- Model has 96.4% accuracy on the testing dataset
- Kolmogorov Smirnov statistic value of 50.84
    - KS statistic value is a value that determines how similar two samples are (how likely it is that one sample came from the other)

<br />

*Insights:*
- 17 hours to train is very long
    - With a training time this long, the model likely has poor generalization, is difficult to validate, and cannot be actually implemented
- 96.4% is not exactly a useful metric
    - What about recall, precision, etc.? This could just be predicting 1 on a fraud dataset. What is the problem type?
- Big banks have extensive validation pipelines to make sure that their models are not acting unfairly. Explainability is huge. How can a model like this ever be implemented in the real world?
    - The feasability of homomorphic encryption is difficult to see
- Bootstrapping dominates the overall training time and so improvements in the bootstrapping operation is the key to contributing to the field
- Could compare SGD, mini-batch GD, GD performances in HE

## Logistic Regression Model Training based on the Approximate Homomorphic Encryption
##### Authors: Andrey Kim, Yongsoo Song, Miran Kim, Keewoo Lee, and Jung Hee Cheon
###### Published: 2018

<br />

Available: https://eprint.iacr.org/2018/254.pdf<br />

Summary:  
- HEAAN/CKKS encryption scheme
- Done in response to the 2017 iDASH competition
- Introduces and evaluates a LR model that utilizes packing and NAG
- The model is trained on a tiny dataset and yields a training time of 6 minutes (which is somehow comparatively fast)
- Research performed by CKKS authors (these are not data scientists)

<br />

> Security concerns have been raised since big data became a prominent tool in data
analysis. For instance, many machine learning algorithms aim to generate prediction models
using training data which contain sensitive information about individuals. Cryptography community is considering secure computation as a solution for privacy protection. In particular,
practical requirements have triggered research on the efficiency of cryptographic primitives.
This paper presents a practical method to train a logistic regression model while preserving
the data confidentiality We apply the homomorphic encryption scheme of Cheon et al. (ASIACRYPT 2017) for an efficient arithmetic over real numbers, and devise a new encoding method
to reduce storage of encrypted database. In addition, we adapt Nesterov’s accelerated gradient
method to reduce the number of iterations as well as the computational cost while maintaining
the quality of an output classifier.
Our method shows a state-of-the-art performance of homomorphic encryption system in a realworld application. The submission based on this work was selected as the best solution of Track
3 at iDASH privacy and security competition 2017. For example, it took about six minutes to
obtain a logistic regression model given the dataset consisting of 1579 samples, each of which
has 18 features with a binary outcome variable.

Method:
- Packing method utilized
- NAG for convergence rate

Results:
- Performance evaluated on a 1579 x 18 dataset
- Training time is 6 minutes (this was compared with some of the other methods but different storage capacities were used so it is difficult to quantify the performance increase/decrease)

<br />

*Insights:*
- A 1579 x 18 dataset is pathetically small and would never be used in any real application
    - Scaling this up would result in training times that are not practical. These mathematicians are forgetting about HP tuning, data analysis techniques, and the core principles that data scientists follow
        - Companies don't own "advanced proprietary models" that need to be protected or used as a service
        - Models need to be validated in order to be used by most institutions

## Logistic regression over encrypted data from fully homomorphic encryption
##### Authors: Hao Chen, Ran Gilad-Bachrach, Kyoohyung Han, Zhicong Huang, Amir Jalali, Kim Laine, Kristin Lauter
###### Published: 2018

<br />

Available: https://eprint.iacr.org/2018/462.pdf<br />

Summary:  
- BFV encryption scheme
- Done in response to the 2017 iDASH competition
- The 1-Bit GD method offers training time improvements and sacrifices some performance in turn
- These datasets do not approximate practical data science scenarios

<br />

> One of the tasks in the 2017 iDASH secure genome analysis competition was to enable training of logistic regression models over
encrypted genomic data. More precisely, given a list of approximately
1500 patient records, each with 18 binary features containing information on specific mutations, the idea was for the data holder to encrypt the
records using homomorphic encryption, and send them to an untrusted
cloud for storage. The cloud could then apply a training algorithm on the
encrypted data to obtain an encrypted logistic regression model, which
can be sent to the data holder for decryption. In this way, the data holder
could successfully outsource the training process without revealing either
her sensitive data, or the trained model, to the cloud. Our solution to this
problem has several novelties: we use a multi-bit plaintext space in fully
homomorphic encryption together with fixed point number encoding; we
combine bootstrapping in fully homomorphic encryption with a scaling
operation in fixed point arithmetic; we use a minimax polynomial approximation to the sigmoid function and the 1-bit gradient descent method
to reduce the plaintext growth in the training process. As a result, our
training over encrypted data takes 0.4–3.2 hours per iteration of gradient
descent.

Method:
- BFV encryption scheme
- Polynomial approximation of the Sigmoid function
- Batching of vectors and SIMD operations
- Modified 1-Bit GD with data batching
- Tested their method on a 1579 x 18 dataset and a modified binary classification version of the MNIST dataset ("3" or "8")

Results:
- iDASH dataset:
    - GD: 115.33h training time, 0.690/0.690 AUC scores (encrypted/unencrypted)
    - 1-Bit GD: 14.9h training time, 0.668/0.690 AUC scores (encrypted/unencrypted)
- BC MNIST:
    - GD: 48.76h training time,  0.974/0.977 AUC scores (encrypted/unencrypted)
    - 1-Bit GD: 27.1h training time, 0.974/0.978 AUC scores (encrypted/unencrypted)

<br />

*Insights:*
- Just as with the CKKS logistic regression experiments, a 1579 x 18 dataset is pathetically small
    - No real considerations to a real data science problem
- The 1-Bit GD method using the BFV scheme offers training time improvements and sacrifices some performance

## Secure Logistic Regression Based on Homomorphic Encryption: Design and Evaluation
##### Authors: Miran Kim, Yongsoo Song, Shuang Wang, Yuhou Xia, and Xiaoqian Jiang
###### Published: 2018
<br />

Available: https://eprint.iacr.org/2018/074.pdf<br />

Summary:  
- Homomorphic encryption was used to create a logistic regression model
- CKKS encryption scheme was used
- Degree 3 and 7 polynomial approximations were compared

<br />

> Learning a model without accessing raw data has been an intriguing idea to the
security and machine learning researchers for years. In an ideal setting, we want to encrypt
sensitive data to store them on a commercial cloud and run certain analysis without ever
decrypting the data to preserve the privacy. Homomorphic encryption technique is a promising
candidate for secure data outsourcing but it is a very challenging task to support real-world
machine learning tasks. Existing frameworks can only handle simplified cases with low-degree
polynomials such as linear means classifier and linear discriminative analysis.
The goal of this study is to provide a practical support to the mainstream learning models
(e.g. logistic regression). We adapted a novel homomorphic encryption scheme optimized for real
numbers computation. We devised (1) the least squares approximation of the logistic function for
accuracy and efficiency (i.e., reduce computation cost) and (2) new packing and parallelization
techniques.
Using real-world datasets, we evaluated the performance of our model and demonstrated its feasibility in speed and memory consumption. For example, it took about 116 minutes to obtain the
training model from homomorphically encrypted Edinburgh dataset. In addition, it gives fairly
accurate predictions on the testing dataset. We present the first homomorphically encrypted
logistic regression outsourcing model based on the critical observation that the precision loss of
classification models is sufficiently small so that the decision plan stays still.

Intro Discussion:
- Biomedical institutions are highly regulated and so data sharing is acceptable only when security can be absolutely guaranteed
- *Train the model without accessing the data* and only obtain the estimated model parameters in a global manner (GLORE)
    - Also developed by Xiaoqian Jiang
- Homomorphic encryption can be used in conjunction with GLORE to ensure that all computation can be done in the encrypted format
- The goal of this paper is to introduce a framework to make logistic regression models on encrypted data feasible based on HE


Method:
- Logistic regression model to minimize the negative log-likelihood
- Utilizing CKKS (HEAAN)
- Chose the gradient descent optimization method (as opposed to the "Newton-Raphson" method)
- Least squares approximation of the sigmoid function (degree 3 and 7)
- Model is based on fixed hyperparameters that were decided before starting the evaluation

Results:
- Degree 7 polynomial approximation yields better accuracy than the degree 3 polynomial approximation
- The difference between the model parameters obtained from encrypted/unencrypted evaluations was less than 2^-11 for a degree 7 polynomial approximation


<br />

*Insights:*
- Training the model with fixed hyperparameters implies that you had to have had access to the model in the first place
    - In a totally encrypted scenario, hyperparameter tuning would have to take place beforehand or in the encrypted domain
