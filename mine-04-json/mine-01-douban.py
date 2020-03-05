import requests
import json
from pprint import pprint


def main():
    sesssion = requests.session()
    douban_movie_url = "https://m.douban.com/movie/"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
    sesssion.get(url=douban_movie_url, headers=headers)
    douban_movie_json = "https://m.douban.com/rexxar/api/v2/movie/modules?need_manual_chart_card=1&for_mobile=1"

    headers2 = {
        "Referer": "https://m.douban.com/movie/",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }

    response = sesssion.get(url=douban_movie_json, headers=headers2)
    # json.loads 把字符串转成python类型
    json_result = json.loads(response.content.decode("utf-8"))

    # pretty print
    pprint(json_result)

    # json.dumps 能够把python类型转成json字符串
    with open("douban.json", "w", encoding="utf-8") as f:
        # unicode字符串转成中文
        # indent  缩进
        f.write(json.dumps(json_result, ensure_ascii=False, indent=4))

    with open("douban.json", "r", encoding="utf-8") as f:
        result = f.read()
        result2 = json.loads(result)
        print(result2)
        print(type(result2))


def load_dump():
    # 使用json.load 提取类文件中的对象
    result = None
    with open("douban.json", "r", encoding="utf-8") as f:
        result4 = json.load(f)
        result = result4
        print(result4)
        print(type(result4))

    # json.dump 能够把python放入类文件对象中
    with open("douban2.json", "w", encoding="utf-8") as f2:
        json.dump(result, f2, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
    # load_dump()
