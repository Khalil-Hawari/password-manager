import os
clear = lambda: os.system("clear")

import edits

master_pw = input('What is the master password?\nEnter:  ')
clear()

mpw_check = input('Enter the master password:  ')
clear()

while mpw_check != master_pw: 
  mpw_check = input('Wrong entry, please retry\nEnter:  ')
  clear()


app_list = []

while True:
  
  mode = input('Which mode would you like to use?\nEnter:  ').lower()
  clear()
  
  while not (mode in ['quit', 'view', 'edit']): 
    mode = input('Wrong entry, please retry\nEnter:  ').lower()
    clear()

  
  if mode == 'quit':
    break

  
  elif mode == 'view': # Press enter to continue feature
    mpw_check = input('Enter the master password to view your passwords:  ')
    clear()
    
    if mpw_check == master_pw:
      try:
        count = 0
        for i in edits.view():
          count += 1
          print('(' + str(count) + ') APPLICATION:  ', i, '\n(' + str(count) + ') PASSWORD:  ', edits.view()[i], '\n')
        
        if count == 0:
          print('You have nothing to view! Save passwords with Edit Mode\n')
        continue_msg = input('Press Enter to continue  ')
        
      except:
        print('You have nothing to view! Save passwords with Edit Mode\n')
        
      continue_msg = input('Press Enter to continue  ')
      clear()

    else:
      continue_msg = input('Wrong password! Press Enter to go back to menu  ')

  
  elif mode == 'edit': # Add changing mpw
    edit_mode = input('What kind of change would you like to make?\nEnter:  ').lower()
    
    while not (edit_mode in ['add', 'remove']):
      edit_mode = input('Wrong entry, please retry\nEnter:  ')
      clear()

      
    if edit_mode == 'add': # Does not address duplicate app entries, does not ask for mpw
      new_app = input('What is the name of the application?\nEnter:  ')
      new_pw = input('What is the password?\nEnter:  ') 
      edits.add(new_app, new_pw)
      app_list.append(new_app)
      
      new_app, new_pw = [None, None]
      clear()
      
        
    elif edit_mode == 'remove': # Add mpw check
      removal = input('Which application would you like to remove?\nEnter:  ')
      while not (removal in app_list):
        removal = input('No app ' + '\"' + str(removal) + '\"' + ' please retry\nEnter:  ')

      for app in app_list:
        if app == removal:
          app_list.remove(app)

      edits.remove(removal)
      clear()

      
# Msg shows that the loop has broken
print('Program_ended, go touch grass')

try:
  os.remove('passwords.txt')
except:
  pass