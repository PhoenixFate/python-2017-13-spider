import requests
import json
from pprint import pprint
import re


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    }
    url = "https://36kr.com/"
    response = requests.get(url=url, headers=headers)
    result = re.findall("<script>window.initialState=(.*?)</script>", response.content.decode("utf-8"))[0]
    json_result = json.loads(result)
    with open("36ke.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(json_result,ensure_ascii=False, indent=4))

    pass


if __name__ == '__main__':
    main()
