import sys
import json

def hw(tweet_file,sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    responses = []
    for line in tweet_file:
        if line.startswith('{"delete"'):
            pass
        else:
            responses.append(json.loads(line))
    results = []
    for response in responses:
        results.append(response['text'])
    tweet_scores = []
    new_sent_scores = {}
    for result in results:
        total = 0
        words = combos(result)
        for word in words:
            if word in scores.iterkeys():
                total += scores[word]
        tweet_scores.append([(total),words])
        for word in words:
            if word.isalpha():
                word = word.lower()
                if word not in scores.iterkeys():
                    if word not in new_sent_scores.iterkeys():
                        if tweet_scores[-1][1] != 0:
                            new_sent_scores[word] = tweet_scores[-1][0]/float(len(tweet_scores[-1][1]))
                        else:
                            new_sent_scores[word] = .0125
                    else:
                        if tweet_scores[-1][0] > 0:
                            new_sent_scores[word] += .125
                        if tweet_scores[-1][0] < 0:
                            new_sent_scores[word] += -.125
                        if tweet_scores[-1][0] == 0:
                            new_sent_scores[word] += .01              
        for key,value in new_sent_scores.iteritems():
            print key,value
                                                                
    
    

def combos(text):
    input_list = text.split()
    return input_list       

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #sent_file = open("AFINN-111.txt")
    #tweet_file = open("problem_1_submission.txt")
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(tweet_file,sent_file)

if __name__ == '__main__':
    main()
