from typing import List
from convokit import Corpus, download
import pandas as pd

def random_pick(
    df,
    columns=["text", "meta.Normalized Score", "meta.Binary", "meta.parsed"],
    num=1250,
):
    return df[columns].sample(n=num)


def concat_df(frames: List):
    return pd.concat(frames)


if __name__ == "__main__":
    wiki_corpus = Corpus(filename=download("wikipedia-politeness-corpus"))
    stack_corpus = Corpus(filename=download("stack-exchange-politeness-corpus"))

    print("wiki_corpus length: ", len(wiki_corpus.get_utterance_ids()))
    print("stack_corpus length: ", len(stack_corpus.get_utterance_ids()))

    wiki_df = wiki_corpus.get_utterances_dataframe()
    stack_df = stack_corpus.get_utterances_dataframe()
    wiki_df.to_csv("data/wikipedia.csv")
    stack_df.to_csv("data/stack.csv")

    wiki_df_1250 = random_pick(wiki_df)
    stack_df_1250 = random_pick(stack_df)

    contat_df = concat_df([wiki_df_1250, stack_df_1250])
    contat_df.to_csv("data/should_be_annotated.csv")
    print("should_be_annotated length: ", len(contat_df))

