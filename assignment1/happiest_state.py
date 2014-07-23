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
    state_scores = {}
    for response in responses:
        if response['place'] != None:
            if ',' in response['place']['full_name']:
                state = response['place']['full_name'].split(",")[1]
                state = state.replace('2\n','')
                state = state.replace(" ",'')
            if len(state) == 2:
                results.append([response['text'],state])
    for result in results:
        total = 0
        words = combos(result[0],scores)
        for word in words:
            for key in scores.iterkeys():
                if word == key:
                    total += scores[word]
        state_scores[result[1]] = total
    the_max = ["dummy state",0]
    for key, value in state_scores.iteritems():
        if value > the_max[1]:
            the_max = [key,value]
    print the_max[0]
    
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
    #sent_file = open("AFINN-111.txt")
    #tweet_file = open("output.txt")
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(tweet_file,sent_file)

if __name__ == '__main__':
    main()
