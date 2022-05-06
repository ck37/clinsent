from collections import defaultdict
import re

# Via https://stackoverflow.com/a/20885799
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

# This class designed by Hunter Mills.
class KeywordFinder():
    '''
    class to collect positive and negative sentiment keywords and return 
    sentiment score.
    '''
    def __init__(self, 
                 positive_keywords=[], 
                 negative_keywords=[]):
        '''
        init function. Cretes regex for positive and negative keywords and 
        map between positive and negative sentiment words.

        INPUTS:
            positive_keywords (list): list of positive sentiment keywords
            negative_keywords (list): list of negative sentiment keywords

        OUTPUTS:
            None

        DEMO USAGE:
            >>> positive_keywords = ['good', 'best']
            >>> negative_keywords = ['not good', 'worst']
            >>> kwf = KeywordFinder(positive_keywords=positive_keywords,
            ...                     negative_keywords=negative_keywords)
            >>>
            >>> text = 'it was a good day'
            >>> hits, score = kwf.run(text)
            >>> print(score)
            ...    0
            >>> print(hits)
            ...    {'good' : 1}
            >>>
            >>> text = 'I was not good today'
            >>> hits, score = kwf.run(text)
            >>> print(score)
            ...    1
            >>> print(hits)
            ...    {'not good' : 1}
            >>>
            >>> text = 'it was the best of times, it was the worst of times'
            >>> hits, score = kwf.run(text)
            >>> print(score)
            ...    0.5
            >>> print(hits)
            ...    {'best' : 1, 'worst' : 1}
            >>>
            >>> text = 'sentence void of sentiment'
            >>> hits, score = kwf.run(text)
            >>> print(score)
            ...    None
            >>> print(hits)
            ...    {}
        '''
        # clean input and generate mapping for keywords
        self.negative_keywords=[i.strip().lower() for i in negative_keywords]
        self.positive_keywords=[i.strip().lower() for i in positive_keywords]
        self.sent_map = {word : 'positive' for word in self.positive_keywords}
        self.sent_map.update({word : 'negative' 
                              for word in self.negative_keywords})

        # build regex. 
        # Ordered longest to shortest by keyword length to prevent miss counts
        self.keywords = self.positive_keywords + self.negative_keywords        
        kws = sorted(set(self.keywords), key=lambda x: -len(x))
        self.regex = re.compile(r'\b(' +  r')|('.join(kws) + r')\b')

        
    def find_keywords(self, text):
        '''
        function to find keywords.


        INPUTS:
            text (str): text to collect and score

        OUTPUTS:
            hits (dict): dictionary mapping keywords to total mentions in text
        '''
        # apply regex and count matches
        hits = defaultdict(int)
        for match in re.finditer(self.regex, text.lower()):
            hits[match.group()] += 1
            
        # convert from defaultdict to dict
        return dict(hits)
    
    
    def score_sentiment(self, hits):
        '''
        function to score keyword sentiment


        INPUTS:
            hits (dict): dictionary mapping keywords to total mentions in text

        OUTPUTS:
            score (float): sentiment score ranging from 0 to 1, 
                           with 1 being extremely negative
        '''
        # if no keywords return None
        if len(hits) == 0:
            return None
        
        # count total negative and positive keywords
        score = defaultdict(int)
        for kw, cnt in hits.items():
            score[self.sent_map[kw]] += cnt
            
        return score['negative'] / (score['negative'] + score['positive'])
    
    
    def run(self, text):
        '''
        function to run KeywordFinder.

        INPUTS:
            text (str): text to collect and score

        OUTPUTS:
            hits (dict): dictionary mapping keywords to total mentions in text
            score (float): sentiment score ranging from 0 to 1, 
                           with 1 being extremely negative
        '''
        hits = self.find_keywords(text)
        return hits, self.score_sentiment(hits)
