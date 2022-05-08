import requests
import fake_useragent
from bs4 import BeautifulSoup
import json

def get_news():
	user = fake_useragent.UserAgent().random
	header = {
		"user-agent": user
	}
	url = "https://www.sports.kz/news"

	response = requests.get(url, headers=header).text
	


	soup = BeautifulSoup(response, "lxml")
	time = soup.find("ul", class_="news_all today_").find_all("li")
	new_dict = {}
	
	texts = []
	for info in time:
		text = info.find("span").text
		texts.append(text)
	texts.pop(0)
	datas = soup.find("ul", class_="news_all today_").find_all("i")
	hours = []
	for i in datas:
		hours.append(i.text)

	title =soup.find("ul", class_="news_all today_").find_all("b")
	Titles = []
	for j in title:
		Titles.append(j.find("a").text)

	links = soup.find("ul", class_="news_all today_").find_all("a")
	linkses = []
	for p in links:
		ssylka = p.get("href")
		linkses.append(ssylka)

	for g in range(0, len(linkses)//2):
		linkses.pop(g)


	for_returning = []
	#with open("data.json","w", encoding="utf-8") as file:

	for plus in range(0, len(hours)):
		stroka = f'{hours[plus]}     {Titles[plus]}:\n \n https://www.sports.kz{linkses[plus]}\n\n\n'
		for_returning.append(stroka)
		#file.write(stroka)
	return for_returning

def fresh_news():
	user = fake_useragent.UserAgent().random
	header = {
		"user-agent": user
	}
	url = "https://www.sports.kz/news"

	response = requests.get(url, headers=header).text
	


	soup = BeautifulSoup(response, "lxml")
	time = soup.find("ul", class_="news_all today_").find_all("li")
	new_dict = {}
	
	texts = []
	for info in time:
		text = info.find("span").text
		texts.append(text)
	texts.pop(0)
	datas = soup.find("ul", class_="news_all today_").find_all("i")
	hours = []
	for i in datas:
		hours.append(i.text)

	title =soup.find("ul", class_="news_all today_").find_all("b")
	Titles = []
	for j in title:
		Titles.append(j.find("a").text)
	
	links = soup.find("ul", class_="news_all today_").find_all("a")
	linkses = []
	for p in links:
		ssylka = p.get("href")
		linkses.append(ssylka)

	linkses.pop(0)
	linkses.pop(1)
	linkses.pop(2)

	for_return = []
	for plus in range(0, 3):
		stroka = f'{hours[plus]}     {Titles[plus]}:\n \n https://www.sports.kz{linkses[plus]}\n\n\n'
		
		for_return.append(stroka)
	return for_return


def main():
	get_news()


if __name__ == '__main__':
	main()





