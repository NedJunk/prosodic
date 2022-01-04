from tools import *
import sys
import pickle
sys.path.append('./')

filepath = sys.argv[1]
fileNew = open(filepath+'.pickle', 'w')
pickle.dump(loadDict(filepath), fileNew)
