#!/usr/bin/python
import os
import sys
sys.path.append("./pyata")

from pyata import Pd


class ModulesList:

	def __init__(self):
		self.filenames = next(os.walk("./modules"))[2]
		self.modules = []
		for filename in self.filenames:
			f = open('./modules/' + filename)
			for line in f:
				# #X coords 0 -1 1 1 100w 200h 2 100 100;
				# module must have coords to be used?
				if line.find('coords') >= 0:
					coords = [line.split()[6], line.split()[7]]
					modules = {
						'name': filename[:-3],
						'filename': filename,
						'width': coords[0],
						'height': coords[1],
						'coords': line.split()[2:]
					}
					self.modules.append(modules)
		

ModulesList()