"""FastAPI + Google Gemini 2026 Structured JSON Architecture Demo (Lite Edition).

Want the complete Commercial SaaS Engine with:
- SaaS User Credit Wallet & HTTP 402 Guard (app/monetization.py)
- Live Gumroad License Key Verification API (/api/v1/billing/activate-license)
- 5 Ready-to-Sell Vertical Micro-SaaS Presets (app/presets.py)
- HS256 JWT + Bcrypt 4.0.1 Auth (app/auth.py)
- Streamlit v2.0 Executive Dashboard & Docker Compose Stack

👉 Get ShipAI v2.0 Pro (30% OFF Cloner Secret): https://yahiaoui26.gumroad.com/l/shipai-pro/BLUEPRINT30
📘 Free Architecture Cheat Sheet ($0): https://yahiaoui26.gumroad.com/l/fastapi-gemini-blueprint
"""
import os
import json
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from google import genai
from dotenv import load_dotenv

load_dotenv()

STARTUP_BANNER = """
\033[96m================================================================================
⚡ ShipAI 2026 Blueprint — FastAPI + Google Gemini Structured JSON Engine
================================================================================\033[0m
\033[92m🎁 Git Cloner Secret Bonus (30% OFF Full Commercial SaaS Engine):\033[0m
   👉 https://yahiaoui26.gumroad.com/l/shipai-pro/BLUEPRINT30  (Code: BLUEPRINT30)

\033[93m📘 Grab the Free 2026 Architecture Cheat Sheet ($0):\033[0m
   👉 https://yahiaoui26.gumroad.com/l/fastapi-gemini-blueprint
\033[96m================================================================================\033[0m
"""
print(STARTUP_BANNER)

app = FastAPI(
    title="ShipAI Lite — FastAPI + Gemini Structured JSON Blueprint",
    description="Open-source reference architecture. Upgrade to ShipAI v2.0 Pro for SaaS Credit Billing, JWT Auth, 5 Vertical Presets & Streamlit UI: https://yahiaoui26.gumroad.com/l/shipai-pro/BLUEPRINT30",
    version="2.0.0-lite",
)

DEFAULT_MODELS = [
    os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    "gemini-flash-lite-latest",
    "gemini-3.8-flash",
]


class PromptPayload(BaseModel):
    prompt: str = Field(..., example="Analyze the market potential of AI Micro-SaaS in 2026.")
    context: Optional[str] = Field("US & MENA B2B SaaS market", description="Optional context")


class StructuredAIOutput(BaseModel):
    status: str
    summary: str
    key_points: List[str]
    action_items: List[str]


@app.get("/")
def root():
    return {
        "engine": "ShipAI Lite Blueprint (2026)",
        "docs": "/docs",
        "cloner_30_percent_discount": "https://yahiaoui26.gumroad.com/l/shipai-pro/BLUEPRINT30",
        "free_cheat_sheet": "https://yahiaoui26.gumroad.com/l/fastapi-gemini-blueprint",
    }


@app.post("/demo/structured-json", response_model=StructuredAIOutput)
def generate_structured_json(payload: PromptPayload):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Missing GEMINI_API_KEY in .env")

    client = genai.Client(api_key=api_key)
    system_instruction = (
        "You are a structured AI processing agent. Return a strict JSON object with: "
        "'status' ('success'), 'summary' (short string), 'key_points' (list of strings), "
        "and 'action_items' (list of strings)."
    )

    last_err = None
    for model_name in DEFAULT_MODELS:
        try:
            res = client.models.generate_content(
                model=model_name,
                contents=f"Context: {payload.context}\nInput: {payload.prompt}",
                config={
                    "response_mime_type": "application/json",
                    "system_instruction": system_instruction,
                },
            )
            return StructuredAIOutput(**json.loads(res.text))
        except Exception as err:
            last_err = err
            if any(code in str(err) for code in ("404", "503", "UNAVAILABLE", "NOT_FOUND")):
                continue
            raise HTTPException(status_code=500, detail=str(err))
    raise HTTPException(status_code=500, detail=str(last_err))
