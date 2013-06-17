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

from mailer import Mailer
from register import Register
from user import User
from training import Training
from academy import Academy

import webapp2

class AppHandler(webapp2.RequestHandler):

		def get(self):
				self.response.set_status(200)
				self.response.write("Funcionou")

def decode(s):

		vector = s.split("&")

		params = {}

		for v in vector:
				aux = v.split("=")
				params[aux[0]] = aux[1]

		return params

class MainHandler(webapp2.RequestHandler):

  	def get(self):

				#Academy.add_training(self, 'Sex', '19h', 'Paulo')

				Academy.get_trainings(self)

				#1. URL_fetch====================================================

				Register.register(self)

				self.response.set_status(200)

				self.response.write("App no Ar - Solicitacao Recebida<br />")

				#2. E-mail=======================================================

				user_address = "kenny.is.inmortal@gmail.com"
				subject = "Comprovacao de inscricao"
				body = "Seu email foi cadastrado com sucesso na academia.\n\nTaekwan."

				#Mailer.send_mail(self, user_address, subject, body)

  	def put(self):
				params = decode(self.request.body)

				#self.response.write('params ' + params)

				if (params["request_type"] == "training"):
						Academy.add_training(self, params["t_day"], params["t_time"], params["t_instructor"])
				elif (params ["request_type"] == "user"): 
						Academy.add_user(self, params["u_name"], params["u_type"])
				elif (params ["request_type"] == "delete"):
						Academy.delete_training(self, params["t_day"])
				else:
						'Operacao invalida!'

  	def delete(self):
				params = decode(self.request.body)

				Academy.delete_training(self, params["t_day"])




app = webapp2.WSGIApplication([
    ('/seuraul-pd-app/academy', MainHandler),
    ('/handler', AppHandler)
], debug=True)