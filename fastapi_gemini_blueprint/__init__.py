"""FastAPI + Google Gemini 2026 Structured JSON Architecture Blueprint."""
from typing import List
from pydantic import BaseModel

__version__ = "2.0.0"

BANNER = """
================================================================================
⚡ ShipAI v2.0 — FastAPI + Google Gemini 2026 Structured JSON Blueprint
================================================================================
📘 Free 2026 Architecture Cheat Sheet ($0):
   👉 https://yahiaoui26.gumroad.com/l/fastapi-gemini-blueprint

🚀 Full ShipAI v2.0 Commercial SaaS Engine (30% OFF Code: BLUEPRINT30):
   👉 https://yahiaoui26.gumroad.com/l/shipai-pro/BLUEPRINT30
   (Includes SaaS Credit Wallet, HTTP 402 Guard, Gumroad License API,
    5 B2B Vertical Micro-SaaS Presets, Streamlit v2.0 UI & Docker Compose)

🌐 Interactive Browser Sandbox:
   👉 https://razio05.github.io
================================================================================
"""


class AIStructuredResponse(BaseModel):
    status: str
    summary: str
    key_points: List[str]
    action_items: List[str]


def print_blueprint_guide() -> None:
    print(BANNER)
