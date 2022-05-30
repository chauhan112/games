import dill as pickle
import os
import gzip

class Serializationer:
    def pickleOut(dataStructure, outFileName):
        data = pickle.dumps(dataStructure)
        dataCompressed = gzip.compress(data)
        with open(outFileName, "wb") as f:
            f.write(dataCompressed)

    def readPickle(filePath):
        with open(filePath, "rb") as f:
            binValCompressed = f.read()
        try:
            binVal = gzip.decompress(binValCompressed)
        except:
            binVal = binValCompressed
        return pickle.loads(binVal)