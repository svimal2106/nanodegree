import json
import logging
import pprint
import requests
from functools import reduce

logging.basicConfig()
logger = logging.getLogger(__name__)

levelMapping = {"mild": 0, "strong": 1}

class ProfanityEditor:
    def __init__(self, filterLevel, fileName):
        self.filterLevel = filterLevel
        with open(fileName, 'r') as file:
            self.profaneWordsDict = json.load(file)

        for key in self.profaneWordsDict.keys():
            if levelMapping[key] < self.filterLevel:
                del self.profaneWordsDict[key]

        print self


    def containsProfaneWords(self, emailContent):
        return len(self.findProfaneWords(emailContent)) > 0

    def findProfaneWords(self, words):
        foundProfaneWords = []
        for word in words:
            for key in self.profaneWordsDict.keys():
                if word in self.profaneWordsDict[key]:
                    foundProfaneWords.append(word)
        return foundProfaneWords


def profanityEditorOnline(wordList):
    r = requests.get('http://www.wdylike.appspot.com/?q=' + wordList)
    if r.content == "true":
        return True
    else:
        return False

def readFileContentString(fileName):
    wordList = readFileContent(fileName)
    return ' '.join(wordList)

def readFileContent(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    words = [line.strip().split() for line in lines]
    return reduce((lambda x, y: x + y), words)

if __name__ == "__main__":
    emailFileList = ["email_sample.txt", "email_sample_1.txt", "email_sample_2.txt"]
    profaneWordsFile = "profane_words.json"
    pp = pprint.PrettyPrinter()
    profanityEditor = ProfanityEditor(1, profaneWordsFile)
    for emailFile in emailFileList:
        fileContent = readFileContentString(emailFile)
        if profanityEditorOnline(fileContent):
            print "Email ", emailFile, "contains profane words => "
        # profaneWords = profanityEditor.findProfaneWords(fileContent)
        # if len(profaneWords) > 0:
        #     print "Email ", emailFile, "contains profane words => ", pp.pformat(profaneWords)
        # else:
        #     print "Email ", emailFile, " is clean"
