#!/usr/bin/python
# -*- coding: utf-8 -*-

values = []
weights = []

o = {}

def O(capacity, items):
	global values, weights, o

	if capacity in o:
		if items in o[capacity]:
			return o[capacity][items]
	else:
		o[capacity] = {}

	if capacity < 1:
		return 0
	if items < 1:
		return 0
	if weights[items-1] > capacity:
		value = O(capacity, items-1)
	else:
		value1 = O(capacity, items-1)
		value2 = O(capacity-weights[items-1], items-1) + values[items-1]
		value = max(value1, value2)

	o[capacity][items] = value
	return value

def solveIt(inputData):
	global values, weights

	# parse the input
	lines = inputData.split('\n')

	firstLine = lines[0].split()
	items = int(firstLine[0])
	capacity = int(firstLine[1])

	values = []
	weights = []

	for i in range(1, items+1):
		line = lines[i]
		parts = line.split()

		values.append(int(parts[0]))
		weights.append(int(parts[1]))

	items = len(values)

	value = O(capacity, items)

	weight = 0
	taken = []

	# prepare the solution in the specified output format
	outputData = str(value) + ' ' + str(1) + '\n'
	outputData += ' '.join(map(str, taken))
	return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

