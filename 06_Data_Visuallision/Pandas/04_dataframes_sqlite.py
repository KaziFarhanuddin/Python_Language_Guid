import sqlite3

con = sqlite3.connect("database.db")

df = pd.read_sql_query("SELECT * FROM purchases", con)

print(df)
df.plot(kind='scatter', x='rating', y='revenue_millions', title='Revenue (millions)  vs Rating')
