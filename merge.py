from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import files

#read csv file
merge_planets_df = pd.read_csv("/content/PRO-NASA-Exoplanet-Processed-Data/merge_planets.csv")

#check number of rows and columns
print(merge_planets_df.shape)

merge_planets_df.head()

merge_planets_df.columns

merge_planets_df.drop(columns=['luminosity', 'pl_insol', 'pl_insolerr1','pl_insolerr2', 'pl_insollim','st_metratio'], inplace=True)

merge_planets_df.to_csv('merge.csv')


files.download('main.csv')