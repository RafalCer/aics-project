def reformat_to_bigrams(data):
    reformatted_to_bigrams = list()
    for sentence in data:
        bigrammed = list()
        for i, word in enumerate(sentence[:-1]):
            bigram = (sentence[i], sentence[i+1])
            bigrammed.append(bigram)
        reformatted_to_bigrams.append(bigrammed)
    return reformatted_to_bigrams


def evaluate(predicted, actual, f):
    predicted = reformat_to_bigrams(predicted)
    
    new_actual = list()
    for item in actual:
        item = reformat_to_bigrams(item)
        new_actual.append(item)
    
    actual = new_actual
    scores = dict()

    for i1, predicted_caption in enumerate(predicted):
        
        scores[i1] = dict()
        for i2, real_caption in enumerate(actual[i1]):
            if predicted_caption == real_caption:
                f.write(f'\nComplete match at image {i1} caption number {i2}')
            tp = 0
            for tupler in real_caption:
                if tupler in predicted_caption:
                    tp += 1
            try:
                score = tp/len(real_caption)*100
            except:
                score = 0
            scores[i1][i2] = score
            
    return scores


def average_evaluations(scores, actual, maximize=True):
    new_scores = list()
    for img_id, per_caption_scores in scores.items():
        per_caption_scores = per_caption_scores.values()
        score_list = list(per_caption_scores)
        if maximize:
            biggest = max(score_list)
            new_scores.append(biggest)
        else:
            avg = sum(score_list)/10
            new_scores.append(avg)
    return sum(new_scores)/len(actual)
