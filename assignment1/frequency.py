# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 16:42:50 2014

@author: lagosaurusrex
"""
import sys
import json

def frequency(tweet_file):
    responses = []
    for line in tweet_file:
        if line.startswith('{"delete"'):
            pass
        else:
            responses.append(json.loads(line))
    results = []
    for response in responses:
        results.append(response['text'])
    frequencies = {}
    for result in results:
        words = result.split()
        for word in words:
            if word.isalpha():
                if word not in frequencies.iterkeys():
                    frequencies[word] = 1
                else:
                    frequencies[word] += 1
    total_words = sum(frequencies.itervalues())
    for key, value in frequencies.iteritems():
        print key, float(value)/float(total_words)
                
        
        

def main():
    #tweet_file = open('problem_1_submission.txt')
    tweet_file = open(sys.argv[1])
    frequency(tweet_file)

if __name__ == '__main__':
    main()