from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

#Add some text
pdf.set_font(family='Times', size = 24, style='B')
pdf.cell(w=100, h=80, txt='Flatemates Bill', border=1, align='C')
pdf.cell(w=50, h=40, txt='Period', border=1)


#Print the Pdf
pdf.output("bill.pdf")