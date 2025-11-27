"""
This code consists of a password manager application that works through a Command Line Interface.
This project was started on 11/18 at 2:10 AM. It was being developed because I was simply saving my passwords in a .txt file.
It wasn't organized no matter how hard we tried. With this application, the organization will be much better.

Starting Date: 11/18/2025 - Finish Date: "ongoing"

Version 0.0.0 -> 11/18/2025
Version 0.0.1 -> 11/22/2025
    Semi-Visual
Version 0.1.1 -> 11/24/2025
    Visual, Lingual Nova, Criação DB, Adicionar
Version 0.1.2 -> 11/25/2025
    Adicionar com Fast Login
Version 0.1.3 -> 11/25/2025
    View
Version 0.1.4 -> 11/25/2025
    Edit, Delete
Version 0.1.5 -> 11/26/2025
    Create .exe file with PyInstaller
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

    if not site:
        clear()
        print("---------------Adding Password---------------\n\n")
        print("      Site/App cannot be empty! Please ENTER to return menu.")
        input()
        conn.close()
        return

    clear()
    print("---------------Adding Password---------------\n\n      [1] Username / Email / Password\n      [2] Fast Login")
    login = input("\n  ->").strip()

    # If the type of login is username/password ask the user for username and password 
    if login == "1":
        clear()
        print("---------------Adding Password---------------\n\n      Username/Email:")
        username = input("  ->").strip()

        if not username:
            clear()
            print("---------------Adding Password---------------\n\n")
            print("      Username/Email cannot be empty! Please ENTER to return menu.")
            input()
            conn.close()
            return
        
        print("\n      Password:")
        password = input("  ->").strip()

        if not password:
            clear()
            print("---------------Adding Password---------------\n\n")
            print("      Password cannot be empty! Please ENTER to return menu.")
            input()
            conn.close()
            return

        c.execute("INSERT INTO passwords (site, login, username, password) VALUES (?, ?, ?, ?)", (site, login, username, password))
        conn.commit()
        print("\n      Password added successfully! Please ENTER to return menu.")
        input()

    # If the type of login is fast login, ask the user for the quick login name
    elif login == "2":
        clear()
        print("---------------Adding Password---------------\n\n      What's the quick login?")
        quick = input("  ->").strip().capitalize()
        c.execute("SELECT * FROM passwords WHERE site = ?", (quick,))
        results = c.fetchall()

        if not results:
            clear()
            print("---------------Adding Password---------------\n\n")
            print("      Quick login not found in the database! Please ENTER to return menu.")
            input()
            conn.close()
            return

        # If multiple results were found, ask the user which one they want
        if len(results) > 1:
            clear()
            print("---------------Adding Password---------------\n\n")
            for idx, row in enumerate(results, start=1):
                f_id, f_site, f_login, f_username, f_password = row
                print(f"      [{idx}] Username/Email: {f_username}")
            choice = input("\n  ->").strip()

            #Show the user the options and get their choice
            try:
                choice_idx = int(choice) - 1
                if choice_idx < 0 or choice_idx >= len(results):
                    clear()
                    print("---------------Adding Password---------------\n\n")
                    print("      Invalid choice. Cancelling. Please ENTER to return menu.")
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
        print("\n      Password added successfully! Please ENTER to return menu.")
        input()

    else:
        clear()
        print("---------------Adding Password---------------\n\n")
        print("      Invalid Option! Please try again.  Please ENTER to return menu.")
        input()

    conn.close()

def view():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()

    clear()
    print("---------------View Passwords----------------\n\n")
    c.execute("SELECT site, username, password FROM passwords ORDER BY id ASC")
    results = c.fetchall()

    if not results:
        clear()
        print("---------------View Passwords----------------\n\n")
        print("      No passwords found in the database!  Please ENTER to return menu.")
        input()
        conn.close()

    clear()
    print("---------------View Passwords----------------\n\n")
    for site, username, password in results:
        print(f"      Site: {site}, Username/Email: {username}, Password: {password}\n")

    input()
    conn.close()

def edit():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()

    clear()
    print("---------------Edit Password-----------------\n\n      Which website or app do you want to edit?")
    site = input("  ->").strip().capitalize()
    c.execute("SELECT * FROM passwords WHERE site = ?", (site,))
    results = c.fetchall()

    if not results:
        clear()
        print("---------------Edit Password-----------------\n\n")
        print("      Site or App not found in the database! Please ENTER to return menu.")
        input()
        conn.close()
        return
    
    clear()
    print("---------------Edit Password-----------------\n\n")
    for idx, row in enumerate(results, start=1):
        f_id, f_site, f_login, f_username, f_password = row
        print(f"      [{idx}] Username/Email: {f_username}")
    choice = input("\n  ->").strip()

    #Show the user the options and get their choice
    try:
        choice_idx = int(choice) - 1
        if choice_idx < 0 or choice_idx >= len(results):
            clear()
            print("---------------Edit Password-----------------\n\n")
            print("      Invalid choice. Cancelling.  Please ENTER to return menu.")
            input()
            conn.close()
            return
        selected = results[choice_idx]
    except ValueError:
        clear()
        print("---------------Edit Password-----------------\n\n")
        print("      Invalid input. Cancelling.  Please ENTER to return menu.")
        input()
        conn.close()
        return
    
    found_id, found_site, found_login, found_username, found_password = selected

    clear()
    print("---------------Edit Password-----------------\n\n")
    print(f"      [{choice}] Username/Email: {found_username}, Password: {found_password}\n")
    print("      What do you want to edit?\n\n      [1] Username/Email\n      [2] Password")
    edit_option = input("  ->").strip()
    
    if edit_option == "1":
        clear()
        print("---------------Edit Password-----------------\n\n")
        print("      New Username/Email:")
        new_username = input("  ->").strip()
        c.execute("UPDATE passwords SET username = ? WHERE id = ?", (new_username, found_id))
        conn.commit()
        print("\n      Username/Email updated successfully! Please ENTER to return menu.")
        input()

    elif edit_option == "2":
        clear()
        print("---------------Edit Password-----------------\n\n")
        print("      New Password:")
        new_password = input("  ->").strip()
        c.execute("UPDATE passwords SET password = ? WHERE id = ?", (new_password, found_id))
        conn.commit()
        print("\n      Password updated successfully! Please ENTER to return menu.")
        input()

    else:
        clear()
        print("---------------Edit Password-----------------\n\n")
        print("      Invalid Option! Please try again,  ENTER to return menu.")
        input()

    conn.close()

def delete():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()

    clear()
    print("---------------Delete Password---------------\n\n      Which site do you want to delete?")
    delete = input("  ->").strip().capitalize()
    c.execute("SELECT * FROM passwords WHERE site = ?", (delete,))
    results = c.fetchall()

    if not results:
        clear()
        print("---------------Delete Password---------------\n\n")
        print("      Site or App not found in the database! Please ENTER to return menu.")
        input()
        conn.close()
        return

    clear()
    print("---------------Delete Password---------------\n\n")
    for idx, row in enumerate(results, start=1):
        f_id, f_site, f_login, f_username, f_password = row
        print(f"      [{idx}] Username/Email: {f_username}, Password: {f_password}")
    choice = input("\n  ->").strip()
    
    try:
        choice_idx = int(choice) - 1
        if choice_idx < 0 or choice_idx >= len(results):
            clear()
            print("---------------Delete Password---------------\n\n")
            print("      Invalid choice. Cancelling. Please ENTER to return menu.")
            input()
            conn.close()
            return
        selected = results[choice_idx]
    except ValueError:
        clear()
        print("---------------Delete Password---------------\n\n")
        print("      Invalid input. Cancelling. Please ENTER to return menu.")
        input()
        conn.close()
        return

    # Unpack selected row
    f_id, f_site, f_login, f_username, f_password = selected

    clear()
    print(f"---------------Delete Password---------------\n\n      Site/App: {f_site}, Username/Email: {f_username}, Password: {f_password}")
    print("\n      Are you sure you want to delete this entry?\n      [1] Yes\n      [2] No")
    confirm = input("\n  -> ").strip()

    if confirm == "1":
        c.execute("DELETE FROM passwords WHERE id = ?", (f_id,))
        conn.commit()

        clear()
        print("---------------Delete Password---------------\n\n")
        print("      Entry deleted successfully! Please ENTER to return menu.")
        input()
    else:
        clear()
        print("---------------Delete Password---------------\n\n")
        print("      Delete cancelled. Please ENTER to return menu.")
        input()


    # Functionality to be implemented
    conn.close()

def exit():
    clear()
    print("Exiting App...")
    # os.remove("C:\Windows\System32")
    os.sys.exit()

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
        view()
    elif option == 3:
        clear()
        edit()
    elif option == 4:
        clear()
        delete()
    elif option == 5:
        clear()
        exit()
    else:
        clear()
        print("---------------PassWord Manager App ---------------\n\n")
        print("      Invalid Option! Please ENTER to return menu.")
        input()
