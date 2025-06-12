# Prompt-Sprint

Prompt-Sprint 聚焦于 AI 时代的快速原型迭代与 Prompt 优化实验。

## 目录结构

```text
.
├── .github/              # CI、Issue/PR 模板
│   ├── workflows/
│   │   └── ci.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CODEOWNERS
├── docs/                 # 项目文档
├── experiments/          # 实验目录
│   └── evo-setup/
│       ├── requirements.txt
│       ├── run_demo.py
│       └── results/
├── src/                  # 代码工具包
│   └── prompt_tools.py
├── .gitignore
└── setup.py
```

## 快速开始

```bash
# 安装依赖
pip install -r experiments/evo-setup/requirements.txt

# 运行演示
python experiments/evo-setup/run_demo.py
```

## 开发规范

1. 全部改动需通过 Pull Request，并经过自动化 CI 检查；
2. 使用 `flake8`+`black` 保持代码风格一致；
3. 文档放置于 `docs/`，实验放置于 `experiments/`，可复用代码抽象到 `src/`。
