from twitter import *

access_token = "1599356215-qa11pFEAhQK8SblVtI7wle2VfjpvjRu9jpLMWsm"
access_token_secret = "K6txr8MprO2zK72DT0k2YIvoyDoeDmjQlJZoOrCHjjoMm"
consumer_key = "wO6QvPUnrfNkJstvhnvDCxyMj"
consumer_secret = "mqaZFXSGDROhyKOgxEpZisxi8qZJYEAmg73qOoKwcXsTkEEhSi"

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

t.statuses.update(status="Twitter API test")
