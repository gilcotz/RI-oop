print("\nWelcome to my ROI calculation program\n")
print("This programs will calculate your Rent Investment\n"
      "\nBefore you continue have all the values in $$ before starting the program, please enter the values for your Income, Expenses and Investments before starting the program\n")


class RentInvest:

    def __init__(self, income=[], expenses=[], investment=[]):
        self.income = income
        self.expenses = expenses
        self.investment = investment

    def add_gains(self):
        add_income = int(
            input("Enter the number inputs are you adding to your income?\n "))
        for n in range(add_income):
            add_income2 = int(input("Enter you income "))
            print("\nwhen you are done please choose another form!\n")
            self.income.append(add_income2)

    def show_income(self):
        if self.income == []:
            print(f'sorry you dont have anything in your list.')
        else:
            print("This is in your income input list")
            for inco in self.income:
                print(inco)

    def addingList(self):
        finish = 0
        for ele in range(0, len(self.income)):
            ad = finish + self.income[ele]
        print(ad)

    def add_expenses(self):
        add_xpenses = int(
            input("\nEnter the number inputs are you adding to your expenses? "))
        for n in range(add_xpenses):
            add_xpenses2 = int(input("Enter you expenses "))
            print("\nwhen you are done please choose another form!\n")
            self.expenses.append(add_xpenses2)

    def show_expenses(self):
        print("This is in your total expenses total")
        if self.expenses == []:
            print(f'sorry you dont have anything in your list.')
        else:
            print("\nThis is in your expense input list")
            for expe in self.expenses:
                print(expe)

    def addingListEx(self):
        lost = 0
        for ele in range(0, len(self.income)):
            ae = lost + self.expenses[ele]
        print(ae)

    def add_investment(self):
        add_invest = int(
            input("\nEnter the number inputs are you adding to your investments? "))
        for n in range(add_invest):
            add_invest2 = int(input("Enter you investments "))
            print("\nwhen you are done please choose another form!")
            self.investment.append(add_invest2)

    def show_invest(self):
        print("This is in your total expenses total")
        if self.investment == []:
            print(f'sorry you dont have anything in your list.')
        else:
            print("This is in your investment input list")
            for inve in self.investment:
                print(inve)

    def addingListInvest(self):
        invest = 0
        for ele in range(0, len(self.income)):
            ain = invest + self.expenses[ele]
        print(ain)

    def cashflow(self):
        cashflow = (int(ad) - int(ae))
        print("Your cash flow is " + cashflow)

    def showcashflow(self):
        print(cashflow)

    def yearcash(self):
        annualflow = cashflow * 12

    def show_ROI(self):
        cashOncash = annualflow / totalInvest * 100
        print("Your RI for this ROI is " + cashOncash)


def cal():
    result = RentInvest([], [], [])
    while True:
        roi_question = input("Type: income, expenses, investment to fill out forms or quit\n"
                             "\nType: income-l, expenses-l, invest-l to view your list or quit\n"
                             "\nType: cashflow to view your cash flow or quit\n"
                             "\nType: SHOW ROI to see your Cash on Cash ROI or quit\n")

        if roi_question.lower() == "income":
            result.add_gains()
        elif roi_question.lower() == "expenses":
            result.add_expenses()
        elif roi_question.lower() == "investment":
            result.add_investment()
        elif roi_question.lower() == "income-l":
            result.show_income()
        elif roi_question.lower() == "expenses-l":
            result.show_expenses()
        elif roi_question.lower() == "invest-l":
            result.show_invest()
        elif roi_question.lower() == "cashflow":
            result.showcashflow()
        elif roi_question.upper() == "SHOW ROI":
            result.show_ROI()
        elif roi_question.lower() == "quit":
            print("Thank you for using RI calculator")
            break
        else:
            print("Your typed the wrong input please try again...")


cal()
