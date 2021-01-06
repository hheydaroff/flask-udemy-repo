import sqlite3

connection = sqlite3.connect('data.db')


cursor = connection.cursor() #cursor does do execute the queries we send to sqldb.

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')

insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)


users = [v
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')
]
cursor.executemany(insert_query, users)


select_query = "SELECT * from users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()