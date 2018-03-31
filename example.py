import clt_demo as clt
import numpy as np

def run():
	# CLT works for any distribution, we use standard t distribution for illustration
	distr = np.random.standard_t(10, size=10000)
	clt.plot_distribution(distr, "Population distribution", num_bins = 50)
	# sample_size --> infinity
	sample_sizes = [3, 5, 10, 15, 20, 30]
	demo = clt.CLTDemo(distr)
	for n in sample_sizes:
		demo.run_demo(n)