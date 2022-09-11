money = int(input("enter the amount of money "))
year = int(input("enter how long the money will be in the bank "))
annual_interest = float(0.04)
r = 1
total = money * (r + annual_interest/r) ^ year
print("the total amount of money you will wet after", year, "years is", total)
