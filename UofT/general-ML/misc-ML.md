# Index
- ['Less Than One'-Shot Learning: Learning N Classes From M](#less-than-one-shot-learning-learning-n-classes-from-m)

## 'Less Than One'-Shot Learning: Learning N Classes From M
##### Authors: I. Sucholutsky and M. Schonlau
###### Published: 2021

<br />

Available: https://arxiv.org/pdf/2009.08449.pdf<br />

Summary:  
- Introduces LO-shot learning where you supply the model with less than N classes and expect it to be able to discern N classes
- The method utilizes soft-label prototypes and illustrates its results with the kNN algo.

<br />

> Deep neural networks require large training sets but suffer
from high computational cost and long training times. Training on much smaller training sets while maintaining nearly
the same accuracy would be very beneficial. In the few-shot
learning setting, a model must learn a new class given only
a small number of samples from that class. One-shot learning is an extreme form of few-shot learning where the model
must learn a new class from a single example. We propose the
‘less than one’-shot learning task where models must learn
N new classes given only M < N examples and we show
that this is achievable with the help of soft labels. We use a
soft-label generalization of the k-Nearest Neighbors classifier
to explore the intricate decision landscapes that can be created in the ‘less than one’-shot learning setting. We analyze
these decision landscapes to derive theoretical lower bounds
for separating N classes using M < N soft-label samples
and investigate the robustness of the resulting systems.

Research Gap/Problem Statement:
- Deep ML models are extremely data-hungry

*Few-Shot learning: (FSL)*
- An approach to making models more sample efficient
- Giving a model a handful of examples per class

*One-Shot Learning: (OSL)*
- Giving a model one example per class

*Less Than One-Shot Learning: (LO-shot learning):*
- A setting where the model must learn N new classes given only M < N examples
    - "[C]onsider an alien zoologist who arrived on Earth and is being tasked with catching a unicorn. It has no familiarity with local fauna and there are no photos of unicorns, so humans show it a photo of a horse and a photo of a rhinoceros, and say that a unicorn is something in between. With just two examples, the alien has now learned to recognize three different animals."


Method:
- "Soft-label prototypes" are used in conjunction with the kNN algo. to seperate N classes using less than 1 example per class 

Results:
- This paper lays the groundwork for showing that LO-shot learning is a viable new direction in ML research
