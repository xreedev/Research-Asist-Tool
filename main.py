import pdf_util as pdf
import ppt_util as ppt
import pubmedAPI as pm

# Path to the PDF file
pdf_path = "C:\\Users\\dell\\Pictures\\Desktop\\btech\\Main Project\\AI.pdf"

# Extract text from the PDF file
#text,abs = pdf.pdf_to_text(pdf_path)

# Print the extracted text
#print(text,"\n",abs)
url = "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC10415512/unicode"
i=0
# Extract full text
full_text = pm.extract_full_text(url)
if full_text:
    print("Full Text:")
    for text in full_text:
        print(i,text)
        i=i+1
else:
    print("No full text extracted")


# Create a PowerPoint presentation from the extracted text
#presentation = ppt.create_ppt(text)

# Save the presentation to a file
#presentation.save("C:\\Users\\dell\\Pictures\\Desktop\\btech\\Main Project\\scientificsummary.pptx")


