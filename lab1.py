import requests
import time

url = input('Enter a URL : ') # Ask the user to input a url

with requests.get(url) as response:
    resp = requests.get(url)
    hdrs = response.headers

    print("\nFinding Software")
    if 'Server' in resp.headers :
        print("Server : ", resp.headers['Server'])
    
    for key, value in enumerate(response.cookies) :
        print("\nFinding Cookies")
        print("Cookie {} expires in {} days".format(key, round((value.expires - time.time())/86400)))
