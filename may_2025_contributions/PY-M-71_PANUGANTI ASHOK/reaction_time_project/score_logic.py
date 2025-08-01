from score_storage import load_scores

def update_scores(new_time):
    scores = load_scores()
    scores.append(new_time)
    scores.sort()
    return scores[:3]
