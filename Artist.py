#Artist Class
import requests

class Artist:
	def __init__(self, ArtistName):
		self._ArtistName = ArtistName
		self._ArtistID = requests.get("https://api.spotify.com" + "/v1/search", 
		params = {"q":ArtistName, "type":"artist","limit":"1"}).json()["artists"]["items"][0]["id"]
	def __hash__(self):
		return hash((self._ArtistName, self._ArtistID))
	def __eq__(self, other):
		return((self._ArtistName, self._ArtistID) == (other._ArtistName, other._ArtistID))
	def __ne__(self, other):
		return not((self._ArtistName, self._ArtistID) == (self._ArtistName, self._ArtistID))
	def __repr__(self):
		return("Artist(" + self._ArtistName +","+ self._ArtistID + ")")

	def getName(self):
		return self._ArtistName
	# def serialize(self):
	# 	return self._ArtistName

	def getRelatedArtists(self):
		r = requests.get("https://api.spotify.com/v1/artists/" + self._ArtistID + "/related-artists",
				   params = {"q":self._ArtistName,"type":"artist","limit":"1"})

		relatedList = []
		for artist in r.json()['artists']:
			relatedList.append(artist['name'].replace(' ', '+'))

		return relatedList
