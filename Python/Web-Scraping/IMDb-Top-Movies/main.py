import requests
from bs4 import BeautifulSoup

def main(n: int) -> list:
    return [" ".join(x.text.split('\n')[2:4]).strip() for x in BeautifulSoup(requests.get('https://www.imdb.com/chart/top/').text, 'lxml').find_all(class_='titleColumn')][0:n]

if __name__ == "__main__":
    print(
        "\n".join(
            main(10)
        )
    )