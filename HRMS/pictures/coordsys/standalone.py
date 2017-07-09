#!/usr/bin/python
import subprocess

cmd1 = 'pdflatex coordsys.tex'
cmd2 = 'pdftops -eps coordsys.pdf'
cmd3 = 'convert -density 600 coordsys.eps coordsys.png'

subprocess.call([cmd1], shell = True)
subprocess.call([cmd2], shell = True)
subprocess.call([cmd3], shell = True)


