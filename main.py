from fpdf import FPDF
import webbrowser
import os

class Bill:
    """
    Object that contains data about a bill, such as total 
    amount and period of that bill
    """
    
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period 


class Flatmate:
    """ 
    Creates a flatmate person who lives in the flat, 
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house= days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return bill.amount * weight 



class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmate such as their names, their due ammount,
    and period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pays = str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2))

        flatmate2_pays = str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add house icon to top
        pdf.image(name = "house.png", w=30, h=30)

        #Insert Title 
        pdf.set_font(family='Times', size = 24, style='B')
        pdf.cell(w=0, h=80, txt='Flatemates Bill', border=0, align='C', ln=1)

        #Insert Period label and value
        pdf.set_font(family= "Times", size=14, style ='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        #Insert Name and due Amount of first Flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pays, border=0, ln=1)

        #Insert Name and due Amount of first Flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pays, border=0, ln=1)

        #Print the Pdf
        pdf.output(self.filename)

        #Open PDF automaticlly, if windows : webbrowser.open(self.filename)
        webbrowser.open('file://'+os.path.realpath(self.filename))


the_bill = Bill(amount = float(input("Ender the total bill amount: ")) , period = input("Enter the bill period: "))
flatmate1 = Flatmate(name=input("Enter flatmate 1 name: ") , days_in_house= float(input("Enter flatmate 1 days in house: ")))
flatmate2 = Flatmate(name=input("Enter flatmate 2 name: "), days_in_house= float(input("Enter flatmate 2 days in house: ")))

print(flatmate1.name, "Pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(flatmate2.name, "Pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename  = "Report1.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2= flatmate2, bill=the_bill)
