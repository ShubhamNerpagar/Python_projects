import webbrowser

from fpdf import FPDF
import os

class PdfReport:
    """
    Create a pdf file that contains data about the flatmates such as their name,
    their due amount and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename


    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("Files/house.png", w=100, h=100)

        # Flatmate has to pay
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))


        # Insert the title

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=0, align='C', ln=1)

        # Insert period label and value

        pdf.cell(w=100, h=40, txt='Period', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        #Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=0,ln=1)

        #Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=0,ln=1)

        # Change dir to files and open the PDF

        os.chdir("Files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
