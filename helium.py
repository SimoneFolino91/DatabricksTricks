import helium
import time
import json


with open('C:\\Users\\Utente\\Desktop\\Data Engineering\\Community\\config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
    f.close()

###
Documentation at https://selenium-python-helium.readthedocs.io/en/latest/api.html
###


helium.start_firefox()
helium.go_to('https://outlook.live.com')
helium.click('Accedi')
helium.write(config['username'], into='E-mail, telefono o Skype')
helium.click('Avanti')
helium.write(config['password'].capitalize(), into = 'Password')
helium.click('Accedi')
helium.wait_until(condition_fn=helium.Button('No').exists)
helium.click('No')
helium.wait_until(condition_fn=helium.Button('New message').exists, timeout_secs=20)
helium.click('New message')
helium.wait_until(condition_fn=helium.Button('To').exists, timeout_secs=20)
helium.write('example@example.com', into=helium.TextField(to_right_of='To'))
body = helium.find_all(helium.TextField(below=helium.TextField('Add a subject')))
helium.write('Message Automation', into= 'Add a subject')
helium.write('Follow my github for more code =) ', into = body[0])
