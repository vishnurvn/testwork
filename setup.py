from setuptools import setup

setup(name='testwork',
      version=1.0,
      description='Test automation framework',
      author='Vishnu Raveendran',
      author_email='vishnunilambur@gmail.com',
      license='MIT',
      zip_safe=False,
      packages=['testwork'],
      install_requires=['Flask==1.1.1', 'selenium==3.141.0'])
