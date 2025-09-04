class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name.center(30, '*')}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc:<23}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Title
    chart = "Percentage spent by category\n"

    # Calculate total withdrawals and per-category percentages
    withdrawals = []
    total_spent = 0
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        withdrawals.append(spent)
        total_spent += spent

    percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in withdrawals]

    # Build vertical bar chart
    for i in range(100, -1, -10):
        line = f"{i:>3}|"
        for pct in percentages:
            line += " o " if pct >= i else "   "
        chart += line + " \n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "    "  # 4 spaces for left margin
        for cat in categories:
            char = cat.name[i] if i < len(cat.name) else " "
            line += f" {char} "
        chart += line + " \n"



    return chart.rstrip("\n")
