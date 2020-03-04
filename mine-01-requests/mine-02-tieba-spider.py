import requests


class TiebaSipder:

    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}

    def get_url_list(self):
        # url_list = []
        # for i in range(10):
        #     url_list.append(self.url_temp.format(i * 50))
        # return url_list
        # !!!!!!!!!!!!!!!!!!!!!上面4句话的简写方式
        return [self.url_temp.format(i*50) for i in range(5)]

    def parse_url(self, url):
        """发送请求，获取响应"""
        response = requests.get(url, headers=self.headers)
        return response

    def save_html(self, html_str, page_number):
        """保存贴吧内容"""
        file_path = "{}-第{}页.html".format(self.tieba_name, page_number)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        """贴吧爬虫脚本主要实现"""
        # 1.构造url
        url_list = self.get_url_list()
        # 2.遍历，发送请求，获取响应
        for url in url_list:
            print("正在爬：%s", url)
            html_str = self.parse_url(url).content.decode("utf-8")
            # 3.保存
            page_number = url_list.index(url) + 1
            self.save_html(html_str, page_number)


def main():
    tiebaSpider = TiebaSipder("李毅")
    tiebaSpider.run()


if __name__ == '__main__':
    temp_list = ['a' for i in range(3)]
    print(temp_list)

    # main()

