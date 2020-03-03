import requests

"""
111.231.207.107:15847,HTTP/HTTPS,10752
123.206.18.205:34024,HTTP/HTTPS,10752
118.89.170.196:64516,HTTP/HTTPS,10753
123.207.243.183:8329,HTTP/HTTPS,10753
123.206.20.243:13240,HTTP/HTTPS,10752
"""


def main():
    proxies = {
        "http": "http://111.231.207.107:15847"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    }
    response = requests.get("http://www.baidu.com", proxies=proxies, headers=headers)
    print(response)
    pass


if __name__ == '__main__':
    main()
