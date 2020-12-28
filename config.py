#!/bin/python3

baseURL = "https://zhycorp.com"
botsURL = "https://bot.zhycorp.com"

def getBotURL(botID: str) -> str:
  return f"{baseURL}/bot/{botID}"

version = "0.0.1"
author = "Hanif Dwy Putra S"