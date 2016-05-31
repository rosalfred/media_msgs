## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['smarthome_media_msgs'],
    package_dir={'': 'script'},
    requires=['std_msgs', 'rospy'])

setup(**setup_args)
