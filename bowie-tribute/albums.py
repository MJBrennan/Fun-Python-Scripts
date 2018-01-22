import os


class AlbumData:

	albumdata = []
	finaldata = []

	def __init__(self):
		self.fileNames()
		self.albumdata.sort()

	def albums(self):
		data = self.albumdata
		return data


	def fileNames(self):
		for subdir,dirs,files in os.walk('./images'):
			for file in files:
				file = "images/"+file
				self.albumdata.append(file)

