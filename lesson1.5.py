revenue = float(input("Give your reveneu: "))
costs = float(input("Give your costs: "))
if revenue > costs:
    rev_ = revenue - costs
    print(f"Profit is {rev_}")
    workers = float(input("Kow much workers do you have?: "))
    average = float(rev_ / workers)
    print("Every worker earned ", "%.2f" % average, " in average!")
if revenue == costs:
        print("Your firma has not revenue but they has not costs too.")


else:
    print("Your firma has costs!!!")
