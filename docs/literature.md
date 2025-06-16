# Prompt Engineering 方法文献综述

本文档旨在提炼和总结几种前沿的提示工程（Prompt Engineering）优化方法的核心思路、输入输出以及优缺点。

## EvoPrompt [1]

### 核心思路

将提示（prompt）视为进化算法中的基因序列。通过核心进化操作——突变（随机修改提示组件）、交叉（组合成功提示的元素）和选择（选择表现最佳的提示作为父代）——来实现提示的自动工程化。这是一个通过进化搜索实现自动化提示工程的关键创新。

### 输入/输出

- **输入**: 候选提示的初始种群；用于评估性能的目标任务。
- **输出**: 经过迭代优化后，在目标任务上表现最佳的提示。

### 优缺点

- **优点**: 通过进化搜索实现了提示工程的自动化，减少了人工干预。
- **缺点**: 可能会消耗大量的计算资源，尤其是在复杂的搜索空间中；优化结果可能陷入局部最优。

## TextGrad [2]

### 核心思路

基于文本的梯度下降方法。它将文本视为可微变量，并使用大语言模型（LLM）的反馈作为"文本梯度"来优化解。该方法用自然语言替代了数值梯度。

### 输入/输出

- **输入**: 初始的文本解决方案。
- **输出**: 基于LLM反馈迭代优化后的解决方案。优化过程包括：前向传播（LLM评估解决方案质量）和后向传播（LLM生成改进反馈）。

### 优缺点

- **优点**: 创新性地使用自然语言替代数值梯度，实现了端到端的文本优化。
- **缺点**: 优化的效果高度依赖于LLM生成反馈的质量和一致性；可能需要多次迭代才能收敛。

## DSPy [3]

### 核心思路

一种声明式的提示编程框架，其核心是基于编译器的提示优化。用户通过声明式的方式定义任务和模块，然后由编译器将其编译成自优化的流程。

### 输入/输出

- **输入**: 任务定义（例如，输入文本，输出情感）；选择的模块（例如 ChainOfThought）；以及用于优化的评估指标（例如 accuracy_metric）。
- **输出**: 一个优化后的分类器或处理流程。对于给定的输入文本，它可以产生结构化的输出，包含结果和推理过程。

### 优缺点

- **优点**: 结构化和模块化的方法，提高了提示的可复用性和可维护性；能够自动优化复杂的提示流程。
- **缺点**: 对于初学者来说，学习曲线可能较陡峭；框架的灵活性可能会受到预定义模块的限制。

## APOHF (Prompt Optimization with Human Feedback) [4]

### 核心思路

一种基于人类偏好反馈的提示优化方法。其核心是通过向人类提问"你更喜欢哪个答案？"来收集偏好，从而对提示进行优化，灵感来源于决斗老虎机（dueling bandits）算法。

### 输入/输出

- **输入**: 成对的提示及其对应的答案；人类对这些答案的偏好选择。
- **输出**: 经过迭代更新后，符合人类偏好的优化提示。

### 优缺点

- **优点**: 方法简单直观；优化过程无需数值评分；适用于黑盒大语言模型；优化效率高。
- **缺点**: 严重依赖人类反馈的质量和可用性，规模化成本高；可能存在主观偏见。

## HbBoPs (Hyperband-based Bayesian Optimization for Black-box Prompt Selection) [5]

### 核心思路

使用基于Hyperband的贝叶斯优化，从一个预定义的集合中高效地选择最佳提示。该方法将提示视为模块化组件，并结合了结构感知的深度核函数与Hyperband调度器。

### 输入/输出

- **输入**: 一个预定义的提示集合。
- **输出**: 从集合中选出的最佳提示。

### 优缺点

- **优点**: 搜索过程的样本效率高；支持多保真度评估；是一种黑盒优化方法；性能优于当前最优（SOTA）方法。
- **缺点**: 效果受限于预定义的提示集合，无法生成全新的提示。

## IO vs EO (Instruction Optimization vs Exemplar Optimization) [6]

### 核心思路

这是一项比较研究，旨在通过强化学习找到指令（Instruction）和范例（Exemplar）的最佳组合。其核心是指令优化（IO）和范例优化（EO）的协同组合。

### 输入/输出

- **输入**: 用于构建提示的指令和范例。
- **输出**: 经过优化的指令和范例组合。

### 关键发现 (Key Findings)

- 范例优化（EO）的效果可能优于指令优化（IO）。
- 简单的范例优化（EO）可能比复杂的指令优化（IO）更有效。
- 将两者结合的优化方法能取得最佳效果。

## EASE (Efficient ordering-aware automated SElection of exemplars) [7]

### 核心思路

一种高效的范例选择方法，它不仅选择范例，还考虑它们的排列顺序。该方法利用了带有预训练模型嵌入的神经老虎机算法。

### 输入/输出

- **输入**: 一组待选的范例。
- **输出**: 一组经过优化选择并排序的范例。

### 优缺点

- **优点**: 实现了高效的范例选择；考虑了范例的顺序；在测试时无需额外计算；实现了任务级别的优化；可以与指令联合优化；性能优于现有方法。
- **缺点**: 主要关注范例的选择和排序，而不是生成或修改范例内容本身。

## 参考文献

[1] Guo Y. et al. Connecting large language models with evolutionary algorithms yields powerful prompt optimizers. 2024.

[2] Yuksekgonul M. et al. Optimizing generative AI by backpropagating language model feedback. 2025.

[3] Khattab O. et al. DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines. 2024.

[4] Lin X. et al. Prompt optimization with human feedback. 2024.

[5] Schneider L. et al. Hyperband-based bayesian optimization for black-box prompt selection. 2025.

[6] Wan X. et al. Teach better or show smarter? On instructions and exemplars in automatic prompt optimization. 2024: 58174-244.

[7] Wu Z. et al. Prompt optimization with EASE? Efficient ordering-aware automated selection of exemplars. 2024: 122706-40.
