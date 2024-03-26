# get api key from spotify for developer in dashboard and use int create a new application 


# use dotenv to get the client id and secret
from dotenv import load_dotenv
import os
import base64
from requests import post,get   
import json

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
# print(client_id, client_secret)


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search(token, artust_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={artust_name}&type=artist&limit=1"
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print("No artist found with that name")
        return None
    return json_result[0]
def get_song_by_artist(token, artist_id):
    url = "https://api.spotify.com/v1/artists/" + artist_id + "/top-tracks"
    headers = get_auth_header(token)
    query = "market=US"
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


token = get_token()
search_for_artist = search(token, "kendrick lamar")
artist_id = search_for_artist["id"]
# print(search_for_artist["name"])
songs = get_song_by_artist(token, artist_id)
for index, songs in enumerate(songs):
    print(index + 1, songs["name"])