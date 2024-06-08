# video tutorial: https://www.youtube.com/watch?v=z4DQYprjPSs&list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-&index=5&pp=iAQB

import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# article summary and analysis

def summarize():
    url = input.get("1.0", "end").strip()

    article = Article(url)

    analysis = TextBlob(article.text)

    # change fields

    article.download()
    article.parse()

    article.nlp()

    title.config(state="normal")
    authors.config(state="normal")
    pdate.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    title.delete("1.0", "end")
    title.insert("1.0", article.title)

    summary.delete("1.0", "end")
    summary.insert("1.0", article.summary)

    pdate.delete("1.0", "end")
    pdate.insert("1.0", article.publish_date)

    authors.delete("1.0", "end")
    authors.insert("1.0", article.authors)

    sentiment.delete("1.0", "end")
    sentiment.insert("1.0", f"Sentiment: {'positive' if analysis.polarity > 0 else 'negative' if analysis.polarity < 0 else 'neutral'}")

    title.config(state="disabled")
    authors.config(state="disabled")
    pdate.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")


# GUI
root = tk.Tk()
root.title("News Summarizer")
root.geometry("1200x600")

# title section
tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

# author section

alabel = tk.Label(root, text="Authors")
alabel.pack()

authors = tk.Text(root, height=1, width=140)
authors.config(state="disabled", bg="#dddddd")
authors.pack()

# publication date section

plabel = tk.Label(root, text="Publication Date")
plabel.pack()

pdate = tk.Text(root, height=1, width=140)
pdate.config(state="disabled", bg="#dddddd")
pdate.pack()

# summary section

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

# sentiment analysis section
selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

# URL input
ulabel = tk.Label(root, text="URL")
ulabel.pack()

input = tk.Text(root, height=1, width=140)
input.pack()

# button
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()