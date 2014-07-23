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
        results.append(response['text'].strip())
        if response['place'] != None:
            if response['place']['country'] == 'United States':
                print response['place']['full_name'].split(",")[1]
    tweet_scores = []
    for result in results:
        total = 0
        words = combos(result.strip(),scores)
        for word in words:
            word = word.strip()
            for key in scores.iterkeys():
                if word == key:
                    total += scores[word]
        tweet_scores.append([(total),words])
    new_sent_scores = {}
    for i in xrange(len(tweet_scores)):
        if tweet_scores[i][0] > 0:
            for word in tweet_scores[i][1]:
                word = word.replace('"','')
                if word.isalpha():
                    if word not in new_sent_scores:
                        if word in scores.iterkeys():
                            new_sent_scores[word] = scores[word]
                        if word not in scores.iterkeys():
                            new_sent_scores[word] = 1
                    else:
                        new_sent_scores[word] += .25
        if tweet_scores[i][0] > 0:
            for word in tweet_scores[i][1]:
                word = word.replace('"','')
                if word.isalpha():
                    if word not in new_sent_scores:
                        if word in scores.iterkeys():
                            new_sent_scores[word] = scores[word]
                        if word not in scores.iterkeys():
                            new_sent_scores[word] = -1
                    else:
                        new_sent_scores[word] -= .25
        if tweet_scores[i][0] == 0:
            for word in tweet_scores[i][1]:
                word = word.replace('"','')
                bleh = []
                if word.isalpha():
                    bleh.append(word)
                    if word not in new_sent_scores:
                        if word in scores.iterkeys():
                            new_sent_scores[word] = scores[word]
                        if word not in scores.iterkeys():
                            new_sent_scores[word] = .125
                    else:
                        new_sent_scores[word] += .125
    for key, value in new_sent_scores.iteritems():
        pass
        #print key, value
            

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
    sent_file = open("AFINN-111.txt")
    tweet_file = open("output.txt")
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    hw(tweet_file,sent_file)

if __name__ == '__main__':
    main()
