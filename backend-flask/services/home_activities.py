from datetime import datetime, timedelta, timezone
import logging

from lib.db import db

class HomeActivities:
  #def run():
  #def run(logger):
  def run(cognito_user_id=None):
    sql = db.template('activities','home')
    results = db.query_array_json(sql)
    return results