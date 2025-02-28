#Run k-means on Homolig similarity matrices.
#Using mbkmeans on raw similarity matrices - not doing any kind of dimensional reduction.
#User inputs 'expected' number of clusters C.  This script will sweep across that value 1/2C, C, 2C, 4C
#AAG 27 May 2023

import sys
import argparse
from time import localtime, strftime
import warnings
warnings.filterwarnings("ignore")

import scanpy as sc
import pandas as pd
import numpy as np
from sklearn.cluster import MiniBatchKMeans

#ARGPARSE------------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', help = "Input .h5ad file")
parser.add_argument('-c', '--num_clusters', help = "Expected number of clusters. May be any integer.")
parser.add_argument('-o', '--output',  help = "Desired output file path/filename. Defaults to input file directory.")

#Read arguments from command line.
args = parser.parse_args()

if args.input is None:
    sys.exit('Please specify input file.')
if args.num_clusters is None:
    sys.exit('Please specify expected number of groups in data.')
if args.output is None:
    args.output = args.input[0:-5] + '_clusters.csv'


#Load in the data /assign variables. ---------------------------------------------

inputfile=args.input
outputfile=args.output
C=int(args.num_clusters)

now = strftime("%Y-%m-%d %H:%M:%S", localtime())
print('[' + now + ']', 'Homolig version 0.1 mbkmeans Clustering')  # Find a way to add __version__ attribute to package at later date.
print('                         input_file: ', inputfile)
print('                        output_file: ', outputfile)
print('                       num_clusters: ', C)


#Execute clustering!--------------------------------------------------------------

adata = sc.read_h5ad(inputfile)

x = np.asarray(adata.X.todense())


kmeans1 = MiniBatchKMeans(n_clusters = round(C / 2), random_state = 99, batch_size = 1024, n_init = 10)
kmeans2 = MiniBatchKMeans(n_clusters = C, random_state = 99, batch_size = 1024, n_init = 10)
kmeans3 = MiniBatchKMeans(n_clusters = 2 * C, random_state = 99, batch_size = 1024, n_init = 10)
kmeans4 = MiniBatchKMeans(n_clusters = 4 * C, random_state = 99, batch_size = 1024, n_init = 10)


clusters1 = kmeans1.fit_predict(x)
clusters2 = kmeans2.fit_predict(x)
clusters3 = kmeans3.fit_predict(x)
clusters4 = kmeans4.fit_predict(x)

info_list = list(zip( clusters1, clusters2, clusters3, clusters4))

df = pd.DataFrame( info_list,
                   columns = [ 'C1', 'C2', 'C3', 'C4'])

obs = adata.obs
obs.reset_index(drop=True, inplace=True)
df.reset_index(drop=True,inplace=True)
cluster_info = pd.concat([obs, df], axis=1)

cluster_info.to_csv(outputfile)


#Print Closing Message and Exit-------------------------------------
now = strftime("%Y-%m-%d %H:%M:%S", localtime())
print('[' + now + ']', 'Homolig clustering completed.')
