#
# CST 205 Lab16
#    created by: Alejandro Caicedo
#                Ivan Alejandre 
# 12/10/18


# this is the function to be called from console

def create_newSite():
  # create 'isolatedHeadlines.html' somewhere on your system, then change the
  # location in the following variable
  headlinesHTML = 'D:\Users\Ivan\Documents\school\CST 205\CST-205\mod 7\lab16HomePage\isolatedHeadlines.html'
  
  # grab headlines from our saved webpage that is bundled in the zip.
  headlines = get_headlines()
  
  # create two variables, containing generic html code to create a webpage
  openingHTML = ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01",
  "Transition//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">",
  "<html>",
  "<head><title>BBC Headlines frozen in time</title>",
  "</head>",
  "<body>",
  "<h1>"]
  closingHTML = ["</h1>", "</body>", "</html>"]
  
  # now we open our new file and write to it. close it after we're done.
  output = open(headlinesHTML, 'w')
  for line in openingHTML:
    output.write(line)
  for line in headlines:
    output.write(line + "<br>")
  for line in closingHTML:
    output.write(line)
  output.close()

#
# get_headlines()
#    returns raw headlines contained in news containers in BBC page 
def get_headlines():
  import os
  
  # change this to directory where files were extracted from zip
  localUrl = r'D:\Users\Ivan\Documents\school\CST 205\CST-205\mod 7\lab16HomePage\BBC-Homepage.html'
  
  if not os.path.exists(localUrl):
    showInformation("BBC-Homepage.html path does not extist, please enter a correct one and try again")
    return
  
  fullSite = load_fullSite(localUrl)
  #looking for "block-link__overlay-link"
  blockOccur = find_all_occurances("block-link__overlay-link", fullSite)
  #find closing bracket ">"
  nextCloseBracketOccur = find_all_occurances_afterIndicies(">", fullSite, blockOccur)
  nextOpenBracketOccur = find_all_occurances_afterIndicies("<", fullSite, nextCloseBracketOccur)
  
  outputHeadlines = list()
  for i in range(0, len(nextCloseBracketOccur)):
    outputHeadlines.append( fullSite[nextCloseBracketOccur[i]:nextOpenBracketOccur[i]] )
  
  return trim_whitespaceCharacters(outputHeadlines) 

#
# load_fullSite
#    returns HTML as 1 long string
def load_fullSite(fileLoc):
  fileObj = open(fileLoc, 'r')
  fullTxt = fileObj.read()
  fileObj.close()
  return fullTxt


#
# find_all_occurances(subStr, mainStr)
#   find ALL occurances of substring empty if no occur
def find_all_occurances(subStr, mainStr):
  currLoc = find_nextOccuranceOfSubstring(subStr, mainStr)
  locAry = list()
  while (currLoc != -1):    
    locAry.append(currLoc)
    currLoc = find_nextOccuranceOfSubstring(subStr, mainStr, currLoc + 1)
  return locAry
  
#
# find_all_occurances(subStr, mainStr)
#   find ALL occurances of substring empty if no occur
def find_all_occurances_afterIndicies(subStr, mainStr, indicAry):
  allOccur = list()
  for i in range(0, len(indicAry)):
    allOccur.append(find_nextOccuranceOfSubstring( subStr, mainStr , indicAry[i] + 1))
  return allOccur
    
#
# find_nextOccuranceOfSubstring
#   returns index after next occurance of substr or -1 if not found
def find_nextOccuranceOfSubstring(subStr, mainStr, currLoc = 0):
  try:
    return mainStr.index(subStr, currLoc) 
  except:
    return -1

#
# trim_whitespaceCharacters(headlinesIn)
#  removes unnecessary characters so we end up with just text. saves each headline
#  to an array with each string headline being its own index
def trim_whitespaceCharacters(headlinesIn):
  retArry = list()
  for hl in headlinesIn:
    startLoc = 0
    if hl.startswith('>\n'):
      startLoc = 1
    while hl[startLoc].isspace():
      startLoc = startLoc + 1
    endLoc = 0
    while hl[len(hl) - 1 - endLoc].isspace():
      endLoc = endLoc + 1

    endLoc = len(hl) - 1 - endLoc
    retArry.append( hl[startLoc:endLoc+1] )
  return retArry
    
