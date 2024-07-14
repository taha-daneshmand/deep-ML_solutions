import math

def softmax(scores: list[float]) -> list[float]:
    exp_scores = [math.exp(score) for score in scores]
    
    sum_exp_scores = sum(exp_scores)
    
    probabilities = [exp_score / sum_exp_scores for exp_score in exp_scores]
    
    probabilities = [round(prob, 4) for prob in probabilities]
    
    return probabilities
