from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

# 🔧 Fix para que Python reconozca módulos fuera de /app
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from audit_engine.analyze import run_audit

app = FastAPI()

# CORS para permitir conexiones desde frontend en Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto a tu dominio de Vercel si deseas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/audit")
async def audit_endpoint(
    url: str = Form(...),
    brand_goal: str = Form(None),
    file: UploadFile = None
):
    result = await run_audit(url=url, brand_goal=brand_goal, file=file)
    return result
