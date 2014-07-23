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
    for result in results:
        total = 0
        words = combos(result,scores)
        for word in words:
            for key in scores.iterkeys():
                if word == key:
                    total += scores[word]
        tweet_scores.append(total)
    for score in tweet_scores:
        print score

def combos(text, scores):
    input_list = text.split()
    bigram_list = []
    for i in range(len(input_list)-1):
        if input_list[i] + ' ' + input_list[i+1] in scores.iterkeys():
            bigram_list.append((input_list[i] + ' ' + input_list[i+1]))
    for word_set in bigram_list:
        words = word_set.split()
        for word in words:
            input_list.remove(word)
    return input_list + bigram_list          

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #sent_file = open('AFINN-111.txt') 
    #tweet_file = open('problem_1_submission.txt')
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(tweet_file,sent_file)

if __name__ == '__main__':
    main()
