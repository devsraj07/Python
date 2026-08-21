# Money Exchange Project

This project is a SQLite-based money exchange system. It allows an exchange business to store customers, supported currencies, exchange rates, and completed exchange transactions.

## Database Tables

The database contains **four tables**. Each table represents a separate entity or business concept and avoids storing repeated information in transaction records.

### 1. `Customer`

Stores the people who use the money exchange service.

- `CustomerID`: Primary key that uniquely identifies each customer.
- `Name`: Customer's name.
- `Email`: Customer's email address. It must be unique.
- `PhoneNumber`: Customer's phone number.

This table is necessary so that customer contact information is stored once and can be connected to many exchange transactions.

### 2. `Currency`

Stores the currencies supported by the business.

- `CurrencyCode`: Three-letter primary key, such as `USD` or `EUR`.
- `CurrencyName`: Full currency name.
- `Symbol`: Currency symbol, such as `$` or `€`.

This table is necessary so currencies can be managed centrally and referenced by exchange rates and transactions instead of repeating currency details in every record.

### 3. `ExchangeRate`

Stores the conversion rate between two currencies for a particular date.

- `RateID`: Primary key.
- `FromCurrency`: Currency being exchanged, linked to `Currency.CurrencyCode`.
- `ToCurrency`: Currency received, linked to `Currency.CurrencyCode`.
- `Rate`: Conversion rate.
- `Date`: Date on which the rate applies.

This table is necessary because exchange rates can change over time and different currency pairs can have different rates.

### 4. `ExchangeTransaction`

Stores each completed currency exchange made by a customer.

- `TransactionID`: Primary key.
- `CustomerID`: Customer who made the exchange, linked to `Customer.CustomerID`.
- `FromCurrency`: Currency exchanged, linked to `Currency.CurrencyCode`.
- `ToCurrency`: Currency received, linked to `Currency.CurrencyCode`.
- `Amount`: Amount exchanged.
- `TransactionDate`: Date of the transaction.

This table is necessary to maintain a history of business activity and connect each exchange to its customer and currencies.

## Relationships

- One customer can have many exchange transactions.
- One currency can be used in many exchange rates and transactions.
- `ExchangeRate` has two relationships with `Currency`: one for the source currency and one for the destination currency.
- `ExchangeTransaction` has three relationships: one to `Customer`, one to the source `Currency`, and one to the destination `Currency`.

The entity relationship diagram is available in [MoneyExchangeERD.png](MoneyExchangeERD.png).

## Project Files

- `Activity5.py`: Command-line menu and user input.
- `MoneyExchangeDB.py`: SQLite connection, table creation, insert functions, and retrieval functions.
- `MoneyExchangeERD.png`: Entity relationship diagram.
- `money_exchange.db`: SQLite database file created when the program runs.

## Requirements

- Python 3
- SQLite3, included with Python

No external packages are required.

## How to Run

From this directory, run:

```bash
python Activity5.py
```

The program creates `money_exchange.db` automatically if it does not already exist.

## Menu Options

1. Add customer
2. Add currency
3. Add exchange rate
4. Add transaction
5. View all data
6. Exit

Add customers and currencies before adding exchange rates or transactions so that the referenced records are available.
