# Python Firebase Auth

Using [Firebase API](https://firebase.google.com).

## Installation
Install if you don't have the following modules.
### python 2 (or default to python 3)
```python
    $ pip install pyrebase
    $ pip install flask
```
### python 3
```python
    $ python3 -m pip install pyrebase
    $ python3 -m pip install flask
```
run
```python
	python3 app.py
```@localhost:5000

## Quick Start
### Init
```python
import pyrebase
import requests

config = {
    
};
# init
firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

```

### Signup
```python
try:
	# Create user
	auth.create_user_with_email_and_password(email, password)
	# Get user
	user = auth.sign_in_with_email_and_password(email, password)
	# Verify emails
	auth.send_email_verification(user['idToken'])
except requests.exceptions.HTTPError:
```