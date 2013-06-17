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







app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/handler', AppHandler)
], debug=True)