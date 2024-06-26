import requests
import json
import random
import os
from dotenv import load_dotenv
# Load environment variables from .env file if present
load_dotenv()

url = 'https://api-clicker.pixelverse.xyz/api/users'
def make_post_request(url,secret,tgID):
    random_number = random.randint(1, 50)
    # Specify headers with Content-Type as application/json
    
    headers = {'Content-Type': 'application/json',
               'Secret': secret,
               'Tg-Id': tgID
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





def main():
    # Access environment variables
    secret_value = os.getenv('SECRET')
    tg_id_value = os.getenv('TGID')
    print(f"Secret value: {secret_value}")
    print(f"TG ID value: {tg_id_value}")
    while True:
        make_post_request(url, secret_value, tg_id_value)


if __name__ == '__main__':
    main()
