## Efficient Logistic Regression on Large Encrypted Data
##### Authors: Kyoohyung Han, Seungwan Hong, Jung Hee Cheon, and Daejun Park
<br />

Available: https://eprint.iacr.org/2018/662.pdf<br />
Summary:
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

### Summary
Intro:  
- Explaining fully-encrypted training and inference (no decryption key for either phase)

Method:
- "Approximate HE"
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