#%matplotlib inline

import pandas
from sklearn.cross_validation import train_test_split
import numpy as np
import time
from sklearn.externals import joblib
import Recommenders as Recommenders
import Evaluation as Evaluation

songs_metadata_file = 'Online Retail ai3.csv'


song_df =  pandas.read_csv(songs_metadata_file)

song_df.head()

len(song_df)



