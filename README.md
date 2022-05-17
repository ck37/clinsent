
# clinsent: sentiment measurement in clinical notes

**Key functionality**

-   Keyword-based sentiment measurement
-   Sentence segmentation
-   *To Add: Deep learning-based sentiment measurement*

This package is a work in progress. Manuscript under review: Cobert et
al. ([2022](#ref-cobert2022)).

## Install

### Python

Install the most recent code on GitHub via pip:

``` {bash}
pip install git+https://github.com/ck37/clinsent/
```

## Dependencies

### Python

We recommend python version 3.8, as [3.9 is not currently supported by
PyRush](https://github.com/jianlins/PyRuSH/issues/1), a dependency of
MedSpacy.

## Examples

### Python

#### Keyword analysis

``` python
from clinsent import KeywordFinder

kwf = KeywordFinder()
text = 'bp is improving, but o2 worsening'
hits, score = kwf.run(text)
print('Score:', score)
print('Hits:', hits)
```

    Score: 0.5
    Hits: {'improving': 1, 'worsening': 1}

#### Sentence segmentation

``` python
from clinsent import sentence_segment

sentence_df = sentence_segment("Patient has low bp. Hx of poor a1c control.")
print(sentence_df)
```

       sent_num                     text  chars  words
    0         0      Patient has low bp.     19      5
    1         1  Hx of poor a1c control.     23      6

#### Deep learning analysis

``` python
# Add example here.
```

### R

Examples to be added.

## References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-cobert2022" class="csl-entry">

Cobert, J., Chiu, C., Cook, A., Gologorskaya, O., Farhan, H., Han, M.,
Hodgson, M., Lazzereschi, D., Ashana, D., Lee, S., Smith, A. K.,
Pirracchio, R., and Kennedy, C. J. (2022). Negativity and positivity in
the intensive care unit: Establishing a proof-of-concept for automated
sentiment capture in the electronic health record. *Unpublished
Manuscript*.

</div>

</div>
