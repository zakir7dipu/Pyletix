from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class PDFGenerator:
    @staticmethod
    def generate(path, content_lines, title="Report"):
        c = canvas.Canvas(path, pagesize=letter)
        width, height = letter
        
        c.setFont("Helvetica-Bold", 16)
        c.drawString(72, height - 72, title)
        
        c.setFont("Helvetica", 12)
        y = height - 100
        for line in content_lines:
            c.drawString(72, y, line)
            y -= 20
            if y < 72:
                c.showPage()
                y = height - 72
        
        c.save()
        return path
