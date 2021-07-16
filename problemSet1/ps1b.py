#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Saving, with raise
Finding the right amount to save away
Created on Sun Apr 14 02:14:34 2019
@author: hungtran
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual salary raise: "))

monthly_saved = (annual_salary/12.0)*portion_saved
portion_down_payment = 0.25
current_savings = 0.0
annual_return = 0.04
number_of_months = 0

while (current_savings < 0.25*total_cost):
    current_savings += portion_saved*(annual_salary/12) + current_savings*(annual_return/12)
    number_of_months += 1
    if (number_of_months % 6 == 0):
        annual_salary += semi_annual_raise*annual_salary

print"Number of months: ", number_of_months
