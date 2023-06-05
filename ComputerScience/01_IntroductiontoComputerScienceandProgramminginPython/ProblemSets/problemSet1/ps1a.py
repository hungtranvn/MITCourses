#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
House hunting problem
Created on Sun Apr 14 01:19:09 2019
@author: hungtran
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

monthly_saved = (annual_salary/12.0)*portion_saved
portion_down_payment = 0.25
current_savings = 0.0
annual_return = 0.04
number_of_months = 0

while (current_savings < 0.25*total_cost):
    current_savings += portion_saved*(annual_salary/12) + current_savings*(annual_return/12)
    number_of_months += 1

print"Number of months: ", number_of_months
