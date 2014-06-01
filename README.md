bimm_185_conotoxin
==================

This project is for analysis of conotoxins.
This project mainly used the following external modules (and all their dependencies):
* wxPython
* BioPython
* matplotlib
* scikit-learn

The current build is hosted on Dropbox, mainly due to being too large for Github
in its zipped form (105 MB), and being over 300 MB in its uncompressed form.
The current build is here: https://www.dropbox.com/s/lcriv3gxwsrynos/build.zip

The project right now is extremely unorganized, but this is the general
ordering of things:
* The database of conotoxins was downloaded from ConoServer.
* Various sequences for different things were pulled from the database using
the xml*Parse scripts in the consensus folder, and slightly modified depending
on the data I wanted.
* xmlMachParse script in the consensus folder was used for generating the files
in the nested MachineParse folder.  These csv files were used to try to 
find well defined clusters for the Pharmacological Groups.
* The graphResults script takes the csv files in the MachineParse directory
and graphs them using the matplotlib package.  This is a poorly written
script, various elements have to be altered in the code, rather than provided
at the command line to change what is graphed.
* The align*Fam folders in the consensus directory contain various groups of
sequences that were pulled using the xml*Parse scripts, then aligned using
Clustal Omega (not ClustalW2!).
* The *_tree.txt files are phylogenetic trees in the Newick format, generated
from ClustalW2 Phylogeny.  These can be redrawn using any tool that can
interpret the common Newick tree format.
* The __submodules__ directory is meant to contain scripts that the ConoGUI calls
to get stuff done.
* The __conotoxin __ script was the original attempt at a CLI tool, but has
since been scrapped.