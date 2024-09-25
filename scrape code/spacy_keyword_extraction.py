import pandas as pd
import textacy
from textacy import preprocessing
import spacy
import re

def extract_nouns_verbs(document_text):
    document_text = preprocessing.normalize.whitespace(document_text)
    document_text = preprocessing.remove.punctuation(document_text)
    
    en = spacy.load("en_core_web_sm", disable=("parser",))
    doc = en(document_text)

    nouns_verbs = [(token.text, token.pos_) for token in doc if token.pos_ in ["NOUN", "VERB"]]
    return nouns_verbs

descriptions = re.findall(description_pattern, document_text, re.DOTALL)
noun_verb_list=[]
for description in descriptions:
    nouns_verbs = extract_nouns_verbs(description)
    noun_verb_list.append(nouns_verbs)
data = list(zip(specialties, noun_verb_list))
df = pd.DataFrame(data, columns=['Specialty', 'Nouns'])
df.to_csv('doctor_nouns_verbs.csv', index=False)
print("CSV file saved successfully.")
