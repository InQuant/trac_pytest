py.test-Fixture for Trac
========================

[pytest](http://pytest.org/latest/ "pytest") is a mature full-featured Python testing tool.

This package creates a temporary Trac-Environment with a fully functional database.

Quick Start:
------------

    # Assumes you have Trac and pytest installed
    # This calls the test in ./tests/trac_test.py
    #
    # Creates a sample Ticket and checks if
    # Ticket-Count == 1

    git clone https://github.com/InQuant/trac_pytest.git
    cd trac_pytest
    py.test


Example Usage:
--------------

::

    def test_tickettool(build_trac_env):
        env = build_trac_env
        assert 26 == env.get_version()

Usage with a unittest.TestCase:
-------------------------------

::

    import unittest
    import pytest

    @pytest.mark.usefixtures("build_trac_env")
    class TestCaseSomething(unittest.TestCase):

        def testSomething(self):
            #the build_trac_env fixture created an env and set it on the class
            assert self.env



Use this Fixture with Buildout:
-------------------------------

    # File buildout.cfg

    [buildout]
    parts =
            test

    ( ... )

    [test]
    recipe = zc.recipe.egg
    eggs =
      pytest
      trac
      testmodule
    scripts = py.test=test
    arguments = '${buildout:directory}/src/' + sys.argv[1]

Then call pytest with a module as parameter:

    ./bin/test testmodule
