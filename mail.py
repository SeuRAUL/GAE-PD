#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# -*- coding: utf-8 -*- 

from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.api import capabilities

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()
        if user:
            greeting = ('Bem vindo, %s! (<a href="%s">Sair</a>)' % (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Entre ou registre-se</a>.' % users.create_login_url('/'))

        self.response.out.write('<p>%s</p>' % greeting)


        self.response.write(
            """
              <h1>Unidade 3 - PD</h1>
              <h2>GUI</h2>

              <a href="/mail">E-MAIL</a>
            """
          )

        
#E-mail
class Mail(webapp2.RequestHandler):
    def get(self):
        self.response.write("""<a href="/">HOME</a>""")

        if capabilities.CapabilitySet('mail').is_enabled():
            sender_address = "kenny.is.inmortal@gmail.com"
            user_address = 'kenny.is.inmortal@gmail.com'
            subject = "Comprovacao de inscricao"
            body = "Seu email foi cadastrado com sucesso na academia.\n\nTaekwan."

            mail.send_mail(sender_address, user_address, subject, body)
            self.response.write('E-mail enviado para %s com sucesso <br/>' % user_address)
        else:
            self.response.write('Falha no envio do email.')



"""app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/mail', Mail)
    ], debug=True)
"""