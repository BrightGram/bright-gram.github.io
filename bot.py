import requests
from bs4 import BeautifulSoup
import datetime
import os

# 🔹 CONFIG
BLOG_FOLDER = "."  # current folder (your GitHub repo folder)
AFFILIATE_LINK = "https://www.amazon.com/dp/B08N5WRWNW?tag=your-affiliate-id"  # replace with your real affiliate link

def get_trending_topic():
    """Scrape a trending topic (example: Wikipedia 'On this day')"""
    url = "https://en.wikipedia.org/wiki/Portal:Current_events"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # grab the first headline
    headline = soup.find("li")
    if headline:
        return headline.text.strip()
    return "Interesting topic to discuss today!"

def create_post():
    """Make a new blog post file"""
    topic = get_trending_topic()
    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"{BLOG_FOLDER}/{today}-post.md"

    content = f"# {topic}\n\n" \
              f"This is today’s hot topic: **{topic}**.\n\n" \
              f"If you’re interested, check this out: [Cool Product]({AFFILIATE_LINK})\n\n" \
              f"*Posted automatically by my bot on {today}*"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ New post created: {filename}")

if __name__ == "__main__":
    create_post()
