import requests
import json
import random
import argparse
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
    parser = argparse.ArgumentParser(description='Send POST requests with clicks amount.')
    parser.add_argument('secret', type=str, help='Pixels.xyz telegram secret')
    parser.add_argument('tgID', type=str, help='Telegram ID')
    
    args = parser.parse_args()

    secret = args.secret
    tgID = args.tgID
  
    while True:
        make_post_request(url, secret, tgID)


if __name__ == '__main__':
    main()
