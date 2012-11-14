py.test-Fixture for Trac
========================

Create a temporary Trac-Environment

Example Usage:
--------------

    def test_tickettool(build_trac_env):
        env = build_trac_env[0]
        assert 26 == env.get_version()

Buildout Usage:
---------------

    [buildout]
    parts =
            pytest

    ( ... )

    [pytest]
    recipe = zc.recipe.egg
    eggs =
      pytest
      trac
      teamchilllib
    arguments = '${buildout:directory}/src/' + sys.argv[1]
