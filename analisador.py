import tweepy # Biblioteca de acesso à API do Twitter
import re # Biblioteca de Expressões Regulares
import pandas as pd # Biblioteca de manipulação de dados
from textblob import TextBlob as tb # Biblioteca de análise de sentimento
from googletrans import Translator
from unidecode import unidecode

class Analisador():
  consumer_key = None
  consumer_secret = None
  access_token = None
  access_token_secret = None
  api = None

  def __init__(self):
    self.consumer_key = 'FTNaD5Z8onfViLEceLK2KSeaH'
    self.consumer_secret = 'MYJiY4U6lASYp4q7qe2vWQpxCHUykdBUHmGdm7ybbeKpr3rY4g'
    self.access_token = '1236454673822953477-RLxbfQDriec8LnnD9SuT99DreSkwBo'
    self.access_token_secret = 'qasGdiFqZkh7UUTa5ysFNCsIgSmAMa6AoRnWnadBZAikp'

    auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
    auth.set_access_token(self.access_token, self.access_token_secret)

    self.api = tweepy.API(auth)

  def analisar(self, nome_perfil_usuario):
    list_tweets = self.obter_tweets(nome_perfil_usuario = nome_perfil_usuario)

    analysis = None
    numPos = 0
    numNeg = 0
    numNeu = 0
    total = 0 

    for tweet in list_tweets:
      analysis = tb(tweet)
      polarity = analysis.sentiment.polarity

      total += 1
      if polarity > 0:
        numPos += 1
      elif polarity < 0:
        numNeg += 1
      elif polarity == 0:
        numNeu += 1

    mediaPos = numPos/total
    mediaNeg = numNeg/total
    mediaNeu = numNeu/total

    return { 'media_positiva': mediaPos, 'media_negativa': mediaNeg, 'media_neutra': mediaNeu }

  def obter_tweets(self, nome_perfil_usuario):
    results = self.api.user_timeline(screen_name = nome_perfil_usuario, count = 100, tweet_mode = 'extended')
    tweets = []

    for r in results:
      tweet = re.sub(r'http\S+', '', r.full_text)
      # tweets.append(Translator().translate(tweet.replace('\n', ' ')).text)
      tweets.append(tweet.replace('\n', ' '))

    return tweets