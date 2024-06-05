import os
import pyterrier as pt

data_dir = os.path.normpath(os.getcwd() + os.sep + os.pardir) + "\\AP_collection\\coll"
index_dir = os.path.normpath(os.getcwd() + os.sep + os.pardir) + "\\index\\files"

pt.init()
# list of filenames to index
files = pt.io.find_files(data_dir)

# build the index
indexer = pt.TRECCollectionIndexer(index_dir, verbose=True, blocks=True, overwrite=True)
indexref = indexer.index(files)

# load the index, print the statistics
index = pt.IndexFactory.of(indexref)
print(index.getCollectionStatistics().toString())