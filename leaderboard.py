from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Float, Integer, String, DateTime, MetaData, ForeignKey, func
import os

db=SQLAlchemy()

class User(db.Model):
  user = db.Column(db.String(80), primary_key=True, unique=True)
  submit_token = db.Column(db.String(80))
  pointsEarned = db.Column(Integer, default=0)
  pointsRewarded = db.Column(Integer, default=0)
  ctime = db.Column(DateTime, default=func.now())

def setup(app):
  print('!!! SETTING UP THE APP')
  try:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
  except Exception as e:
    print("[-] DBURI invalid "+str(e))

  db = SQLAlchemy(app)

def init():
  db.create_all()

def bump_user(submit_token):
  thisuser = User.query.filter_by(submit_token=newhost['submit_token']).first()
  if not thisuser:
    return "invalid submit token: '"+newhost['submit_token']+"'"
  newhost['user']=thisuser.user
  thisuser.pointsEarned=thisuser.pointsEarned+1
  db.session.commit()

def get_leaders():
  theleaders = {}
  for user in User.query.all(): # TODO maybe limit by date at some point?
    theleaders[user.user]=user.pointsEarned

  return theleaders

def get_token(user)

  submit_token=""

  try:
    thisuser = User.query.filter_by(user=current_user).first()
  except:
    thisuser = None

  if not thisuser:
    newuser = User()
    newuser.user = current_user
    newuser.submit_token = ''.join(random.choice(string.ascii_lowercase) for i in range(22))
    submit_token = newuser.submit_token
    db.session.add(newuser)
    db.session.commit()
  else:
    submit_token = thisuser.submit_token

  return submit_token


