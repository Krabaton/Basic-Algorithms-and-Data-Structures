import pulp as plp

prob = plp.LpProblem("Wood Company", plp.LpMaximize)

x1 = plp.LpVariable("x1", 0, None, cat=plp.LpContinuous)
x2 = plp.LpVariable("x2", 0, None, cat=plp.LpContinuous)

prob += 6 * x1 + 2 * x2, "Profit"

prob += 4 * x1 + 5 * x2 <= 61, "Wood"
prob += -3 * x1 + 4 * x2 <= 24, "Cement"
prob += 5 * x1 - 3 * x2 <= 30, "Steel"

prob.solve()
print(f"Status: {plp.LpStatus[prob.status]}")
print(f"x1 = {plp.value(x1)}")  # x1.varValue
print(f"x2 = {plp.value(x2)}")
print(f"Profit = {plp.value(prob.objective)}")
