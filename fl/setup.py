from cx_Freeze import setup, Executable

executables = [
    Executable('fl.py')
]

setup(name='hello',
      version='0.1',
      description='Sample cx_Freeze script',
      executables=executables
      )
