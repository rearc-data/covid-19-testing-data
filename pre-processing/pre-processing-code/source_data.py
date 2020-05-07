import os
import boto3
import urllib.request

def source_dataset(s3_bucket, new_s3_key):

	source_dataset_url = 'https://covidtracking.com/api/v1/'

	api_filenames = [
		'states/current',
		'states/daily',
		'states/info',
		'us/current',
		'us/daily',
		'counties',
		'cdc/daily',
		'urls',
		'states/screenshots',
		'press'
	]

	# Download the file from `url` and save it locally:
	for filename in api_filenames:
		print(filename, 'csv')
		urllib.request.urlretrieve(
			source_dataset_url + filename + '.csv', '/tmp/' + filename.replace('/', '_') + '.csv')
		print(filename, 'json')
		urllib.request.urlretrieve(
			source_dataset_url + filename + '.json', '/tmp/' + filename.replace('/', '_') + '.json')

	# uploading new s3 dataset
	s3 = boto3.client('s3')
	folder = "/tmp"

	asset_list = []

	for filename in os.listdir(folder):
		print(filename)
		s3.upload_file('/tmp/' + filename, s3_bucket, new_s3_key + filename)

		asset_list.append({'Bucket': s3_bucket, 'Key': new_s3_key + filename})

	return asset_list