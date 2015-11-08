'''
Created on Oct 10, 2015

@author: catzhangy1
'''
import db, db2

from flask import Flask, render_template, flash, redirect, url_for, Blueprint, request, g
import json
import os
import requests
import urllib
import base64

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

#Config
CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI') 
username = '1231664157'
SCOPE = 'playlist-read-private playlist-read-collaborative'


'''Configuring local Postgres Database on Shell
postgres -D /usr/local/var/postgres -- starts up postgrespo
createuser admin -- create admin user
createdb -U admin testdb'''

app = Flask(__name__)

# profile = Blueprint('profile', __name__,
#                     template_folder='templates',
#                     static_folder='static')
# app.register_blueprint(profile)
# app.config.from_object(__name__)
# # DATABASE = '/tmp/flaskr.db'
# DBNAME = 'testdb'
# DEBUG = True
# # SECRET_KEY = 'development key'
# USERNAME = 'admin'
# HOST = 'localhost'
# PASSWORD = 'default'

auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    # "state": STATE,
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": CLIENT_ID
}

@app.route("/")
def main():
#     try:
#         connect = db.connect_db()
#         db.init_db(connect)
#         print 'Connected to database'
#     except:
#         print "Database not ready to be used"
# #     username = '1231664157'
# #     scope = 'playlist-read-private playlist-read-collaborative'
# #     token = util.prompt_for_user_token(username,scope)
# #    connect.close()
#     return render_template('index.html', name='hello')
"""
    try:
        connect = db.connect_db()
        db.init_db(connect)
        
        #sample query!!! 
        print db.getSongsByGenre(connect, 1);
        print 'Connected to database'
    except:
        print "Database not ready to be used"
"""
    connect = db2.connect_db()
#     connect.close()
#     url_args = "&".join(["{}={}".format(key,urllib.quote(val)) for key,val in auth_query_parameters.iteritems()])
#     auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
#     print auth_url
#     return redirect(auth_url)
    return render_template('index.html', name='hello')

@app.route("/callback")
def callback():
    # Auth Step 4: Requests refresh and access tokens
    auth_token = request.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI
    }
    base64encoded = base64.b64encode("{}:{}".format(CLIENT_ID, CLIENT_SECRET))
    headers = {"Authorization": "Basic {}".format(base64encoded)}
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers)

    # Auth Step 5: Tokens are Returned to Application
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]

    # Auth Step 6: Use the access token to access Spotify API
    authorization_header = {"Authorization":"Bearer {}".format(access_token)}

    #Get user profile data and insert into DB
    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)
    user_name = profile_data['display_name']
    user_id = profile_data['id']
    image_data = profile_data['images']
    image_data = image_data[0]
    image_url = image_data['url']

    #Get and parse user playlist data
    playlist_api_endpoint="{}/users/{}/playlists".format(SPOTIFY_API_URL,user_id)
    playlist_response = requests.get(playlist_api_endpoint, headers=authorization_header)
    playlist_data = json.loads(playlist_response.text)
    print playlist_data
    return 'it works!'

@app.route("/hellotest")
def hellotest():
    return 'hello world'

if __name__ == "__main__":
    app.run(debug=True)
