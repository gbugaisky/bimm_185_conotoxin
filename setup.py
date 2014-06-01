from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = {"packages": ['scipy', 'scipy.special'],
				"include_files": [".\classifier.pkl", ".\mass_isoElectricPoint_cysAvg.csv"],
				"includes": [],
				"excludes": ["C:\python27\lib\site-packages\matplotlib\mpl-data\sample_data\*"],
        "namespace_packages": ['mpl_toolkits'] }

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('conoGUI.py',
    			base=base,
    			)
]

import os, glob2, numpy, scipy
explore_dirs = [os.path.dirname(numpy.__file__), os.path.dirname(scipy.__file__)]

files = []
for d in explore_dirs:
    files.extend( glob2.glob( os.path.join(d, '**', '*.pyd') ) )

for f in files:
    fn = f.split('C:\\Python27\\lib\\site-packages\\',1)[1].replace('\\','.').split('.pyd',1)[0]
    buildOptions["includes"].append(fn)

setup(name='ConoPredict',
      version = '1.0',
      description = 'This program uses classification algorithms to predict what pharma family a Conotoxin will fall into',
      options = {"build.exe": buildOptions},
      executables = executables)

# ("C:\python27\lib\site-packages\scipy\special\_ufuncs.pyd", "_ufuncs.pyd")