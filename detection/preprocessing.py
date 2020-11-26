from convokit import Corpus, download
import pandas as pd

wiki_corpus = Corpus(filename=download("wikipedia-politeness-corpus"))
stack_corpus = Corpus(filename=download("stack-exchange-politeness-corpus"))

print("wiki_corpus length: ", len(wiki_corpus.get_utterance_ids()))
print("stack_corpus length: ", len(stack_corpus.get_utterance_ids()))

wiki_df = wiki_corpus.get_utterances_dataframe()
stack_df = stack_corpus.get_utterances_dataframe()

wiki_df.to_csv("data/wikipedia.csv")
stack_df.to_csv("data/stack.csv")