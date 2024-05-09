import requests
import json
import random


def make_post_request(url):
    random_number = random.randint(1, 50)
    # Specify headers with Content-Type as application/json
    
    headers = {'Content-Type': 'application/json',
               'Secret': 'a64007894fe677faac92ab28bbfafbbb2d2b12d68f5a2c617ec1fdbbd814a16e',
               'Tg-Id':'1739007386'
               }
    postData = {"clicksAmount":random_number}

    try:
        # Make the POST request with JSON data
        
        
        response = requests.post(url, headers=headers, data=json.dumps(postData))
        dataString = json.dumps(response.json(), indent=4)
        data = json.loads(dataString)
        
        # Check if the request was successful (status code 200)
        if response.ok:
            #print('POST request successful', response.status_code)
            print('Energy consumed: ',random_number)
            print('Energy left: ',data['pet']['energy'])
        else:
            print(f'POST request failed with status code: {response.status_code}')

    except requests.exceptions.RequestException as e:
        print('Error making POST request:', e)


url = 'https://api-clicker.pixelverse.xyz/api/users'


while True:
    make_post_request(url)
