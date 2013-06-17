from google.appengine.ext import db

class User(db.Model):

  name = db.StringProperty(required=True)
  type = db.StringProperty(required=True)


  def list_users(self):
    users = db.GqlQuery("SELECT * FROM User")

    self.response.write("TABELA DE USUARIOS: <br/>")

    for u in users:
    	self.response.write("""
          <p>
            <b>Nome:</b> %s <br/>
            <b>Tipo:</b> %s
          </p>
        """ %(u.name, u.type))