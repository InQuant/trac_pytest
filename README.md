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

    def test_tickettool(build_trac_env):
        env = build_trac_env
        assert 26 == env.get_version()

Use this Fixture with Buildout:
-------------------------------

    # File buildout.cfg

    [buildout]
    parts =
            pytest

    ( ... )

    [pytest]
    recipe = zc.recipe.egg
    eggs =
      pytest
      trac
    arguments = '${buildout:directory}/src/' + sys.argv[1]

Then call pytest with a module as parameter:

    ./bin/py.test testmodule
