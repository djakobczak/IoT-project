from manager import ClientManager
from client import Client

url = 'http://localhost:8000/api/v1'
c = Client(url, 'admin', 'secret')
cm = ClientManager(c)
print(cm.get_stats())