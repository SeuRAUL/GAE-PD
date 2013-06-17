from google.appengine.ext import db

from training import Training
from user import User
from mailer import Mailer

class Academy:

  @staticmethod 
  def add_training(self, t_day, t_time, t_instructor):

      t = Training(day = t_day, time = t_time, instructor = t_instructor)

      self.response.write("""
          <p>
            <b>Treino adicionado:</b><br/>
            <b>Dia:</b> %s - %s <br/>
            <b>Instrutor:</b> %s
          </p>
        """ %(t.day, t.time, t.instructor))

      t.put()
      Mailer.send_mail(self, "kenny.is.inmortal@gmail.com", "Novo treino", "Novo treino cadastrado:\n\tDia: %s - %s\n\tProfessor: %s" %(t_day, t_time, t_instructor))

  @staticmethod 
  def get_trainings(self):
    trainings = db.GqlQuery("SELECT * FROM Training")

    self.response.write("TABELA DE TREINOS: <br/>")

    for t in trainings:
      self.response.write("""
          <p>
            <b>Dia:</b> %s - %s <br/>
            <b>Instrutor:</b> %s
          </p>
        """ %(t.day, t.time, t.instructor))


  @staticmethod
  def delete_training(self, t_day):
    trainings = db.GqlQuery("SELECT * FROM Training WHERE day = :1", t_day)
    self.response.write("> Deletado")
    for t in trainings:
      t.delete()

  @staticmethod
  def add_user(self, u_name, u_type):
      u = User(name = u_name, type = u_type)

      self.response.write("""
          <p>
              <b>Usuario adicionado:</b><br/>
              <b>Nome: </b> %s <br/>
              <b>Tipo: </b> %s
          </p>
          """ %(u.name, u.type))

      u.put()

      Mailer.send_mail(self, "kenny.is.inmortal@gmail.com", "Novo usuario", "Novo usuario cadastrado:\n\tNome: %s\n\tTipo: %s" %(u_name, u_type))