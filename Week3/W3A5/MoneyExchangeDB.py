'''
Money Exchange database management
'''
import sqlite3



# 1. Create a database connection and define the schema for the Money Exchange System.
def create_database():
    conn = sqlite3.connect('money_exchange.db')
    cursor = conn.cursor()

    # Create Customer table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customer (
            CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(100) NOT NULL,
            Email VARCHAR(100) NOT NULL UNIQUE,
            PhoneNumber VARCHAR(20) NOT NULL
        )
    ''')

    # Create Currency table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Currency (
            CurrencyCode VARCHAR(3) PRIMARY KEY,
            CurrencyName VARCHAR(100) NOT NULL,
            Symbol VARCHAR(10) NOT NULL
        )
    ''')

    # Create ExchangeRate table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ExchangeRate (
            RateID INTEGER PRIMARY KEY AUTOINCREMENT,
            FromCurrency VARCHAR(3) NOT NULL,
            ToCurrency VARCHAR(3) NOT NULL,
            Rate REAL NOT NULL,
            Date VARCHAR(20) NOT NULL,
            FOREIGN KEY (FromCurrency) REFERENCES Currency(CurrencyCode),
            FOREIGN KEY (ToCurrency) REFERENCES Currency(CurrencyCode)
        )
    ''')

    # Create ExchangeTransaction table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ExchangeTransaction (
            TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
            CustomerID INTEGER NOT NULL,
            FromCurrency VARCHAR(3) NOT NULL,
            ToCurrency VARCHAR(3) NOT NULL,
            Amount REAL NOT NULL,
            TransactionDate VARCHAR(20) NOT NULL,
            FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
            FOREIGN KEY (FromCurrency) REFERENCES Currency(CurrencyCode),
            FOREIGN KEY (ToCurrency) REFERENCES Currency(CurrencyCode)
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def execute_query(query, params=None):
    conn = sqlite3.connect('money_exchange.db')
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    rows = cursor.fetchall() if query.lstrip().upper().startswith('SELECT') else None
    conn.commit()
    conn.close()
    return rows

# 2. Implement functions to add, update, and retrieve data from the database.
def add_customer(name, email, phone_number):
    execute_query('''
        INSERT INTO Customer (Name, Email, PhoneNumber)
        VALUES (?, ?, ?)
    ''', (name, email, phone_number))

def add_currency(currency_code, currency_name, symbol):
    execute_query('''
        INSERT INTO Currency (CurrencyCode, CurrencyName, Symbol)
        VALUES (?, ?, ?)
    ''', (currency_code, currency_name, symbol))

def add_exchange_rate(from_currency, to_currency, rate, date):
    execute_query('''
        INSERT INTO ExchangeRate (FromCurrency, ToCurrency, Rate, Date)
        VALUES (?, ?, ?, ?)
    ''', (from_currency, to_currency, rate, date))

def add_transaction(customer_id, from_currency, to_currency, amount, transaction_date):
    execute_query('''
        INSERT INTO ExchangeTransaction (CustomerID, FromCurrency, ToCurrency, Amount, TransactionDate)
        VALUES (?, ?, ?, ?, ?)
    ''', (customer_id, from_currency, to_currency, amount, transaction_date))

def get_customers():
    return execute_query('SELECT * FROM Customer')

def get_currencies():
    return execute_query('SELECT * FROM Currency')

def get_exchange_rates():
    return execute_query('SELECT * FROM ExchangeRate')

def get_transactions():
    return execute_query('SELECT * FROM ExchangeTransaction') 



