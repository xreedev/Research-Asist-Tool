import pdf_util as pdf
import ppt_util as ppt
import text_speech as speech  # Corrected the import statement

# Path to the PDF file
pdf_path = "C:/Users/JAFAR/Downloads/Summarization_of_Scientific_Paper_Through_Reinforcement_Ranking_on_Semantic_Link_Network.pdf"

# Extract text from the PDF file
text = pdf.pdf_to_text(pdf_path)

# Print the extracted text
print(text)

# Convert text to speech
speech.text_to_speech_with_highlight(text)  # Corrected the function call

# Create a PowerPoint presentation from the extracted text
presentation = ppt.create_ppt(text)

# Save the presentation to a file
presentation.save("scientific_summary.pptx")
