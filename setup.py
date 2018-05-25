from setuptools import setup

setup(name = 'gegede-tool',
      version = '1.0.0',
      description = 'Tools to generate detector geometries',
      author = 'Jose Palomino',
      author_email = 'jose.palominogallo@stonybrook.edu',
      license = 'GPLv2',
      url = 'https://github.com/palominogallo/gegede-tool',
      package_dir = {},
      packages = ['ggd', 'ggd.Det', 'ggd.Component', 'ggd.Active', 'ggd.LocalTools', 'ggd.Booleans'],
      install_requires = [
        "gegede >= 0.4",
        "pint >= 0.5.1",      # for units
        "lxml >= 3.3.5",      # for GDML export],
      ],
  )

