from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

def export_blueprint_to_pdf(blueprint_output, path: str):
    bp = blueprint_output["blueprint"]
    doc = SimpleDocTemplate(path, pagesize=letter)
    styles = getSampleStyleSheet()
    elems = []

    def add_heading(text):
        elems.append(Paragraph(f"<b>{text}</b>", styles["Heading2"]))
        elems.append(Spacer(1, 12))

    def add_body(text):
        elems.append(Paragraph(text, styles["BodyText"]))
        elems.append(Spacer(1, 12))

    add_heading("Significance")
    add_body(bp["significance"])

    add_heading("Innovation")
    add_body(bp["innovation"])

    add_heading("Approach")
    for a in bp["approach"]:
        add_heading(f"Aim: {a['aim']}")
        add_body(a["plan"])

    doc.build(elems)