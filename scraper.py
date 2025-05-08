import requests
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Step 1: Scrape text content from a webpage
url = "https://www.itcportal.com/about-itc/shareholder-value/financial-reports.aspx"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract some dummy paragraphs or replace with actual content logic
content = ""
for para in soup.find_all('p'):
    content += para.get_text(strip=True) + "\n\n"

# Step 2: Save content to a valid PDF using reportlab
pdf_path = "itc_financial_report.pdf"
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter

lines = content.split("\n")
y = height - 40
for line in lines:
    if y < 40:
        c.showPage()
        y = height - 40
    c.drawString(40, y, line[:100])  # Clip line if it's too long
    y -= 15

c.save()
print(f"✅ PDF saved successfully as: {pdf_path}")
