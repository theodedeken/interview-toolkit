from setuptools import setup

setup(name='interview-toolkit',
      version='0.1',
      description='Scripts to generate cv and cover letter',
      url='https://github.com/theodedeken/interview-toolkit',
      author='Theo Dedeken',
      author_email='theo.dedeken@telenet.be',
      license='MIT',
      packages=['interview_toolkit'],
      scripts=['scripts/interview-toolkit'],
      include_package_data=True,
      zip_safe=False)
