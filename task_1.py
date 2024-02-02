from pulp import LpStatus, LpMaximize, LpProblem, LpVariable


model = LpProblem(name="optimization", sense=LpMaximize)

lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Функція цілі (Максимізація прибутку)
model += lemonade + fruit_juice, "Profit"

# Обмеження
model += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
model += lemonade <= 50, "Sugar_Constraint"
model += lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

status = model.solve()
total = lemonade.varValue + fruit_juice.varValue

# print(LpStatus[model.status])

print(
    f"Lemonade: {lemonade.varValue}, Fruit Juice: {fruit_juice.varValue}, Total: {total}"
)
