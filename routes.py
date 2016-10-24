# -*- coding:utf-8 -*-

from flask import request, redirect
import requests

cookiename = 'openAMUserCookieName'
amURL = 'https://openam.example.com/'
validTokenAPI = amURL + 'openam/json/sessions/{token}?_action=validate'
loginURL = amURL + 'openam/UI/Login'

def session_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    usercookie = request.cookies.get(cookiename)
    if usercookie:
      amQuery = requests.post(validTokenAPI.format(token=usercookie))
      if amQuery.json()['valid']:
        return f(*args, **kwargs)
    return redirect(loginURL)
  return decorated_function

@app.route('/members_page')
@session_required
def members_page():
  pass
