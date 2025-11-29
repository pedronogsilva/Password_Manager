"""
This code consists of a password manager application that works through a Command Line Interface.
This project was started on 11/18 at 2:10 AM. It was being developed because I was simply saving my passwords in a .txt file.
It wasn't organized no matter how hard we tried. With this application, the organization will be much better.

Starting Date: 11/18/2025 - Finish Date: 11/27/2025
    Version 1.0.0 - Complete code restructuring
"""

import sqlite3; import os;

def initialize_db():
    conn = sqlite3.connect('passwords.db'); c = conn.cursor();
    c.execute('''CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, site TEXT NOT NULL, login TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL)''');
    conn.commit(); conn.close();

def add():
    conn = sqlite3.connect('passwords.db'); c = conn.cursor();
    clear(); print("------------------------------Adding Password------------------------------\n\n\tWhat is the app or website?");
    site = input("  ->").strip().capitalize();

    if not site:
        clear(); print("------------------------------Adding Password------------------------------\n\n\tSite/App empty! Press ENTER.");input(); conn.close(); return;

    clear(); print("------------------------------Adding Password------------------------------\n\n\t[1] Username/Email, Password\n\t[2] Fast Login");
    login = input("\n  ->").strip();

    if login == "1":
        clear(); print("------------------------------Adding Password------------------------------\n\n\tUsername/Email:");
        username = input("  ->").strip()

        if not username:
            clear(); print("------------------------------Adding Password------------------------------\n\n\tUser/Email empty! Press ENTER."); input(); conn.close(); return;
        
        print("\n\tPassword:"); password = input("  ->").strip();

        if not password:
            clear(); print("------------------------------Adding Password------------------------------\n\n\tPassword empty! Press ENTER."); input(); conn.close(); return;

        c.execute("INSERT INTO passwords (site, login, username, password) VALUES (?, ?, ?, ?)", (site, login, username, password));
        conn.commit(); print("\n\tPassword added! Please ENTER."); input(); conn.close();

    elif login == "2":
        clear(); print("------------------------------Adding Password------------------------------\n\n\tWhat's the quick login?");
        quick = input("  ->").strip().capitalize();
        c.execute("SELECT * FROM passwords WHERE site = ?", (quick,)); results = c.fetchall();

        if not results:
            clear(); print("------------------------------Adding Password------------------------------\n\n\tQuick login not found! Please ENTER."); input(); conn.close(); return;

        if len(results) > 1:
            clear(); print("------------------------------Adding Password------------------------------\n\n");
            for idx, row in enumerate(results, start=1):
                f_id, f_site, f_login, f_username, f_password = row;
                print(f"      [{idx}] Username/Email: {f_username}");
            choice = input("\n  ->").strip();

            try:
                choice_idx = int(choice) - 1;
                if choice_idx < 0 or choice_idx >= len(results):
                    clear(); print("------------------------------Adding Password------------------------------\n\n\tInvalid choice. Cancelling. Please ENTER."); input(); conn.close(); return;
                selected = results[choice_idx];

            except ValueError:
                clear(); print("------------------------------Adding Password------------------------------\n\n\tnvalid input. Cancelling."); input(); conn.close(); return;
        else:
            selected = results[0]; conn.close();

        found_id, found_site, found_login, found_username, found_password = selected

        c.execute("INSERT INTO passwords (site, login, username, password) VALUES (?, ?, ?, ?)", (site, login, found_username, found_password))
        conn.commit(); print("\n\tPassword added! Please ENTER."); input(); conn.close();

    else:
        clear(); print("------------------------------Adding Password------------------------------\n\n"); print("      Invalid Option! Please ENTER."); input();
    conn.close();    

def view():
    conn = sqlite3.connect('passwords.db'); c = conn.cursor();
    clear(); print("------------------------------View Passwords-------------------------------\n\n");
    c.execute("SELECT site, username, password FROM passwords ORDER BY id ASC");
    results = c.fetchall();

    if not results:
        clear(); print("------------------------------View Passwords-------------------------------\n\n\tNo passwords found!  Please ENTER."); input(); conn.close();

    clear(); print("------------------------------View Passwords-------------------------------\n\n");
    for site, username, password in results:
        print(f"\tSite: {site}, Username/Email: {username}, Password: {password}\n");
    input(); conn.close();

def edit():
    conn = sqlite3.connect('passwords.db'); c = conn.cursor();
    clear(); print("------------------------------Edit Password--------------------------------\n\n\tWhich website or app do you want to edit?");
    site = input("  ->").strip().capitalize();
    c.execute("SELECT * FROM passwords WHERE site = ?", (site,)); results = c.fetchall();

    if not results:
        clear(); print("------------------------------Edit Password--------------------------------\n\n\tSite or App not found! Please ENTER."); input(); conn.close(); return;
    
    clear(); print("------------------------------Edit Password--------------------------------\n\n");
    for idx, row in enumerate(results, start=1):
        f_id, f_site, f_login, f_username, f_password = row;
        print(f"\t[{idx}] Username/Email: {f_username}");
    choice = input("\n  ->").strip();

    try:
        choice_idx = int(choice) - 1
        if choice_idx < 0 or choice_idx >= len(results):
            clear(); print("------------------------------Edit Passwordv-----------------\n\n\tInvalid choice.  Please ENTER."); input(); conn.close(); return;
        selected = results[choice_idx];
    
    except ValueError:
        clear(); print("------------------------------Edit Password--------------------------------\n\n\tInvalid choice.  Please ENTER."); input(); conn.close(); return;
    
    found_id, found_site, found_login, found_username, found_password = selected;

    clear(); print("------------------------------Edit Password--------------------------------\n\n");
    print(f"\t[{choice}] Username/Email: {found_username}, Password: {found_password}\n");
    print("\tWhat do you want to edit?\n\n\t[1] Username/Email\n\t[2] Password"); edit_option = input("  ->").strip();
    
    if edit_option == "1":
        clear(); print("------------------------------Edit Password--------------------------------\n\n\tNew Username/Email:"); new_username = input("  ->").strip();
        c.execute("UPDATE passwords SET username = ? WHERE id = ?", (new_username, found_id)); conn.commit();
        print("\n\tUsername/Email updated! Please ENTER."); input();

    elif edit_option == "2":
        clear(); print("------------------------------Edit Password--------------------------------\n\n\tNew Password:"); new_password = input("  ->").strip();
        c.execute("UPDATE passwords SET password = ? WHERE id = ?", (new_password, found_id)); conn.commit();
        print("\n\tPassword updated! Please ENTER."); input();

    else:
        clear(); print("------------------------------Edit Password--------------------------------\n\n\tInvalid Option! Please ENTER."); input();
    conn.close();

def delete():
    conn = sqlite3.connect('passwords.db'); c = conn.cursor();
    clear(); print("------------------------------Delete Password------------------------------\n\n\tWhich site do you want to delete?");
    delete = input("  ->").strip().capitalize();
    c.execute("SELECT * FROM passwords WHERE site = ?", (delete,)); results = c.fetchall();

    if not results:
        clear(); print("---------------Delete Password---------------\n\n\tSite or App not found! Please ENTER."); input(); return;

    clear(); print("---------------Delete Password---------------\n\n");
    for idx, row in enumerate(results, start=1):
        f_id, f_site, f_login, f_username, f_password = row;
        print(f"\t[{idx}] Username/Email: {f_username}, Password: {f_password}");
    choice = input("\n  ->").strip();
    
    try:
        choice_idx = int(choice) - 1;
        if choice_idx < 0 or choice_idx >= len(results):
            clear(); print("------------------------------Delete Password------------------------------\n\n\tInvalid choice. Please ENTER."); input(); return;
        selected = results[choice_idx];
    
    except ValueError:
        clear(); print("------------------------------Delete Password------------------------------\n\n\tInvalid input. Please ENTER."); input(); return;

    # Unpack selected row
    f_id, f_site, f_login, f_username, f_password = selected;

    clear(); print(f"------------------------------Delete Password------------------------------\n\n\tSite/App: {f_site}, Username/Email: {f_username}, Password: {f_password}");
    print("\n\tAre you sure you want to delete this entry?\n\t[1] Yes\n\t[2] No"); confirm = input("\n  -> ").strip();

    if confirm == "1":
        c.execute("DELETE FROM passwords WHERE id = ?", (f_id,)); conn.commit(); conn.close();
        clear(); print("------------------------------Delete Password------------------------------\n\n\tEntry deleted! Please ENTER."); input(); return;
    else:
        clear(); print("------------------------------Delete Password------------------------------\n\n\tDelete cancelled. Please ENTER."); input(); return;
    
def exit(): clear(); print("Exiting App..."); os.sys.exit();

def clear(): os.system("cls");

while True:
    clear(); initialize_db();
    print("---------------PassWord Manager App ---------------\n\n\t[1] Add Password\n\t[2] View Passwords\n\t[3] Edit Password\n\t[4] Delete Password\n\t[5] Exit App");
    option = input("\n  ->");

    if option == "1": clear(); add();
    elif option == "2": clear(); view();
    elif option == "3": clear(); edit();
    elif option == "4": clear(); delete();
    elif option == "5": clear(); exit();
    else: clear(); print("---------------PassWord Manager App ---------------\n\n\tInvalid Option! Please ENTER."); input();