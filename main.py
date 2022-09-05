from scripts import Flatmate
from scripts import Bill
from scripts import PdfReport

amount = int(input("Hey user, enter the bill amount: "))
period = input("Whats is the bill period? E.g. December 2020: ")

bill = Bill(amount, period)

name1 = input('What is your name? ')
days1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))
flatmate1 = Flatmate(name1, days1)

name2 = input('What is the name of the other flatmate? ')
days2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))
flatmate2 = Flatmate(name2, days2)

total_days = flatmate1.days_in_house + flatmate2.days_in_house

print(f"{flatmate1.name} pays: {flatmate1.pays(bill, flatmate2)} ")
print(f"{flatmate2.name} pays: {flatmate2.pays(bill, flatmate1)} ")

filename = 'bill_' + bill.period
report = PdfReport(filename)
report.generate(flatmate1, flatmate2, bill)
