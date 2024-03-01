#Lab1 

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = input('Enter a URL:')

if not url.startswith("http://"):
    url = "http://" + url

with requests.get(url) as response:

    print(f"Website headers are {url} \n , {response.headers} \n\n")

    server = response.headers.get('Server')

    if server:
        print(f"The server is {server}")
    else:
        print("No server found")
        
    cookies = response.headers.get('Set-Cookie')

    if cookies:
        print(f"The cookie is {cookies}")
    else:
        print("No cookie found")