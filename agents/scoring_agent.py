
class ScoringAgent:
    def score(self, job):
        score=0
        if 'transformation' in job.get('title','').lower():
            score += 25
        return score
