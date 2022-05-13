
# clinsent: sentiment measurement in clinical notes

**Key functionality**

-   Keyword-based sentiment measurement
-   Deep learning-based sentiment measurement
-   Sentence segmentation

This package is a work in progress.

## Install

Install the most recent code on GitHub via pip:

``` {bash}
pip install git+https://github.com/ck37/clinsent/
```

## Dependencies

We recommend python version 3.8, as [3.9 is not currently supported by
PyRush](https://github.com/jianlins/PyRuSH/issues/1), a dependency of
MedSpacy.

## Examples

**Keyword analysis**

``` python
from clinsent import KeywordFinder
positive_keywords = ['good', 'best']
negative_keywords = ['not good', 'worst']
kwf = KeywordFinder(positive_keywords = positive_keywords,
                    negative_keywords = negative_keywords)
text = 'it was the best of times, it was the worst of times'
hits, score = kwf.run(text)
print('Score:', score)
print('Hits:', hits)
```

    Score: 0.5
    Hits: {'best': 1, 'worst': 1}

**Deep learning analysis**

``` python
# Deep learning analysis
```

**Sentence segmentation**

``` python
from clinsent import sentence_segment

sentence_df = sentence_segment("Patient has low bp. Hx of poor a1c control.")
print(sentence_df)
```

       sent_num                     text  chars  words
    0         0      Patient has low bp.     19      5
    1         1  Hx of poor a1c control.     23      6

## References
