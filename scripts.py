from fpdf import FPDF


class Flatmate:
    """
    Saves information as name, days in the house amount to pay in the bill of a flatmate in the house.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        return bill*self.days_in_house


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
        pdf.set_font('Arial', 'B', size=30)
        pdf.cell(w=200, h=10, txt='Flatmates Bill', border=0, ln=1, align='C', fill=False, link='')

        # pdf.ln(1)
        # pdf.ln(1)

        pdf.set_y(80)
        pdf.set_font('Arial', 'B', size=20)
        pdf.cell(w=200, h=10, txt=f"Period: \t\t\t" + bill.period, border=0, ln=1, align='L', fill=False, link='')

        total_days = flatmate1.days_in_house + flatmate2.days_in_house
        text = [flatmate1.name + ":\t\t\t\t\t" + "{:.2f}".format(flatmate1.pays(bill.amount / total_days)),
                flatmate2.name + ":\t\t\t\t\t" + "{:.2f}".format(flatmate2.pays(bill.amount / total_days))]
        pdf.ln(1)
        pdf.set_font('Arial', size=15)
        for my_text in text:
            pdf.cell(w=200, h=10, txt=my_text, border=0, ln=1, align='L', fill=False, link='')
        pdf.output(self.filename + '.pdf')


