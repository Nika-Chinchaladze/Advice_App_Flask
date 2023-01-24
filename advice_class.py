import requests


class GetAdvice:
    def __init__(self):
        self.advice_api = "https://api.adviceslip.com/advice"

    def get_advice(self):
        respond = requests.get(url=self.advice_api)
        data = respond.json()["slip"]
        return data

