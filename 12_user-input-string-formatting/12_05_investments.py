# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.
investment_amount = int(input("Input the amouny you would like to invest:"))

return_percent = int(input("input the number percentage of return per year you get on that invetsment:")) * 0.01

years_invested = int(input("input the amount of years you would like to invest for:"))

def invest_return(amount, percent, years):
    profit = (amount * percent) * years
    return profit
    
print(invest_return(investment_amount, return_percent, years_invested))