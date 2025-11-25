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

def add():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()

    clear()
    print("---------------Adding Password---------------\n\n      What is the app or website?")
    site = input("  ->").strip().capitalize()

    clear()
    print("---------------Adding Password---------------\n\n      [1] Username / Password\n      [2] Fast Login")
    login = input("\n  ->").strip()

    # If the type of login is username/password ask the user for username and password 
    if login == "1":
        clear()
        print("---------------Adding Password---------------\n\n      Username/Email:")
        username = input("  ->").strip()
        print("\n      Password:")
        password = input("  ->").strip()
        c.execute("INSERT INTO passwords (site, login, username, password) VALUES (?, ?, ?, ?)", (site, login, username, password))
        conn.commit()

    # If the type of login is fast login, ask the user for the quick login name
    elif login == "2":
        clear()
        print("---------------Adding Password---------------\n\n      What's the quick login?")
        quick = input("  ->").strip().capitalize()
        c.execute("SELECT * FROM passwords WHERE site = ?", (quick,))
        results = c.fetchall()

        if not results:
            print("---------------Adding Password---------------\n\n")
            print("      Quick login not found in the database!")
            input()
            conn.close()
            return

        # If multiple results were found, ask the user which one they want
        if len(results) > 1:
            clear()
            print("---------------Adding Password---------------\n\n")
            for idx, row in enumerate(results, start=1):
                f_id, f_site, f_login, f_username, f_password = row
                print(f"      [{idx}] Username: {f_username}")
            choice = input("\n  ->").strip()

            #Show the user the options and get their choice
            try:
                choice_idx = int(choice) - 1
                if choice_idx < 0 or choice_idx >= len(results):
                    clear()
                    print("---------------Adding Password---------------\n\n")
                    print("      Invalid choice. Cancelling.")
                    input()
                    conn.close()
                    return
                selected = results[choice_idx]
            except ValueError:
                clear()
                print("---------------Adding Password---------------\n\n")
                print("      Invalid input. Cancelling.")
                input()
                conn.close()
                return
        else:
            selected = results[0]

        found_id, found_site, found_login, found_username, found_password = selected

        c.execute("INSERT INTO passwords (site, login, username, password) VALUES (?, ?, ?, ?)", (site, login, found_username, found_password))
        conn.commit()

    else:
        clear()
        print("---------------Adding Password---------------\n\n")
        print("      Invalid Option! Please try again.")
        input()

    conn.close()

def clear():
    os.system("cls")

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