"""no module at all. Just testing an account class."""


class Account:
    """represent a user bank account"""

    def __init__(self, start_credits) -> None:
        self.credits = start_credits

    def display(self) -> None:
        """Return the actual credits of a user"""
        print(self.credits)

    def pay_in(self, amount) -> None:
        """ add a given amoiunt to the user credits """
        self.credits += amount

    def withdraw(self, amount) -> None:
        """ remove a given amount of the user credits """

        if self.credits < amount:
            print(f"Noooo dude! Maximum amount you can withdraw is {self.credits}€!")
            return

        self.credits -= amount


cumstomer_1 = Account(500)
cumstomer_1.display()
# 500
cumstomer_1.pay_in(40)
cumstomer_1.display()
# 540
cumstomer_1.withdraw(25)
cumstomer_1.display()
# 515
cumstomer_1.withdraw(600)
# Noooo dude! Maximum amount you can withdraw is 515€!
