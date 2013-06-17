from google.appengine.ext import db

from training import Training
from user import User

class Academy:

  @staticmethod 
  def add_training(self, t_day, b_time, t_instructor):

  	training = Training(day = t_day, time = t_time, instructor = t_instructor)

    self.response.write(t.day + t.time + t.instructor))

    t.put()

  @staticmethod 
  def get_trainings(self):
    trainings = db.GqlQuery("SELECT * FROM Training")

    for t in trainings:
      self.response.write(t.day + t.time + t.instructor))


  @staticmethod
  def delete_all_trainings(self):
    self.response.write("> Voce apagou o banco de treinos!")
    trainings= db.GqlQuery("SELECT * FROM Trainings")
    for t in trainings:
      t.delete()

  @staticmethod
  def add_user(self, u_name, u_type):
  	user = User(name = u_name, type = u_type)

  	self.response.write(u.name + u.type)

  	u.put()