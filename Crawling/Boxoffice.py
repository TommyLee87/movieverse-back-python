import requests
import json
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/boxoffice/weekly'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

response = requests.get(url, headers=headers)  # headers were missing in your GET request
soup = BeautifulSoup(response.text, 'html.parser')
movieInfoList = soup.find('ol', attrs={'class': 'list_movieranking'}).find_all('li') if soup.find('ol', attrs={'class': 'list_movieranking'}) else []

movie_data = []

for movieInfo in movieInfoList:
    movieTitle = movieInfo.find('a', attrs={'class': 'link_txt'})
    movieRank = movieInfo.find('span', attrs={'class': 'rank_num'})

    movie_data.append({
        'rank': movieRank.get_text() if movieRank else "X",
        'title': movieTitle.get_text().strip() if movieTitle else "X",
    })

# Convert the movie data to JSON
json_data = json.dumps(movie_data, ensure_ascii=False, indent=4)
print(json_data)

