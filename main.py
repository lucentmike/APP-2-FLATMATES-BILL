class Bill:
    """
    Object that contains data about a bill, such as total 
    amount and period of that bill
    """
    
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period 


class Flatmate:
    """ 
    Creates a flatmate person who lives in the flat, 
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house= days_in_house

    def pays(self, bill, flatemate2):
        weight = self.days_in_house / (self.days_in_house + flatemate2.days_in_house)
        return bill.amount * weight 



class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmate such as their names, their due ammount,
    and period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
mary = Flatmate(name="Mary", days_in_house=25)

print("John Pays: ", john.pays(bill=the_bill, flatemate2=mary))
print("Mary Pays: ", mary.pays(bill=the_bill, flatemate2=john))
