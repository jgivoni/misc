#!/usr/bin/python
# -*- coding: utf-8 -*-

itemDataGlobal = []

maxValueCache = {}

def solution(capacity, items):
	global itemDataGlobal, maxValueCache

	if capacity < 1:
		this_solution = [0] * (items + 1)
		return this_solution
	if items < 1:
		this_solution = [0]
		return this_solution

	if capacity in maxValueCache:
		if items in maxValueCache[capacity]:
			return maxValueCache[capacity][items]
	else:
		maxValueCache[capacity] = {}

	this_item = itemDataGlobal[items-1]
	this_value = this_item[0]
	this_weight = this_item[1]

	if this_weight > capacity or this_value == 0:
		this_solution = solution(capacity, items-1)
		this_solution.append(0)
	else:
		this_solution1 = solution(capacity, items-1)
		this_solution1.append(0)
		this_solution2 = solution(capacity-this_weight, items-1)
		this_solution2[0] = this_solution2[0] + this_value
		this_solution2.append(1)
		if (this_solution1[0] > this_solution2[0]):
			this_solution = this_solution1
		else:
			this_solution = this_solution2

	maxValueCache[capacity][items] = list(this_solution)
	return this_solution

def solveIt(inputData):
	global itemDataGlobal, maxValueCache

	itemDataGlobal = []

	maxValueCache = {}

	# parse the input
	lines = inputData.split('\n')

	firstLine = lines[0].split()
	items = int(firstLine[0])
	capacity = int(firstLine[1])

	for i in range(1, items+1):
		line = lines[i]
		parts = line.split()

		itemDataGlobal.append((int(parts[0]), int(parts[1]), int(1000*float(parts[0])/float(parts[1]))))

	items = len(itemDataGlobal)

	# itemDataGlobal = sorted(itemDataGlobal, key=lambda item: item[1])

	this_solution = solution(capacity, items)

	value = this_solution.pop(0)
	weight = 0
	taken = this_solution

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

