"""This code consists of a password manager application that works through a Command Line Interface.
This project was started on 11/18 at 2:10 AM. It was being developed because I was simply saving my passwords in a .txt file.
It wasn't organized no matter how hard we tried. With this application, the organization will be much better."""

import sqlite3; import os;

def initialize_db():
    pasta = "./bin"; os.makedirs(pasta, exist_ok=True); db_path = os.path.join(pasta, "database.db");
    conn = sqlite3.connect(db_path); c = conn.cursor();
    c.execute('''CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, site TEXT NOT NULL, login TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL)''');
    conn.commit(); conn.close();

def add():
    pasta = "./bin"; db_path = os.path.join(pasta, "database.db"); conn = sqlite3.connect(db_path); c = conn.cursor();
    clear(); print("------------------------------Adding Password------------------------------\n\n\tWhat is the app or site?");
    site = input("  ->").strip().capitalize();

    if not site:
        clear(); input("------------------------------Adding Password------------------------------\n\n\t\tSite/App empty! Press ENTER."); conn.close(); return;

    clear(); print("------------------------------Adding Password------------------------------\n\n\t[1] User/Email, Password\n\t[2] Fast Login");
    login = input("\n  ->").strip();

    if login == "1":
        clear(); print("------------------------------Adding Password------------------------------\n\n\tUser/Email:");
        username = input("  ->").strip();

        if not username:
            clear(); input("------------------------------Adding Password------------------------------\n\n\t\tUser/Email empty! Press ENTER."); conn.close(); return;
        
        print("\n\tPassword:"); password = input("  ->").strip();

        if not password:
            clear(); input("------------------------------Adding Password------------------------------\n\n\t\tPassword empty! Press ENTER."); conn.close(); return;

        c.execute("INSERT INTO passwords (site, login, username, password) VALUES (?, ?, ?, ?)", (site, login, username, password));
        conn.commit(); input("\n\t\tPassword added! Please ENTER."); conn.close();

    elif login == "2":
        clear(); print("------------------------------Adding Password------------------------------\n\n\tWhat's the quick login?");
        quick = input("  ->").strip().capitalize();
        c.execute("SELECT * FROM passwords WHERE site = ?", (quick,)); results = c.fetchall();

        if not results:
            clear(); input("------------------------------Adding Password------------------------------\n\n\t\tQuick login not found! Please ENTER."); conn.close(); return;

        if len(results) > 1:
            clear(); print("------------------------------Adding Password------------------------------\n\n");
            for idx, row in enumerate(results, start=1):
                f_id, f_site, f_login, f_username, f_password = row;
                print(f"\t\t[{idx}] User/Email: {f_username}");
            choice = input("\n  ->").strip();

            try:
                choice_idx = int(choice) - 1;
                if choice_idx < 0 or choice_idx >= len(results):
                    clear(); input("------------------------------Adding Password------------------------------\n\n\t\tInvalid choice. Cancelling. Please ENTER."); conn.close(); return;
                else:
                    selected = results[choice_idx];

            except ValueError:
                clear(); input("------------------------------Adding Password------------------------------\n\n\t\tnvalid input. Cancelling. Please ENTER."); conn.close(); return;
        else:
            selected = results[0];

        found_id, found_site, found_login, found_username, found_password = selected

        c.execute("INSERT INTO passwords (site, login, username, password) VALUES (?, ?, ?, ?)", (site, login, found_username, found_password))
        conn.commit(); input("\n\t\tPassword added! Please ENTER."); conn.close();

    else:
        clear(); input("------------------------------Adding Password------------------------------\n\n\t\tInvalid Option! Please ENTER.");
    conn.close();

def view():
    pasta = "./bin"; db_path = os.path.join(pasta, "database.db"); conn = sqlite3.connect(db_path); c = conn.cursor();
    clear(); print("------------------------------View Passwords-------------------------------\n\n\t[1] All\n\t[2] Search");
    choice = input("\n\t->").strip(); c.execute("SELECT site, username, password FROM passwords ORDER BY site ASC"); results = c.fetchall();
    
    if not results:
        clear(); input("------------------------------View Passwords-------------------------------\n\n\t\tNo passwords found!  Please ENTER."); conn.close(); return;

    if choice == "1":
        clear(); print("------------------------------View Passwords-------------------------------\n\n");
        for site, username, password in results:
            print(f"\tSite: {site} | User/Email: {username} | Pass: {password}");
        input("\n\t\tPress ENTER to return menu."); conn.close();
    
    elif choice == "2":
        clear(); c.execute("SELECT DISTINCT site FROM passwords ORDER BY site ASC"); all_sites = [row[0] for row in c.fetchall()];
        page = 0; PAGE_SIZE = 5;
        while True:
            start = page * PAGE_SIZE; end = start + PAGE_SIZE; page_items = all_sites[start:end];

            clear(); print("------------------------------View Passwords-------------------------------\n\n");
            for i, site in enumerate(page_items, start=1): print(f"\t[{i}] Site: {site}");
            print("\t[6] Previous page\t[7] Next page\t[0] Back"); choice = input("\n\t-> ").strip();

            if choice == "0": conn.close(); return;
            elif choice == "6":
                if page > 0: page-=1;
                else: page = 0;
            elif choice == "7":
                if end >= len(all_sites): page = 0;
                else: page+= 1;
                continue;
            
            else:
                try:
                    idx = int(choice) - 1;
                    if idx < 0 or idx >= len(page_items):
                        clear(); input("------------------------------View Passwords-------------------------------\n\n\t\tInvalid Option! Please ENTER."); break;

                    selected_site = page_items[idx]; c.execute("SELECT * FROM passwords WHERE site = ?", (selected_site,)); results = c.fetchall();
                    clear(); print("------------------------------View Passwords-------------------------------\n\n");

                    for i, row in enumerate(results, start=1):
                        f_id, f_site, f_login, f_username, f_password = row; print(f"\tSite: {f_site} | User/Email: {f_username} | Pass: {f_password}");
                    input("\n\t\tPress ENTER to return menu."); break;

                except ValueError:
                    clear(); input("------------------------------View Passwords-------------------------------\n\n\t\tPress ENTER to return menu."); break;
    else:
        clear(); input("------------------------------View Passwords-------------------------------\n\n\t\tInvalid Option! Please ENTER.");
    conn.close();

def edit():
    pasta = "./bin"; db_path = os.path.join(pasta, "database.db"); conn = sqlite3.connect(db_path); c = conn.cursor();
    clear(); print("------------------------------Edit Password--------------------------------\n\n\tWhich site or app do you want to edit?");
    site = input("  ->").strip().capitalize(); c.execute("SELECT * FROM passwords WHERE site = ?", (site,)); results = c.fetchall();

    if not results:
        clear(); input("------------------------------Edit Password--------------------------------\n\n\t\tSite or App not found! Please ENTER."); conn.close(); return;
    
    clear(); print("------------------------------Edit Password--------------------------------\n\n");
    for idx, row in enumerate(results, start=1):
        f_id, f_site, f_login, f_username, f_password = row;
        print(f"\t[{idx}] User/Email: {f_username}");
    choice = input("\n  ->").strip();

    try:
        choice_idx = int(choice) - 1
        if choice_idx < 0 or choice_idx >= len(results):
            clear(); input("------------------------------Edit Passwordv-----------------\n\n\t\tInvalid choice.  Please ENTER."); conn.close(); return;
        selected = results[choice_idx];
    
    except ValueError:
        clear(); input("------------------------------Edit Password--------------------------------\n\n\t\tInvalid choice.  Please ENTER."); conn.close(); return;
    
    found_id, found_site, found_login, found_username, found_password = selected;

    clear(); print("------------------------------Edit Password--------------------------------\n\n");
    print(f"\t[{choice}] User/Email: {found_username}, Password: {found_password}\n");
    print("\tWhat do you want to edit?\n\n\t[1] User/Email\n\t[2] Password"); edit_option = input("  ->").strip();
    
    if edit_option == "1":
        clear(); print("------------------------------Edit Password--------------------------------\n\n\tNew User/Email:"); new_username = input("  ->").strip();
        c.execute("UPDATE passwords SET username = ? WHERE id = ?", (new_username, found_id)); conn.commit();
        input("\n\t\tUser/Email updated! Please ENTER.");

    elif edit_option == "2":
        clear(); print("------------------------------Edit Password--------------------------------\n\n\tNew Password:"); new_password = input("  ->").strip();
        c.execute("UPDATE passwords SET password = ? WHERE id = ?", (new_password, found_id)); conn.commit();
        input("\n\t\tPassword updated! Please ENTER.");

    else:
        clear(); input("------------------------------Edit Password--------------------------------\n\n\t\tInvalid Option! Please ENTER.");
    conn.close();

def delete():
    pasta = "./bin"; db_path = os.path.join(pasta, "database.db"); conn = sqlite3.connect(db_path); c = conn.cursor();
    clear(); print("------------------------------Delete Password------------------------------\n\n\tWhich site or app do you want to delete?");
    delete = input("  ->").strip().capitalize();
    c.execute("SELECT * FROM passwords WHERE site = ?", (delete,)); results = c.fetchall();

    if not results:
        clear(); input("---------------Delete Password---------------\n\n\t\tSite or App not found! Please ENTER."); return;

    clear(); print("---------------Delete Password---------------\n\n");
    for idx, row in enumerate(results, start=1):
        f_id, f_site, f_login, f_username, f_password = row;
        print(f"\t[{idx}] User/Email: {f_username}, Password: {f_password}");
    choice = input("\n  ->").strip();
    
    try:
        choice_idx = int(choice) - 1;
        if choice_idx < 0 or choice_idx >= len(results):
            clear(); input("------------------------------Delete Password------------------------------\n\n\t\tInvalid choice. Please ENTER."); return;
        selected = results[choice_idx];
    
    except ValueError:
        clear(); input("------------------------------Delete Password------------------------------\n\n\t\tInvalid input. Please ENTER."); return;

    # Unpack selected row
    f_id, f_site, f_login, f_username, f_password = selected;

    clear(); print(f"------------------------------Delete Password------------------------------\n\n\tSite/App: {f_site}, User/Email: {f_username}, Password: {f_password}");
    print("\n\tAre you sure you want to delete this entry?\n\t[1] Yes\n\t[2] No"); confirm = input("\n  -> ").strip();

    if confirm == "1":
        c.execute("DELETE FROM passwords WHERE id = ?", (f_id,)); conn.commit(); conn.close();
        clear(); input("------------------------------Delete Password------------------------------\n\n\t\tEntry deleted! Please ENTER."); return;
    else:
        clear(); input("------------------------------Delete Password------------------------------\n\n\t\tDelete cancelled. Please ENTER."); return;

def verify():
    pasta = "./bin"; db_path = os.path.join(pasta, "database.db"); conn = sqlite3.connect(db_path); c = conn.cursor();
    clear(); print("------------------------------Delete Password------------------------------");

def exit(): clear(); print("Exiting App..."); os.sys.exit();

def clear(): os.system("cls");

while True:
    clear(); initialize_db();
    option = input("------------------------------PassWord Manager App------------------------------\n\n\t[1] Add Password\n\t[2] View Passwords\n\t[3] Edit Password\n\t[4] Delete Password\n\t[5] Verify Passwords\n\t[0] Exit App\n\t->");

    if option == "1": clear(); add();
    elif option == "2": clear(); view();
    elif option == "3": clear(); edit();
    elif option == "4": clear(); delete();
    elif option == "5": clear; verify();
    elif option == "0": clear(); exit();
    else: clear(); print("------------------------------PassWord Manager App------------------------------\n\n\t\tInvalid Option! Please ENTER."); input();