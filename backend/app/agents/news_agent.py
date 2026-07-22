from app.services.news_service import NewsService


class NewsAgent:

    def __init__(self):
        self.news = NewsService()

    def analyze(self, pair: str):
        # Create a better search query for Forex-related news
        query = f'"{pair}" OR forex OR currency market OR central bank OR USD OR EUR'

        articles = self.news.get_forex_news(
            query=query,
            page_size=10
        )

        return {
            "pair": pair,
            "total_articles": len(articles),
            "articles": articles
        }