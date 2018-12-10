#
# lab16
#    created by: Alejandro Caicedo
#    created by: Ivan Alejandre 




#
# get_headlines()
#    returns raw headlines contained in news containers in BBC page 
def get_headlines():
  import os
  localUrl = r'/home/captain/CSUMB/CST205/JES_workspace/lab 16/BBC-Homepage.html'
  
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
  return outputHeadlines  

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

# find_all_occurances(subStr, mainStr)
#   find ALL occurances of substring empty if no occur
def find_all_occurances_afterIndicies(subStr, mainStr, indicAry):
  allOccur = list()
  for i in range(0, len(indicAry)):
    allOccur.append(find_nextOccuranceOfSubstring( subStr, mainStr , indicAry[i] + 1))
  return allOccur
    
#
#find_nextOccuranceOfSubstring
#  returns index after next occurance of substr or -1 if not found
def find_nextOccuranceOfSubstring(subStr, mainStr, currLoc = 0):
  try:
    return mainStr.index(subStr, currLoc) 
  except:
    return -1




















