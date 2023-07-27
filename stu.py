import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')
url = 'https://www.searchlogistics.com/learn/statistics/minecraft-user-statistics/#:~:text=Since%20the%20original%20release%20of,141%20million%20active%20players%20worldwide.&text=In%20less%20than%20a%20year,to%20the%20COVID%2D19%20pandemic.'
article = Article(url)
article.download()
article.parse()
article.nlp()
text = article.summary
print(text)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1, positive or not
print(sentiment)
