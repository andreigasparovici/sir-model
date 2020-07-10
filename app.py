import numpy as np
import matplotlib.pyplot as plt

class SIR:
	def __init__(self, beta, gamma, S0, I0, R0):
		self.beta = beta
		self.gamma = gamma

		self.S0 = S0
		self.I0 = I0
		self.R0 = R0

	# Euler method for ODE 
	def euler(v0, F, hmax, step=.1):
		h = 0
		u = v0

		while h <= hmax:
			v = u + h * F(u)
			u = v

			yield h, v

			h += step

	def plot(self, days=7, imgfile='sir.png'):
		v0 = np.array([self.S0, self.I0, self.R0])

		# Population size
		N = sum(v0)

		# Kermack-McKendrick model ODE system
		def F(v):
			S, I, R = v 
			return np.array([
					-self.beta * S * I,
					self.beta * S * I - self.gamma * I,
					self.gamma * I
			])

		Sy, Iy, Ry, X = [], [], [], []

		for h, v in SIR.euler(v0, F, hmax=days):
			S, I, R = v

			X.append(h)

			Iy.append(I)
			Sy.append(S)
			Ry.append(R)

		# Percentage normalization
		def normalize(Y):
			return [y / N * 100 for y in Y]

		# Plot data
		plt.plot(X, normalize(Sy), color='gray')
		plt.plot(X, normalize(Iy), color='red')
		plt.plot(X, normalize(Ry), color='green')

		plt.xlabel('day')
		plt.ylabel('% population')

		plt.legend(['Susceptible', 'Infected', 'Recovered'], frameon=False, loc='upper center', ncol=3)
		plt.title('SIR model for $\\beta$={}, $\\gamma$={}, {} days'.format(self.beta, self.gamma, days))

		plt.savefig(imgfile)
		

# Example
if __name__ == '__main__':
	m = SIR(beta=.001, gamma=.001, S0=5, I0=1, R0=0)
	m.plot(days=30)
