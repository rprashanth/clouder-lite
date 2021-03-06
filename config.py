"""
Instructions for configuring the app:
flask settings::
host: 0.0.0.0,
port: 5000- recommended, 80- if you're accessing from outside the local network. May need su permission
threaded: True- handles multiple requests simultaneously, False- only one request at a time
debug: True- opens a terminal in case of error. DO NOT set it to True if you're accessing the server from outside

app settings::
content_folder: the directory that will be used as root for uploads and downloads.
                Moving 'UP' from this directory will not be allowed for security reasons.
"""

from os import getcwd

configurations = {
  'default': {
    'flask': {
      'host': '0.0.0.0',
      'port': 5000,
      'threaded': True,
      'debug': True, # Change this to False in the future
    },
    'app': {
      'content_folder': getcwd() + '/content/'
    },
  },

  'dev': {
    'flask': {
      'host': '0.0.0.0',
      'port': 5000,
      'threaded': True,
      'debug': True,
    },
    'app': {
      'content_folder': getcwd() + '/content/'
    },
  },

  'external': {
    'flask': {
      'host': '0.0.0.0',
      'port': 80,
      'threaded': True,
      'debug': False,
    },
    'app': {
      'content_folder': getcwd() + '/content/'
    },
  },
}
