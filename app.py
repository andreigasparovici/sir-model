import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class SIRD:
	def __init__(self, beta, gamma, mu, S0, I0, R0):
		self.beta = beta
		self.gamma = gamma
		self.mu = mu

		self.v0 = np.array([S0, I0, R0, 0])
		self.N = sum(self.v0)

	# SIRD model ODE system
	def F(self, v):
		S, I, R, D = v 
		return np.array([
				-self.beta * I * S / self.N,
				self.beta * I * S / self.N - self.gamma * I - self.mu * I,
				self.gamma * I,
				self.mu * I,
		])

	def plot(self, days, filename=None):
		self.v = self.v0
		self.u = self.v0

		X, Y = [], []

		fig, ax = plt.subplots()
		ax.set_xlim(0, days)
		ax.set_ylim(0, self.N)
		
		S_line, = ax.plot(0, 0, color='#4FA1E4')
		I_line, = ax.plot(0, 0, color='#FE2020')
		R_line, = ax.plot(0, 0, color='#40D752')
		D_line, = ax.plot(0, 0, color='#000000')

		def euler(h):
			self.v = self.u + h * self.F(self.u)
			self.u = self.v

			S, I, R, D = self.v

			X.append(h)
			Y.append((S, I, R, D))
			Yt = np.transpose(Y)

			S_line.set_xdata(X)
			S_line.set_ydata(Yt[0])

			I_line.set_xdata(X)
			I_line.set_ydata(Yt[1])

			R_line.set_xdata(X)
			R_line.set_ydata(Yt[2])

			D_line.set_xdata(X)
			D_line.set_ydata(Yt[3])

			return S_line, I_line, R_line, D_line,

		anim = FuncAnimation(fig, func=euler, frames=np.arange(0, days, .1), interval=100, repeat=False)

		plt.xlabel('Day')
		plt.ylabel('% Population')

		plt.legend(['Susceptible', 'Infected', 'Recovered', 'Deceased'], frameon=False, loc='upper center', ncol=4)
		plt.title('SIRD model')

		if filename:
			anim.save(filename, writer='imagemagick', fps=60)
		else:
			plt.show()
		

# Example
if __name__ == '__main__':
	m = SIRD(beta=.1, gamma=.01, mu=.001, S0=500, I0=100, R0=40)
	m.plot(days=7, filename='anim.gif')
