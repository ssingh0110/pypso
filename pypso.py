import numpy as np
import matplotlib.pyplot as plt

# Variables Initialization
VarMin = -10 	# Lower Bound
VarMax = +10 	# Upper Bound
Dim = 5 		# dimension for PSO 
GlobalBestCost = 1000000000000000000000000000000 # Random Large Number
RecordedBestCost = []
# PSO parameters
global nPop
global Maxit
Maxit = 1000	# Maximum iteration
nPop = 50	    # Population size
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
			#print GlobalBestPosition
			#print GlobalBestCost

# PSO Initialization
particle = [empty_particle() for i in range(0, nPop)]
for i in range(0, nPop):
	empty_particle.reshape(particle[i])
	#print i, ": ",particle[i].velocity

# Plotting Results
def plot(arr):
	plt.semilogy(arr)
	plt.grid(b=bool, which="both", axis="both", color = 'g', linestyle = '--')
	plt.xlabel("Iteration")
	plt.ylabel("Best Cost")
	plt.title("PSO Implementation in Python")
	plt.savefig('BestCost.png')
	plt.show(block=False)
	plt.pause(5)
	plt.close()

# Main Loop
for i in range(0, Maxit):
	for j in range(0, nPop):
		# Update Velocity
		a = particle[j].velocity
		b_1 = np.random.rand(Dim)
		b_2 = particle[j].best.position - particle[j].position
		c_1 = np.random.rand(Dim)
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
	print "Iter: %d"%i, " Best Cost: ", GlobalBestCost
	#print "Best Position: ",GlobalBestPosition
	RecordedBestCost.append(GlobalBestCost)
	# Damping Inertia
	w = w*damp

# Calling Plot Function
plot(RecordedBestCost)