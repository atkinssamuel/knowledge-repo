# Index
- [MCUNet: Tiny Deep Learning on IoT Devices](#mcunet-tiny-deep-learning-on-iot-devices)
- [Once for All: Train One Network and Specialize it for Efficient Deployment](#once-for-all-train-one-network-and-specialize-it-for-efficient-deployment)

## MCUNet: Tiny Deep Learning on IoT Devices
##### Authors: J. Lin, W.-M. Chen, Y. Lin, J. Cohn, C. Gan and S. Han
###### Published: 2020

<br />

Available: https://arxiv.org/pdf/2007.10319.pdf<br />

Summary:  
- MCUNet - an ML design framework that uses space constraints as optimization criteria
    - Enables ML on IoT devices
        - Smart retail, smart home, smart manufacturing, autonomous driving (all without querying the cloud)

<br />

> Machine learning on tiny IoT devices based on microcontroller units (MCU) is
appealing but challenging: the memory of microcontrollers is 2-3 orders of magnitude smaller even than mobile phones. We propose MCUNet, a framework that
jointly designs the efficient neural architecture (TinyNAS) and the lightweight
inference engine (TinyEngine), enabling ImageNet-scale inference on microcontrollers. TinyNAS adopts a two-stage neural architecture search approach that
first optimizes the search space to fit the resource constraints, then specializes the
network architecture in the optimized search space. TinyNAS can automatically
handle diverse constraints (i.e. device, latency, energy, memory) under low search
costs. TinyNAS is co-designed with TinyEngine, a memory-efficient inference
engine to expand the search space and fit a larger model. TinyEngine adapts
the memory scheduling according to the overall network topology rather than
layer-wise optimization, reducing the memory usage by 3.4×, and accelerating
the inference by 1.7-3.3× compared to TF-Lite Micro [3] and CMSIS-NN [28].
MCUNet is the first to achieves >70% ImageNet top1 accuracy on an off-the-shelf
commercial microcontroller, using 3.5× less SRAM and 5.7× less Flash compared
to quantized MobileNetV2 and ResNet-18. On visual&audio wake words tasks,
MCUNet achieves state-of-the-art accuracy and runs 2.4-3.4× faster than MobileNetV2 and ProxylessNAS-based solutions with 3.7-4.1× smaller peak SRAM.
Our study suggests that the era of always-on tiny machine learning on IoT devices
has arrived.


Research Gap:
- Microcontrollers and IoT devices do not have as much memory as mobile devices and GPUs
- Current ML architectures do not need to optimize for space
- The current novel ML models exceed the peak memory limit by multiple orders of magnitude

Method:
- MCUNet - "system-model co-design framework that enables ImageNet-scale deep learning on off-the-shelf microcontrollers"


Results:
- ImageNet accuracy of 70.7% on off-the-shelf microcontrollers and accelerated the inference of wake word applications by 2.4-3.4x
    - "The era of always-on tiny machine learning on IoT devices has arrived"
    - The cost of deep learning has been reduced from $5,000 on GPU workstations, to $500 on mobile phones, and now down to $5 on microcontrollers


## Once for All: Train One Network and Specialize it for Efficient Deployment
##### Authors: H. Cai, C. Gan and S. Han
###### Published: 2020

<br />

Available: https://arxiv.org/pdf/1908.09791.pdf<br />

Summary:  
- To avoid training each sub-network for each problem context seperately (because this is computationally expensive and bad for the environment), they propose a "once-for-all" network that supports diverse architectural settings
- They do this by combining the architecture search and the network optimization into one loss function

<br />

> We address the challenging problem of efficient inference across many devices
and resource constraints, especially on edge devices. Conventional approaches
either manually design or use neural architecture search (NAS) to find a specialized
neural network and train it from scratch for each case, which is computationally
prohibitive (causing CO2 emission as much as 5 cars’ lifetime Strubell et al. (2019))
thus unscalable. In this work, we propose to train a once-for-all (OFA) network that
supports diverse architectural settings by decoupling training and search, to reduce
the cost. We can quickly get a specialized sub-network by selecting from the OFA
network without additional training. To efficiently train OFA networks, we also
propose a novel progressive shrinking algorithm, a generalized pruning method
that reduces the model size across many more dimensions than pruning (depth,
width, kernel size, and resolution). It can obtain a surprisingly large number of subnetworks (> 1019) that can fit different hardware platforms and latency constraints
while maintaining the same level of accuracy as training independently. On diverse
edge devices, OFA consistently outperforms state-of-the-art (SOTA) NAS methods
(up to 4.0% ImageNet top1 accuracy improvement over MobileNetV3, or same
accuracy but 1.5× faster than MobileNetV3, 2.6× faster than EfficientNet w.r.t
measured latency) while reducing many orders of magnitude GPU hours and CO2
emission. In particular, OFA achieves a new SOTA 80.0% ImageNet top-1 accuracy
under the mobile setting (<600M MACs). OFA is the winning solution for the
3rd Low Power Computer Vision Challenge (LPCVC), DSP classification track
and the 4th LPCVC, both classification track and detection track. Code and 50
pre-trained models (for many devices & many latency constraints) are released at
https://github.com/mit-han-lab/once-for-all.

Research Gap/Problem Statement:
- The optimal mobile ML network architecture depends on a tremendous number of factors (temperature, processor, memory, etc.)
- This paper introduces a "once-for-all network" that is deployable under diverse architectural configurations

Method:
- The goal of their optimization process is to minimize the sum of the losses of all of the sub-networks 

<br />

*Insights:*
- I'm not sure how this paper relates to the work that I'm doing as I am not deploying NN architectures to IoT/mobile devices
