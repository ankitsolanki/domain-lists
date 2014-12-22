class FileLoader:
	def __init__(self):
		print("in Cons")
		self.adj = {}
		self.noun = {}
		self.adv = {}
		self.verb = {}
		self.keeper = {}
 	def load(self,filePath):
		fileObject = {}
		file = open(filePath, 'r')
		for line in file:
			splitted_line = line.split(" ")
			synset = int(splitted_line[0])
			number_of_terms = int(splitted_line[3],16)
			flag = True
			count = 0
			pointer = 4
			terms = []
			while flag:
				if count < number_of_terms:
					terms.append(splitted_line[pointer])
					pointer = pointer + 2 
					count =  count + 1 
				else :
					flag = False

			fileObject[synset] = terms
		return fileObject
	def loadAllDictionary(self):
		self.adj = self.load("../data/data.adj")
		self.adv = self.load("../data/data.adv")
		self.noun = self.load("../data/data.noun")
		self.verb = self.load("../data/data.verb")
		print("Lookup files loaded....")

	def process(self):
		file = open("../data/domain.data", "r")
		for line in file:
			splitted_line = line.split("\t")
			synset, type = splitted_line[0].split("-")
			domains = splitted_line[1].replace("\n","").split(" ")
			domain_terms = []
			if(type == "n"):
				domain_terms = self.noun[int(synset)]
			elif(type == "v"):
				domain_terms = self.verb[int(synset)]
			elif(type == "r"):
				domain_terms = self.adv[int(synset)]
			elif(type == "a" or type == "s"):
				domain_terms = self.adj[int(synset)]
			else:
				raise Exception("The type of expression" , type)
			for domain in domains:
				if domain not in self.keeper.keys():
					self.keeper[domain] = []
				domain_terms = map(lambda x: x.replace("_" , " " ) , domain_terms)
				self.keeper[domain].extend(domain_terms)
		for key in self.keeper.keys():
			file = open("../output/"+key+".lst","w")
			for term in self.keeper[key]:
				file.write(term.strip().lower()+"\n")

	def main(self):
		self.loadAllDictionary()
		self.process()

if __name__ == "__main__":
	fileLoader = FileLoader()
	fileLoader.main()