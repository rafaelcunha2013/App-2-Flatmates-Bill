from flat import Flatmate, Bill
from report import PdfReport

amount = float(input("Hey user, enter the bill amount: "))
period = input("Whats is the bill period? E.g. December 2020: ")

bill = Bill(amount, period)

name1 = input('What is your name? ')
days1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))
flatmate1 = Flatmate(name1, days1)

name2 = input('What is the name of the other flatmate? ')
days2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))
flatmate2 = Flatmate(name2, days2)

print(f"{flatmate1.name} pays: {round(flatmate1.pays(bill, flatmate2), 2)} ")
print(f"{flatmate2.name} pays: {round(flatmate2.pays(bill, flatmate1), 2)} ")

filename = f"bill_{bill.period}.pdf"
report = PdfReport(filename)
report.generate(flatmate1, flatmate2, bill)
