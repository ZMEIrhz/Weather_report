import sqlite3

db = sqlite3.connect("database.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS "users" (
 "username" TEXT,
 "password" TEXT)""")
db.commit()


def reg():
    username = input("username>> ")
    password = input("password>> ")
    sql.execute(f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?)", (username, password))
        db.commit()
        print('You have registered')
        login()
    else:
        print('Такая запись уже существует')
        for i in sql.execute('SELECT * FROM users'):
            print(i)

def login(username = '', password = '') -> bool:
    if __name__ == '__main__':
        username = input("username>> ")
        password = input("password>> ")

    a = sql.execute(f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'")
    db.commit()
    if not sql.fetchone():
        if __name__ == '__main__':
            print("Нет такой записи")
            for i in sql.execute('SELECT * FROM users'):
                print(i)
            reg()
        return False
    else:
        if __name__ == '__main__':
            print('Welcome')
        return True


if __name__ == '__main__':
    if input('reg or log>>>') == 'reg':
        reg()
    else:
        login()