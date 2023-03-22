import sqlite3
import tkinter as tk

# Connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the users table if it doesn't already exist
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

# Create the main window
window = tk.Tk()
window.title("User Manager")

# Create a label and entry for the username
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Create a label and entry for the password
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create a label and entry for the email
email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

# Create a label and entry for the phone number
phone_label = tk.Label(window, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

# Create a button to add the user to the database
def add_user():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    c.execute("INSERT INTO users (username, password, email, phone) VALUES (?, ?, ?, ?)", (username, password, email, phone))
    conn.commit()

add_button = tk.Button(window, text="Add User", command=add_user)
add_button.pack()

# Create a button to delete a user from the database
def delete_user():
    username = username_entry.get()
    c.execute("DELETE FROM users WHERE username=?", (username,))
    conn.commit()

delete_button = tk.Button(window, text="Delete User", command=delete_user)
delete_button.pack()

# Run the main loop
window.mainloop()

# Close the connection to the database
conn.close()