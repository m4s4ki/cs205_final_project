from mrjob.job import MRJob
#import numpy as np
#import sklearn



class MPTest(MRJob):
    def mapper(self, key, line):
        
        elements = list(line.split(","))
        text = elements[7]
        
        words = list(text.split())
        word_emotion = 0
        char_count = 0
        has_hash = False
        for w in words:
            # -- get hashtag word -- #
            if w.startswith("#"):
                has_hash = True
                yield w, 1

        
        
        
    def reducer(self, key, element):
        
        yield key, sum(element)
        
        
if __name__ == '__main__':
    MPTest.run()