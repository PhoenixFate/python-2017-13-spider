import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
}


@retry(stop_max_attempt_number=3)
def parse_url_content(url, method="GET", data=None,proxies={}):
    print("*" * 10)
    response = None
    if method == "GET":
        response = requests.get(url=url, headers=headers, timeout=3)
    elif method == "POST":
        response = requests.post(url=url, data=data, headers=headers, timeout=3)
    assert response.status_code == 200
    return response.content.decode("utf-8")


if __name__ == '__main__':
    temp_url = "www.baidu.com"
    parse_url_content(temp_url, method="GET")
