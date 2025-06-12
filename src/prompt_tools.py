from __future__ import annotations

"""prompt_tools.py

轻量级工具集合，用于构建、加载与渲染 prompt。
后续可在此扩展更多功能。
"""

from pathlib import Path
from typing import List


PROMPT_DIR = Path(__file__).resolve().parent.parent / "prompts"


def list_prompts() -> List[str]:
    """列出可用的 prompt 名称."""
    if not PROMPT_DIR.exists():
        return []
    return [p.stem for p in PROMPT_DIR.glob("*.txt")]


def load_prompt(name: str) -> str:
    """根据名称加载 prompt 文本.

    参数
    ----
    name: Prompt 文件名（不含扩展名）
    """
    path = PROMPT_DIR / f"{name}.txt"
    if not path.exists():
        raise FileNotFoundError(f"Prompt '{name}' 未找到: {path}")
    return path.read_text(encoding="utf-8")
