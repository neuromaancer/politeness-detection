####python script to annotate a corpus with politeness strategies

import re
import pandas as pd

####### dictionnaries of rules ########
##for each dictionary : first number indicates if the strategy is positive politeness (0) or negative politeness (1)
##second number indicates the strategy number in B&L (1978)
## ex : d_01 is the dictionary of rules for Strategy 1 of positive politeness
## ex2 : d113 is the dictionary of rules for Strategy 13 of negative politeness



d_01 = {'p1' : re.compile(r"[ \w,: ]* (is|\'s) \w+(?!\s+(not|no|bad|worse|wrong|false)) great", re.IGNORECASE),
    'p2' : re.compile(r".*(excellent|wonderful|great)!", re.IGNORECASE),
    'p3': re.compile(r".*(you are|you're) (great|good|excellent).*", re.IGNORECASE)}

d_02 = {'p1' : re.compile(r".*(amazingly|incredibly|marvelous|extraordinary|devastating|\
                incredible|unbelievable|perfect|fantastic|wonderful|ravishing|delightful|divine|\
                )(?!\s+(not|no|bad|worse|wrong|false)).*", re.IGNORECASE),
        "p2" : re.compile(r".*[ a ]?(great|good|excellent) (question|work|idea|way|tool|answer).*", re.IGNORECASE)}

d_04 = {'p1' : re.compile(r"\s*(dude|mate|pal|guys|fellas|buddy)", re.IGNORECASE),
        'p3' : re.compile(r"\s*(?!\s+(you|i|we|they))(mind if|how about|got (any|a|the|one))", re.IGNORECASE)}

d_05 = {'p1' : re.compile(r"^((it|this)\s(is|\'s)\s)*(yes|really\s*[?!]|correct|sure|for sure)", re.IGNORECASE),
        'p2' : re.compile(r"^\w+?\s?(sure|[a-z]ly]|for sure)?\s*did", re.IGNORECASE),
        'p3' : re.compile(r"^\w+?\s?\w+?\s*(is|was|have|had|has)[:punct:]", re.IGNORECASE),
        'p4' : re.compile(r".*(surely|absolutely|exactly)(\.|!)", re.IGNORECASE)
        }

d_06 = {'p1' : re.compile(r"h*u+h*m+",re.IGNORECASE),
        'p2' : re.compile(r"^([:punct:]*)?\s?((not (really|exactly|totally|completely|quite))|yes\s?[:punct:]?\s?but|but|barely|apparently|so)", re.IGNORECASE),
        'p3' : re.compile(r"then([:punct:]*)?$", re.IGNORECASE),
        'p4' : re.compile(r"([:punct:]*)?well([:punct:]*)?", re.IGNORECASE),
        'p7' : re.compile(r"i don\'t know[:punct:]?", re.IGNORECASE)}

d_07 = {'p1' : re.compile(r"((?!\s+(do|did|how|what|where))you know([:punct]*)+)|you know([:punct]*)?$", re.IGNORECASE),
        'p2' : re.compile(r"((?!\s+(do|did|how|what|where))you see([:punct]*)+)|you see([:punct]*)?$", re.IGNORECASE),
        'p3' : re.compile(r"(?!(what|how|where|why|which|who|when)(\w+)*)\b(did|have|was|do|does|has|is|wo|ca|would)(n\'t| not) (I|we|he|she|you|it)", re.IGNORECASE),
        'p4' : re.compile(r'".*"')}

d_09 = {'p1' : re.compile(r".*(\bi\b|\bwe\b) know you.*", re.IGNORECASE)}

d_012 = {'p1' : re.compile(r"let\'s|\bwe\b", re.IGNORECASE)}

d_013 = {'p1' : re.compile(r"why (\w+n\'t|\w+ not|not)", re.IGNORECASE)}

d_014 = {'p1' : re.compile(r".*(i|we) (am|are|was|were) [\w,;: ]+too,.*",re.IGNORECASE)}

d_11 = {'p1' : re.compile(r".*(would|is|will|can|could) (this|there|you).*\?", re.IGNORECASE),
        'p2' : re.compile(r".*(can|could|may) I \w+ you.*\?", re.IGNORECASE),
        'p3' : re.compile(r".*(actually|exactly|more or less|please|roughly|to some extent|all in all|so to speak|i mean|basically|as a matter of fact|so-so|to be honest|frankly|I (have to|must) say).*", re.IGNORECASE),
        'p4' : re.compile(r".*(I am|I'm) not (sure|convinced|certain) (what|that|it|about).*", re.IGNORECASE)}


d_12 = {'p1' : re.compile(r"(I [\w ]*(suppose|guess|think|wonder|bet) [\w,:; ]*you.*\?)|(.*you [\w ]*I [\w ]*(suppose|guess|think|wonder|bet).*\?)", re.IGNORECASE),
        'p2' : re.compile(r"I [\w ]*(sincerely|certainly|completely|definitely).*\?", re.IGNORECASE),
        'p3' : re.compile(r".*(shall we|do you think|I\'m afraid|it (seems|appears)|in fact|in a way|in a sense|don't you (think|agree)).*\?", re.IGNORECASE),
        'p4' : re.compile(r".*(it|you) (might|may).*\?", re.IGNORECASE),
        'p5' : re.compile(r".*if (you|it|I) (can|may|could|want|\'ll (allow|forgive)).*\?", re.IGNORECASE),
        'p6' : re.compile(r".*as ((you|we) know|it is known|(one|you|I) (might|may|would) say|I recall|I understand).*\?", re.IGNORECASE),
        'p8' : re.compile(r".*((^sorry to)|this may not|^hey|^oh|by the way|anyway).*\?", re.IGNORECASE),
        'p9' : re.compile(r".*(while I (remember|think)|i( was [\w,;: ]*just|( have|\'ve) been) (think|remember|wonder)ing)", re.IGNORECASE),
        'p10' : re.compile(r".*(if|since) you( ask|( want| care) to know| want|\'ll (allow|agree))", re.IGNORECASE),
        'p11' : re.compile(r".*(do|have|were|did|would) you \w+", re.IGNORECASE),
        'p12': re.compile(r".*(sort of|like|kind of|in a way|maybe|perhaps|merely|probably|possibly|approximately|somewhat).*\?", re.IGNORECASE),
        'p13': re.compile(r".*i [\w ]? (guess|believe|think|wonder|hope).*\?", re.IGNORECASE)}


d_13 = {'p1' : re.compile(r".*I (do not|don't) (except|assume|suppose|imagine|believe).*", re.IGNORECASE),
        'p2' : re.compile(r".*you (wo|would|could)(n\'t| not).*", re.IGNORECASE)}

d_14 = {'p1' : re.compile(r"I just|just a", re.IGNORECASE)}

d_15 = {'p1' : re.compile(r"\bSir\b", re.IGNORECASE)}

d_16 = {'p1' : re.compile(r"I(\'m| am) sure (this|you)|I hope (i|this|you) (\w+)*(n\'t|not)", re.IGNORECASE),
        'p2' : re.compile(r"I don\'t want to|I hate to|I(\'m| am)(\s\w+ )* embarrassed", re.IGNORECASE),
        'p3' : re.compile(r"I\'m sorry|excuse me|I beg", re.IGNORECASE)}

d_17 = {'p1' : re.compile(r"I (tell|assure|ask)", re.IGNORECASE),
        'p2' : re.compile(r"it (is|would be) ([a-z]y|[a-z]ed|possible)", re.IGNORECASE),
        'p3' : re.compile(r"it ((appears|seems|looks) (that|to me)|(needs|wants|requires))", re.IGNORECASE),
        'p4' : re.compile(r"(was|were|is) [a-z]ed", re.IGNORECASE),
        'p5' : re.compile(r"let it be", re.IGNORECASE),
        'p6' : re.compile(r".*((one|someone) (might|would|can|can't|will|shouldn't|should|won\'t)|(might|would|cant'|can|will|should|shouldn't|won\'t) (someone|one)).*", re.IGNORECASE),
        'p7' : re.compile(r"^OK", re.IGNORECASE),
        'p8' : re.compile(r".*\bwe\b.*", re.IGNORECASE),
        'p9' : re.compile(r"I (wondered (whether|if)|felt|hoped|thought) I", re.IGNORECASE),
        'p10' : re.compile(r"I did (wonder|hope|feel|think)", re.IGNORECASE),
        'p11' : re.compile(r"I was (wonder|hop|feel|think)ing", re.IGNORECASE)}

d_110 = {'p1' : re.compile(r".*I would(n\'t| not) mind.*", re.IGNORECASE),
        'p2' : re.compile(r".*It would(n\'t| not) be any.*", re.IGNORECASE),
        'p3' : re.compile(r".*i could (\w+)* (do|make).*", re.IGNORECASE),
        'p4' : re.compile(r".*\bme\b a favour.*", re.IGNORECASE),
        'p5' : re.compile(r".*help \bme\b.*", re.IGNORECASE),
        'p6' : re.compile(r".*(i'd|i) would be (grateful|happy|appreciative|thankful|obliged).*")}

d_f = {'p1' : re.compile(r"\?$", re.IGNORECASE)}

list_d = [d_01, d_02, d_04, d_05, d_06, d_07, d_09, d_012, d_013, d_014, d_11, d_12, d_13, d_14, d_15, d_16, d_17, d_110]
list_lb = ['d_01', 'd_02', 'd_04', 'd_05', 'd_06', 'd_07', 'd_09', 'd_012', 'd_013','d_014','d_11', 'd_12', 'd_13', 'd_14', 'd_15','d_16', 'd_17', 'd_110']

def annotate_str(df, d, label) :
    p_c = []
    labl = label
    if labl == 'd_f' :
        for i in range(len(df)):
            if df.iloc[i, 2] == 0 :
                for p in d.values():
                    p_c.append(p.search(str(df.iloc[i, 1])))
                if any(p_c):
                    df.iloc[i, 2] = 'd_12'
            else:
                pass
    else :
        for i in range(len(df)) :
            p_c =[]
            for p in d.values() :
                p_c.append(p.search(str(df.iloc[i,1])))
            if any(p_c) :
                df.iloc[i, 2] = labl
    return df

def fs_annotation(df, list_d, list_lb) :
    df['label'] = [0]*len(df)
    for d, lbl in zip(list_d, list_lb):
        ddf = annotate_str(df, d, lbl)
        df = ddf
        print(f'Corpus processed for strategy {lbl}')
    print(df['label'].value_counts())
    return df

# def fs_annotation(df, dico) :
#     for i in range(len(df)):
#         for d in dico.keys() :
#             p_c = []
#             for p in dico[d].values() :
#                 p_c.append(p.search(str(df.iloc[i, 1])))
#             if any(p_c) :
#                 df.iloc[i, 2] = d
#     # pf = d_f['p1']
#     # for i in range(len(df)):
#     #     if df.iloc[i, 2] == 0 :
#     #         if pf.search(str(df.iloc[i, 1])):
#     #             df.iloc[i, 2] = 'd_12'
#     print(df['label'].value_counts())
#     return df

def full_pipe(path_corpus, path_corpus_out) :
    df = pd.read_csv(path_corpus)
    annotated = fs_annotation(df, list_d, list_lb)
    annotated.to_csv(path_corpus_out)

# def batch_annotation_depr(df, dic)
#     # df['label'] = [0]*len(df)
#     # num_batch = math.ceil(len(df)/n)
#     # list_df = []
#     # for i in range(num_batch) :
#     #     ddf = df[i:(i+1)*num_batch]
#     #     an = fs_annotation(ddf, dic)
#     #     list_df.append(an)
#     # dff = df[num_batch:len(df)-num_batch]
#     # af = fs_annotation(dff, dic)
#     # list_df.append(af)
#     # fdf = list_df[0]
#     # for j in range(1, len(list_df)):
#     #     fdf.append(list_df[i])
#     # return fdf

full_pipe("./sentence_to_annotate.csv","./result_automatic_annotation.csv")





