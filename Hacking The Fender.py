import csv
import json


compromised_users = []
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

with open('compromised_users.txt', 'w') as compromised_users_file:
  for user in compromised_users:
    compromised_users_file.write(user + '\n')

with open('boss_message.json','w') as boss_message:
  boss_message_dict = {}
  boss_message_dict['recipient'] = 'The Boss'
  boss_message_dict['message'] = 'Mission  Success'
  json.dump(boss_message_dict, boss_message)

with open('new_passwords.csv','w') as new_passwords_obj:
  slash_null_sig = """ _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)

#Test to see if new_passwords_obj has the slash null sig
"""
with open('new_passwords.csv', 'r') as new_passwords_obj:
    content = new_passwords_obj.read()
    print(content)
"""

# Task 19 copy the contents of the new passwords file into the old passwords file

with open('new_passwords.csv') as new_passwords_csv:
  content = new_passwords_csv.read()

with open('passwords.csv','w') as password_csv:
  password_csv.write(content)

# **Now because we overwrite the old file passwords.csv an error will occur from earlier topics :    compromised_users.append(password_row['Username'])KeyError: 'Username'





