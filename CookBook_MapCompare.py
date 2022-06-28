import numpy
import pandas as pd

# load data from csv
dat = list(pd.read_csv("result.csv",";").itertuples(index=False))
imgSize = (3840,2160)

test = draw_heatmap(dat,imgSize)

where_are_NaNs = (test)
test[where_are_NaNs] = 0

numpy.nanmin(test)

test[test <= 1000] = "nan"



fig, ax = draw_display(imgSize, imagefile=None)
ax.imshow(test, cmap='jet', alpha=0.5)
ax.invert_yaxis()
