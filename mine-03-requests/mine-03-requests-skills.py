import requests
import utils_parse_url

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
}


def main():
    response = requests.get("https://www.baidu.com", headers=headers)
    print(response.cookies)
    # cookie转字典
    cookie_dictionary = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookie_dictionary)

    # 字典转cookie
    dictionary = {"name": "tom"}
    requests.utils.cookiejar_from_dict(dictionary)

    # url解码
    url1 = requests.utils.unquote("https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9D%8E%E6%AF%85&fr=search")
    print(url1)

    # url编码
    url2 = requests.utils.quote("https://tieba.baidu.com/f?ie=utf-8&kw=李毅&fr=search")
    print(url2)


def ssl_test():
    # 不验证ssl证书 verify=False
    response = requests.get("https://98tang.com/", headers=headers, verify=False)
    print(response.content.decode("utf-8"))


def time_out():
    # 不验证ssl证书 verify=False
    response = requests.get("https://www.baidu.com/", headers=headers, timeout=10)
    # 配合状态码判断请求是否成功
    assert response.status_code == 200
    print(response.content.decode("utf-8"))
    pass


def utils_test():
    url = "https://www.baidu.com"
    content = utils_parse_url.parse_url_content(url)
    print(content)


if __name__ == '__main__':
    # main()
    # ssl_test()
    # time_out()
    utils_test()
