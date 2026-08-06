from setuptools import setup

setup(name='ldsc',
      version='1.0',
      description='LD Score Regression (LDSC)',
      url='http://github.com/bulik/ldsc',
      author='Brendan Bulik-Sullivan and Hilary Finucane',
      author_email='',
      license='GPLv3',
      packages=['ldscore'],
      scripts=['ldsc.py', 'munge_sumstats.py', 'make_annot.py'],
      python_requires='>=3.11',
      install_requires = [
            'bitarray>=2.9,<4',
            'pybedtools>=0.12,<1',
            "scipy>=1.13,<2; python_version < '3.14'",
            "scipy>=1.18,<2; python_version >= '3.14'",
            "numpy>=2.4,<3; python_version < '3.14'",
            "numpy>=2.5,<3; python_version >= '3.14'",
            'pandas>=2.2,<4',
            'pytest>=7'
      ]
)
