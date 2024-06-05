import os
import pyterrier as pt


os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
pt.init()


index_dir = '/home/ehengirmen/github/ceng596-termproject/ceng596/index/files/'
index = pt.IndexFactory.of(index_dir)

bm25 = pt.BatchRetrieve(index, wmodel="BM25")
tfidf = pt.BatchRetrieve(index, wmodel="TF_IDF")


def search_query(query):
    results = bm25.search(query)
    print(results)
    best_20 = [i for i in results[:20]['docno']]
    return best_20




