import matplotlib.pyplot as plt

# Scope of InterestCalculator calculates interest and future values based on pricipal, interest rate, and compounding period
# Excluding years allows users to create an instance of 'InterestCalculator' and perform calculations for different years without
# having to recreate the object
class InterestCalculator:
    def __init__(self, principal, interest_rate, period):
        self.principal = principal
        self.interest_rate = interest_rate
        self.period = period
        self.future_values = [] #list atribute allows for storage of balances over years
        
    # Function for compound interest that iterates from year 0 to input year
    def compound_interest(self, years):
        self.future_values = []
        for year in range(years + 1):
            #Compound interest formula
            future_value = self.principal * (1 + self.interest_rate / self.period) ** (self.period * year)
            self.future_values.append(future_value)
        return self.future_values
    
    # Function using monthly contributions, which are also affected by compounding period (i.e. annually, monthly, and daily in this certain calculator)
    def add_monthly_contributions(self, monthly_contributions, years):
        self.future_values = []
        future_value = self.principal
        if self.period == 1:  # Annually
            for year in range(years + 1):
                if year > 0:
                    future_value = future_value * (1 + self.interest_rate / self.period) + 12 * monthly_contributions
                self.future_values.append(future_value)
        elif self.period == 12:  # Monthly
            for month in range(years * 12 + 1):
                if month > 0:
                    future_value = future_value * (1 + self.interest_rate / self.period) + monthly_contributions
                if month % 12 == 0:
                    self.future_values.append(future_value)
        elif self.period == 365:  # Daily
            days_in_a_month = 365 / 12 # This may vary from calculator to calculator found online
            for day in range(years * 365 + 1):
                if day > 0:
                    future_value = future_value * (1 + self.interest_rate / self.period)
                    if day % int(days_in_a_month) == 0:
                        future_value += monthly_contributions
                if day % 365 == 0:
                    self.future_values.append(future_value)
        return self.future_values

if __name__ == '__main__':
    while True:
        principal = float(input('Enter the principal amount ($): \n'))
        if principal < 0:
            print("Principal can't be less than zero")
        else:
            break
    while True:
        interest = float(input('Enter the annual percent interest rate (%): \n')) / 100
        if interest < 0:
            print("Interest can't be less than zero")
        else:
            break
    while True:
        period = int(input('Enter frequency compounded per year (e.g. annually = 1, monthly = 12, daily = 365): \n'))
        if period < 0:
            print("Period can't be less than zero")
        elif period not in [1, 12, 365]:
            print("Period must be one of the following: 1 (annually), 12 (monthly), 365 (daily)")
        else:
            break
    while True:
        years = int(input('Enter the time in years: \n'))
        if years < 0:
            print("Years can't be less than zero")
        else:
            break
    while True:
        monthly_contributions = float(input('Enter the monthly contribution amount ($): '))
        if monthly_contributions < 0:
            print("Monthly Contributions can't be less than zero")
        else:
            break
    
    calculator = InterestCalculator(principal, interest, period)
    calculator.add_monthly_contributions(monthly_contributions, years)

    total = calculator.future_values[-1]
    print(f'Balance after {years} year(s): ${(total):.2f}')
    
    #arrays of years and balances for matplotlib to plot
    years_array = list(range(years + 1))
    balances_array = calculator.future_values
    
    # plot of balances over years
    plt.plot(years_array, balances_array, marker='o')
    plt.xlabel('Years')
    plt.ylabel('Balance ($)')
    plt.title('Balance Over Years')
    plt.grid(axis='y')
    plt.show()