

import PyPDF2 

# Create a pdf file object 
pdfFileObj = open('savedfile.pdf', 'wb') 

# Create a pdf writer object for the pdf file 
pdfWriter = PyPDF2.PdfFileWriter() 

# Set the title of the pdf document 
pdfWriter.addMetadata({'/Title': 'Hello'}) 

# Write the pdf document to the file 
pdfWriter.write(pdfFileObj) 

# Close the pdf file object 
pdfFileObj.close()