#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:17:48 2019
@author: hungtran
"""

starting_salary = int(input("Enter the starting salary: "))
semi_annual_raise = 0.07
annual_return = 0.04
total_cost = 1000000
portion_down_payment = 0.25 * total_cost
saving_months = 36

min_rate = 0        # 0%
max_rate = 10000    # 100%

guess_rate = (max_rate + min_rate) / 2.0
steps = 0
found = False
current_savings = 0.0

while abs(current_savings - portion_down_payment) > 100:
    annual_salary = starting_salary
    current_savings = 0.0
    print(guess_rate)

    for i in range(1, saving_months + 1):
        current_savings += (guess_rate/100)*(annual_salary/12) + current_savings*(annual_return/12)

        if i % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    print(current_savings)

    if current_savings > portion_down_payment:
        max_rate = guess_rate
    else:
        min_rate = guess_rate

    guess_rate = (max_rate + min_rate) / 2.0
    steps += 1

if guess_rate <= 100:
    print "Best savings rate: ", guess_rate / 100
    print "Steps in bisection search:", steps
else:
    print "It is not possible to pay the down payment in three years "
