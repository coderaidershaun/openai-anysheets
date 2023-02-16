

import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
canvas = canvas.Canvas(packet, pagesize=letter)
textobject = canvas.beginText()
textobject.setTextOrigin(10, 740)
textobject.setFont("Times-Roman", 12)

textobject.textLines('''Road safety is an important factor in ensuring the safety of all drivers, passengers, and pedestrians. 
It is essential to be aware of the rules of the road and to follow them at all times. 
This includes following the speed limit, obeying traffic signals, and being aware of other drivers. 
It is also important to be aware of the weather conditions and to adjust your driving accordingly. 
By following these rules, you can help to ensure the safety of everyone on the road.''')

canvas.drawText(textobject)
canvas.save()

packet.seek(0)
new_pdf = packet.read()

#Save pdf file
with open("savedfile.pdf", "wb") as f:
    f.write(new_pdf)