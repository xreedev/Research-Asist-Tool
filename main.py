import pdf_util as pdf
import ppt_util as ppt

# Path to the PDF file
pdf_path = "C:\\Users\\dell\\Pictures\\Desktop\\btech\\Main Project\\AI.pdf"

# Extract text from the PDF file
text = pdf.pdf_to_text(pdf_path)

# Print the extracted text
print(text)



# Create a PowerPoint presentation from the extracted text
presentation = ppt.create_ppt(text)

# Save the presentation to a file
presentation.save("scientific_summary.pptx")


