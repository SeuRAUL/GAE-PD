from google.appengine.ext import db

class Training(db.Model):

  day = db.StringProperty(required=True)
  time = db.StringProperty(required=True)
  instructor = db.StringProperty(required=True)


  def list_trainings(self):
    trainings = db.GqlQuery("SELECT * FROM Training")

    for t in trainings:
      self.response.write(t.day + t.time + t.instructor)