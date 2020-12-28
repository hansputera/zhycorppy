from config import getBotURL, botsURL
import requests
from bs4 import BeautifulSoup 

class GetData:
  def __init__(self, botID: str):
    self.botID = None
    if len(botID) < 18 or len(botID) > 18:
      print("[ZhycorpPY]: Invalid BotID")
    else:
      self._bots = []
      self.botID = botID
      self.owner = None
      self.bot = None
      self.isRegistered = None
      self.isApproved = None
      self.prefix = None
      self.url = self.getURL()

      self.fetch()
      self.scrape()

  def getURL(self):
    return getBotURL(self.botID)

  def fetch(self):
    response = requests.get(botsURL)
    data = response.json()
    for bot in data:
      self._bots.append(bot)
      if bot['botID'] == self.botID:
        self.prefix = bot['prefix']
        self.isRegistered = bot['registered']
        self.isApproved = bot['approved']
    return self


  def scrape(self):
    response = requests.get(self.url)
    if response.reason == "OK":
      soup = BeautifulSoup(response.content, 'html5lib')

      # Owner
      owner: str = soup.find_all('a')[9].text
      ownerAvatar: str = soup.find('img', { 'alt': 'own '}).attrs['src']

      self.owner = { 
        "text": owner.strip(),
        "avatar": ownerAvatar
      }

      # Bot
      botName: str = soup.find('h3').text
      botAvatar: str = soup.find('img', { 'alt': 'Sample avatar' }).attrs['src']

      self.bot = {
        "id": self.botID,
        "name": botName.strip(),
        "avatar": botAvatar
      }

      return { "bot": self.bot, "owner": self.owner }
    else:
      del self.bot
      del self.owner
      msg = f"Error: {response.reason} {response.status_code}"
      print(msg)
      return msg