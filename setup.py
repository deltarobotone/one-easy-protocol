from setuptools import setup
setup(
  name = 'one-easy-protocol',
  packages = ['easyprotocol'],
  version = '0.4',      
  license='LGPLv3+',
  description = 'Easy protocol for serial communication between a Device and Delta-Robot One',
  author = 'Delta-Robot One',
  author_email = 'deltarobotone@web.de',
  url = 'https://github.com/deltarobotone',
  download_url = 'https://github.com/deltarobotone/one-easy-protocol/archive/v0.4.tar.gz',
  install_requires=['pyserial'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Topic :: Communications',
    'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)
