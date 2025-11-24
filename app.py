"""
This code consists of a password manager application that works through a Command Line Interface.
This project was started on 11/18 at 2:10 AM. It was being developed because I was simply saving my passwords in a .txt file.
It wasn't organized no matter how hard we tried. With this application, the organization will be much better.

Starting Date: 11/18/2025 - Finish Date: "ongoing"

Version 0.0.0 -> 11/18/2025
Version 0.0.1 -> 11/22/2025 -> 11/24/2025
    Semi-Visual
Version 0.1.2 -> 11/24/2025 -> XX/XX/202X
    Visual, Lingual Nova, Criação DB, Adicionar
Version 0.0.0 -> XX/XX/202X -> XX/XX/202X
Version 0.0.0 -> XX/XX/202X -> XX/XX/202X
"""

import sqlite3
import os

def initialize_db():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site TEXT NOT NULL,
            login TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def clear():
    os.system("cls")


def add():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()

    clear()
    print("---------------Adding Password---------------\n\n      What is the app or website?")
    site = input("  ->").strip().capitalize()

    clear()
    print("---------------Adding Password---------------\n\n      [1] Username / Password\n      [2] Fast Login")
    login = input("\n  ->").strip()

    if login == "1":
        clear()
        print("---------------Adding Password---------------\n\n      Username/Email:")
        username = input("  ->").strip()
        print("\n      Password:")
        password = input("  ->").strip()
        c.execute("INSERT INTO passwords (site, login, username, password) VALUES (?, ?, ?, ?)", (site, login, username, password))
        conn.commit()

    elif login == "2":
        clear()
        print("---------------Adding Password---------------\n\n      What's the quick login?")
        quick = input("  ->").strip().capitalize()
        c.execute("SELECT * FROM passwords WHERE site = ?", (quick,))
        result = c.fetchall()

        print("---------------Adding Password---------------\n\n")


        found_id, found_site, found_login, found_username, found_password = result

        c.execute("INSERT INTO passwords (site, login, username, password) VALUES (?, ?, ?, ?)", (site, login, found_username, found_password))
        conn.commit()


        """if result is None:
            print("\nQuick login not found in the database!")
            return
        """

        


    else:
        print("Invalid Option! Please try again.")
    






while True:

    clear()
    initialize_db()
    print("---------------PassWord Manager App ---------------\n\n      [1] Add Password\n      [2] View Passwords\n      [3] Edit Password\n      [4] Delete Password\n      [5] Exit App")
    option = int(input("\n  ->"))
    print(option)

    if option == 1:
        clear()
        add()
    elif option == 2:
        clear()
        print("2")
    elif option == 3:
        clear()
        print("3")
    elif option == 4:
        clear()
        print("4")
    elif option == 5:
        clear()
        print("5")
    else:
        clear()
        print("Invalid Option! Please try again.")