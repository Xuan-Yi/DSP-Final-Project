import jieba.analyse # 匯入關鍵字提取庫
import pandas as pd # 匯入pandas
import newspaper
import nltk

nltk.download('punkt')

link='https://tw.news.yahoo.com/%E6%B0%91%E9%80%B2%E9%BB%A8-%E6%95%97%E9%81%B8%E6%AA%A2%E8%A8%8E-%E6%9C%89%E7%AD%94%E6%A1%88%E4%BA%86-%E6%AD%B8%E5%92%8E%E5%8E%9F%E5%9B%A0%E9%80%A3%E6%8A%96%E9%9F%B3%E4%B9%9F%E8%A2%AB%E9%BB%9E%E5%90%8D-142821107.html'

article=newspaper.Article( link,language='zh')
article.download()
article.parse()
article.nlp()
print(article.summary)
string_data=''.join(article.keywords)

def get_key_words(sttring_data,how=''):
    if how=='textrank':
        tags_pairs=jieba.analyse.textrank(string_data,topK=10,withWeight=True)
    else:
        tags_pairs=jieba.analyse.extract_tags(string_data,topK=10,withWeight=True)
    tags_list=[]
    for i in tags_pairs:
        tags_list.append((i[0],i[1]))
    tags_pd=pd.DataFrame(tags_list,columns=['word','weight'])
    return tags_pd

keywords=get_key_words(string_data) # TF-IDF
print(keywords)

keywords_tr=get_key_words(string_data,how='textrank')   # TextRank
print(keywords_tr)