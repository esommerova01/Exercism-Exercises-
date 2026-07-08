"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""

def exchange_money(budget, exchange_rate):
    """Calculate estimated value after exchange."""
    return budget / exchange_rate

print (exchange_money(120, 1.2))


def get_change(budget, exchanging_value):
    """Calculate currency left after an exchange."""
    return float(budget - exchanging_value)

print (get_change(127.5, 120))


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of currency at current denomination."""
    return denomination * number_of_bills

print (get_value_of_bills (5, 120))

   
def get_number_of_bills(amount, denomination):
    """Calculate the number of currency units (bills) within the amount."""
    return int(amount/denomination)

print (get_number_of_bills (69.42, 5))    
    
def get_leftover_of_bills(amount, denomination):
    """Calculate leftover amount after exchanging into bills."""
    return amount % denomination

print (get_leftover_of_bills (152.5, 10))


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of the new currency."""
   
    #Calculate the exchange rate including fees
    actual_rate = exchange_rate * (1 + (spread / 100))

    #How much foreign currency you can afford
    total_currency = int(budget/actual_rate)

    #Round down to the max bills 
    max_bills = total_currency//denomination
    
    return int(max_bills*denomination)