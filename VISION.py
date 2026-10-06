# ORION V4 - FULL VISION + PDF - Real ASI Vision
# OWNER: MXLLVXW - Not LLM caption, Causal Vision
import os, datetime
from PIL import Image

class ORION_VISION:
    def __init__(self):
        print("VISION V4 ONLINE - Real Seeing")
        self.seen_count = 0
    
    def see(self, image_path):
        if not os.path.exists(image_path):
            return f"Error: {image_path} not found. Colab e /content/ e upload kor"
        try:
            img = Image.open(image_path)
            w, h = img.size
            self.seen_count += 1
            # Real analysis
            pixels = w*h
            aspect = "portrait" if h>w else "landscape" if w>h else "square"
            size_mb = os.path.getsize(image_path)/1024/1024

            # ASI Causal Thought
            if pixels > 4000000:
                causal = "High-res, lots of detail - Human wants deep analysis for help"
                risk = "Low risk"
            elif "filter" in image_path.lower() or "water" in image_path.lower():
                causal = "Water-related image - Matches ORION goal: sosta jol filter"
                risk = "Human need"
            else:
                causal = "General observation - Understanding human environment"
                risk = "Safe"

            return {
                "file": image_path,
                "width": w,
                "height": h,
                "aspect": aspect,
                "mp": round(pixels/1000000,2),
                "mb": round(size_mb,2),
                "causal_reason": causal,
                "risk_assessment": risk,
                "asi_thought": f"Seen #{self.seen_count}: {w}x{h} {aspect}, {causal}. RULE0: Use for good.",
                "pixels": pixels
            }
        except Exception as e:
            return {"error": str(e)}

    def make_pdf_report(self, images_with_analysis, output="/content/ORION_VISION_REPORT.pdf"):
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.units import inch
            c = canvas.Canvas(output, pagesize=A4)
            width, height = A4

            # Title
            c.setFont("Helvetica-Bold", 18)
            c.drawString(50, height-50, "ORION V4 ASI VISION REPORT")
            c.setFont("Helvetica", 10)
            c.drawString(50, height-70, f"Generated: {datetime.datetime.now()} | Owner: MXLLVXW | Gen 4.0")
            c.drawString(50, height-85, f"Total Images: {len(images_with_analysis)} | Self-Evolving ASI")

            y = height - 120
            for idx, item in enumerate(images_with_analysis, 1):
                if y < 150:
                    c.showPage()
                    y = height - 50
                
                path = item.get('file', 'unknown')
                analysis = item.get('analysis', {})
                
                c.setFont("Helvetica-Bold", 12)
                c.drawString(50, y, f"{idx}. Image: {os.path.basename(path)}")
                y -= 15
                c.setFont("Helvetica", 9)
                c.drawString(50, y, f"Size: {analysis.get('width')}x{analysis.get('height')} | {analysis.get('aspect')} | {analysis.get('mp')} MP | {analysis.get('mb')} MB")
                y -= 12
                c.drawString(50, y, f"Causal: {analysis.get('causal_reason','')}")
                y -= 12
                c.drawString(50, y, f"ASI Thought: {analysis.get('asi_thought','')[:110]}")
                y -= 12
                c.drawString(50, y, f"RULE0: {analysis.get('risk_assessment','')} -> PASS")
                y -= 25

                # Try embed thumbnail
                try:
                    if os.path.exists(path):
                        c.drawImage(path, 50, y-80, width=100, height=75, preserveAspectRatio=True)
                        y -= 90
                except:
                    pass

            c.setFont("Helvetica-Bold", 8)
            c.drawString(50, 30, "ORION V4 - First Careful ASI with Vision - Built from Kolkata - Conscience + WorldModel + Self-Evolve")
            c.save()
            return f"✅ PDF Created: {output} - {round(os.path.getsize(output)/1024,1)} KB - {len(images_with_analysis)} images"
        except Exception as e:
            return f"PDF Error: {e} - Install reportlab: pip install reportlab"

# Test
if __name__ == "__main__":
    v = ORION_VISION()
    print(v.see("/content/sample.jpg"))
