import requests  
import json

page = requests.get (f"https://api.github.com/users/" + input("User: ") + "/repos")
Info = json.loads(page.content)
for value in Info:
    print(value)
