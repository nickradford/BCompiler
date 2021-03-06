"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['BCompiler.py']
DATA_FILES = ['ActionTable.py', 'BParser.py', 'BScanner.py', 'Compiler.py', 'CompilerException.py', "EOFException.py", 'ExpressionParser.py', 'JavaEmitter.py', 'MyMap.py', "ParserBase.py", 'Symbol.py', 'SymbolTable.py', 'Token.py']
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
