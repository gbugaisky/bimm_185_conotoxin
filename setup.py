from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = {"packages": ['scipy'],
				"include_files": ["classifier.pkl",
				("C:\python27\lib\site-packages\scipy\special\_ufuncs.pyd", "_ufuncs.pyd")],
				"excludes": ["C:\python27\lib\site-packages\matplotlib\mpl-data\sample_data\*"] }

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('conoGUI.py', base=base)
]

setup(name='ConoPredict',
      version = '1.0',
      description = 'This program uses classification algorithms to predict what pharma family a Conotoxin will fall into',
      options = {"build.exe": buildOptions},
      executables = executables)
