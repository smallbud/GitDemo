import os
import requests
from bs4 import BeautifulSoup
from html_download import HtmlDownLoad

class SpiderMain(object):
    def __init__(self, url, count):
        self.base_url = url
        self.count = count
        self.download = HtmlDownLoad()

    def mkdir(self, path):
        path = path.strip()

        isExist = os.path.exists(path)
        if not isExist:
            os.mkdir(path)
            return True
        else:
            return False

    def save_all_images(self):
        for index in range(self.count + 1):
            url = self.base_url + str(index+1)
            content = requests.get(url).text
            soup = BeautifulSoup(content, 'lxml')
            for link in soup.find_all('a', class_='lady-name'):
                html_url = 'http:' + link['href'].strip()
                print('创建目录:',link.text,' 并下载:', html_url)
                self.mkdir(link.text)
                self.download.crawl(link.text, html_url)


if __name__ == '__main__':
    obj_spider = SpiderMain('http://mm.taobao.com/json/request_top_list.htm?page=', 1)
    obj_spider.save_all_images()


