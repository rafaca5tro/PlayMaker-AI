def compute_score(content):
    score = 0
    if "sponsor" in content.lower(): score += 20
    if "fan" in content.lower(): score += 20
    if len(content) > 1000: score += 30
    return min(score + 30, 100)
