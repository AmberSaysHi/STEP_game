from textblob import TextBlob
with open('myText.txt', 'r') as f:
  text = f.read()
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
