# Hacking-The-Fender
Solution of Hacking The Fender (CodeAcademy -> Projects)

#
The Fender, a notorious computer hacker and public enemy, has gained access to several highly confidential passwords, including yours. Your mission involves three critical tasks. First, you need to penetrate The Fender's systems. Next, you must modify his "passwords.txt" file to encrypt the sensitive information. Finally, you need to append the signature of Slash Null, another hacker whose malicious activities could be prevented by The Fender if he perceives Slash Null as a rival.

Utilize your expertise in Python file handling to extract, modify, obscure, and generate data as you embark on this mission for justice. Engage with CSV files and other text formats in this demonstration of Python's powerful file manipulation capabilities.
#
Task 1
We've established a secure link to The Firewall’s hidden server. You need to write a script to read the compromised 'usernames' and 'passwords' stored in a file named "credentials.csv".

First, import the CSV module for parsing the data:
import.csv
#
Task 2
Create a list to store the usernames of compromised accounts and assign it to 'compromised_users':
compromised_users = []
#
Task 3
Open the "credentials.csv" file and assign the file object to 'credentials_file':
with open('credentials.csv', 'r') as credentials_file:
#
Task 4
Pass credentials_file to csv.DictReader and save the result as 'credentials_csv':
 credentials_csv = csv.DictReader(credentials_file)
#
Task 5
Iterate over each row in 'credentials_csv':
for credential_row in credentials_csv:
#
Task 6
Print the 'Username' field from each row to verify the data:
 print(credential_row['Username'])
#
Task 7
Replace the print statement with an append operation to add each username to 'compromised_users':
compromised_users.append(credential_row['Username'])
#
Task 8
Exit the with block. We have all the necessary data. Now, open a new file "compromised_users.txt" in write mode:
with open('compromised_users.txt', 'w') as compromised_users_file:
#
Task 9
Within this new context, iterate over each username in 'compromised_users':
for compromised_user in compromised_users:
#
Task 10
Write each compromised_user to 'compromised_users_file':
compromised_users_file.write(compromised_user + '\n')
#
Task 11
Exit the with block. You've successfully gathered and documented the compromised data.

Informing Command
Task 12
Your superior needs confirmation of your success. Encode a message using JSON. First, import the json module:
import json
#
Task 13
Open a new JSON file named "command_message.json" in write mode:
with open('command_message.json', 'w') as command_message_file:
#
Task 14
Create a dictionary with the message details and assign it to 'command_message_dict':
    command_message_dict = {
        "recipient": "Commander",
        "message": "Operation Successful"
    }
#
Task 15
Serialize 'command_message_dict' to 'command_message_file' using json.dump():
  json.dump(command_message_dict, command_message_file)
#
Encrypting the Secrets
Task 16
Having retrieved the compromised data, it’s time to replace the "credentials.csv" file. Open "new_secrets.csv" in write mode:
with open('new_secrets.csv', 'w') as new_secrets_file:
#
Task 17
We want The Firewall to believe that Phantom Ghost is behind this operation. Phantom Ghost leaves a signature in the files he modifies. Define this signature:
phantom_ghost_sig = 
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
#
Task 18
Write phantom_ghost_sig to 'new_secrets_file':
  new_secrets_file.write(phantom_ghost_sig)

 
