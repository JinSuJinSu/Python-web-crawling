import requests
from bs4 import BeautifulSoup




def scrape_IT_news(): 
    print("IT 뉴스")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
    soup = BeautifulSoup(res.text,"lxml")
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li",limit = 3)

         


    # 출력
    for index, news in enumerate(news_list):
        a_idx=0
        img = news.find("img")

        if img:
            a_idx = 1
            #img 태그가 있으면 1번째 a 태크의 정보를 사용


        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print("{}. {}".format(index+1, title))
        print(" (링크 : {})".format(link))


if __name__ == "__main__":
    scrape_IT_news() # IT 뉴스 정보 가져오기
