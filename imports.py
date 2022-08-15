# Essential libraries
import os
import json
import requests

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Data hanlding
import pandas as pd
import numpy as np
import pydataset
import scipy.stats as stats
import statistics as s

# Data visualization
import plotly
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import missingno as msno
from mpl_toolkits.mplot3d import Axes3D

# Sklearn
from sklearn.cluster import KMeans, DBSCAN
from sklearn.neighbors import NearestNeighbors
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, RFE, f_regression, SequentialFeatureSelector
from sklearn.metrics import mean_squared_error

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import PolynomialFeatures

from sklearn.linear_model import LassoLars
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import TweedieRegressor

from sklearn.model_selection import train_test_split

# Local files
# import env
# import acquire
# import prepare
# import clustering
# import modeling
# Text display
import colorama
from colorama import Fore