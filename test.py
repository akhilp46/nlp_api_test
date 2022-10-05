import cohere
from cohere.classify import Example

from twitterscraper import *

#initialize nlp api
api_key = open('cohere_api_key.txt').readline()
co = cohere.Client(api_key)

#training set
examples = [Example("The order came 5 days early", "positive"), 
            Example("The item exceeded my expectations", "positive"), 
            Example("I ordered more for my friends", "positive"), 
            Example("I would buy this again", "positive"), 
            Example("I would recommend this to others", "positive"), 
            Example("The package was damaged", "negative"), 
            Example("The order is 5 days late", "negative"), 
            Example("The order was incorrect", "negative"), 
            Example("I want to return my item", "negative"), 
            Example("The item\'s material feels low quality", "negative"), 
            Example("The product was okay", "neutral"), 
            Example("I received five items in total", "neutral"), 
            Example("I bought it from the website", "neutral"), 
            Example("I used the product this morning", "neutral"), 
            Example("The product arrived yesterday", "neutral")]

#getting tweets from a specific twitter user in the last 5 days (limit set to 20 tweets)
account = "jaden"
inputs = get_tweets(account)

#initialize nlp model
response = co.classify(
  model='medium',
  inputs=inputs,
  examples=examples)

#print results
print(response.classifications)