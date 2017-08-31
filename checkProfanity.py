import urllib

def readText():
    quotes = open("/Users/jostein/temp/movie_quotes.txt")
    contentOfQuotes = quotes.read()
    return contentOfQuotes

def checkProfanity(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text)
    response = connection.read()
    print(response)
    connection.close()

checkProfanity(readText())
