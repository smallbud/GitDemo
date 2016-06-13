import requests
from bs4 import BeautifulSoup
from selenium import webdriver

class HtmlDownLoad(object):

    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def crawl(self, path, url):
        self.path = path
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        content = soup.find('div', class_='mm-p-info mm-p-domain-info')
        if content is None:
            return
        print(type(content))
        span = content.find('span')
        print(type(span))
        base_url = 'http:' + span.text.strip()
        print(path, '的个性域名:', base_url)
        self.save_all_images(path, base_url)

    def save_all_images(self, path, url):
        content = requests.get(url).text
        soup = BeautifulSoup(content, 'lxml')
        imageList = soup.find('div', class_='mm-aixiu-content')
        count = 1
        for image in imageList.find_all('img'):
            if image.has_attr('src'):
                image_url = 'http:' + image['src'].strip()
                print('下载', path, ' 的第',count, ' 张图片:', image_url)
                self.downloadimage(path, image_url)
                count += 1

    def downloadimage(self, path, url):
        if url is None:
            return

        filename = url.split('/')[-1]
        response = requests.get(url)
        file_path = path + '/' + filename
        fp = open(file_path, 'wb')
        fp.write(response.content)
        fp.close()