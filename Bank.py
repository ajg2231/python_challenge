import pandas as pd
c = pd.read_csv("/Users/alexandergoldstein/Downloads/03-Python_Homework_PyBank_Resources_budget_data.csv")

a = c['Date'].count()

b = c['Profit/Losses'].sum()


d = c.max()


e = c.min()

with open("Bank.txt", "w") as text_file:
    print(f"Total months are: {a}", file=text_file)
    print(f"Total profit is: {b}", file=text_file)
    print(f"Maximum Profits: {d}", file=text_file)
    print(f"Maximum Losses: {e}", file=text_file)
    

#print(a) #returns total number of months under "Month"
#print("Total Profit is", b) #returns total profit/loss
#print("Maximum Profits:", d) #maximum profits, date and amount
#print("Maximum Losses", e) #maximum losses, date and amount

