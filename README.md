# clinsent: sentiment measurement in clinical notes

**Key functionality**

- Keyword-based sentiment measurement
- Sentence segmentation
- *To Add: Deep learning-based sentiment measurement*

This package is a work in progress.

Citation: Kennedy et al. ([2023](#ref-kennedy2023)).

## Install

### Python

Install the most recent code on GitHub via pip:

``` {bash}
pip install git+https://github.com/ck37/clinsent/
```

## Dependencies

### Python

This package is tested with python version 3.8, but 3.9 should also
work.

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

<div id="ref-kennedy2023" class="csl-entry">

Kennedy, Chris J, Catherine Chiu, Allyson Cook Chapman, Oksana
Gologorskaya, Hassan Farhan, Mary Han, Macgregor Hodgson, Daniel
Lazzareschi, Deepshikha Ashana, Sei Lee, Alexander K Smith, Edie Espejo,
John Boscardin, Romain Pirracchio, and Julien Cobert. 2023. “Negativity
and Positivity in the ICU: Exploratory Development of Automated
Sentiment Capture in the Electronic Health Record.” *Crit Care Explor* 5
(10): e0960. <https://doi.org/10.1097/CCE.0000000000000960>.

</div>

</div>
