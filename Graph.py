#Graph Class

class Graph:
	def __init__(self, graph = None):
		if graph == None:
			self._graph = {}
		else:
			self._graph = graph

	def addNode(self, artist):
		if artist not in self._graph:
			self._graph[artist] = artist.getRelatedArtists()

	def getEdges(self, artist):
		if artist in self._graph:
			return self._graph[artist]
		else:
			return None

	def getNodes(self):
		return self._graph.keys()

	def getGraph(self):
		return self._graph

	def __str__(self):
		return str(self._graph.items())

	# def serialize(self):
	# 	return self._graph


