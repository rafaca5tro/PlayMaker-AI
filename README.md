# PlayMaker AI – BrandAudit AI (Sports Edition)

An AI-powered tool that audits sports brands instantly based on their website, social media, or pitch decks.

## Tech Stack
- Frontend: Next.js + TailwindCSS
- Backend: FastAPI (Python)
- LLM: OpenAI (via LangChain or direct API)
- Storage: Firebase
- Payments: Stripe

## Structure
```
PlayMaker-AI/
├── backend/
│   ├── app/
│   ├── audit_engine/
│   ├── scraper/
│   ├── scorer/
│   └── pdf_generator/
├── frontend/
│   └── pages/
├── requirements.txt
├── README.md
```

## Getting Started

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Deploy
- Frontend: Vercel
- Backend: Render / Cloud Run
