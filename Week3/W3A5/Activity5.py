'''
Week 3 - Activity 5: Money Exchange Project with Database
============================================================
Design ER diagram and develop a database for the money exchange project (with at least three entities and OOP style). 
In a README file, clearly describe how many tables you have created and justify why each table is necessary. 
Project scope: The Money Exchange System should allow a exchange business to manage customers, currencies, 
exchange rates, and currency exchange transactions.

README
======

This project uses four tables:

1. Customers - Stores customer names and contact details so customers can be
    identified and managed.
2. Currencies - Stores currency codes, names, and symbols. A separate table
    prevents currency information from being repeated in every transaction.
3. ExchangeRates - Stores conversion rates between currencies and the dates
    on which they were added, allowing rate history to be maintained.
4. Transactions - Records each customer's exchange, including the currencies,
    amount, and date. This table represents the main business activity.

These four tables are necessary because they separate customer data, reusable
currency data, exchange-rate history, and transaction records. This reduces
duplication, supports relationships between entities, and makes the database
easier to maintain and query.
'''

from datetime import date

from MoneyExchangeDB import (
    create_database,
    add_customer,
    add_currency,
    add_exchange_rate,
    add_transaction,
    get_customers,
    get_currencies,
    get_exchange_rates,
    get_transactions,
)

def main():
    create_database()
    
    menu = """
            1. Add customer
            2. Add currency
            3. Add exchange rate
            4. Add transaction
            5. View all data
            6. Exit
            """
    while True:
        print(menu)
        choice = input("Select an option: ").strip()

        try:
            if choice == "1":
                name = input("Customer name: ").strip()
                email = input("Customer email: ").strip()
                phone = input("Customer phone: ").strip()
                add_customer(name, email, phone)
                print("Customer added successfully.")

            elif choice == "2":
                code = input("Currency code (for example, USD): ").strip().upper()
                name = input("Currency name: ").strip()
                symbol = input("Currency symbol: ").strip()
                add_currency(code, name, symbol)
                print("Currency added successfully.")

            elif choice == "3":
                from_currency = input("From currency code: ").strip().upper()
                to_currency = input("To currency code: ").strip().upper()
                rate = float(input("Exchange rate: ").strip())
                add_exchange_rate(from_currency, to_currency, rate, date.today().isoformat())
                print("Exchange rate added successfully.")

            elif choice == "4":
                customer_id = int(input("Customer ID: ").strip())
                from_currency = input("From currency code: ").strip().upper()
                to_currency = input("To currency code: ").strip().upper()
                amount = float(input("Amount: ").strip())
                add_transaction(
                    customer_id,
                    from_currency,
                    to_currency,
                    amount,
                    date.today().isoformat(),
                )
                print("Transaction added successfully.")

            elif choice == "5":
                print("Customers:", get_customers())
                print("Currencies:", get_currencies())
                print("Exchange rates:", get_exchange_rates())
                print("Transactions:", get_transactions())

            elif choice == "6":
                print("Goodbye.")
                break

            else:
                print("Invalid option. Please select 1-6.")
        except (ValueError, TypeError) as error:
            print(f"Invalid input: {error}")
        except Exception as error:
            print(f"Unable to complete the operation: {error}")


if __name__ == "__main__":
    main()



