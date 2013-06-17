from google.appengine.ext import db

class User(db.Model):

  name = db.StringProperty(required=True)
  type = db.StringProperty(required=True)


  def list_trainings(self):
    users = db.GqlQuery("SELECT * FROM User")

    for u in users:
      self.response.write(u.name + u.type)