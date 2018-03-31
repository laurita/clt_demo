import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class CLTDemo(object):
	
	def __init__(self, distribution):
		self.distribution = distribution

	def sample(self, n):
		x = np.random.choice(self.distribution, n)
		return x

	def run_demo(self, sample_size):
		means = []
		for i in range(1, 100):
			mean = sum(self.sample(sample_size)) / sample_size
			means.append(mean)
		ttl = "Sample mean distribution for sample size %s" % sample_size
		plot_distribution(means, ttl, num_bins = 50)

		
def plot_distribution(distribution, title, num_bins = None):

	# set style for plots
	plt.rcParams["patch.force_edgecolor"] = True
	sns.set(style="darkgrid")
	sns.set_palette("PuBuGn_d")

	if (num_bins != None):
		distr_min, distr_max = min(distribution), max(distribution)
		bin_width = (distr_max - distr_min) / num_bins
		bins = np.arange(distr_min, distr_max + bin_width, bin_width)
		plt.hist(distribution, bins=bins)
	else:
		plt.hist(distribution)

	if (title != None):
		plt.title(title)

	plt.xlabel('Observation')
	plt.ylabel('Frequency')
	plt.show()