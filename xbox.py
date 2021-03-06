"""
Xbox API module to get song information and data from Microsoft Xbox Music API.
"""

import requests
import json

CLIENT_ID = "albumartist"
CLIENT_SECRET = "YWAyia4PM2caxFrTcOBKPR5K9Ze9V4kSJyOO3IIdpV0="

#query = "alice in chains them bones"

def get_song(query):
    auth_url = "https://datamarket.accesscontrol.windows.net/v2/OAuth2-13"          # https://msdn.microsoft.com/en-us/library/dn546686.aspx  https://msdn.microsoft.com/en-us/library/dn546659.aspx
    url = "https://music.xboxlive.com"

    scope = "http://music.xboxlive.com"
    grant_type = "client_credentials"

    auth_payload = {'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'scope': scope, 'grant_type': grant_type}

    auth = requests.post(auth_url, data=auth_payload).json()

    namespace = "music"

    search_url = url + "/1/content/{0}/search".format(namespace, query, auth['access_token'])   # https://msdn.microsoft.com/en-us/library/dn546694.aspx

    r = requests.get(search_url, params={'q':query, 'accessToken': "Bearer " + auth['access_token']})             # https://msdn.microsoft.com/en-us/library/dn546686.aspx

    return r.json()


if __name__ == "__main__":

    results = get_song(query)

    with f = open("xbox_results.json", 'w+'):
      f.write(results)

    print(results)

# Ideal album art 900x900 https://msdn.microsoft.com/en-us/library/dn546678.aspx

#for track in results['Tracks']['Items']:
#    print(track['Artists'][0]['Artist']['Name'])

