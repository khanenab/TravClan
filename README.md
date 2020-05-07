# TravClan
PAYNOW sample application

Setup
The first thing to do is to clone the repository:

$ git clone https://github.com/khanenab/TravClan.git
$ cd TravClan
Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd project
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/admin/.

In order to test the wallet, transaction flows, http://127.0.0.1:8000/wallets/ to get the wallet detail API and http://127.0.0.1:8000/transaction/<wallet_id>/ to get the list of transactions for a given wallet API.
