import os
import json

class Filehandler:
    def __init__(self):
        pass

    
    def getRealPath(self, filename):
        return f"{os.getcwd()}/{filename}"
    
   
    def writeJson(self, data, filename):
        with open(self.getRealPath(filename), "w") as file:
            json.dump(data, file, indent=4)

    
    def getJson(self, filename):
        with open(self.getRealPath(filename), 'r') as jsonFile:
            return json.load(jsonFile)[0]

    def vbsWrite(self, data, filename):
        with open(self.getRealPath(filename), 'w') as vbsFile:
            vbsFile.write(data)