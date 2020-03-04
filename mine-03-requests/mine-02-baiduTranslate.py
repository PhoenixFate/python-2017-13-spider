import requests
import json
import re
import js2py


class BaiduTranslate:

    def __init__(self, translate_data):
        self.session = requests.session()
        self.translate_data = translate_data
        self.baidu_url = "https://www.baidu.com"
        self.translate_root_url = "https://fanyi.baidu.com"
        self.language_detect_url = "https://fanyi.baidu.com/langdetect"
        self.translate_url = "https://fanyi.baidu.com/v2transapi"
        self.headers = headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        }
        self.session.headers = headers

    def parse_url(self, url, data):
        response = requests.post(url=url, data=data, headers=self.headers)
        return response.content.decode("utf-8")

    def get_token_gtk(self):
        """获取token和gtk(用于合成Sign)"""
        self.session.get(self.translate_root_url)
        resp = self.session.get(self.translate_root_url)
        html_str = resp.content.decode()
        token = re.findall(r"token: '(.*?)'", html_str)[0]
        gtk = re.findall(r"window.gtk = '(.*?)'", html_str)[0]
        return token, gtk

    def lang_detect(self):
        """获取语言转换类型.eg: zh-->en"""
        lang_resp = self.session.post(self.language_detect_url, data={"query": self.translate_data})
        lang_json_str = lang_resp.content.decode()  # {"error":0,"msg":"success","lan":"zh"}
        print(lang_json_str)
        lan = json.loads(lang_json_str)['lan']
        to = "en" if lan == "zh" else "zh"
        return lan, to

    def generate_sign(self, gtk):
        """生成sign"""
        # 1. 准备js编译环境
        context = js2py.EvalJs()
        with open('webtrans.js', encoding='utf8') as f:
            js_data = f.read()
            js_data = re.sub("window\[l\]", '"' + gtk + '"', js_data)
            # js_data = re.sub("window\[l\]", "\"{}\"".format(gtk), js_data)
            # print(js_data)
            context.execute(js_data)
        sign = context.e(self.translate_data)
        return sign

    def final_result(self, post_data):
        response = self.session.post(url=self.translate_url, data=post_data)
        result = json.loads(response.content.decode("utf-8"))["trans_result"]["data"][0]["dst"]
        print("{}: {}".format(self.translate_data, result))

    def run(self):
        # 1.获取百度的cookie,(缺乏百度首页的cookie会始终报错998)
        # self.session.get(self.baidu_url)

        token, gtk = self.get_token_gtk()
        print(token + " : " + gtk)
        sign = self.generate_sign(gtk)
        print(sign)
        lan, to = self.lang_detect()
        print(lan + " : " + to)

        # 5. 发送请求,获取响应,输出结果
        post_data = {
            "from": lan,
            "to": to,
            "query": self.translate_data,
            "transtype": "realtime",
            "simple_means_flag": 3,
            "sign": sign,
            "token": token
        }
        self.final_result(post_data)


def main():
    translate_data = "中文"
    translate = BaiduTranslate(translate_data)
    translate.run()


if __name__ == '__main__':
    main()
