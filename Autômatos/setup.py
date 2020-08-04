from cx_Freeze import setup, Executable

setup(name='aut',
      version='0.1',
      description='jogo da vida',
      executables = [Executable('Game_of_Life.py')])
