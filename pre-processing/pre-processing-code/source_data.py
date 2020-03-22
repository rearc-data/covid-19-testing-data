import os
import pandas as pd
import boto3

source_dataset_url = "https://covidtracking.com/api/"

def source_dataset(s3_bucket, new_s3_key):
	states = pd.read_csv(source_dataset_url + "states.csv", header=0, index_col=None)
	states.to_csv("/tmp/states.csv", index=False)

	states_daily = pd.read_csv(source_dataset_url + "states/daily.csv", header=0, index_col=None)
	states_daily.to_csv("/tmp/states_daily.csv", index=False)

	states_info = pd.read_csv(source_dataset_url + "states/info.csv", header=0, index_col=None)
	states_info.to_csv("/tmp/states_info.csv", index=False)

	us = pd.read_csv(source_dataset_url + "us.csv", header=0, index_col=None)
	us.to_csv("/tmp/us.csv", index=False)

	us_daily = pd.read_csv(source_dataset_url + "us/daily.csv", header=0, index_col=None)
	us_daily.to_csv("/tmp/us_daily.csv", index=False)

	counties = pd.read_csv(source_dataset_url + "counties.csv", header=0, index_col=None)
	counties.to_csv("/tmp/counties.csv", index=False)

	#uploading new s3 dataset
	s3 = boto3.client('s3')
	folder = "/tmp"

	for filename in os.listdir(folder):
		print(filename)
		s3.upload_file('/tmp/' + filename, s3_bucket, new_s3_key + filename)
