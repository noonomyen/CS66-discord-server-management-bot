from env import CONFIG
from client import Client

client = Client()
client.run(CONFIG.TOKEN)
