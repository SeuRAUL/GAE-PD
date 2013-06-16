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
from google.appengine.api import images
from google.appengine.ext import db

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(
            """
              <h1>Unidade 3 - PD</h1>
              <h2>GUI</h2>

              <a href="/mail">E-MAIL</a>
              <a href="/img">IMAGEM</a>
            """
          )

        self.response.write(
            """
              <form action="/mail" method="get">
                Enviar e-mail para:<br />
                <div><input type="text" name="user_address"></input></div>
                <div><input type="submit" value="Send mail"></div>
              </form>
            """
          )

#E-mail
class Mail(webapp2.RequestHandler):
    def get(self, user_address):

        sender_address = "kenny.is.inmortal@gmail.com"
        user_address = 'kenny.is.inmortal@gmail.com'
        subject = "Comprovacao de inscricao"
        body = "Seu email foi cadastrado com sucesso na academia.\n\nTaekwan."

        self.response.write(
            """
              <h1>E-mail para enviado com sucesso!</h1>
              <br/>
              <h3>Metodo de envio comentado!</h3>
            """
          )

        #mail.send_mail(sender_address, user_address, subject, body)
        self.response.write(user_address)
        self.response.write("""<a href="/">HOME</a>""")


class Photo(db.Model):
    title = db.StringProperty()
    full_size_image = db.BlobProperty()

class Thumbnailer(webapp2.RequestHandler):
    def get(self):
        #if self.request.get("id"):
        photo = "https://developers.google.com/appengine/docs/python/images/transform_before.jpg" #Photo.get_by_id(int(self.request.get("id")))
        self.response.write('<img src=\"' + photo + '\"><br />')
        #img = images.Image(photo.full_size_image).resize(width=80, height=100)
        #self.response.write('<img src=\"' + photo + '\"><br />')


       #if photo:
       #   img = images.Image(photo.full_size_image)
       #   print img
       #   img.resize(width=80, height=100)
       #   img.im_feeling_lucky()
       #   thumbnail = img.execute_transforms(output_encoding=images.JPEG)

       #   self.response.headers['Content-Type'] = 'image/jpeg'
       #   self.response.out.write(thumbnail)
       #    return

        # Either "id" wasn't provided, or there was no image with that ID
        # in the datastore.
       #self.error(404)

        self.response.write("""<a href="/">HOME</a>""")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/mail', Mail),
    ('/img', Thumbnailer)
    ], debug=True)
