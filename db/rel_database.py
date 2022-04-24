import sqlite3

connect = sqlite3.connect('database.sqlite')

cursor = connect.cursor()

# cursor.execute("""
#     CREATE table bots (id integer primary key, name text, username text, id_platform integer);
# """)

# cursor.execute("""
#     CREATE table bots_platform (
#         id integer primary key,
#         platform text
#     );""")

# cursor.execute("""
#     CREATE table bots_functions (
#         id integer primary key,
#         functions text
#     );""")

# cursor.execute("insert into bots values(1, 'MeteoBot', '@Meteo21Bot', 1)")
# cursor.execute("insert into bots values(2, 'GlobalKeeperBot', '@GlobalKeeperBot', 1)")
# cursor.execute("insert into bots values(3, 'GlobalNoteBot', '@GlobalNoteBot', 1)")
# cursor.execute("insert into bots values(4, 'WPTestGroup', 'https://vk.com/public211069718', 2)")
# cursor.execute("insert into bots values(5, 'BreadyBot', 'https://vk.com/happy_pilot', 2)")

# cursor.execute("insert into bots_platform values(1, 'Telegram')")
# cursor.execute("insert into bots_platform values(2, 'VK')")

# cursor.execute("insert into bots_functions values(1, 'Вывод погоды в любом городе, просмотр закатов и рассветов и т.д.')")
# cursor.execute("insert into bots_functions values(2, 'Просмотр курсов валют, компаний, банков и т.д по названию/ИНН')")
# cursor.execute("insert into bots_functions values(3, 'Создание напоминаний и заметок')")
# cursor.execute("insert into bots_functions values(4, '-')")
# cursor.execute("insert into bots_functions values(5, 'Оформление заказов в дизайнерской студии через бота')")

# cursor.execute("""
#     SELECT models.model, cars.color, owners.owner, owners.driver_card
#     FROM cars, owners, models
#     WHERE cars.id_owner=owners.id and cars.id_model=models.id
# """)
# print(cursor.fetchall())

# cursor.execute("""
#     SELECT models.model, cars.color, owners.owner, owners.driver_card
#     FROM cars, owners, models
#     WHERE cars.id_owner=owners.id and cars.id_model=models.id and models.mark="Chevrolet"
# """)
# print(cursor.fetchall())

for i in range(1, 3):
    cursor.execute(f"DELETE FROM users WHERE id = {i}")

connect.commit()