import requests


class NewsService:

    def __init__(self):
        # Paste your real NewsAPI key below
        self.api_key = "9dcb950a240a486da19403b73be6e16c"

    def get_forex_news(self, query="forex", page_size=10):

        url = "https://newsapi.org/v2/everything"

        params = {
            "q": query,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": page_size,
            "apiKey": self.api_key,
        }

        response = requests.get(url, params=params)

        # Debug information
        print("Status Code:", response.status_code)

        data = response.json()

        print("Response:", data)

        if response.status_code != 200:
            return []

        articles = []

        for article in data.get("articles", []):

            articles.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "source": article.get("source", {}).get("name"),
                "url": article.get("url"),
            })

        return articles