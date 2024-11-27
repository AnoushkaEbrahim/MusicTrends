import os
os.environ['KAGGLE_CONFIG_DIR'] = 'C:/Users/Anoushka/New folder/DA/.kaggle'
from kaggle.api.kaggle_api_extended import KaggleApi 
api = KaggleApi()
api.authenticate()

# Downloading Spotify Audio Features dataset
api.dataset_download_files('tomigelo/spotify-audio-features', path='/datasets', unzip=True)

# Downloading Spotify Dataset 1921-2020
api.dataset_download_files('yamaerenay/spotify-dataset-19212020-600k-tracks', path='/datasets', unzip=True)
