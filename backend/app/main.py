from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from audit_engine.analyze import run_audit

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
