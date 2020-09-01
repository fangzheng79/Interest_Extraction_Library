# Interest_Extraction_Library

This library integrate various unsupervised keyphrase extraction 
algorithms and involves Wikipedia to select candidates from  keyphrase extraction results to infer user's interests.

Install the required dependencies using
```
pip install -r requirements.txt
```

This project also requires external resources that can be obtained using:
```
python -m nltk.downloader stopwords
python -m nltk.downloader universal_tagset
python -m spacy download en # download the english model
```
