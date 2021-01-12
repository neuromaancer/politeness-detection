# Data

## Description

There are two corpus: [Stanford Politeness Corpus (Stack Exchange)](https://convokit.cornell.edu/documentation/stack_politeness.html) and [Stanford Politeness Corpus (Wikipedia)](https://convokit.cornell.edu/documentation/wiki_politeness.html).

Each utterance corresponds to a Stack Exchange request. For each utterance, we provide:

- id: row index of the request given in the original data release.
- speaker: the author of the utterance.
- conversation_id: id of the first utterance in the conversation this utterance belongs to, which in this case is the id of the utterance itself
- reply_to: None. In this dataset, each request is seen as a full conversation, and thus all utterances are at the ‘root’ of the conversations
- timestamp: “NOT_RECORDED”.
- text: textual content of the utterance.

Metadata for each utterance is inherited from the general CMV corpus:

- Normalized Score: Normalized politeness score computed based on annotations.
- Binary: A binarized politeness label where 1=”polite”, 0=”neutral”, -1 = “impolite”.
- Annotations: the original annotations from Amazon Mechanical Turkers for the given utterance. Ratings are on a 1-25 scale.
- parsed: dependency-parsed version of the utterance text

which corresponds to (without annotation of strategies):

- stack.csv
- wikipedia.csv

## History file

- bert_history.csv: Storing the loss and accuracy log of bert model.
- w2v_history.csv: Storing the loss and accuracy log of w2v model.
- history.csv: combined file with bert_history.csv and w2v_history.csv

## Data file

- data.csv: raw data file.
- clean_dataset.csv: preprocessed data file (clean the text).
- testset_human.csv: 50 samples annotated by 3 annotator. -> Ground Truth.
