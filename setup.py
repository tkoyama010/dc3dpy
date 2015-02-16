from setuptools import setup, find_packages

setup(name='dc3dpy',
      version='0.0.1',
      description='Python wrapper for dc3d',
      author='Tetsuo Koyama',
      author_email='tkoyama010@gmail.com',
      url='https://tkoyama010@bitbucket.org/tkoyama010/dc3dpy.git',
      packages=find_packages(),
      entry_points="""
      [console_scripts]
      greet = dc3dpy.dc3dpy:main
      """,)
