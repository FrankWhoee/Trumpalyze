import requests
import json
import datetime
from matplotlib.pyplot import hist
import matplotlib.pyplot as plot

url = "https://api.tronalddump.io/random/quote"
times = []
for i in range(0,100):
    response = requests.get(url)
    plain_json = response.text
    data = json.loads(plain_json)
    # print(data["created_at"])
    date = datetime.datetime.strptime(data["appeared_at"],"%Y-%m-%dT%H:%M:%S")
    times.append(int(date.time().hour) * 3600 + int(date.time().minute) * 60 + int(date.time().second))
    print(date.time())

hist(times)
plot.show()