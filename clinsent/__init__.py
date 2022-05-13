from .version import __version__

from .sentences import sentence_segment
from .keywords import KeywordFinder

# if somebody does "from somepackage import *", this is what they will
# be able to access:
__all__ = [
  "KeywordFinder",
  "sentence_segment"
]
