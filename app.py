from flask import Flask, render_template, url_for, redirect,session
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
import os

app = Flask(__name__)
app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!/xd5\xa2\xa0\x9fR"\xa1\xa8'

'''
    Set SERVER_NAME to localhost as twitter callback
    url does not accept 127.0.0.1
    Tip: set callback origin(site) for Facebook and Twitter
    as http://domain.com (or use your domain name) as these providers
    don't accept 127.0.0.1 / localhost
'''

app.config['SERVER_NAME'] = 'localhost:5000'
oauth = OAuth(app)


nonce = generate_token()

@app.route('/')
def index():
    title= 'home'
    user_name = session.get('user')
    print(user_name)
    user=""
    if(user_name):
        user = user_name['given_name']
        if(len(user)>20):
            user = user_name['given_name'][0:20]

    # given_name = user_name.split()[0]

    return render_template('index.html',user=user,title=title)

@app.route('/google/')
def google():

    # Google Oauth Config
    # Get client_id and client_secret from environment variables
    # For development purpose, you can directly put it
    # here inside double quotes
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    
    # Redirect to google_auth function
    redirect_uri = url_for('google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    session['user'] = token['userinfo']
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
