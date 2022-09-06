from fpdf import FPDF
import webbrowser
import os

from flat import Flatmate, Bill


class PdfReport:
    """
    Generates a PDF report stating the names of the flatmates, the period, and how much each of them had to pay.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF()
        pdf.add_page()
        # Insert image
        pdf.image("files/house.png", 10, 8, 13)

        # Insert tittle
        pdf.set_y(50)
        pdf.set_font(family='Arial', style='B', size=30)
        # w=0 --> Cell takes the entire length of the page
        pdf.cell(w=0, h=10, txt='Flatmates Bill', border=0, ln=1, align='C', fill=False, link='')

        # Insert Period, flatmates name and bill
        pdf.set_y(80)
        pdf.set_font('Arial', 'B', size=20)

        pdf.cell(w=50, h=10, txt="Period:", border=0, ln=0, align='L')
        pdf.cell(w=50, h=10, txt=bill.period, border=0, ln=1, align='L')

        pdf.set_font('Arial', size=15)

        pdf.cell(w=50, h=10, txt=flatmate1.name, border=0, ln=0, align='L')
        pdf.cell(w=50, h=10, txt="{:.2f}".format(flatmate1.pays(bill, flatmate2)), border=0, ln=1, align='L')

        pdf.cell(w=50, h=10, txt=flatmate2.name, border=0, ln=0, align='L')
        pdf.cell(w=50, h=10, txt="{:.2f}".format(flatmate2.pays(bill, flatmate1)), border=0, ln=1, align='L')

        pdf.output(f"files/{self.filename}")

        # Open the .pdf file in the default computer viewer
        # For MAC and LINUX
        # webbrowser.open('file://' + os.path.realpath(self.filename))
        # The bellow command changes the directory
        # To print the directory: os.getcwd()
        # To return to the previous directory: os.chdir("..")
        os.chdir("files")
        webbrowser.open(self.filename)


if __name__ == '__main__':
    my_bill = Bill(100, 'December 2022')
    rafael = Flatmate("Rafael", 20)
    caio = Flatmate("Caio", 13)

    report = PdfReport(f"bill_{my_bill.period}.pdf")
    report.generate(rafael, caio, my_bill)



