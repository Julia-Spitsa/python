import json
firms = {}
av_profit = {}
average_profit = 0
count = 0
with open('file7.txt', 'r', encoding="utf-8") as f:
    for line in f:
        firm, form, revenue, cost = line.split()
        profit = int(revenue) - int(cost)
        firms.update({firm: profit})
        if profit > 0:
            average_profit += profit
            count += 1
    average_profit = average_profit / count
    av_profit.update({"average_profit": average_profit})
    profit_list = [firms, av_profit]
    print(profit_list)
with open("file7.json", 'w') as f:
    json.dump(profit_list, f)
