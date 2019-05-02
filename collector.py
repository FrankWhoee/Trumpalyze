import requests
import json
import datetime
from matplotlib.pyplot import hist
import matplotlib.pyplot as plot
import logging
import time
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

url = "https://api.tronalddump.io/random/quote"

# Sample size
n = 5000

# Number of attempts before giving up connection
max_attempts = 100
logging.info("Connecting to " + url)
logging.info("Sampling " + str(n) + " tweets.")
times = []

# Initial time
t0 = time.time()
for i in range(0,n):
    # Get response from API
    attempts = 0
    while attempts < max_attempts:
        try:
            # Attempt response
            response = requests.get(url)
            # If response is successful, break loop.
            break
        except:
            # If response is not successful, try again
            logging.info("Could not connect to API (Attempt " + str(attempts) + " out of " + str(max_attempts) + ")")
            # If there have been more than 25 attempts, wait 5 seconds between each attempt
            if attempts > 25:
                logging.info("Attempting again in 5 seconds.")
                time.sleep(5)
            attempts += 1

    # Get JSON content from API response
    plain_json = response.text
    # Parse content from JSON
    data = json.loads(plain_json)
    # Get when the tweet was sent
    date = datetime.datetime.strptime(data["appeared_at"],"%Y-%m-%dT%H:%M:%S")
    # Record time as seconds after midnight GMT
    times.append(int(date.time().hour) * 3600 + int(date.time().minute) * 60 + int(date.time().second))
    print(str(i) + " out of " + str(n) + " retrieved [" + str((i/n) * 100)[0:5] + "%]")

# Final time
tf = time.time()

# Use matplotlib to plot histogram of data
hist(times)
plot.show()
logging.info("Retrieved and plotted " + str(len(times)) + "tweets in " + str(tf - t0) + " seconds.")