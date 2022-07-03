def view():
  db = {}
  
  with open('passwords.txt', 'r') as f:
    
    for line in f.readlines():
      pair = line.rstrip()
      
      app, pw = pair.split('|') # splits a string at any '|' operator and returns a list of strings
      db[app] = pw
      
  return db


def add(app: str, pw: str): # Consider using a database instead of a txt file you idiot XD
  with open('passwords.txt', 'a') as f:
    f.write(app + '|' + pw + '\n')


def remove(removal):
  with open('passwords.txt', 'r') as f:
    pairs = f.readlines()
  with open('passwords.txt', 'w') as f:
    for pair in pairs:
      app = pair.split('|')[0]
      if app != removal:
        f.write(pair)
      

def encrypt(): # ADD AN ENCRYPTION FEATURE
  pass