# Linna · 知识链星球

> 将 AI 对话、笔记、思考自动沉淀为 3D 星球宇宙。星球之间通过知识链相连，随时间动态生长。

<!-- SCREENSHOT: 放一张主界面截图 here -->

## 功能

- **AI 智能对话** — 基于 RAG 架构的知识库问答，用自然语言检索和关联个人知识
- **3D 星球可视化** — 知识节点以星座形式展示在三维宇宙中，支持缩放、筛选、关联跳转
- **时间线浏览** — 按时间轴展示知识积累过程，支持按分类和时间范围筛选
- **多格式导入** — 支持 Markdown、PDF、网页等多源内容导入，自动提取结构化信息
- **知识图谱** — 自动检测知识节点之间的关联，形成网状知识结构
- **暗色主题** — 默认暗色视觉，支持亮色切换

<!-- SCREENSHOT: 放一张3D星球截图 here -->

## 技术栈

| 层 | 技术 |
|----|------|
| 前端 | React 18 + TypeScript + Vite |
| 3D 可视化 | Three.js (react-three-fiber) |
| 样式 | Tailwind CSS + Framer Motion |
| 状态管理 | Zustand |
| 后端 | Python + FastAPI |
| 数据存储 | SQLite (WAL + FTS5) |
| AI | RAG 检索增强生成 |

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/Linnaphia/linna-knowledge-cosmos.git
cd linna-knowledge-cosmos

# 安装前端依赖
cd packages/web
npm install
npm run dev

# 启动后端（需要 Python 3.12+）
cd ../api
pip install -r requirements.txt
python -m cosmos_api.main
```

## 项目结构

```
packages/
├── web/          # 前端应用 (React + TypeScript)
├── api/          # 后端服务 (FastAPI)
├── core/         # 数据模型 + 图谱操作
├── extractor/    # 知识提取引擎 (Python)
├── cli/          # 命令行工具 (Click)
└── viz/          # 3D 可视化组件
```

## 开源协议

MIT License

## 作者

Filinna — [GitHub](https://github.com/Linnaphia)
