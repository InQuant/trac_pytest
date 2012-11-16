#  -*- coding: utf-8 -*-
#
#  File Name: ticket_test.py
#  Creation Date: 2012 Nov 06
#  Last Modified: 2012 Nov 16

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
import tempfile
from trac.admin.console import TracAdmin
from trac.env import Environment
from shutil import rmtree

@pytest.fixture
def build_trac_env(request):
    """Create a Trac Environment in a tmp dir
    """
    path = tempfile.mkdtemp()
    ta = TracAdmin()
    ta.env_set(path)
    ta.do_initenv(u'ExampleTracEnv sqlite:db/trac.db')
    env = Environment(path)

    def fin():
        rmtree(path)
    request.addfinalizer(fin)

    return env
