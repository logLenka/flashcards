import sqlite3
import pandas as pd

# 1. load data file
# df = pd.read_csv('data.csv')
df = pd.read_csv(r'F:\OneDrive\Desktop\flashcards_app\data.csv')



# 2. data clean up
df.columns = df.columns.str.strip()

# 3. create / connect to SQLite database
connection = sqlite3.connect('db.sqlite3')

# 4. load data file to SQLite
df.to_sql('cards_card', connection, if_exists='replace')

# 5. close connection
connection.close()
print("hello!")

