from Graph import Graph
from Artist import Artist
import customSerializer
import json
name = "Bob+Dylan"

startArtist = Artist(name)

artistGraph = Graph()

artistGraph.addNode(startArtist)

for node in artistGraph.getEdges(startArtist):
	newArtist = Artist(node)
	artistGraph.addNode(newArtist)

allArtists = []
for node in artistGraph.getNodes():
	for related in artistGraph.getEdges(node):
		allArtists.append(related)

for musician in set(allArtists):
	newArtist = Artist(musician)
	artistGraph.addNode(newArtist)

allArtists = []
for node in artistGraph.getNodes():
	for related in artistGraph.getEdges(node):
		allArtists.append(related)
with open("spotifygraph.json","w", encoding = "utf-8") as f:
	json.dump(artistGraph, f)

#print(artistGraph)