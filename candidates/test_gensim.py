import logging # 使用 logging 追蹤進度
import time
from gensim.corpora import WikiCorpus
start = time.time()
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s') # logging 格式設定
logging.root.setLevel(level=logging.INFO) # logging level設定
input_filename = 'materials/zh_classicalwiki-latest-pages-articles.xml.bz2' # 輸入file名稱，也就是步驟1下載的檔案 （記得要放到跟程式碼同一個資料夾下）
output_filename = 'wiki-preprocessed-raw.txt' # 輸出檔案名稱

# Lemmatize 需要用到一個 Library 叫做 pattern，但我無論如何都裝不進我的電腦，因此放棄，如果要lemmatize的話，請跳到步驟三 (二)
wiki = WikiCorpus(input_filename,lower=False, dictionary={}) 
with open(output_filename, 'w') as output_f:
  for index, text in enumerate(wiki.get_texts()):
    output_f.write(''.join(text) + '\n')
    if (index % 10000 == 0):
      logging.info("Saved "+ str(index) + "articles")
 
logging.info("Finished preprocessed data in {} seconds".format(time.time() - start))

if __name__ == "__main__":
    freeze_support()