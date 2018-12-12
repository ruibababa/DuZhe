# @Author  : ShiRui

import requests
from bs4 import BeautifulSoup
import os


def getHtml(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
	}
	html = requests.get(url=url, headers=headers).content.decode("utf-8")

	soup = BeautifulSoup(html, 'lxml')

	return soup


def getData(url):

	soup = getHtml(url)
	link = soup.select('.booklist a')
	for i in link:
		article = base_url + i['href']
		# print(article)
		each_article = getHtml(article)
		title = each_article.find('h1').string
		writer = each_article.find(id="pub_date").string
		content = each_article.select(".blkContainerSblkCon p")
		# print(title + ':' + writer)
		filename = path + '\\' + title + '.txt'
		with open(filename, "a", encoding="utf-8") as f:
			f.write("<<" + title + ">>" + "\n\n" + writer)
			for p in content:
				context = p.text
				f.write(context)


def main(url):

	getData(url)


if __name__ == '__main__':

	time = "2017_24"
	base_url = 'http://www.52duzhe.com/' + time + '/'
	url = 'http://www.52duzhe.com/' + time + '/index.html'
	path = os.getcwd() + u'/读者'
	if not os.path.isdir(path):
		os.mkdir(path)

	main(url)
