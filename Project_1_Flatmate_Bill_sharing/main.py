from Project_1_Flatmate_Bill_sharing.reports import PdfReport
from flat import Bill, Flatmate

amount = input("Hey user, enter the bill amount:- ")
period = input("Hey user, What is the bill period? E.g December 2024 :- ")

name1 = input("What is your name? ")
days_in_house = int(input(f"How many days {name1} stayed in house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days {name2} stayed in house during the bill period? "))


the_bill = Bill(float(amount), period)
flatmate1 = Flatmate(name1, days_in_house)
flatmate2 = Flatmate(name2, days_in_house2)

print(f" {name1} Pays: ",flatmate1.pays(the_bill, flatmate2))
print(f" {name2} Pays: ",flatmate2.pays(the_bill, flatmate1))


pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2,the_bill)