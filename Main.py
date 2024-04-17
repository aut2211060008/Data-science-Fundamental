Here's a Python code snippet to scrape app reviews from the Google Play Store using the BeautifulSoup library:

```python
import requests
from bs4 import BeautifulSoup

def scrape_play_store_reviews(app_id, num_reviews):
    base_url = f"https://play.google.com/store/apps/details?id={app_id}&showAllReviews=true"
    reviews = []

    while len(reviews) < num_reviews:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        review_divs = soup.find_all('div', class_='d15Mdf')

        for review_div in review_divs:
            review = review_div.find('span', class_='')  # adjust class as needed
            if review:
                reviews.append(review.text)

        next_button = soup.find('div', class_='U26fgb')
        next_button_url = next_button.find('a')['href']
        base_url = f"https://play.google.com{next_button_url}"

    return reviews[:num_reviews]

# Example usage:
app_id = 'com.example.app'  # Replace with the app ID of the target app
num_reviews = 100  # Number of reviews to scrape
reviews = scrape_play_store_reviews(app_id, num_reviews)
for i, review in enumerate(reviews, start=1):
    print(f"Review {i}: {review}")
```

This code defines a function `scrape_play_store_reviews` that takes the app ID and the number of reviews to scrape as input parameters. It then scrapes the reviews from the Play Store page of the specified app using BeautifulSoup, iterates through the reviews, and returns a list of review texts.

You need to replace `'com.example.app'` with the actual app ID of the target app and adjust the review class (`'d15Mdf'`) if necessary based on the structure of the Play Store page. Additionally, you might need to handle pagination if the number of reviews exceeds what's displayed on a single page.
