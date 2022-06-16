from re import L
from typing import List
from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "5585968e850acd9685b8"

printer = PrettyPrinter()

#getting currencies
def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"  # what is f string
    url = BASE_URL + endpoint
    data = get(url).json()['results'] #getting the dictionary in data as results

    data = list(data.items()) #converting dictionary into list so that we can sort it

    data.sort()

    return data


def print_currencies(currencies):
    for name,currency in currencies:  #list of tuples
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol","") #get tries to get the value from currency and if not there returns empty string
        print(f"{_id} - {name} - {symbol}")


    
def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print('Invalid currencies.')
        return
    
    rate = list(data.values())[0] #converting value into list
    print(f"{currency1} -> {currency2} = {rate}")

    return rate

# data=get_currencies()
# print_currencies(data)
# rate = exchange_rate("USD","CAD")
# print(rate)

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1,currency2)
    if rate is None: #if there is no valid rate 
        return
    
    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    converted_amount = rate * amount 
    print(f"{amount} {currency1} is equal to {converted_amount}  {currency2}")
    return converted_amount

def main():
    currencies = get_currencies() 

    print("Welcome to currency converter!")
    

    while True:
        print("List of commands : ")
        print("List - lists the different currencies")
        print("Convert - convert from one currency to another")
        print("Rate - get the exchange rate of two currencies")
        print()#seperater
        command = input("Enter a command (q to quit) : ").lower()

        if command == "q":
            break

        elif command == "list":
            print_currencies(currencies)
            print("-----------------------")

        elif command == "convert":
            currency1 = input("Enter a base  currency : ").upper()
            amount = input("Enter an amount you want to convert: ")
            currency2 = input("Enter a currency to convert to : ").upper()

            convert(currency1,currency2,amount)
            print("-----------------------")

        elif command == "rate":
            currency1 = input("Enter a base  currency : ").upper()
            currency2 = input("Enter a currency to convert to : ").upper()
            exchange_rate(currency1,currency2)
            print("-----------------------")
        else:
            print("unrecognized command!")
            print("-----------------------")


main()#calling main function 

            





