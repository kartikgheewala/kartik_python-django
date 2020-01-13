import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/registerationinfo/'
resp = requests.get(BASE_URL+ENDPOINT)
data = resp.json()
for user in data:
    print("Registration Id : ", user['Registration_ID'])
    print("First Name : ", user['FirstName'])
    print("Middel Name : ", user['MiddelName'])
    print("Last Name : ", user['LastName'])
    print("Age : ", user['Age'])
    print("Gender : ", user['Gender'])
    print("Mobile Number : ", user['MobileNo'])
    print("Qualification : ", user['Qualification'])
    print("Reason_For_Visite : ", user['Reason_For_Visite'])
    print()
