# -*- coding:utf-8 -*-

from flask import request, redirect
import requests

cookiename = 'openAMUserCookieName'
amURL = 'https://openam.example.com/'
validTokenAPI = amURL + 'openam/identity/istokenvalid?tokenid='
loginURL = amURL + 'openam/UI/Login'

def session_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    usercookie = request.cookies.get(cookiename)
    if usercookie:
      amQuery = requests.get(validTokenAPI + usercookie)
      if 'boolean=true' in amQuery.text:
        return f(*args, **kwargs)
    return redirect(loginURL)
  return decorated_function

@app.route('/members_page')
@session_required
def members_page():
  pass
