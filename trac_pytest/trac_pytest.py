#  -*- coding: utf-8 -*-
#
#  File Name: ticket_test.py
#  Creation Date: 2012 Nov 06
#  Last Modified: 2012 Nov 14

#  Copyright (c) 2003-2012 InQuant GmbH
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


__author__ = 'Rainer Hihn <rainer.hihn@inquant.de>'
__docformat__ = 'plaintext'

import pytest
import os
from trac.admin.console import TracAdmin
from trac.env import Environment
from trac.web import Request
from trac.ticket.query import Query
from teamchilllib.ticket import TicketTool
from shutil import rmtree

@pytest.fixture
def build_trac_env(request):
    # Create the Test-Environment
    path = '/tmp/foo'

    if os.path.exists(path):
        rmtree(path)

    ta = TracAdmin()
    ta.env_set(path)
    ta.do_initenv(u'NameOfTracEnv sqlite:db/trac.db')
    env = Environment(path)

    # Env-Dict for fcgi
    env_dict = {}
    env_dict['trac.base_url'] = 'http://127.0.0.1:8000/trac/'

    # Create the Request
    req = Request(env_dict, None)
    req.authname ='foo'
    req.perm = 'TICKET_ADMIN'
    req.tz = 42

    def fin():
        rmtree(path)
    request.addfinalizer(fin)
    return env, req
