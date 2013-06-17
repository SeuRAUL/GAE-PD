from google.appengine.api import mail
from google.appengine.api import capabilities

class Mailer:

  @staticmethod 
  def send_mail(self, user_address, subject, body):

    if capabilities.CapabilitySet('mail').is_enabled():
      self.response.write("> E-mail ok! \n <br/>")

      sender_address = "kenny.is.inmortal@gmail.com"

      mail.send_mail(sender_address, user_address, subject, body)

      self.response.write('E-mail enviado para %s com sucesso <br/>' % user_address)
    else:
      'Falha no envio do email.'