from distutils.core import setup, Extension

module1 = Extension('getch',
                    include_dirs = ['/usr/local/include', '/usr/include'],
                    library_dirs = ['/usr/local/lib', '/usr/lib'],
                    sources = ['getchmodule.c'])

setup(name='getch',
      version='1.0',
      description='Does single char input, like C getch/getche',
      long_description='''The getch module does single-char input by
providing wrappers for the conio.h library
functions getch() and getche(), if conio.h
does not exist, it uses a stub-library using
termios.h and other headers to emulate this
behaviour.''',
      ext_modules=[module1])
