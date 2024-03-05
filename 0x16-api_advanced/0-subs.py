#!/usr/bin/python3
from requests import get

def number_of_subscribers(subreddit):
   """Queries the Reddit API to retrieve the number of subscribers for a given subreddit.

   Args:
       subreddit (str): The name of the subreddit to query.

   Returns:
       int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid or an error occurs.
   """

   url = f"https://www.reddit.com/r/{subreddit}/about.json"
   headers = {"User-Agent": "YourAppName/0.1"}  # Set a custom User-Agent

   try:
       response = requests.get(url, headers=headers, allow_redirects=False)  # Prevent redirects
       response.raise_for_status()  # Raise an exception for error responses

       data = response.json()
       return data["data"]["subscribers"]

   except requests.exceptions.RequestException as error:
       print(f"Error fetching subreddit data: {error}")
       return 0

