def generate_summary(sentences, sentence_score_dict, threshold):
    sentence_count = 0
    summary = ""

    for sentence in sentences:
        if sentence[:15] in sentence_score_dict and sentence_score_dict[sentence[:15]] >= (threshold):
            summary += " " + sentence
            sentence_count += 1

    return summary
