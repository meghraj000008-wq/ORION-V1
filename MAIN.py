from BRAIN import ORION_BRAIN
print("ORION V4 - FULL VISION + PDF - READY")
brain = ORION_BRAIN()

# Vision test - Colab e image upload korar por ei 2 line cholbe
# Upload kor: Colab er left sidebar -> Files -> Upload
# Then:
# result = brain.ask("Ei chobite ki ache? Manusher upokar kivabe hobe?", lang="bn", image_path="/content/tor_image.jpg")
# print(result)

# PDF Report test
images = ["/content/tor_image.jpg"] # tomar uploaded image path
analysis_list = []
for p in images:
    a = brain.vision.see(p)
    if "error" not in str(a):
        analysis_list.append({"file": p, "analysis": a})

if analysis_list:
    print(brain.vision.make_pdf_report(analysis_list))
else:
    print("Kono image paini - Files e upload kor /content/ e")
    print(brain.ask("sosta jol filter er design de", lang="bn"))
