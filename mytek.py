#This program takes tex command as input and output svg files. You must have texlive, pdftocairo installed in our system, the program is written for linux os. Written by Sasanka Dowarah.
#This program takes tex command as input and output svg files. You must have texlive, pdftocairo installed in our system, the program is written for linux os. Written by Sasanka Dowarah.
import os
#Takes input from user.
tex_equation = input("Type equation - ")
#open files to write.
tex_file = open('tex_file.tex','w')
tex_file.writelines("\documentclass[tikz]{standalone}\n")
tex_file.writelines("\\begin{document}\n")
tex_file.writelines("\\begin{tikzpicture}\n")
tex_file.writelines("\draw[line width=0mm] (0,0) rectangle (0,0) node [midway]\n")
tex_file.writelines("{$")
tex_file.writelines(tex_equation)
tex_file.writelines("$};\n")
tex_file.writelines("\end{tikzpicture}\n")
tex_file.writelines("\end{document}\n")
tex_file.close()
#system command to compile the tex file.
os.system('pdflatex tex_file.tex')
#system command to convert the pdf file to svg file.
os.system('pdftocairo -svg tex_file.pdf output.svg')
#os.system('pdftocairo -svg tex_file.pdf output.png')
#os.system('pdftocairo -svg tex_file.pdf output.jpeg')
#os.system('pdftocairo -svg tex_file.pdf output.tirf')
#os.system('pdftocairo -svg tex_file.pdf output.ps')
#os.system('pdftocairo -svg tex_file.pdf output.eps')
os.system('rm tex_file.aux tex_file.log tex_file.pdf tex_file.tex')
os.system('exit')
print("Output is written in output.svg")

