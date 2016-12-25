import math as m
import numpy as np

h = 6.62607 * 10**(-34)
c = 2.99792 * 10**(10)
amu = 1.66054 * 10**(-27)

class Particle(object):

	atoms = {"F" : 19, "C" : 12, "H" : 1, "O" : 16}

	def __init__(self, x, y, z, name = None):
		self.x = x * 10**(-10)
		self.y = y * 10**(-10)
		self.z = z * 10**(-10)
		self.name = name

		self._set_mass()

	def _print_coordinates(self):
		print "atom: {0}; x: {1}; y: {2}; z: {3}".format(self.name, self.x * 10**(10), self.y * 10**(10), self.z * 10**(10))

	def _set_mass(self):
		for atom in self.atoms:
			if self.name == atom:
				self.m = self.atoms.get(atom) * amu

class Molecule(object):
	def __init__(self, molecule_name):
		self.molecule_name = molecule_name
		self.atoms = self._read_xyz_file()

		com = self._calculate_COM()
		self.COM = Particle(com[1], com[2], com[3], 'COM')
		self.COM._print_coordinates()

		for atom in self.atoms:
			atom.x = atom.x - self.COM.x
			atom.y = atom.y - self.COM.y
			atom.z = atom.z - self.COM.z

		self.inertia_tensor = self._inertia_tensor()
		eigvals, eigvecs = np.linalg.eig(self.inertia_tensor)
		print "tensor inertia eigenvalues: {0}".format(eigvals)
		
		rotational_constants = self._rotational_constants(eigvals)
		print "rotational_constants: {0} (in MHz)".format(rotational_constants)

		self._rotate_molecule()

	def _read_xyz_file(self):

		particles = []

		with open(self.molecule_name, mode = 'r') as inputfile:
			data = inputfile.readlines()
			
			for line in data:
				line = line.split()
	
				if len(line) == 4:
					particle = Particle(float(line[1]), float(line[2]), float(line[3]), line[0])
					particles.append(particle)

		return particles

	def _calculate_COM(self):
		total_mass = sum([atom.m for atom in self.atoms])
		x_com = sum([atom.m * atom.x for atom in self.atoms]) / total_mass
		y_com = sum([atom.m * atom.y for atom in self.atoms]) / total_mass
		z_com = sum([atom.m * atom.z for atom in self.atoms]) / total_mass

		return [total_mass, x_com * 10**(10), y_com * 10**(10), z_com * 10**(10)]

	def _inertia_tensor(self):

		Ixx = sum([atom.m * (atom.y ** 2 + atom.z ** 2) for atom in self.atoms])
		Iyy = sum([atom.m * (atom.x ** 2 + atom.z ** 2) for atom in self.atoms])
		Izz = sum([atom.m * (atom.x ** 2 + atom.y ** 2) for atom in self.atoms])
		Ixy = - sum([atom.m * atom.x * atom.y for atom in self.atoms])
		Ixz = - sum([atom.m * atom.x * atom.z for atom in self.atoms])
		Iyz = - sum([atom.m * atom.y * atom.z for atom in self.atoms])

		return np.mat([[Ixx, Ixy, Ixz], [Ixy, Iyy, Iyz], [Ixz, Iyz, Izz]])

	def _rotate_molecule(self):

		inertia_tensor = self._inertia_tensor()

		for i in range(len(inertia_tensor)):
			for j in range(len(inertia_tensor[i])):
				inertia_tensor[i][j] = inertia_tensor[i][j] / amu * 10**(20)

		eigvals, eigvecs = np.linalg.eig(inertia_tensor)

		eigvecs = self._swap_rows(eigvecs, 0, 0)

		xyzFile = open('ch2f2_rotated.xyz', mode = 'w')

		xyzFile.write(str(len(self.atoms)) + '\n\n')

		for atom in self.atoms:

			vec = np.array( [atom.x * 10**(10), atom.y * 10**(10), atom.z * 10**(10)] )
			vec_rotated = eigvecs.dot(vec)
			
			xyzFile.write(atom.name)
			xyzFile.write(self._needed_space_first(vec_rotated[0, 0]))
			xyzFile.write(self._needed_space_second(vec_rotated[0, 1]))
			xyzFile.write(self._needed_space_second(vec_rotated[0, 2]) + '\n')

		xyzFile.close()

	def _swap_rows(self, matrix, n, m):

		temp = np.copy(matrix[n, :])
		matrix[n, :] = matrix[m, :]
		matrix[m, :] = temp

		return matrix

	def _needed_space_first(self, value):
		if value < 0:
			return ' '*9 + str.format("{0:.5f}", value)
		else:
			return ' '*10 + str.format("{0:.5f}", value)

	def _needed_space_second(self, value):
		if value < 0:
			return ' '*7 + str.format("{0:.5f}", value)
		else:
			return ' '*8 + str.format("{0:.5f}", value)

	def _rotational_constants(self, eigvals):

		#inverse_constants = [(8 * m.pi ** 2 * val * c) / h for val in eigvals] in cm^(-1)
		inverse_constants = [(8 * m.pi ** 2 * val * 10**(6)) / h for val in eigvals] # in MHz
		return [1 / val for val in inverse_constants]
	
molecule = Molecule("ch2f2.xyz")
#molecule = Molecule("dimethylether.xyz")