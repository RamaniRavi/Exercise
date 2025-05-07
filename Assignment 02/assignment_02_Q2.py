from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Example documents
docs = ["Python programming language", "Python and data analytics", "Programming in Python"]

text = " ".join(docs)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Document Terms")
plt.show()