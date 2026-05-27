"""Convert Linna paper Markdown to styled HTML for PDF printing."""
import markdown
import os

paper_md = r"I:\CLAUDE\output\linna-knowledge-cosmos\paper\linna-knowledge-cosmos.pdf.md"
output_html = r"I:\CLAUDE\output\linna-knowledge-cosmos\paper\linna-knowledge-cosmos.html"

with open(paper_md, "r", encoding="utf-8") as f:
    md_content = f.read()

html_body = markdown.markdown(md_content, extensions=["tables", "fenced_code", "codehilite"])

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Linna: A Personal Knowledge Cosmos — 3D Spatial Knowledge Organization with AI-Driven Personal Memory</title>
<style>
  @page {{ size: A4; margin: 2.5cm 2cm; }}
  body {{
    font-family: "Times New Roman", "Songti SC", Georgia, serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #1a1a1a;
    max-width: 700px;
    margin: 0 auto;
    padding: 40px 20px;
  }}
  h1 {{ font-size: 18pt; text-align: center; margin-bottom: 4pt; }}
  h2 {{ font-size: 14pt; border-bottom: 1px solid #333; padding-bottom: 4pt; margin-top: 28pt; }}
  h3 {{ font-size: 12pt; margin-top: 20pt; }}
  h4 {{ font-size: 11pt; }}
  p {{ text-align: justify; margin: 8pt 0; }}
  table {{ border-collapse: collapse; width: 100%; margin: 12pt 0; font-size: 10pt; }}
  th, td {{ border: 1px solid #666; padding: 5pt 8pt; text-align: left; }}
  th {{ background: #f0f0f0; }}
  code {{ font-family: "Courier New", monospace; font-size: 9pt; background: #f5f5f5; padding: 1pt 3pt; }}
  pre {{ background: #f5f5f5; padding: 10pt; font-size: 9pt; overflow-x: auto; border-left: 3px solid #333; }}
  blockquote {{ border-left: 3px solid #999; padding-left: 12pt; color: #555; margin: 12pt 0; }}
  strong {{ color: #1a1a1a; }}
  .author {{ text-align: center; font-size: 12pt; margin: 6pt 0; }}
  .date {{ text-align: center; font-size: 10pt; color: #666; margin-bottom: 24pt; }}
  .abstract {{
    background: #fafafa;
    border: 1px solid #ddd;
    padding: 14pt 18pt;
    margin: 20pt 0;
    font-size: 10.5pt;
  }}
  .abstract strong {{ display: block; margin-bottom: 6pt; font-size: 12pt; }}
  @media print {{
    body {{ padding: 0; }}
    .page-break {{ page-break-before: always; }}
  }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

with open(output_html, "w", encoding="utf-8") as f:
    f.write(html)

print(f"HTML generated: {output_html}")
print(f"Size: {os.path.getsize(output_html)/1024:.1f} KB")
print("Open this file in a browser and press Ctrl+P → Save as PDF")
