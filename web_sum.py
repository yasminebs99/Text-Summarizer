import nltk
import pandas as pd
nltk.download('stopwords')
def top10_sent(wiki):
    required_text=wiki
    stopwords=nltk.corpus.stopwords.words("english")
    sentences=nltk.sent_tokenize(required_text)
    words=nltk.word_tokenize(required_text)
    word_freq={}
    for word in words:
        if word not in stopwords:
            if word not in word_freq:
                word_freq[word]=1
            else:
                word_freq[word]+=1
    max_word_freq=max(word_freq.values())
    for key in word_freq.keys():
        word_freq[key]/=max_word_freq
    sentences_score=[]
    for sent in sentences:
        curr_words=nltk.word_tokenize(sent)
        curr_score=0
        for word in curr_words:
            if word in word_freq:
                curr_score+=word_freq[word]
        sentences_score.append(curr_score)
    sentences_data=pd.DataFrame({"sent":sentences, "score":sentences_score})
    sorted_data= sentences_data.sort_values(by = "score", ascending=False).reset_index()
    top10_rows =sorted_data.iloc[0:11,:]
    return  "".join(list(top10_rows["sent"]))