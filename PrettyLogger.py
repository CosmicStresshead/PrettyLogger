'''
TODO
Add modes (output choices: file, console, custom)
Add color to console output
Add config import

'''

from datetime import datetime

class Logger():
  def __init__(self, level:int=0, **kwargs):
    # states
    self.level_list = ["INFO", "WARNING", "ERROR"]
    self.level = self.level_list[level]

  def log(self, level:int, message:str):
    dt = datetime.now()
    print(f"\n{dt.strftime('%d/%m/%Y')} | {dt.strftime('%H:%M:%Ss')} - {self.level_list[level]}\n\"{message}\"")

  def info(self, message):
    self.log(0, message)

if __name__ == "__main__":
  logger = Logger()
  logger.log(2, "Help!")
  logger.info("This works, then.")