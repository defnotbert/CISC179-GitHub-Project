# CISC179-GitHub-Project
# This program is a graphed compound interest calculator with monthly contributions and is checked against https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator
# It utilizes a class called Interestcalculator that encompasses functions that contain the formulae for compound interest and monthly contributions.
# The code requires the inputs for Principal, Annual percent interest rate, Frequency compounded (limited to annually, monthly, and daily for simplicity's sake), Monthly contribution amount, and Time invested in years. All of these inputs cannot be negative.
# It then outputs the balance as well as a plotted graph "Balance over Years" which plots years along the X-axis and Balance ($) on the Y-axis.
# One note is that the daily compound balance is slightly different (within 1.1% in a 25 year period) when checked against the aforementioned website. This could be due to the calculation used for how many days there are in a month, etc.
