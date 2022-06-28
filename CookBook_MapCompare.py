import numpy
import pandas as pd

# load data from csv
Result = pd.read_csv("Data_local\\result.csv",";")

# loop and create results for each image
from joblib import Parallel, delayed

def gazeMapResult(csv_data,filter1, filter2, filter3):
    for i in csv_data[filter1].unique():
         for j in csv_data[filter2].unique():
             for k in csv_data[filter3].unique():

                 loop_temp_data = csv_data.loc[(csv_data[filter1] == i) &
                                               (csv_data[filter2] == j) &
                                               (csv_data[filter2] == k)]

    return loop_temp_data






dat = list(pd.read_csv("Data_local\\result.csv",",").itertuples(index=False))
imgSize = (3840,2160)

test = heatmap(dat,imgSize)


numpy.nanmin(test)

test[test <= 1000] = "nan"



fig, ax = draw_display(imgSize, imagefile=None)
ax.imshow(test, cmap='jet', alpha=0.5)
ax.invert_yaxis()


"Q:\System\Git\Saliency_map_Vs_gazemap\Data_local\result.csv"