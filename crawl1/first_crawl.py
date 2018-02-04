import requests
from bs4 import BeautifulSoup
# h4 안에있는 텍스트
# 그 밑에 ul li 에 있는 a태그의 링크주소와 텍스트들을 리스트에 넣고 for문으로 return가능하게 함수설정
# 각 요일마다 같은 구조를 취하고 있으니 전부 모아서 커다란 리스트로 return

url = "http://comic.naver.com/webtoon/weekday.nhn"

response = requests.get(url)

# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

webtoon_list = soup.select('div#container > div div.daily_all ul li')
#순회하는 것들 이어야함 ul 안에 li이의 form들이 다 같기 때문에

# print(webtoon_list)
result = []

for li in webtoon_list:
# 왜냐면 여기서 li는 html안의 li가 아니라 webtoon_list 안에 있는 각각의 객체들이기 때문에
    webtoon_link = li.select_one('a.title').get('href')
    webtoon_title = li.select_one('a.title').get_text(strip=True)
    webtoon = [webtoon_link, webtoon_title]
    result.append(webtoon)
print(result)
