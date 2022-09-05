class Flatmate:
    """
    Saves information as name, days in the house amount to pay in the bill of a flatmate in the house.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        print(f"{self.name} pays: {bill*self.days_in_house} ")


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
        pass
