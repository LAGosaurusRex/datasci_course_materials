# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 15:33:26 2014

@author: lagosaurusrex
"""

import sys
import json

def hw(tweet_file):
    responses = []
    for line in tweet_file:
        if line.startswith('{"delete"'):
            pass
        else:
            responses.append(json.loads(line))
    results = []
    for response in responses:
        results.append(response['entities']['hashtags'])
    hashtag_dic = {}
    total_tweets = 0
    for result in results:
        if len(result) >= 1:
            hashtag = result[0]['text'].lower()
            if hashtag not in hashtag_dic.iterkeys():
                hashtag_dic[hashtag] = 1
                total_tweets += 1
            else:
                hashtag_dic[hashtag] += 1
                total_tweets += 1
    hashtag_list = []
    for key, value in hashtag_dic.iteritems():
        hashtag_list.append([value,key])
    hashtag_list = sorted(hashtag_list)
    hashtag_list = hashtag_list[::-1]
    for i in range(10):
        print hashtag_list[i][1], hashtag_list[i][0]

def main():
    #sent_file = open('AFINN-111.txt') 
    #tweet_file = open('output.txt')
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
