# latex-to-svg
Visit wiki for demo.
This program takes LaTeX equations as input and output the equation as svg file. It is a command line tool made for linux machines.

Requirements 
- pdfcairo
- tikz(LaTeX package)
- standalone(LaTeX package)
- PIL package (python library)

pdfcairo, tikz and standalone are necessary. If you want scaling in your output file (which is required in blender), you may use PIL library. It is recommended that you install texlive full in linux (sudo apt install texlive -full), this will provide both tikz and standalone package.

The program to generate svg files which can be used in blender does not work till now, under development.
