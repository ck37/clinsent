import re
import pandas as pd
import medspacy, spacy

nlp = medspacy.load(load_rules = False,
                    enable = ["medspacy_tokenizer"])

# explicitly adding component to pipeline
# (recommended - makes it more readable to tell what's going on)
nlp.add_pipe("medspacy_pysbd", first = True)

def sentence_segment(note_text,
      newlines_to_spaces = True,
      remove_quotes = True,
      extra_clean = True):
    
    # This can raise an AttributeError() when note.text is for some reason a float.
    note_text = note_text.strip()
   
    # Custom processing to improve sentence segmentation.
    # Do this before we replace newlines to avoid clobbering a lot of text.
    if extra_clean:
        note_text = re.sub(r' (q\. ?d(ay)?\.?)', r" qd", note_text)

        note_text = note_text.replace("p.o.", "po")
        note_text = note_text.replace("p.r.n.", "prn")
    
    # This is important, otherwise a newline always seem to lead to a sentence break.
    if newlines_to_spaces:
        note_text = note_text.replace("\n", " ")
        note_text = note_text.replace("\r", " ")
        
    if extra_clean:
        note_text = re.sub(r'q\.( *\d+(\-\d+)?h?)\.', r'q\1', note_text)
        # Long series of _____ converted to shorter word then newline.
        note_text = re.sub('_{5,}', '\n_LINE_\n', note_text)
    
    # Only double-quotes for now, since single quotes can be used in contractions.
    if remove_quotes:
        note_text = note_text.replace('"', '')
        
    # Extract all sentences from this note.
    doc = nlp(note_text)
    sentence_iterator = doc.sents

    doc_sents = []
    # Loop over each sentence in the note based on the sentencizer.
    for i, sent in enumerate(sentence_iterator):
        # Remove leading and trailing whitespace - especially newlines but also spaces.
        sent_clean = sent.text.strip()
        # Replace multiple spaces with a single space.
        sent_clean = re.sub(r' +', ' ', sent_clean)
        
        word_count = len(sent)
            
        result = {
          "sent_num": i,
          # We need to extract the raw text from the sentence object,
          # otherwise we'll run into a "pickling a span is not supported" spacy error.
          "text": sent_clean,
          "chars": len(sent_clean),
          "words": word_count}
        doc_sents.append(result)
        
    return(pd.DataFrame(doc_sents))
