# AI Bootstrap 4 周学习计划

> **起止时间：2026-09-16 ～ 2026-10-13**  
> 目标：按照导师《研究生人工智能入门 Bootstrap 指南（4 周）》完成基础 AI 技术栈学习，并形成可运行、可修改、可解释、可评测的项目能力。  
> 原则：**不追求“看完课程”，追求“跑通东西”。**

---

## 使用说明

每天按照以下顺序执行：

1. 先看当天“必须懂”的知识清单。
2. 定位当天推荐课程 / 资源。
3. 学到能解释即可，不强求把整节视频看完。
4. 立刻进入代码 / 实验。
5. 最后脱离 AI 和代码，自己解释当天核心概念。

每天看代码时固定问自己：

- 输入是什么？
- 输出是什么？
- Tensor shape 是什么？
- 为什么这样写？
- 删除这一段会发生什么？
- 这一步是在训练还是推理？

---

# Week 1｜9/16–9/22

## 主题：机器学习 → PyTorch → CNN → 完整训练流程

---

## Day 1｜9/16
### 机器学习与深度学习基本框架

### 今天完成

1. 建立 GitHub 仓库 `ai-bootstrap-yourname`
2. 完成 Week 1 自测，不查答案
3. 理清：
   - Artificial Intelligence
   - Machine Learning
   - Deep Learning
   - Supervised Learning
4. 跑通最简单的 FashionMNIST / MNIST PyTorch demo

### 今天必须懂

- [ ] AI / ML / DL 的关系
- [ ] supervised learning 是什么
- [ ] input / feature / label
- [ ] classification
- [ ] train / validation / test
- [ ] batch
- [ ] epoch

### 推荐资源

**李宏毅《生成式人工智慧与机器学习导论 2025》**

- 推荐定位：**第 5 讲：一堂课搞懂机器学习与深度学习的基本原理**
- 官方课程页：  
  https://speech.ee.ntu.edu.tw/~hylee/GenAI-ML/2025-fall.php

> 不要求完整看完。能够回答上面的知识清单即可停。

---

## Day 2｜9/17
### Tensor + Dataset + DataLoader

### 今天完成

重点拆解：

```text
Dataset
 ↓
DataLoader
 ↓
x, y
 ↓
Model
```

亲自打印：

```python
print(x.shape)
print(y.shape)
print(logits.shape)
```

### 今天必须懂

- [ ] Tensor 是什么
- [ ] tensor shape 是什么
- [ ] Dataset 做什么
- [ ] `__getitem__()` 大概是什么
- [ ] DataLoader 做什么
- [ ] batch size
- [ ] shuffle 为什么需要
- [ ] x 和 y 分别是什么
- [ ] `B × C × H × W` 表示什么

### 推荐资源

**PyTorch Learn the Basics**

按顺序看：

1. Tensors
2. Datasets & DataLoaders

官方入口：  
https://docs.pytorch.org/tutorials/beginner/basics/

> 今天核心问题：**数据到底如何一批一批进入模型？**

---

## Day 3｜9/18
### Loss、Gradient、Backward、Optimizer

### 今天完成

逐行搞懂：

```python
optimizer.zero_grad()

logits = model(x)

loss = criterion(logits, y)

loss.backward()

optimizer.step()
```

### 今天必须懂

- [ ] forward
- [ ] logits
- [ ] prediction
- [ ] loss
- [ ] loss 和 accuracy 的区别
- [ ] gradient
- [ ] parameter
- [ ] `loss.backward()`
- [ ] optimizer
- [ ] `optimizer.step()`
- [ ] learning rate

最终能够自己画：

```text
Input
 ↓
Model
 ↓
Prediction
 ↓
Loss
 ↓
Backward
 ↓
Gradient
 ↓
Optimizer
 ↓
Updated Model
```

### 推荐资源

**PyTorch Learn the Basics**

重点：

- Automatic Differentiation with `torch.autograd`
- Optimizing Model Parameters

官方入口：  
https://docs.pytorch.org/tutorials/beginner/basics/

---

## Day 4｜9/19
### CNN 基础

### 今天完成

自己画：

```text
Image
 ↓
Convolution
 ↓
Feature Map
 ↓
Activation
 ↓
Pooling
 ↓
Classifier
```

### 今天必须懂

- [ ] convolution
- [ ] kernel / filter
- [ ] feature map
- [ ] channel
- [ ] stride
- [ ] padding
- [ ] pooling
- [ ] receptive field
- [ ] CNN 为什么适合图像

### 推荐资源

**Stanford CS231n**

- 推荐定位：**Lecture 5 — Image Classification with CNNs**
- 官方课程页：  
  https://cs231n.stanford.edu/

> 不需要继续看 detection / segmentation。

---

## Day 5｜9/20
### ResNet + CIFAR-10 Baseline

### 今天完成

使用：

- CIFAR-10
- CNN 或 ResNet18

完成正式 baseline。

记录：

| 项目 | 结果 |
|---|---|
| Model | |
| Epoch | |
| Batch size | |
| Learning rate | |
| Training loss | |
| Validation accuracy | |

### 今天必须懂

- [ ] baseline
- [ ] train mode / eval mode
- [ ] validation
- [ ] overfitting
- [ ] ResNet 是什么
- [ ] residual connection 大概解决什么问题
- [ ] ImageNet 是什么

### 推荐资源

**Stanford CS231n**

- 推荐定位：**Lecture 6 — CNN Architectures**
- 重点：AlexNet → VGG → **ResNet**
- 官方课程页：  
  https://cs231n.stanford.edu/

---

## Day 6｜9/21
### Learning Rate + 对照实验

### 今天完成

做两个实验。

#### Experiment A

```text
learning rate × 10
```

#### Experiment B

改变：

```text
hidden dimension / channels / network width
```

### 今天必须懂

- [ ] hyperparameter
- [ ] learning rate
- [ ] SGD
- [ ] Adam
- [ ] control experiment
- [ ] 为什么一次最好只改一个变量
- [ ] learning rate 太大 / 太小会怎样
- [ ] model capacity

### 推荐资源

**Stanford CS231n**

- 推荐定位：**Lecture 3 — Regularization and Optimization**
- 重点：
  - SGD
  - Momentum
  - Adam
  - Learning-rate schedules

官方课程页：  
https://cs231n.stanford.edu/

> 今天重点是 learning rate，不需要深入研究所有优化器。

---

## Day 7｜9/22
### Week 1 验收

### 今天完成

不学习新知识。

脱离代码回答：

- [ ] 为什么需要 loss？
- [ ] `loss.backward()` 做了什么？
- [ ] optimizer 做了什么？
- [ ] train / validation / test 有什么区别？
- [ ] 为什么测试集不能用来调参？
- [ ] CNN 为什么适合图像？
- [ ] 什么是 overfitting？

完成：

```text
week1/
└── image_classification/

notes/
└── week1_summary.md
```

### 推荐资源

**李宏毅《生成式人工智慧与机器学习导论 2025》**

- 推荐定位：**第 6 讲：一堂课搞懂训练类神经网络的各种诀窍**
- 重点按需查：
  - Dropout
  - CNN
  - Normalization
  - Pretraining

官方课程页：  
https://speech.ee.ntu.edu.tw/~hylee/GenAI-ML/2025-fall.php

> 今天只查漏补缺，不完整重看。

---

# Week 2｜9/23–9/29

## 主题：Transformer → Foundation Model → LLM → RAG

---

## Day 8｜9/23
### Token + Tokenizer + Embedding

### 今天完成

拿一句话实际查看：

```text
Text
 ↓
Tokenizer
 ↓
Token IDs
 ↓
Embedding
 ↓
Vectors
```

### 今天必须懂

- [ ] token
- [ ] tokenizer
- [ ] vocabulary
- [ ] token ID
- [ ] embedding
- [ ] embedding matrix
- [ ] positional embedding
- [ ] 为什么 token ID 本身不代表语义

### 推荐资源

**Hugging Face LLM Course**

- 推荐定位：**Chapter 2 → Tokenizers**

官方课程：  
https://huggingface.co/learn/llm-course/

---

## Day 9｜9/24
### Self-Attention

### 今天完成

重点搞懂：

```text
X
├→ Q
├→ K
└→ V

QKᵀ
 ↓
softmax
 ↓
attention weights
 ↓
weighted V
```

### 今天必须懂

- [ ] Q / K / V
- [ ] attention score
- [ ] softmax
- [ ] attention weight
- [ ] self-attention
- [ ] 为什么一个 token 能获得其他 token 的信息

### 推荐资源

**李宏毅 Machine Learning 2021**

官方课程页中定位：

```text
CNN & Self-Attention
└── Self-Attention
    ├── Chinese 1
    └── Chinese 2
```

官方课程页：  
https://speech.ee.ntu.edu.tw/~hylee/ml/2021-spring.php

---

## Day 10｜9/25
### Transformer Block

### 今天完成

画完整 Transformer Block。

### 今天必须懂

- [ ] Multi-Head Attention
- [ ] Feed Forward Network
- [ ] residual connection
- [ ] LayerNorm
- [ ] causal mask
- [ ] Transformer Block
- [ ] autoregressive
- [ ] next-token prediction

### 推荐资源

**李宏毅 Machine Learning 2021**

定位：

```text
Transformer
├── Chinese 1
└── Chinese 2
```

官方课程页：  
https://speech.ee.ntu.edu.tw/~hylee/ml/2021-spring.php

> LayerNorm 如果不理解，再回头补 Normalization。

---

## Day 11｜9/26
### 一个 LLM 是怎么训练出来的

### 今天完成

建立：

```text
Large Corpus
 ↓
Pretraining
 ↓
Base Model
 ↓
Instruction / Post-training
 ↓
Assistant Model
 ↓
Inference
```

### 今天必须懂

- [ ] pretraining
- [ ] base model
- [ ] next-token prediction
- [ ] fine-tuning
- [ ] instruction tuning
- [ ] post-training
- [ ] inference
- [ ] context window
- [ ] temperature
- [ ] hallucination

### 推荐资源

**李宏毅《生成式人工智慧与机器学习导论 2025》**

- 推荐定位：**第 7 讲：大型语言模型的学习历程**

官方课程页：  
https://speech.ee.ntu.edu.tw/~hylee/GenAI-ML/2025-fall.php

---

## Day 12｜9/27
### Hugging Face 模型调用

### 今天完成

至少跑一个：

- text generation
- sentiment classification
- zero-shot classification

然后拆开 `pipeline()`。

### 今天必须懂

- [ ] Hugging Face 是什么
- [ ] checkpoint
- [ ] `from_pretrained()`
- [ ] tokenizer
- [ ] input tensor
- [ ] model output
- [ ] inference vs training

### 推荐资源

**Hugging Face LLM Course**

- 推荐定位：**Chapter 2 → Behind the pipeline**

官方课程：  
https://huggingface.co/learn/llm-course/

---

## Day 13｜9/28
### Embedding Semantic Search

### 今天完成

准备 30–100 段文本，实现：

```text
Documents
 ↓
Embedding Model
 ↓
Vectors

Query
 ↓
Embedding
 ↓
Similarity
 ↓
Top-k Documents
```

### 今天必须懂

- [ ] semantic search
- [ ] vector
- [ ] embedding similarity
- [ ] cosine similarity
- [ ] Top-k
- [ ] retriever
- [ ] keyword search vs semantic search

### 推荐资源

**Hugging Face Learn / Cookbook**

- 推荐定位：**Advanced RAG → Retriever / Embeddings**
- 官方入口：  
  https://huggingface.co/learn/cookbook/advanced_rag

> 今天只看 Retriever 部分。

---

## Day 14｜9/29
### Simple RAG + Week 2 验收

### 今天完成

```text
Question
 ↓
Embedding
 ↓
Retrieve Documents
 ↓
Context + Question
 ↓
LLM
 ↓
Answer
```

完成：

```text
week2/
├── huggingface_demo/
├── semantic_search/
└── simple_rag/
```

并完成：

```text
notes/week2_summary.md
```

题目：

> 一个现代 LLM 系统从 token 到最终回答，中间发生了什么？

### 今天必须懂

- [ ] RAG
- [ ] retrieval
- [ ] context
- [ ] RAG 为什么可能减少 hallucination
- [ ] retrieval 错误会怎样
- [ ] RAG vs fine-tuning

### 推荐资源

**李宏毅 2025**

- 推荐定位：**HW2 — Build a Basic RAG System**
- 官方课程页：  
  https://speech.ee.ntu.edu.tw/~hylee/GenAI-ML/2025-fall.php

---

# Week 3｜9/30–10/6

## 主题：AI Agent

---

## Day 15｜9/30
### Agent 到底是什么

### 今天完成

理解：

```text
Agent =
Model
+ Context
+ Memory
+ Tools
+ Environment
+ Control Logic
+ Evaluation
```

### 今天必须懂

- [ ] Agent vs chatbot
- [ ] context
- [ ] memory
- [ ] tool
- [ ] environment
- [ ] control logic
- [ ] evaluation

### 推荐资源

**李宏毅 2025**

- 推荐定位：**第 2 讲：上下文工程（Context Engineering）—— AI Agent 背后的关键技术**
- 官方课程页：  
  https://speech.ee.ntu.edu.tw/~hylee/GenAI-ML/2025-fall.php

---

## Day 16｜10/1
### Agent Loop / ReAct

### 今天完成

理解：

```text
Thought
 ↓
Action
 ↓
Observation
 ↓
Thought
 ↓
...
```

### 今天必须懂

- [ ] Thought
- [ ] Action
- [ ] Observation
- [ ] ReAct
- [ ] agent loop
- [ ] history
- [ ] stop condition

### 推荐资源

**Hugging Face Agents Course**

- 推荐定位：**Unit 1 → Thought-Action-Observation Cycle**
- 接着看：
  - Thought, Internal Reasoning
  - ReAct Approach

官方课程：  
https://huggingface.co/learn/agents-course/en/unit1/introduction

---

## Day 17｜10/2
### 阅读真正的 Agent 项目：mini-SWE-agent

### 今天完成

只追五个问题：

- [ ] agent loop 在哪里
- [ ] model 在哪里调用
- [ ] tool / environment 在哪里
- [ ] history 怎么保存
- [ ] 什么情况下停止

### 推荐资源

**mini-SWE-agent**

优先顺序：

1. `docs/advanced/control_flow.md`
2. `src/minisweagent/agents/default.py`

GitHub：  
https://github.com/SWE-agent/mini-swe-agent

> 不需要读完整个 repository。

---

## Day 18｜10/3
### 自己写 Simple Agent

### 今天完成

至少两个工具，例如：

```text
Agent
├── Calculator
└── File Search
```

### 今天必须懂

- [ ] tool description
- [ ] tool argument
- [ ] tool output
- [ ] tool selection
- [ ] observation
- [ ] loop
- [ ] final answer

### 推荐资源

**Hugging Face Agents Course**

- 推荐定位：**Unit 1 → What are Tools?**
- 如果进度快：
  - `Let's Create Our First Agent Using smolagents`

官方课程：  
https://huggingface.co/learn/agents-course/en/unit1/introduction

---

## Day 19｜10/4
### Agent Evaluation

### 今天完成

建立 30–50 个固定任务。

每次记录：

```text
task
success / failure
answer
tool calls
trajectory
latency
token usage
failure reason
```

### 今天必须懂

- [ ] task set
- [ ] benchmark
- [ ] success criterion
- [ ] success rate
- [ ] trajectory
- [ ] latency
- [ ] token usage
- [ ] failure analysis

### 推荐资源

**Stanford CS329A — Self-Improving AI Agents**

- 推荐定位：**Part 8 — Agentic Evaluations and Long Horizon Tasks**
- 官方课程：  
  https://cs329a.stanford.edu/

---

## Day 20｜10/5
### 修改 Agent + 第二次 Evaluation

### 今天完成

执行：

```text
第一次 Evaluation
        ↓
找失败案例
        ↓
修改 Agent
        ↓
重新 Evaluation
```

计算：

- success rate
- average tool calls
- average latency
- average tokens

### 今天必须懂

- [ ] failure case
- [ ] reliability
- [ ] iteration
- [ ] why demo ≠ evaluation
- [ ] 为什么更复杂不一定更好

### 推荐资源

**Anthropic — Building Effective Agents**

重点看：

- Building blocks, workflows, and agents
- Evaluator-optimizer
- Agents

文章：  
https://www.anthropic.com/engineering/building-effective-agents

---

## Day 21｜10/6
### Week 3 Agent 总复习

### 今天完成

脱离代码画：

```text
Task
 ↓
Agent
 ↓
Model
 ↓
Tool
 ↓
Environment
 ↓
Observation
 ↓
Agent
 ↓
...
 ↓
Answer
```

完成：

```text
week3/
└── simple_agent/

notes/
└── week3_summary.md
```

### 今天必须懂

- [ ] Agent 为什么不是“更大的 LLM”
- [ ] tool calling
- [ ] memory
- [ ] planning
- [ ] agent loop
- [ ] evaluation

### 推荐资源

**Lilian Weng — LLM Powered Autonomous Agents**

重点：

1. Agent System Overview
2. Planning
3. Memory
4. Tool Use

文章：  
https://lilianweng.github.io/posts/2023-06-23-agent/

---

# Week 4｜10/7–10/13

## 主题：AI 前沿地图 + 综合项目 + Evaluation

---

## Day 22｜10/7
### 现代 AI 技术地图

### 今天完成

自己画：

```text
Machine Learning
 ↓
Deep Learning
 ↓
CNN / Transformer
 ↓
Foundation Model
 ↓
LLM / Vision Model
 ↓
RAG / Tool
 ↓
Agent
 ↓
Memory / Planning / Evaluation
 ↓
Self-Improving AI
```

### 今天必须懂

每个词能够用 1–2 句话解释：

- [ ] Foundation Model
- [ ] larger-scale pretraining
- [ ] multimodal model
- [ ] domain foundation model
- [ ] post-training
- [ ] SFT
- [ ] preference learning
- [ ] RL
- [ ] reasoning
- [ ] verifier
- [ ] test-time compute
- [ ] tool use
- [ ] planning
- [ ] memory
- [ ] coding agent
- [ ] web agent

### 推荐资源

**Stanford CS329A**

- 推荐定位：**Part 1 — Course Overview**
- 官方课程：  
  https://cs329a.stanford.edu/

---

## Day 23｜10/8
### Compound AI / Agent Engineering / Self-Improving AI

### 今天完成

继续扩展技术地图。

### 今天必须懂

- [ ] compound AI system
- [ ] context engineering
- [ ] RAG
- [ ] MCP
- [ ] agent orchestration
- [ ] benchmark
- [ ] judge
- [ ] reliability
- [ ] reflection
- [ ] experience
- [ ] trajectory learning
- [ ] prompt / program optimization
- [ ] automated agent design
- [ ] continual learning
- [ ] multimodal AI

### 推荐资源

**Stanford CS329Z — Engineering AI Agents**

- 官方课程：  
  https://cs329z.stanford.edu/

重点优先：

- Foundations
- LLMs for Builders
- RAG
- Tool Use
- Agent Frameworks

> 该课程为 2026 Fall 新课程，到当天以官网实际已发布内容为准。

---

## Day 24｜10/9
### Final Project：Baseline

### 今天完成

先建立：

```text
Baseline:
single LLM call
```

准备：

- task set
- input
- expected output
- evaluation metric

跑 baseline。

### 今天必须懂

- [ ] baseline
- [ ] task
- [ ] metric
- [ ] success criterion
- [ ] 为什么先有 baseline
- [ ] model vs system

### 推荐资源

**Berkeley AI Research**

文章：

**The Shift from Models to Compound AI Systems**

https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/

今天重点思考：

> Baseline 哪里失败？  
> 加哪个组件才能解决这个具体失败？

---

## Day 25｜10/10
### Final Project：RAG / Tool / Agent System

### 今天完成

在 baseline 上增加至少一种能力：

```text
Baseline
 ↓
RAG / Tool / Agent
 ↓
Improved System
```

### 今天必须懂

- [ ] system vs model
- [ ] external feedback
- [ ] tool use
- [ ] agent loop
- [ ] system complexity
- [ ] 为什么增加组件必须解决具体问题

### 推荐资源

**Stanford CS329A**

- 推荐定位：**Part 4 — Learning from Feedback with Tools / Code**
- 重点：
  - ReAct
  - Tool Interaction
  - Execution Feedback

官方课程：  
https://cs329a.stanford.edu/

---

## Day 26｜10/11
### Final Project：Evaluation

### 今天完成

比较：

| Metric | Baseline | System |
|---|---:|---:|
| Success rate | | |
| Accuracy | | |
| Latency | | |
| Token usage | | |
| Failure cases | | |

### 今天必须懂

- [ ] evaluation
- [ ] benchmark
- [ ] reliability
- [ ] failure case
- [ ] ablation
- [ ] 如何证明系统是真的变好了

### 推荐资源

**Stanford CS329A**

- 推荐定位：**Part 8 — Agentic Evaluations and Long Horizon Tasks**
- 重点复习：
  - evaluation methodology
  - failure modes
  - reliability

官方课程：  
https://cs329a.stanford.edu/

---

## Day 27｜10/12
### 论文阅读 + Research Proposal

### 今天完成

论文阅读统一回答：

1. Problem
2. Why important?
3. Key idea
4. Method
5. Dataset / Environment
6. Evaluation
7. Main result
8. Limitation
9. One question

执行标准：

- 15 篇快速结构化阅读
- 其中 5 篇形成完整正式记录

Research Proposal 回答：

- 我想研究什么？
- 为什么重要？
- 现在别人怎么做？
- 我想尝试什么？
- 怎么知道做得好不好？

### 今天必须懂

- [ ] problem formulation
- [ ] baseline
- [ ] dataset / environment
- [ ] metric
- [ ] result
- [ ] limitation
- [ ] research question

### 推荐资源

**Stanford CS329A**

- 推荐结合 **Part 4**
- 重点阅读对应论文：
  - **ReAct**

官方课程：  
https://cs329a.stanford.edu/

> 阅读论文时先判断它在整个技术地图中的位置，再进入 Method。

---

## Day 28｜10/13
### 最终口试 + 完整复盘

### 今天完成

今天不学习任何新知识。

### Deep Learning

- [ ] ML 和 DL 的区别
- [ ] train / validation / test
- [ ] loss vs metric
- [ ] gradient descent
- [ ] optimizer
- [ ] overfitting
- [ ] CNN 为什么适合图像

### Transformer

- [ ] token
- [ ] tokenizer
- [ ] embedding
- [ ] positional embedding
- [ ] Q / K / V
- [ ] self-attention
- [ ] Transformer
- [ ] next-token prediction

### LLM

- [ ] pretraining
- [ ] fine-tuning
- [ ] instruction tuning
- [ ] post-training
- [ ] context window
- [ ] temperature
- [ ] hallucination

### RAG

- [ ] embedding retrieval
- [ ] semantic search
- [ ] Top-k
- [ ] RAG
- [ ] retrieval error
- [ ] RAG vs fine-tuning

### Agent

- [ ] Agent vs chatbot
- [ ] tool calling
- [ ] agent loop
- [ ] memory
- [ ] planning
- [ ] environment
- [ ] evaluation

### Research

- [ ] baseline
- [ ] benchmark
- [ ] metric
- [ ] ablation
- [ ] failure analysis
- [ ] 怎么判断系统是真的变强，而不是 demo 更好

### 推荐资源

**李宏毅 2025**

- 推荐定位：**第 1 讲：一堂课搞懂生成式人工智慧的原理**
- 今天不完整重看。
- 把它作为 Final Check：
  - 视频提到一个概念
  - 暂停
  - 自己解释
  - 解释不出来就记录为后续知识洞

官方课程页：  
https://speech.ee.ntu.edu.tw/~hylee/GenAI-ML/2025-fall.php

---

# 最终仓库结构

```text
ai-bootstrap-yourname/
│
├── README.md
├── requirements.txt
│
├── week1/
│   └── image_classification/
│
├── week2/
│   ├── huggingface_demo/
│   ├── semantic_search/
│   └── simple_rag/
│
├── week3/
│   └── simple_agent/
│
├── week4/
│   └── final_project/
│
├── papers/
│   └── paper_notes.md
│
└── notes/
    ├── week1_summary.md
    ├── week2_summary.md
    ├── week3_summary.md
    └── final_reflection.md
```

---

# 最终通过标准

完成这 4 周后，应至少能够：

- [ ] 自己维护 GitHub repository
- [ ] 独立运行 PyTorch 项目
- [ ] 修改模型或超参数并解释结果
- [ ] 使用 Hugging Face 模型
- [ ] 实现简单 semantic search
- [ ] 实现简单 RAG
- [ ] 实现 simple tool-using agent
- [ ] 为 Agent 建立固定 evaluation
- [ ] 阅读 AI 论文并做结构化总结
- [ ] 解释现代 AI 技术地图
- [ ] 面对 AI 项目时知道从输入、模型、数据、训练信号、输出、评价、baseline 和 failure 开始分析

---

# 学习原则

## 1. 课程不是任务主体

不要：

```text
今天是 CNN
→ 把 CS231n 一整讲强行看完
```

应该：

```text
先看知识清单
→ 定位相关课程
→ 学到能理解
→ 马上写代码
→ 自己解释
```

## 2. AI 可以写代码，但不能替代理解

对于任何核心代码，都应该能够回答：

```text
输入是什么？
输出是什么？
shape 是什么？
为什么这样写？
删掉会怎样？
训练还是推理？
```

## 3. 每天至少留下一个可见成果

可以是：

- 一次 Git commit
- 一个能运行的 notebook
- 一个实验结果
- 一张模型流程图
- 一篇 summary
- 一个 README 更新
- 一组 evaluation logs

不要只留下：

> “今天看了两个小时视频。”

## 4. 推荐资源优先级

这 4 周最值得认真学习的核心资源：

1. **李宏毅 ML 2021 — Self-Attention + Transformer**
2. **Stanford CS231n — CNN**
3. **Hugging Face Agents Course Unit 1**
4. **mini-SWE-agent — `control_flow.md` + `default.py`**

其余课程主要用于按需查漏补缺。
