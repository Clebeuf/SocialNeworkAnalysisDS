#!/usr/bin/python
import sys
import re
import string
import json

rawData = open(sys.argv[1])

nodes = []
edges = []

for line in rawData:
	temp = line.split()
	if temp[0] not in nodes:
		nodes.append(temp[0])
	if temp[1] not in nodes:
		nodes.append(temp[1])
	edges.append(temp)

print "nodedef> name"

for node in nodes:
	print node

print "edgedef> node1,node2"

for edge in edges:
	print edge[0] + ',' + edge[1]