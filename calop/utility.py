# coding: utf-8


import math
import scipy.stats

# --------------------------------------
# Constants
# --------------------------------------



# --------------------------------------
# Functions
# --------------------------------------
def pv_factor(r_in_pct, T = 1):
	'''
	return the present value of 1 unit of currency T year(s) from now, given the 
	continous compounded interest rate in percent form.
	'''
	return math.e ** (- r_in_pct / 100.0 * T)


# --------------------------------------
# Classes
# --------------------------------------
class Norm():
	
	def __init__(self, loc=0.0, var= 1.0):
		self.loc = 0.0
		self.var = 1.0
		self.z = 0.0
		self.rv = scipy.stats.norm(loc, var)

	def zscore(self, x):
		return (x - self.loc) / float(self.var)

	def cdf(self, x):
		return self.cdf(self.zscore(x))

	def pdf(self, x):
		return self.pdf(self.zscore(x))

# --------------------------------------
# Tests
# --------------------------------------
if __name__ == '__main__':
	assert pv_factor(1) == math.e ** (-0.01)
	assert pv_factor(3, 0.25) == math.e ** (-0.0075)
	assert pv_factor(1, 0) == 1.0
	