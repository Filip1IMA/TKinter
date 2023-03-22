import sqlite3
import tkinter as tk

# Koble til databasen
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Lag en tabell for brukere
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL
    )
''')
conn.commit()

# Lag hoved vinduet
window = tk.Tk()
window.title("User Manager")

# Lag en label og en entry for brukernavn
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Lag en label og en entry for passord
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Lag en label og en entry for epost
email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

# Lag en label og en entry for telefonnummer
phone_label = tk.Label(window, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

# Lag en knapp for å legge til bruker i databasen
def add_user():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    c.execute("INSERT INTO users (username, password, email, phone) VALUES (?, ?, ?, ?)", (username, password, email, phone))
    conn.commit()

add_button = tk.Button(window, text="Add User", command=add_user)
add_button.pack()

# lag en knapp for å slette bruker fra databasen
def delete_user():
    username = username_entry.get()
    c.execute("DELETE FROM users WHERE username=?", (username,))
    conn.commit()

delete_button = tk.Button(window, text="Delete User", command=delete_user)
delete_button.pack()


window.mainloop()

conn.close()