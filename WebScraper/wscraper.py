# Web Scraper de noticias
# Autor: mfs9 - github.com/mfs9

"""
Script de Web Scraping em Python para extrair notícias de um site específico.

Dependências:
- requests
- beautifulsoup4

Instruções de uso:
1. Defina o URL do site na variável news_url.
2. Execute o script para extrair as notícias e exibir os resultados.

Personalização:
- Modifique o código para extrair informações diferentes do site.
- Tenha cuidado ao realizar Web Scraping e respeite os termos de uso do site.

"""

import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news_articles = soup.find_all('div', class_='feed-post-body')

    news_data = []
    for article in news_articles:
        title = article.find('a', class_='feed-post-link').text.strip()
        date_element = article.find('time')
        date = date_element.text.strip() if date_element else "No date available"
        summary_element = article.find('div', class_='feed-post-body-resumo')
        summary = summary_element.text.strip() if summary_element else "No summary available"

        news = {
            'title': title,
            'date': date,
            'summary': summary
        }

        news_data.append(news)

    return news_data

# Teste do Web Scraper
news_url = 'https://g1.globo.com/'
scraped_news = scrape_news(news_url)
for news in scraped_news:
    print(f"Title: {news['title']}")
    print(f"Date: {news['date']}")
    print(f"Summary: {news['summary']}")
    print()
