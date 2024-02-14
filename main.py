from functions import getWordsFromInputFileAndGenerateArray, removeDuplicatesAndFalsyWordsAndSort, checkFirst4Letters, checkWithOtherSeeds, createOutputFile, getFilenamesFromFolder

filesTobeTested = getFilenamesFromFolder()
print(filesTobeTested)
for index, file in enumerate(filesTobeTested):

  # Read the file and generate array
  arr = getWordsFromInputFileAndGenerateArray(file)

  # Remove duplicates and falsy words and sort
  arr = removeDuplicatesAndFalsyWordsAndSort(arr)

  # Check the first 3/4 letters and remove them if they are the same
  arr = checkFirst4Letters(arr)

  # Check with other seed words
  arr = checkWithOtherSeeds(arr)

  createOutputFile(file, arr)

  print(str(index+1)+". Process for " + file + " completed.")

print('Process is completed')