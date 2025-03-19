import subprocess
from nltk import download
import nltk

cmd = ['python','-m','textblob.download_corpora']
subprocess.run(cmd)
print("TextBlob corpora installed")

download('punkt_tab')
# Download NLTK words list
nltk.download('words')