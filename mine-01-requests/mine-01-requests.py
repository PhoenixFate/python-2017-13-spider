import requests


def main():
    response = requests.get("http://www.baidu.com")
    print(response)
    print("获取response编码方式：%s" % response.encoding)
    # 修改编码方式
    response.encoding = "utf-8"
    # response.text是string
    print(response.text)
    # response.content是bytes
    print(response.content)
    # 推荐使用这种方式获取html文本
    print(response.content.decode("utf-8"))

    # 常用方法
    # 获得状态码
    # response.status_code
    print(response.status_code)
    assert response.status_code == 200
    # 获得请求headers
    print("request.headers: %s" % response.request.headers)
    # 获得响应头
    print("response.header: %s" % response.headers)

    print("request.url: %s" % response.request.url)
    print("response.url: %s" % response.url)
    pass


def save_picture():
    response = requests.get("http://t8.baidu.com/it/u=581096476,2560083681&fm=79&app=86&f=JPEG?w=1242&h=1800")
    with open("a.jpg", "wb") as f:
        f.write(response.content)


def request_with_headers():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
    response = requests.get("http://www.baidu.com", headers=headers)
    print("new content: %s", response.content.decode("utf-8"))


def request_with_parameters():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
    parameters = {
        "wd": 'python中文'
    }
    response = requests.get("http://www.baidu.com", headers=headers, params=parameters)
    print(response.status_code)
    print(response.request.url)
    pass


def request_with_parameters2():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
    url = "http://www.baidu.com?wd={}".format("python中文")
    response = requests.get(url=url, headers=headers)
    print(response.status_code)
    print(response.request.url)


if __name__ == '__main__':
    main()
    # save_picture()
    # request_with_headers()
    # request_with_parameters()
    request_with_parameters2()
