import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times'
mpl.rcParams['text.latex.preamble'] = [
    r"\usepackage{amsmath}"
]

mpl.rcParams['figure.titlesize'] = "x-large"
mpl.rcParams['legend.fontsize'] = "large"
mpl.rcParams['axes.labelsize'] = "x-large"

mpl.rcParams['xtick.labelsize'] = "x-large"
mpl.rcParams['ytick.labelsize'] = "x-large"

def read_data(filename):
    
    with open(filename, mode = 'r') as inputfile:
        lines = inputfile.readlines()

    r = np.array([])
    dipz = np.array([])

    for line in lines:
        
        data = line.split()
        if len(data) > 1:

            r = np.append(r, float(data[0]))
            dipz = np.append(dipz, float(data[1]))

    return r, dipz

r_ab_initio_pi2, dipz_ab_initio_pi2 = read_data('ab_initio_pi2.txt')
r_ab_initio_pi4, dipz_ab_initio_pi4 = read_data('ab_initio_pi4.txt')
r_ab_initio_pi6, dipz_ab_initio_pi6 = read_data('ab_initio_pi6.txt')

r_lr_pi2, dipz_lr_pi2 = read_data('long_range_pi2.txt')
r_lr_pi4, dipz_lr_pi4 = read_data('long_range_pi4.txt')
r_lr_pi6, dipz_lr_pi6 = read_data('long_range_pi6.txt')

fig = plt.figure()

lw = 1.75
#plt.title(r'\Large \textbf{Z-components of dipole moment}')

plt.xlabel(r'\textbf{R, (Bohrs)}')
plt.ylabel(r'$\boldsymbol{\mu}_{\textbf{z}}$ \textbf{(a.u.)}')

color1 = '#cc2a2a'
color2 = '#2a66cc' 

lab1, = plt.plot(r_ab_initio_pi2, dipz_ab_initio_pi2, color = color1, linestyle = 'solid', linewidth = lw)
#lab2, = plt.plot(r_ab_initio_pi4, dipz_ab_initio_pi4, color = color2, linestyle = 'solid', linewidth = lw)
lab3, = plt.plot(r_ab_initio_pi6, dipz_ab_initio_pi6, color = color2, linestyle = 'solid', linewidth = lw)

llr1, = plt.plot(r_lr_pi2, dipz_lr_pi2, color = color1, linestyle = 'dashed', linewidth = lw)
#llr2, = plt.plot(r_lr_pi4, dipz_lr_pi4, color = color2, linestyle = 'dashed', linewidth = lw)
llr3, = plt.plot(r_lr_pi6, dipz_lr_pi6, color = color2, linestyle = 'dashed', linewidth = lw)

fig.legend((lab1, lab3, llr1, llr3), (r'\textit{Ab Initio}, $\Theta = \pi / 2$', r'\textit{Ab Initio}, $\Theta = \pi / 6$', r'Long-Range, $\Theta = \pi / 2$', r'Long-Range, $\Theta = \pi / 6$'), 'lower center', ncol = 4, fancybox = True, shadow = True) 

plt.tight_layout()

plt.grid(linestyle = ':', alpha = 0.7)
plt.show()




