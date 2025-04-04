from scraper.scrape import extract_text
from scorer.score import compute_score
from pdf_generator.export import create_pdf

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def run_audit(url, brand_goal=None, file=None):
    content = extract_text(url)

    prompt = f"""
    Act as a sports brand strategist. Audit the following content:
    ---
    {content}
    ---
    Goal: {brand_goal}
    Analyze tone, clarity, and consistency. Suggest improvements.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    score = compute_score(content)
    pdf_path = create_pdf(content, score, response['choices'][0]['message']['content'])

    return {
        "score": score,
        "insights": response['choices'][0]['message']['content'],
        "report_url": pdf_path
    }
