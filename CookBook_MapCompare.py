import matplotlib.pyplot
import numpy
import pandas as pd
from PIL import Image
from tqdm import tqdm

# load data from csv
Result = pd.read_csv("Data_local\\result.csv",";")

# loop and create results for each image
from joblib import Parallel, delayed

dat = list(pd.read_csv("Data_local\\result.csv",",").itertuples(index=False))
imgSize = (3840,2160) # size pf stimulz image

def gazeMapResult(csv_data,filter1, filter2, filter3, ):
    for i in tqdm(csv_data[filter1].unique()):
         for j in csv_data[filter2].unique():
             for k in csv_data[filter3].unique():

                 loop_temp_data = csv_data.loc[(csv_data[filter1] == i) &
                                               (csv_data[filter2] == j) &
                                               (csv_data[filter3] == k)]

                 map_csv = list(loop_temp_data.iloc[:,-3:].itertuples(index=False))

                 # create heatmap
                 outData = heatmap(map_csv,imgSize)
                 # # create tresholded map 2% > 20%
                 Q1heatmap = outData
                 Q1heatmap[Q1heatmap <= numpy.quantile(Q1heatmap[~numpy.isnan(Q1heatmap)], 0.25)] = "nan"

                 Q2heatmap = outData
                 Q2heatmap[Q2heatmap <= numpy.quantile(Q2heatmap[~numpy.isnan(Q1heatmap)], 0.5)] = "nan"

                 Q3heatmap = outData
                 Q3heatmap[Q3heatmap <= numpy.quantile(Q1heatmap[~numpy.isnan(Q3heatmap)], 0.75)] = "nan"

                 # Binarize images and save
                 maxval = 255
                                  #
                 Q1heatmap_name = i+"_"+j+"_"+k+"Q1"+".png"
                 Q1heatmap_bin = (Q1heatmap > numpy.quantile(Q1heatmap[~numpy.isnan(Q1heatmap)], 0.25)) * maxval
                 Image.fromarray(numpy.uint8(Q1heatmap_bin)).save(Q1heatmap_name)

                 Q2heatmap_name = i + "_" + j + "_" + k + "Q2" + ".png"
                 Q2heatmap_bin = (Q2heatmap > numpy.quantile(Q2heatmap[~numpy.isnan(Q2heatmap)], 0.55)) * maxval
                 Image.fromarray(numpy.uint8(Q2heatmap_bin)).save(Q2heatmap_name)

                 Q3heatmap_name = i + "_" + j + "_" + k + "Q3" + ".png"
                 Q3heatmap_bin = (Q3heatmap > numpy.quantile(Q3heatmap[~numpy.isnan(Q3heatmap)], 0.75)) * maxval
                 Image.fromarray(numpy.uint8(Q3heatmap_bin)).save(Q3heatmap_name)

                 outData_name = i + "_" + j + "_" + k + "RAW" + ".png"
                 rawheatmap_bin = (outData > numpy.nanmin(outData)) * maxval
                 Image.fromarray(numpy.uint8(rawheatmap_bin)).save(outData_name)


    return map_csv

# multithreat processing

