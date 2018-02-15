# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:55:55 2018

@author: James  Chen
"""

import numpy as np
import matplotlib.pyplot as plt 

present_val = np.pv(rate=0.01, nper=3, pmt=0, fv=100)
print(present_val)

future_val = np.fv(rate=0.05, nper=3, pmt=0, pv=-100)
print(future_val)

# Calculate investment_1
investment_1 = np.fv(rate=0.08, nper=10, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 10 years")

# Calculate investment_2
investment_1_discounted = np.pv(rate=0.03, nper=10, pmt=0, fv=investment_1)
print("After adjusting for inflation, investment 1 is worth $" + \
      str(round(-investment_1_discounted, 2)) + " in today's dollars")

# =============================================================================
# #Net Present Value (NPV) - sum off all discounted cash flows
# =============================================================================
#cash flow analysis
project1_cf = np.array([-100, 100, 125, 150, 175])
project2_cf = np.array([100, 100, -100, 200, 300])

# #Net Present Value
np_proj1 = np.npv(rate=0.03, values=project1_cf)
np_proj2 = np.npv(rate=0.03, values=project2_cf)
print(" Project 1 NPV: ${0:.2f}\n Project 2 NPV: ${1:.2f}".format(np_proj1,np_proj2))


# #Get paid now
# Calculate investment_1
investment_1 = np.pv(rate=0.03, nper=30, pmt=0, fv=100)
print("Investment 1 is worth $" + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = np.pv(rate=0.03, nper=50, pmt=0, fv=100)
print("Investment 2 is worth $" + str(round(-investment_2, 2)) + " in today's dollars")

# Calculate investment_3
investment_3 = np.pv(rate=0.03, nper=100, pmt=0, fv=100)
print("Investment 3 is worth $" + str(round(-investment_3, 2)) + " in today's dollars")

# =============================================================================
# #Internal Rate of Return (IRR) - solve for IRR in the NPV equation
# =============================================================================
project_1 = np.array([-100, 150, 200])
irr_proj1 = np.irr(project_1)
print("Internal rate of return of Project_1 is: {0:.3f}%".format(irr_proj1*100))

# Create a numpy array of cash flows for Project 1
cf_project_1 = np.array([-1000, 200, 250, 300, 350, 400, 450, 500, 550, 600])

# Create a numpy array of cash flows for Project 2
cf_project_2 = np.array([-1000, 150, 225, 300, 375, 425, 500, 575, 600, 625])

# Scale the original objects by 1000x
cf_project1 = cf_project_1*1000
cf_project2 = cf_project_2*1000

# Calculate the internal rate of return for Project 1
irr_project1 = np.irr(cf_project1)
print("Project 1 IRR: " + str(round(100*irr_project1, 2)) + "%")

# Calculate the internal rate of return for Project 2
irr_project2 = np.irr(cf_project2)
print("Project 2 IRR: " + str(round(100*irr_project2, 2)) + "%")

# =============================================================================
# #Weighted Average Cost of Capital (WACC)
# =============================================================================
percent_equity = 0.80
percent_debt = 0.20
cost_equity = 0.14
cost_debt = 0.12
tax_rate = 0.35

wacc = (percent_equity*cost_equity) + (percent_debt*cost_debt)*\
    (1-tax_rate)
print("wacc:  ",wacc)

#sample project
cf_project1 = np.repeat(100,5)
npv_project1 = np.npv(0.13, cf_project1)
print("npv_project1: ",npv_project1)

#another example
# Set the market value of debt
mval_debt = 1e6
# Set the market value of equity
mval_equity = 1000000

# Compute the total market value of your company's financing
mval_total = mval_debt + mval_equity

# Compute the proportion of your company's financing via debt
percent_debt = mval_debt/mval_total
print("Debt Financing: " + str(round(100*percent_debt, 2)) + "%")

# Compute the proportion of your company's financing via equity
percent_equity = mval_equity/mval_total
print("Equity Financing: " + str(round(100*percent_equity, 2)) + "%")

# Set the cost of equity
cost_equity = 0.18

# Set the cost of debt
cost_debt = 0.12

# Set the corporate tax rate
tax_rate = 0.35

# Calculate the WACC
wacc = (percent_equity*cost_equity) + (percent_debt*cost_debt)*\
    (1-tax_rate)
print("WACC: " + str(round(100*wacc, 2)) + "%")

#cash flows
cf_project1 = np.array([-1000000,   200000,   250000,   300000,   350000,\
    400000, 450000,   500000,   550000,   600000])
cf_project2 = np.array([-1000000,   150000,   225000,   300000,   375000,\
    425000, 500000,   575000,   600000,   625000])

# Calculate the net present value for Project 1
npv_project1 = np.npv(rate=wacc, values=cf_project1)
print("Project 1 NPV: " + str(round(npv_project1, 2)))

# Calculate the net present value for Project 2
npv_project2 = np.npv(rate=wacc, values=cf_project2)
print("Project 2 NPV: " + str(round(npv_project2, 2)))

# =============================================================================
# #Equivalent Annual Annuity - assume each project is a loan of value NPV
#paying out each year a payment that sums to the NPV
#Comparing projects of different lifespans
# =============================================================================

# Create a numpy array of cash flows for Project 1
cf_project_1 = np.array([-700, 100, 150, 200, 250, 300, 350, 400])

# Create a numpy array of cash flows for Project 2
cf_project_2 = np.array([-400, 50, 100, 150, 200, 250, 300])

# Scale the original objects by 1000x
cf_project1 = cf_project_1*1000
cf_project2 = cf_project_2*1000

# Calculate the IRR for Project 1
irr_project1 = np.irr(cf_project1)
print("Project 1 IRR: " + str(round(100*irr_project1, 2)) + "%")

# Calculate the IRR for Project 2
irr_project2 = np.irr(cf_project2)
print("Project 2 IRR: " + str(round(100*irr_project2, 2)) + "%")

# Set the wacc equal to 12.9%
wacc = 0.129

# Calculate the NPV for Project 1
npv_project1 = np.npv(rate=wacc,values=cf_project1)
print("Project 1 NPV: " + str(round(npv_project1, 2)))

# Calculate the NPV for Project 2
npv_project2 = np.npv(rate=wacc, values=cf_project2)
print("Project 2 NPV: " + str(round(npv_project2, 2)))

# Calculate the EAA for Project 1
eaa_project1 = np.pmt(rate=wacc, nper=8, pv=-1*npv_project1, fv=0)
print("Project 1 EAA: " + str(round(eaa_project1, 2)))

# Calculate the EAA for Project 2
eaa_project2 = np.pmt(rate=wacc, nper=7, pv=-1*npv_project2, fv=0)
print("Project 2 EAA: " + str(round(eaa_project2, 2)))

# =============================================================================
# #Mortgage Basics
# =============================================================================

annual_rate = 0.0438
montly_rate = (1+annual_rate)**(1/12)-1
montly_payments = np.pmt(rate=montly_rate, nper=12*30, pv=300000)
print("monlthly mortgage payment: ${0:.2F}".format(montly_payments))

# =============================================================================
# Interst and Principal Payments
# =============================================================================

mortgage_loan = 640000.0

mortgage_payment_periods = 360

mortgage_rate_periodic = 0.003072541703255549

periodic_mortgage_payment = 2941.1253631889758

# Calculate the amount of the first loan payment that will go towards interest
initial_interest_payment = mortgage_loan*mortgage_rate_periodic

print("Initial Interest Payment: " + str(round(initial_interest_payment, 2)))

# Calculate the amount of the first loan payment that will go towards principal
initial_principal_payment = periodic_mortgage_payment-initial_interest_payment

print("Initial Principal Payment: " + str(round(initial_principal_payment, 2)))

# Initialize the principal remaining array with length equal to the number of payment periods
# Initialize variables
interest_paid = np.repeat(0.0, mortgage_payment_periods)
principal_paid = np.repeat(0.0, mortgage_payment_periods)
principal_remaining = np.repeat(0.0, mortgage_payment_periods)

# Loop through each mortgage payment period
for i in range(0, mortgage_payment_periods):
    
    # Handle the case for the first iteration
    if i == 0:
        previous_principal_remaining = mortgage_loan
    else:
        previous_principal_remaining = principal_remaining[i-1]
        
    # Calculate the interest and principal payments
    interest_payment = round(previous_principal_remaining*mortgage_rate_periodic, 2)
    principal_payment = round(periodic_mortgage_payment-interest_payment, 2)
    
    # Catch the case where all principal is paid off in the final period
    if previous_principal_remaining - principal_payment < 0:
        principal_payment = previous_principal_remaining
        
        # Collect the historical values
    interest_paid[i] = interest_payment
    principal_paid[i] = principal_payment
    # Collect the principal remaining values in an array
    principal_remaining[i] = previous_principal_remaining - principal_payment
    
    # Output the results
    print("Period " + str(i) + ": " + \
    "Interest Paid: " + str(interest_payment) + \
    " | Principal Paid: " + str(principal_payment) + \
    " | Remaining Balance: " + str(principal_remaining[i]))
    

# Plot the interest vs principal
plt.plot(interest_paid, color="red", label ='Interest')
plt.plot(principal_paid, color="blue", label = 'Principal')
plt.legend(loc=2)
plt.show()
plt.close()
# =============================================================================
# #Home Ownership, Equity and forcasting
# =============================================================================
home_value = 800000

down_payment_percent = 0.20

mortage_loan = home_value*(1-down_payment_percent)

mortgage_payment_periods = 360

mortgage_rate_periodic = 0.003072541703255549  #montly_rate = (1+annual_rate)**(1/12)-1

annual_rate = (mortgage_rate_periodic+1)**12-1


# Initialize the principal remaining array with length equal to the number of payment periods
# Initialize variables
interest_paid = np.repeat(0.0, mortgage_payment_periods)
principal_paid = np.repeat(0.0, mortgage_payment_periods)
principal_remaining = np.repeat(0.0, mortgage_payment_periods)

# Loop through each mortgage payment period
for i in range(0, mortgage_payment_periods):
    
    # Handle the case for the first iteration
    if i == 0:
        previous_principal_remaining = mortgage_loan
    else:
        previous_principal_remaining = principal_remaining[i-1]
        
    # Calculate the interest and principal payments
    interest_payment = round(previous_principal_remaining*mortgage_rate_periodic, 2)
    principal_payment = round(periodic_mortgage_payment-interest_payment, 2)
    
    # Catch the case where all principal is paid off in the final period
    if previous_principal_remaining - principal_payment < 0:
        principal_payment = previous_principal_remaining
        
        # Collect the historical values
    interest_paid[i] = interest_payment
    principal_paid[i] = principal_payment
    # Collect the principal remaining values in an array
    principal_remaining[i] = previous_principal_remaining - principal_payment
    
    # Output the results
    print("Period " + str(i) + ": " + \
    "Interest Paid: " + str(interest_payment) + \
    " | Principal Paid: " + str(principal_payment) + \
    " | Remaining Balance: " + str(principal_remaining[i]))
    
# Plot the interest vs principal
plt.plot(interest_paid, color="red", label ='Interest')
plt.plot(principal_paid, color="blue", label = 'Principal')
plt.legend(loc=2)
plt.show()
plt.close()
# Calculate the cumulative home equity (principal) over time
cumulative_home_equity = np.cumsum(principal_paid)

# Calculate the cumulative interest paid over time
cumulative_interest_paid = np.cumsum(interest_paid)

# Calculate your percentage home equity over time
cumulative_percent_owned = down_payment_percent + (cumulative_home_equity/home_value)
print(cumulative_percent_owned)

# Plot the cumulative interest paid vs equity accumulated
plt.plot(cumulative_interest_paid, color='red', label='Cumulative Interest Paid')
plt.plot(cumulative_home_equity, color='blue', label='Cumulative Home Equity')
plt.legend(loc=2)
plt.show()
plt.close()

# Assume a 0.25% growth rate per month
periodic_home_value_growth = 0.0025

# Initialize an array of growth rates
growth_array = np.repeat(periodic_home_value_growth, mortgage_payment_periods)

# Calculate the cumulative growth over time
cumulative_growth_forecast = np.cumprod(1+growth_array)

# Forecast the home value over time
home_value_forecast = home_value*cumulative_growth_forecast

# Forecast the home equity value owned over time
cumulative_home_value_owned = home_value_forecast*cumulative_percent_owned

# Plot the home value vs equity accumulated
plt.plot(home_value_forecast, color='red', label='Home Value')
plt.plot(cumulative_home_value_owned, color='blue', label='Equity')
plt.legend(loc=2)
plt.show()
plt.close()

# Assume a 0.45% decrease in housing prices per month
periodic_home_value_decline = -0.0045

# Initialize an array of growth rates
decline_array = np.repeat(periodic_home_value_decline, mortgage_payment_periods)

# Calculate the cumulative growth over time
cumulative_decline_forecast = np.cumprod(1+decline_array)

# Forecast the home value over time
home_value_forecast = home_value*cumulative_decline_forecast

# Print all periods where your mortgage is underwater
underwater = home_value_forecast < principal_remaining
print(underwater)

# Plot the home value vs principal remaining
plt.plot(home_value_forecast, color='red', label='home value')
plt.plot(principal_remaining, color='blue', label = 'principle remaining')
plt.legend(loc=2)
plt.show()
plt.close()

