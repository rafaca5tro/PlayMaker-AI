from fpdf import FPDF
import uuid

def create_pdf(content, score, insights):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"PlayMaker AI – BrandAudit Report\nScore: {score}/100\n\nInsights:\n{insights}")
    filename = f"report_{uuid.uuid4().hex}.pdf"
    path = f"/tmp/{filename}"
    pdf.output(path)
    return path
