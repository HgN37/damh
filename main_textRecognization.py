from textDetection import textDetection

test = textDetection('./text.jpg')
test.getTextCandidate()
result = test.letterClassify()
test.showCandidate()
test.textReconstruct()
