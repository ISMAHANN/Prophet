import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
########
from google.colab import drive
drive.mount('/content/drive')
#####
df = pd.read_excel ('/content/NDV.xlsx')
#####
%pip install prophet
