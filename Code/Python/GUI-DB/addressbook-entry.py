import sqlite3
conn = sqlite3.connect('/home/vimal/Projects/pycode-browser/Code/Python/GUI-DB/addressbook.db')
cur = conn.cursor()
while 1:
  name = raw_input("Name : ")
  if name == "" :
    break
  email = raw_input("Email : ")
  phone = raw_input("Phone : ")
  
  cur.execute('INSERT INTO Addressbook (Name, Email, Phone) VALUES ( ?, ?, ? )', ( name, email, phone ) )

conn.commit()
cur.close()


