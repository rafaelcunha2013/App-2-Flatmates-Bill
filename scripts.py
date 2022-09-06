from fpdf import FPDF


class Flatmate:
    """
    Saves information as name, days in the house amount to pay in the bill of a flatmate in the house.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        return bill.amount*self.days_in_house/(self.days_in_house + other_flatmate.days_in_house)


class Bill:
    """
    Has the amount and period of a bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class PdfReport:
    """
    Generates a PDF report stating the names of the flatmates, the period, and how much each of them had to pay.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF()
        pdf.add_page()
        pdf.image('.\\files\\house.png', 10, 8, 13)

        pdf.set_y(50)
        pdf.set_font(family='Arial', style='B', size=30)
        # w=0 --> Cell takes the entire length of the page
        pdf.cell(w=200, h=10, txt='Flatmates Bill', border=0, ln=1, align='C', fill=False, link='')

        # pdf.ln(1)
        # pdf.ln(1)

        pdf.set_y(80)
        pdf.set_font('Arial', 'B', size=20)

        pdf.cell(w=50, h=10, txt="Period:", border=0, ln=0, align='L')
        pdf.cell(w=50, h=10, txt=bill.period, border=0, ln=1, align='L')

        pdf.set_font('Arial', size=15)

        pdf.cell(w=50, h=10, txt=flatmate1.name, border=0, ln=0, align='L')
        pdf.cell(w=50, h=10, txt="{:.2f}".format(flatmate2.pays(bill, flatmate1)), border=0, ln=1, align='L')

        pdf.cell(w=50, h=10, txt=flatmate2.name, border=0, ln=0, align='L')
        pdf.cell(w=50, h=10, txt="{:.2f}".format(flatmate1.pays(bill, flatmate2)), border=0, ln=1, align='L')

        pdf.output(self.filename + '.pdf')


if __name__ == '__main__':
    bill = Bill(100, 'December 2022')
    flatmate1 = Flatmate("Rafael", 20)
    flatmate2 = Flatmate("Caio", 13)

    report = PdfReport('bill_' + bill.period)
    report.generate(flatmate1, flatmate2, bill)



