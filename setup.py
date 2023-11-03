from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='MedicalImageConversion',
  version='1.0.0',
  author='Vasiliy Tekhin',
  author_email='tekhinvasiliy@gmail.com',
  description='Convert medical images',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Constanter/MedicalImageConversion',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='example python',
  project_urls={
    'Documentation': 'link'
  },
  python_requires='>=3.7'
)