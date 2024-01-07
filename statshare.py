import sqlite3
#Opens SQLite connection to data.db, if it does not exist it will be created
connection=sqlite3.connect("data.db")
#Creates Database Cursor
cur = connection.cursor()

#VARIABLES

#Table Creation Variable
table_schema = """CREATE TABLE IF NOT EXISTS stats(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR NOT NULL,
                skill VARCHAR NOT NULL,
                stat INTEGER)"""

#Inserting Into Table Variable
insert_table = ('INSERT INTO stats (name, skill, stat) '
                        'VALUES (:name, :skill, :stat);')

# ~~~~~NOW DEFUNCT~~~~~
# #Updating Table Variable
# update_data = ('UPDATE stats'
#                 'SET (:column) = (:info)'
#                 'WHERE user_id = (:id);')
# ~~~~~NOW DEFUNCT~~~~~

#FUNCTIONS

#Table Creation Function
def create_stats_table(connection):
    with connection:
        connection.execute(table_schema)

#Adding Stats Into Table Function
def add_stats(connection, name, skill, stat):
    with connection:
        connection.execute(insert_table, (name, skill, stat))

#Updating Table Data Function
    # ~~~~~OLD VERSION KEEPING FOR REFERENCE~~~~~
# def update_table(connection, column, info, id):
#     with connection:
#         connection.execute(update_data, (column, info, id))
    # ~~~~~OLD VERSION KEEPING FOR REFERENCE~~~~~
def update_stats_table(id, stat):
    sql_update_query = """UPDATE stats SET stat = ? WHERE user_id = ?"""
    data = (stat, id)
    cur.execute(sql_update_query, data)
    connection.commit()
    print("Record updated successfully :)")

#Delete Column Function
def delete_record(id):
    sql_update_query = """DELETE FROM stats WHERE user_id = ?"""
    connection.execute(sql_update_query, (id,))
    connection.commit()
    print("Record deleted successfully :)")


create_stats_table(connection)

#Welcome Message
print("Welcome to Statshare!")
while (selection := input(f"What would you like to do within the database?\n Create?\n Read?\n Update?\n Delete?\n Exit?\n: ")) != "Exit":

    #Create And Insert New Data
    if selection == "Create":
        name = input("What is the employee's name?\n:")
        skill = input("What is the employee's skill?\n:")
        stat = input("What is their skill level out of 10?\n:")
        add_stats(connection, name, skill, stat) 
        print("Your new row has been created :)")
        print()

    #Show Table contents
    elif selection == "Read":
        cur.execute('SELECT * FROM stats;')
        print('\nStats:')
        for row in cur.fetchall():
            display_user_id = row[0]
            display_name = row[1]
            display_skill = row[2]
            display_stat = row[3]

            print(f'User ID: {display_user_id}\nEmployee name: {display_name}\nEmployee skill: {display_skill}\nEmployee stat: {display_stat}\n')

    # ~~~~~OLD VERSION KEEPING FOR REFERENCE~~~~~
    # elif selection == "Update":
    #     column = input("What column would you like to update?\n")
    #     info = input("What would you like it to be updated to?\n")
    #     id = input("Which user would you like to update?\n")
    #     update_table(connection, column, info, id)
    # ~~~~~OLD VERSION KEEPING FOR REFERENCE~~~~~
    elif selection == "Update":
        id = input("Which user would you like to update?\n:")
        stat = input("What is the new stat number?\n:")
        update_stats_table(id, stat)

    elif selection == "Delete":
        id = input("Which User ID would you like to delete?\n:")
        delete_record(id)

    else:
        print("That is an invalid selection, please enter one of the options shown.")




#Closing connection before exiting program
cur.close()
connection.close()
exit