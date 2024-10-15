import sqlite3
db_name = '< / >'
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

table_name = """
CREATE TABLE xyz(x VARCHAR(35), y VARCHAR(10));
"""

# Make table and insert some data
cursor.execute(table_info)
# cursor.execute(''' INSERT INTO xyz VALUES('x','y')''')
# cursor.execute(''' INSERT INTO xyz VALUES('x','y')''')



# Ensure this line is included after insertions
connection.commit()  


# data = cursor.execute('''SELECT * FROM xyz''')
# for row in data:
    # print(row)

connection.close()