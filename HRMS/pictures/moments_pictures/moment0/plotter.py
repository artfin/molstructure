from __future__ import print_function

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times'
#mpl.rcParams['text.latex.preamble'] = [
    #r"\usepackage{amsmath}"
#]

mpl.rcParams['figure.titlesize'] = "xx-large"
mpl.rcParams['legend.fontsize'] = "large"
mpl.rcParams['axes.labelsize'] = "x-large"
mpl.rcParams['axes.titlesize'] = "large"

mpl.rcParams['xtick.labelsize'] = "large"
mpl.rcParams['ytick.labelsize'] = "large"

def read_data(filename):

    with open(filename, mode = 'r') as inputfile:
        lines = inputfile.readlines()
    
    temperatures = []
    moments = []

    for line in lines:
        
        data = line.split()
        
        if len(data) > 1:
            
            temperatures.append(float(data[0]))
            moments.append(float(data[1]))

    return temperatures, moments

# long range
temperatures_t_lr, moments_t_lr = read_data('ab_init_lr_1.txt')
temperatures_t_ab, moments_t_ab = read_data('ab_init_new_ab_init.txt')
temperatures_e, moments_e = read_data('experiment.txt')

temperatures_e1 = [temperatures_e[0], temperatures_e[2]]
moments_e1 = [moments_e[0], moments_e[2]]

temperatures_e2 = [temperatures_e[1], temperatures_e[3]]
moments_e2 = [moments_e[1], moments_e[3]]

fig = plt.figure()

lw = 1.75
#plt.title(r'\Large \textbf{Temperature dependence of zeroth spectral moment}')

plt.xlim((0, 500))
plt.ylim((0, 0.0008))

plt.xlabel(r'\textbf{T}, (K)')
plt.ylabel(r'\textbf{M}$_0$, (cm$^{-1}$ $\cdot$ amagat$^{-1}$)')

marker_size = 50
l1, = plt.plot(temperatures_t_lr, moments_t_lr, color = '0.3', linestyle = 'solid', linewidth = lw)
l2, = plt.plot(temperatures_t_ab, moments_t_ab, color = '0.3', linestyle = 'dashed', linewidth = lw)
e1 = plt.scatter(temperatures_e1, moments_e1, color = 'k', marker = '^', s = marker_size)
e2 = plt.scatter(temperatures_e2, moments_e2, color = 'k', marker = 's', s = marker_size)

fig.legend((l1, l2, e1, e2), ('Long-Range dipole', r'\textit{Ab Initio} \ dipole', r'I. R. Dagg \textit{et al.} [8]', r'M. V. Tonkov [9]'), 'lower center', ncol = 4, fancybox = True, shadow = True)

#fig.legend((l1, l2, e1, e2), ('Long-Range dipole', 'Ab Initio Dipole', r'I. R. Dagg \textit{et al.}, \textit{Can. J. Phys.} \textbf{64}, 1485, (1986)', r'M. V. Tonkov In: \textit{Collision- and Interaction-Induced Spectroscopy}. Kluwer, AP, 1995'), 'lower center',  ncol = 3, fancybox = True, shadow = True, prop = {'size': 'large'}) 


plt.grid(linestyle = ':', alpha = 0.7)
plt.tight_layout()
#plt.savefig('_version.png')
plt.show()
