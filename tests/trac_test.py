#  -*- coding: utf-8 -*-
#
#  File Name: trac_pytest_example.py
#  Creation Date: 2012 Nov 16
#  Last Modified: 2012 Nov 22

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

# vim: set ft=python ts=4 sw=4 expandtab :

from trac.web import Request
from trac.ticket.query import Query
import trac.ticket.model as model

def test_trac(build_trac_env):
    """Create a sample Ticket and check if
    the Ticket-Count == 1
    """
    env = build_trac_env
    env_dict = {}
    env_dict['trac.base_url'] = 'http://127.0.0.1:8000/trac/'

    # Create the Request
    req = Request(env_dict, None)
    req.authname = 'JohnDoe'
    req.perm = 'TICKET_ADMIN'
    req.tz = 42
    req.locale = 42

    # Create a Ticket
    t = model.Ticket(env)
    t['summary'] = 'Summary'
    t['description'] = 'Description'
    t['reporter'] = req.authname
    t['status'] = 'new'
    t['resolution'] = ''
    t.insert()

    # Count Tickets
    q = Query(env)
    qc = q.count(req)
    assert qc == 1
