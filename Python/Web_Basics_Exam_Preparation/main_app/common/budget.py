def calculate_left_budget(profile, expenses):
    return profile.budget - sum(expense.price for expense in expenses)
