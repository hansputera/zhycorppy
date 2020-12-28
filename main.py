from GetData import GetData
from config import author, version

class Zhycorppy:
  def __init__(self, botID: str):
    self.author = author
    self.version = version

    if len(botID) < 18 or len(botID) > 18:
      print(f"{botID} invalid")
    else:
      self.botID = botID
      self.data = GetData(botID)

    def getData(self):
      return self.data


def getBot(botID: str):
    if len(botID) < 18 or len(botID) > 18:
      print(f"{botID} invalid")
      return None
    else:
      bot = Zhycorppy(botID)
      return bot