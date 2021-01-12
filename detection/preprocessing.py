from typing import List
from convokit import Corpus, download
import pandas as pd
from rich import print
import nltk
from nltk import tokenize

nltk.download("punkt")


def random_pick(
    df,
    columns=["text", "meta.Normalized Score", "meta.Binary", "meta.parsed"],
    num=1250,
):
    return df[columns].sample(n=num)


def concat_df(frames: List):
    return pd.concat(frames)


def sents_2_list(df):
    return df["Sentence"].values.tolist()


def split_sent(text):
    return tokenize.sent_tokenize(text)


def normalise_text(text):
    text = text.strip()
    text = text.lower()  # lowercase
    text = text.replace(r"\#", "")  # replaces hashtags
    text = text.replace(r"http\S+", "URL")  # remove URL addresses
    text = text.replace(r"@", "")
    text = text.replace(r"[^A-Za-z0-9()!?\'\`\"]", " ")
    text = text.replace("\s{2,}", " ")
    text = text.replace(r"\#", "")
    return text


if __name__ == "__main__":
    # wiki_corpus = Corpus(filename=download("wikipedia-politeness-corpus"))
    # stack_corpus = Corpus(filename=download("stack-exchange-politeness-corpus"))

    # print("wiki_corpus length: ", len(wiki_corpus.get_utterance_ids()))
    # print("stack_corpus length: ", len(stack_corpus.get_utterance_ids()))

    # wiki_df = wiki_corpus.get_utterances_dataframe()
    # stack_df = stack_corpus.get_utterances_dataframe()
    # wiki_df.to_csv("data/wikipedia.csv")
    # stack_df.to_csv("data/stack.csv")
    # contat_df = concat_df([wiki_df, stack_df])
    # contat_df = contat_df[contat_df["meta.Binary"] == 1]
    # contat_df_2500 = random_pick(contat_df, num=2500)

    # contat_df_2500.to_csv("data/should_be_annotated.csv")
    # print("should_be_annotated length: ", len(contat_df_2500))

    df = pd.read_csv("data/should_be_annotated.csv")
    li = list(map(split_sent, df.text.values))
    flattened_list = [y for x in li for y in x]
    print(flattened_list[1:20])
    df_flatten = pd.DataFrame(flattened_list, columns=["Sentence"])
    df_flatten.to_csv("data/sentence_to_annotated.csv")
