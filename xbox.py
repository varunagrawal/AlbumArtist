"""
Xbox API module to get song information and data from Microsoft Xbox Music API.
"""

import requests
import json

#query = "alice in chains them bones"

def get_song(query):
    auth_url = "https://datamarket.accesscontrol.windows.net/v2/OAuth2-13"          # https://msdn.microsoft.com/en-us/library/dn546686.aspx  https://msdn.microsoft.com/en-us/library/dn546659.aspx
    url = "https://music.xboxlive.com"

    client_id = "albumartist"
    client_secret = "YWAyia4PM2caxFrTcOBKPR5K9Ze9V4kSJyOO3IIdpV0="

    scope = "http://music.xboxlive.com"
    grant_type = "client_credentials"

    auth_payload = {'client_id': client_id, 'client_secret': client_secret, 'scope': scope, 'grant_type': grant_type}

    auth = requests.post(auth_url, data=auth_payload).json()

    namespace = "music"

    search_url = url + "/1/content/{0}/search".format(namespace, query, auth['access_token'])   # https://msdn.microsoft.com/en-us/library/dn546694.aspx

    r = requests.get(search_url, params={'q':query, 'accessToken': "Bearer " + auth['access_token']})             # https://msdn.microsoft.com/en-us/library/dn546686.aspx

    return r.json()


results = get_song(query)

print(results)

# Ideal album art 900x900 https://msdn.microsoft.com/en-us/library/dn546678.aspx

#for track in results['Tracks']['Items']:
#    print(track['Artists'][0]['Artist']['Name'])


"""
1. Create account on Azure Market Place
2. Activate Xbox service https://datamarket.azure.com/dataset/xboxmusic/XboxMusicPlatform#
3. Create new application https://datamarket.azure.com/developer/applications
4. Run the code using Xbox API https://msdn.microsoft.com/en-us/library/dn546696.aspx
"""
