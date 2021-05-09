import requests
from bs4 import BeautifulSoup




def scrape_headline_news(): 
    print("오늘의 헤드라인 뉴스")
    url = "https://news.naver.com/"
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
    soup = BeautifulSoup(res.text,"lxml")
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li",limit = 3)

         


    # 출력
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print(" (링크 : {})".format(link))


if __name__ == "__main__":
    scrape_headline_news() # 헤드라인 뉴스 정보 가져오기


     