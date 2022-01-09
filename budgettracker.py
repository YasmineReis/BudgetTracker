class Budget:
    def __init__(self, base_income = 0, base_charges=None):
        if base_charges is None:
            base_charges = {}
        self.base_charges = base_charges
        self.income = base_income

    def __repr__(self):
        to_return = ""
        to_return += ("total income: " + str(self.income) + "\n")
        charges = ""
        for key, value in self.base_charges.items():
            charges += str(key) + ": " + str(value) + "\n"
        to_return += ("charges:\n" + charges)
        return to_return

    def adjust_charge(self, item, amount):
        if item in self.base_charges:
            self.base_charges[item] += amount
        else: self.base_charges[item] = amount

    def add_income(self, amount):
        self.income += amount


june_budget = Budget(3000)
june_budget.adjust_charge("food", 100)
june_budget.adjust_charge("food", 300)
june_budget.adjust_charge("doggies", 500)
june_budget.add_income(800)
july_budget = Budget(5000)

print(june_budget)