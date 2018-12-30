import numpy as np

# Variables Initialization
VarMin = -10 	# Lower Bound
VarMax = +10 	# Upper Bound
Dim = 5 		# dimension for PSO 
GlobalBestCost = 100000000000 # Random Large Number

# PSO parameters
global nPop
global Maxit
Maxit = 50		# Maximum iteration
nPop = 100	    # Population size
w = 1 			# Inertia coefficient
damp = 0.99		# Damping ration of inertia
c1 = 2			# Personal acceleration coefficient
c2 = 2 			# Social acceleration coefficient

# Objective Function
def Cost(arr):
	return sum(np.multiply(arr, arr))

# Template
class empty_particle:

	def __init__(self):
		self.position = np.array([])
		self.velocity = np.array([])
		self.cost = np.array([])
		self.best = self.Best()
	
	class Best:
		def __init__(self):
			self.position = np.array([])
			self.cost = np.array([])

	@classmethod
	def reshape(cls, self):
		global VarMin
		global VarMax	
		global GlobalBestCost
		global GlobalBestPosition
		global Dim
		for i in range(0, Dim):
			# Generate Random Solution 
			self.position = np.append(self.position, np.random.uniform(VarMin, VarMax))
			self.velocity = np.append(self.velocity, 0)
		# Evaluation of Cost
		self.cost = Cost(self.position)
		# Update Personal Best
		self.best.position = self.position
		self.best.cost = self.cost
		# Update Global Best
		if self.best.cost < GlobalBestCost:
			GlobalBestCost = self.best.cost
			GlobalBestPosition = self.best.position

# PSO Initialization
particle = [empty_particle() for i in range(0, nPop)]
for i in range(0, nPop):
	empty_particle.reshape(particle[i])
	print i, ": ",particle[i].position, particle[i].cost

# Main Loop
for i in range(0, Maxit):
	for j in range(0, nPop):
		# Update Velocity
		a = particle[j].velocity
		b_1 = np.random.uniform(Dim)
		b_2 = particle[j].best.position - particle[j].position
		c_1 = np.random.uniform(Dim)
		c_2 = GlobalBestPosition - particle[j].position

		particle[j].velocity = w*a \
					+ c1*np.multiply(b_1, b_2) \
					+ c2*np.multiply(c_1, c_2) 
		
		# Update Position
		particle[j].position = particle[j].position \
					+ particle[j].velocity

		# Evaluation of Cost
		particle[j].cost = Cost(particle[j].position)

		# Update Personal Best
		if particle[j].cost < particle[j].best.cost:
			particle[j].best.cost = particle[j].cost
			particle[j].best.position = particle[j].position

		# Update Global Best
		if particle[j].best.cost < GlobalBestCost:
			GlobalBestCost = particle[j].best.cost
			GlobalBestPosition = particle[j].best.position

		# Best Cost
	print "Iteration = ", i, ": Best Cost", GlobalBestCost, GlobalBestPosition

	# Damping Inertia
	w = w*damp