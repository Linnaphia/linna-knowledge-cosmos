# 研究文献索引

> 每份文献标注：关键发现 + 对 Linna 的设计影响

---

## 已发表研究

### Li et al. (2024)
**"Comparative Study on 2D and 3D User Interface for Eliminating Cognitive Loads in Augmented Reality Repetitive Tasks"**
*International Journal of Human-Computer Interaction, 40(23)*

- **方法**：40 人对照实验，眼动追踪 + NASA-TLX 主观负荷量表
- **关键发现**：设计良好的 3D 界面显著降低认知负荷（更短眨眼时长、注视时长、更低主观负荷）。2D 与 3D 在学习性上无显著差异。
- **对 Linna 的影响**：支撑 3D 宇宙作为默认主界面。前提是导航不依赖大量 3D 位移。

---

### Sudár & Csapó (2024)
**"Comparing Desktop 3D Virtual Reality with Web 2.0 Interfaces"**
*Heliyon*

- **方法**：对比 2D Web 2.0 布局与两种桌面 3D VR 仪表盘。眼动追踪 + 行为数据。
- **关键发现**：3D 可以降低认知负荷并保持同等表现——但不是自动的。关键设计因素：位移最小化（旋转优先于平移移动）。
- **对 Linna 的影响**：相机飞行时间控制在 1.2s 以内；减少层级跳跃次数；旋转 > 平移。

---

### Hubenschmid et al. (2025)
**"Revisiting Hybrid Input Devices for Immersive Analytics"**

- **方法**：论证性论文，综述混合 2D/3D 系统。
- **关键发现**：纯 2D 或纯 3D 都不如混合系统。用户应"停留在最优模态中"完成每个子任务，避免模态间的破坏性切换。
- **对 Linna 的影响**：3D 宇宙 + 搜索/列表并存（混合模式）。决策 1 和决策 4 的直接支撑。

---

### Wang et al. (2025)
**"Knowledge Sharing Platform Users' Switching Intention from the Perspective of the Push-Pull-Mooring Framework"**
*International Journal of Mobile Communications, 25(3), 339-368*

- **方法**：结构方程模型，330 份有效问卷，中国知识共享平台用户。
- **关键发现**：锚定效应（转换成本、媒体依恋）是用户留存的最强调节变量。媒体依恋显著调节推力效应（不满）与转换意愿的关系。
- **对 Linna 的影响**：创造情感连接（"这是我的世界"）比堆功能更能留住用户。宇宙隐喻的直接研究支撑。

---

### Lee & Lee (2025)
**"Enhancing Recognition Memory in Virtual Memory Palaces Using Worlds-in-Miniature"**
*Applied Sciences, 15(5), 2304*

- **方法**：40 人实验，虚拟记忆宫殿 + Worlds-in-Miniature 界面。即时/7天/14天三次测试。
- **关键发现**：WIM 界面显著提升识别记忆。空间组织带来的留存优势持续至 14 天。
- **对 Linna 的影响**：空间隐喻不只是审美——它有可测量的记忆留存优势。支撑决策 2（保留宇宙隐喻）。

---

### Chu & Chen (2025)
**"Investigating 2D and 3D Interactive Labeling with Connector Cues for Symptom-Assisted Appointment Scheduling in mHealth"**
*HCI International 2025, Springer LNCS*

- **方法**：2×2 被试间设计，32 人。2D vs 3D × 有/无连接线。
- **关键发现**：3D 模式更直观，减少视角切换挫折感。但连接线提示在密集布局中反而增加认知负荷。
- **对 Linna 的影响**：连接线需渐进展示（默认隐藏，hover 高亮）。决策 5 的直接研究支撑。

---

### UC Berkeley School of Information (2025)
**"ScrollWise: A Personal Knowledge Management Tool"**
*Product Report*

- **关键发现**：约 50% 已保存内容从未被重新打开。"数字囤积"现象——用户因 FOMO 不断积累，直到无法管理。知识工作者每天约 2.5 小时（30%工作时间）用于搜索之前存过的信息。
- **对 Linna 的影响**：用户需要引导才能开始。支撑决策 3（轻量提问 + AI 生成初始宇宙）。

---

### Forsey & Leahy
**"Designing for Learnability: Improvement Through Layered Interfaces"**

- **关键发现**：分层界面（渐进展示）有效提升可学习性。将复杂度推迟到用户准备好时再呈现。
- **对 Linna 的影响**：引导应嵌入使用过程（渐进式），而非前置一次性教程。

---

## 竞品分析（非学术）

| 产品 | 类别 | 与本项目差异 |
|------|------|------------|
| Obsidian | 本地知识管理 + 双向链接 | 无 3D 空间组织，AI 仅社区插件，2D 图谱 |
| Notion AI | 全能文档 + AI | 无 3D，AI 不基于用户知识库个性化，云端 |
| Mem.ai | AI 自动整理笔记 | 无 3D，无"宇宙"隐喻，单一功能 |
| Tana | AI 知识图谱 | 2D 界面，面向工作场景，非个人知识宇宙 |
| TwinMind | 持续录音 + 个人记忆 | 无 3D 空间，被动采集而非主动构建 |
| K3D (Knowledge3D) | 3D 空间知识架构 | 开源技术框架（非产品），面向开发者，无 AI 助手集成 |
| Mem0 | AI 记忆层 API | 基础设施（无用户界面），非消费级应用 |
| Rewind AI | 全时屏幕录制 | Mac 限定，被动记录，无知识结构，隐私争议大 |

---

## 结论

Linna 的组合——3D 空间宇宙 + 个人知识库驱动的 AI + 多模型载体平台——在当前已发表的学术文献和商业产品中**未见同类组合**。
