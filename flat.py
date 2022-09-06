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
