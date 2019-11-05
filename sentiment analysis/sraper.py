from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

counters = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

df = pd.DataFrame(counters)
np.savetxt(r'output.txt', df.values, fmt ='%d')


