from google.appengine.ext import db

class Training(db.Model):

  day = db.StringProperty(required=True)
  time = db.StringProperty(required=True)
  instructor = db.StringProperty(required=True)


  def list_trainings(self):
    trainings = db.GqlQuery("SELECT * FROM Training")

    self.response.write("TABELA DE TREINOS: <br/>")

    for t in trainings:
      self.response.write("""
          <p>
            <b>Dia:</b> %s - %s <br/>
            <b>Instrutor:</b> %s
          </p>
        """ %(t.day, t.time, t.instructor))