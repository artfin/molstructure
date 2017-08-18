import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times'

mpl.rcParams['figure.titlesize'] = "xx-large"
mpl.rcParams['legend.fontsize'] = "large"
mpl.rcParams['axes.labelsize'] = "x-large"
mpl.rcParams['axes.titlesize'] = "large"

mpl.rcParams['xtick.labelsize'] = "large"
mpl.rcParams['ytick.labelsize'] = "large"

def crop_tonkov( freqs, tonkov ):
    new_freqs = []
    new_tonkov = []

    for f, t in zip(freqs, tonkov):
	if ( f >= 20 ):
	    new_freqs.append(f)
	    new_tonkov.append(t)

    return new_freqs, new_tonkov

def crop_dagg( freqs, dagg ):
    freqs_cropped = []
    dagg_cropped = []

    freqs_dashed = []
    dagg_dashed = []

    for f, d in zip(freqs, dagg):
       if ( f >= 30 ):
          freqs_cropped.append(f)
	  dagg_cropped.append(d)

          if (f == 30 ):
              freqs_dashed.append(f)
              dagg_dashed.append(d)
       else:
	  freqs_dashed.append(f)
	  dagg_dashed.append(d)

    return freqs_cropped, dagg_cropped, freqs_dashed, dagg_dashed

def read_data(filename):

    with open(filename, mode = 'r') as inputfile:
        lines = inputfile.readlines()

    freqs = []
    
    dagg  = []
    tonkov = []

    for line in lines:
	if len(line) > 0:
	    data = line.split()

	    freqs.append(float(data[0]))
	    tonkov.append(float(data[1]))
	    dagg.append(float(data[2]))

    return freqs, dagg, tonkov

freqs, dagg, tonkov = read_data('spc.txt')

freqs_tonkov, tonkov = crop_tonkov(freqs, tonkov)
freqs_dagg_cropped, dagg_cropped, freqs_dagg_dashed, dagg_dashed = crop_dagg(freqs, dagg)

fig = plt.figure()

plt.xlabel(r'$\nu$, \textbf{cm}$^{-1}$')
plt.ylabel(r'$\alpha(\nu)$, 10$^{-6}$ \textbf{cm}$^{-1} \cdot$ \textbf{amagat}$^{-2}$') 

l1, = plt.plot(freqs_dagg_cropped, dagg_cropped, color = 'blue')
l2, = plt.plot(freqs_dagg_dashed, dagg_dashed, color = 'blue', linestyle = 'dashed')
l3, = plt.plot(freqs_tonkov, tonkov, color = 'green')

fig.tight_layout()

fig.legend((l1, l3), (r'I.R. Dagg \textit{et al.} [9]', r'M. V. Tonkov [10]'), 'lower center', ncol = 2, fancybox = True, shadow = True)

plt.grid(linestyle=':', alpha=0.7)

plt.show()
