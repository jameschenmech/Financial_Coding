# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:59:41 2018

@author: James
"""

import numpy as np
import matplotlib.pyplot as plt


# Enter your annual salary
salary = 85000

# Assume a tax rate of 30%
tax_rate = 0.30

# Calculate your salary after taxes
salary_after_taxes = salary*(1-tax_rate)
print("Salary after taxes: " + str(round(salary_after_taxes, 2)))

# Calculate your monthly salary after taxes
monthly_takehome_salary = salary_after_taxes/12
print("Monthly takehome salary: " + str(round(monthly_takehome_salary, 2)))

# Enter your monthly rent
monthly_rent = 1200

# Enter your daily food budget
daily_food_budget = 30

# Calculate your monthly food budget assuming 30 days per month
monthly_food_budget = 30*30

# Set your monthly entertainment budget
monthly_entertainment_budget = 200

# Allocate funds for unforeseen expenses, just in case
monthly_unforeseen_expenses = 250

# Next, calculate your total monthly expenses
monthly_expenses = monthly_rent+monthly_food_budget+monthly_entertainment_budget+monthly_unforeseen_expenses
print("Monthly expenses: " + str(round(monthly_expenses, 2)))

# Finally, calculate your monthly take-home savings
monthly_savings = monthly_takehome_salary - monthly_expenses
print("Monthly savings: " + str(round(monthly_savings, 2)))


# Create monthly forecasts up to 15 years from now
forecast_months = 12*15

# Set your annual salary growth rate
annual_salary_growth = 0.05

# Calculate your equivalent monthly salary growth rate
monthly_salary_growth = (1+annual_salary_growth)**(1/12) - 1

# Forecast the cumulative growth of your salary
cumulative_salary_growth_forecast = np.cumprod(np.repeat(1 + monthly_salary_growth, forecast_months))

# Calculate the actual salary forecast
salary_forecast = cumulative_salary_growth_forecast*monthly_takehome_salary

# Plot the forecasted salary
plt.figure(1)
plt.plot(salary_forecast, color='blue', label='salary forecast')
plt.legend(loc=2)
plt.show()


# Create monthly forecasts up to 15 years from now
forecast_months = 12*15

# Set the annual inflation rate
annual_inflation = 0.025

# Calculate the equivalent monthly inflation rate
monthly_inflation = (1+annual_inflation)**(1/12)-1

# Forecast cumulative inflation over time
cumulative_inflation_forecast = np.cumprod(np.repeat(1 + monthly_inflation, forecast_months))

# Calculate your forecasted expenses
expenses_forecast = monthly_expenses*cumulative_inflation_forecast

# Plot the forecasted expenses
plt.figure(2)
plt.plot(expenses_forecast, color='red', label='expenses forecast')
plt.legend(loc=2)
plt.show()



# Calculate your savings for each month
savings_forecast = salary_forecast-expenses_forecast

# Calculate your cumulative savings over time
cumulative_savings = np.cumsum(savings_forecast)

# Print the final cumulative savings after 15 years
final_net_worth = cumulative_savings[-1]
print("Your final net worth: " + str(round(final_net_worth, 2)))

# Plot the forecasted savings
plt.figure(3)
plt.plot(cumulative_savings, color='blue', label='cumulative savings')
plt.legend(loc=2)
plt.show()

# Forecast out 15 years ahead, 12 months at a time
forecast_months = 15*12

# Set the annual investment return to 7%
investment_rate_annual = 0.07

# Calculate the monthly investment return
investment_rate_monthly = (1+investment_rate_annual)**(1/12)-1

# Calculate your required monthly investment to amass $1M
required_investment_monthly = np.pmt(rate=investment_rate_monthly, nper=15*12, pv=0, fv=-1e6)
print("You will have to invest $" + str(round(required_investment_monthly, 2)) + " per month to amass $1M over 15 years")


# Calculate your monthly cash flow after expenses
cash_flow_forecast = salary_forecast - expenses_forecast

# Set the percentage of your income to deposit each month
monthly_investment_percentage = 0.30

# Calculate your monthly deposit into your investment account
investment_deposit_forecast = cash_flow_forecast*monthly_investment_percentage

# The rest goes into your savings account
savings_forecast_new = cash_flow_forecast*(1-monthly_investment_percentage)

# Calculate your cumulative savings over time
cumulative_savings_new = np.cumsum(savings_forecast_new)

# Plot your forecasted monthly savings vs investments
plt.figure(4)
plt.plot(investment_deposit_forecast, color='red', label=('investment deposit'))
plt.plot(savings_forecast_new, color='blue', label='savings forecast')
plt.legend(loc=2)
plt.show()

# Initialize the investments array and net worth array
investment_portfolio = np.repeat(0.0, forecast_months)
net_worth = np.repeat(0.0, forecast_months)

# Loop through each forecast period
for i in range(forecast_months):
    
    # Find the previous investment deposit amount
    if i == 0: 
        previous_investment = 0
    else:
        previous_investment = investment_portfolio[i-1]
        
    # Calculate the value of your previous investments, which have grown
    previous_investment_growth = previous_investment*(1 + investment_rate_monthly)
    
    # Add your new deposit to your investment portfolio
    investment_portfolio[i] =  previous_investment_growth + investment_deposit_forecast[i]
    
    # Calculate your net worth at each point in time
    net_worth[i] = investment_portfolio[i]+cumulative_savings_new[i]
    
    # Print the results at each period
    print("Period " + str(i) + ": Current Investment Balance: " + \
          str(round(investment_portfolio[i], 2)) + \
          " | Savings Account: " + str(round(cumulative_savings_new[i], 2)) + \
          " | Net Worth: " + str(round(net_worth[i], 2)) \
         )
         
# Plot your forecasted cumulative savings vs investments and net worth
plt.figure()
plt.plot(investment_portfolio, color='red', label='investment portfolio')
plt.plot(cumulative_savings_new, color='blue',label='cumulative savings new')
plt.plot(net_worth, color='green', label='net worth')
plt.legend(loc=2)
plt.show()


# Set your future net worth
future_net_worth = 900000

# Set the annual inflation rate to 2.5%
annual_inflation = 0.025

# Calculate the present value of your terminal wealth over 15 years
inflation_adjusted_net_worth = np.pv(rate=annual_inflation, nper=15, pmt=0, fv=-1*future_net_worth)
print("Your inflation-adjusted net worth: $" + str(round(inflation_adjusted_net_worth, 2)))

#plt.close('all')