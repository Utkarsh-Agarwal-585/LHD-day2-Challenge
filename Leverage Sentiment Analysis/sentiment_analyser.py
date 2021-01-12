"""TextBlob is a Python (2 and 3) library for processing textual data. 
It provides a simple API for diving into common natural language processing (NLP) tasks
such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more
"""


from textblob import TextBlob
x = input("Enter your review : ")
edu = TextBlob(x)
y = edu.sentiment.polarity

#if negative then  
if y<0:
    print("Negative")

#if neutral then
elif y==0:
    print("Neutral")

#if Positive then
elif y>0 and y<=1:
    print("Positive")
