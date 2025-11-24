"""
This code consists of a password manager application that works through a Command Line Interface.
This project was started on 11/18 at 2:10 AM. It was being developed because I was simply saving my passwords in a .txt file.
It wasn't organized no matter how hard we tried. With this application, the organization will be much better.

Starting Date: 11/18/2025 - Finish Date: "ongoing"

Version 0.0.0 -> 11/18/2025
Version 0.0.1 -> 11/22/2025 -> XX/XX/202X (Visual)
Version 0.0.0 -> XX/XX/202X -> XX/XX/202X
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
            id INTEGER PRIMARY KEY,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def clear():
    os.system("cls")







clear()
print("---------------PassWord Manager App ---------------\n\n      [1] Add Password\n      [2] View Passwords\n      [3] Edit Password\n      [4] Delete Password\n      [5] Exit App")
Option = int(input("\n  ->"))
print(Option)

if Option == 1:
    clear()
    print("1")
elif Option == 2:
    clear()
    print("2")
elif Option == 3:
    clear()
    print("3")
elif Option == 4:
    clear()
    print("4")
elif Option == 5:
    clear()
    print("5")
else:
    print("Invaid Input")