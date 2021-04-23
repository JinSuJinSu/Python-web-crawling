import re
import requests
from bs4 import BeautifulSoup

 


def scrape_english(): 
    print("오늘의 영어 회화")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
    soup = BeautifulSoup(res.text,"lxml")
    sentences = soup.find_all("div",attrs={"id":re.compile("^conv_kor_t")})


    print("영어 지문")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())

    print()

    print("한글 지문")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())

if __name__ == "__main__":
    scrape_english() # 오늘의 영어 회화 가져오기
