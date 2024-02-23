from util import readFromTXTFileAndGenerateArray, writeToFile
import re, os, sys

DIR_PATH = "/Users/efecini-plentific/Desktop/bip-0039:turkish.txt/"
INPUT_FOLDER = 'TXT_FILES_INPUT/'
OUTPUT_FOLDER = 'TXT_FILES_OUTPUT/'
HELPER_FOLDER = 'HELPER_FILES/'
def getWordsFromInputFileAndGenerateArray(filename):
  try:
    return readFromTXTFileAndGenerateArray(DIR_PATH+INPUT_FOLDER+filename)
  except FileNotFoundError:
    print("Dosya bulunamadı.(Dosya uzantısını da yazdınız mı?)")
  except Exception as e:
    print(f"HATA. {e}")

def removeDuplicatesAndFalsyWordsAndSort(arr):
  arr2 = []
  for obj in arr:
    # Remove lines containing non-English alphabet characters and 'x', 'w', 'q'
    if re.search(r'[^a-zA-Z\s]', obj) or any(char in obj for char in [' ', 'x', 'w', 'q']):
      print('ERROR. Contains a non-english letter, sign or a blank character:', obj)
      continue
    elif len(obj)<3 or len(obj)>8:
      print('ERROR. Length:', str(len(obj)), obj)
      continue
    else:
      arr2.append(obj.lower())
  arr2 = list(set(arr2))
  arr2.sort()
  return arr2

def checkFirst4Letters(arr):
  arr_ = []
  seen_prefixes = set()
  for obj in arr:
    if len(obj)==3:
      prefix = obj+" "
    else:
      prefix = obj[:4]

    if prefix not in seen_prefixes:
      arr_.append(obj)
      seen_prefixes.add(prefix)
  return arr_

def checkWithOtherSeeds(arr):
  arr_not_to_be_added = set()
  arr_to_be_added = []
  arr_all = readFromTXTFileAndGenerateArray(DIR_PATH+HELPER_FOLDER+'allseed.txt')
  for a in arr:
    for a_all in arr_all:
      a_ = a
      a_all_ = a_all
      if len(a) == 3:
        a_ = a + ' '
      if len(a_all) == 3:
        a_all_ = a_all + ' '
      if a_[:4] == a_all_[:4]:
        arr_not_to_be_added.add(a)
  
  arr_to_be_added = list(set(arr) - set(arr_not_to_be_added))
  print('Failed while comparing with other seeds:',arr_not_to_be_added)
  print('Passed while comparing with other seeds:', arr_to_be_added)
  return arr_to_be_added

def checkWithOtherTurkishSeeds(arr):
  arr_not_to_be_added = set()
  arr_to_be_added = []
  arr_all = readFromTXTFileAndGenerateArray(DIR_PATH+HELPER_FOLDER+'final.txt')
  for a in arr:
    for a_all in arr_all:
      a_ = a
      a_all_ = a_all
      if len(a) == 3:
        a_ = a + ' '
      if len(a_all) == 3:
        a_all_ = a_all + ' '
      if a_[:4] == a_all_[:4]:
        arr_not_to_be_added.add(a)
  
  arr_to_be_added = list(set(arr) - set(arr_not_to_be_added))
  print('Failed while comparing with other Turkish seeds:',arr_not_to_be_added)
  print('Passed while comparing with other Turkish seeds:', arr_to_be_added)
  return arr_to_be_added

def createOutputFile(filename, arr):

  if not os.path.exists(DIR_PATH+OUTPUT_FOLDER):
    os.mkdir(DIR_PATH+OUTPUT_FOLDER)

  from datetime import datetime
  with open(DIR_PATH+OUTPUT_FOLDER+filename+''+'_'+datetime.now().strftime("%H:%M:%S")+'.txt', 'w') as output_file:
    for a in sorted(arr):
      output_file.write(a+'\n')

def getFilenamesFromFolder():
  dir_path = DIR_PATH+INPUT_FOLDER
  res = []

  # Iterate directory
  for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
  if len(res)==0:
    print('There is no file in the '+dir_path+' folder.\nProcess is stopped.')
    sys.exit()
  return sorted(res)