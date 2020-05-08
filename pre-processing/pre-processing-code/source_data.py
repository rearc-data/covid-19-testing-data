import os
import boto3
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from multiprocessing.dummy import Pool

def data_to_s3(data):

	# catching any issues if an error occured and returns `False`
	# otherwise downloads and uploads to s3

	source_dataset_base = 'https://covidtracking.com/api/v1/'

	try:
		response = urlopen(source_dataset_base + data)

	except HTTPError as e:
		print('HTTPError: ', e.code, data)
		return False

	except URLError as e:
		print('URLError: ', e.reason, data)
		return False

	else:
		filename = data.replace('/', '_')
		file_location = '/tmp/' + filename

		with open(file_location, 'wb') as f:
			f.write(response.read())

		# variables/resources used to upload to s3
		s3_bucket = os.environ['S3_BUCKET']
		data_set_name = os.environ['DATA_SET_NAME']
		new_s3_key = data_set_name + '/dataset/'
		s3 = boto3.client('s3')

		s3.upload_file(file_location, s3_bucket, new_s3_key + filename)			
		
		print('Uploaded: ' + filename)

		# deletes to preserve limited space in aws lamdba
		os.remove(file_location)

		# dicts to be used to add assets to the dataset revision
		return {'Bucket': s3_bucket, 'Key': new_s3_key + filename}

def source_dataset():

	# list of enpoints to be used to access data included with product
	api_endpoints = [
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

	# multithreading speed up accessing data, making lambda run quicker
	with (Pool(20)) as p:
		asset_list = p.map(data_to_s3, [
					   *map(lambda x: x + '.csv', api_endpoints), *map(lambda x: x + '.json', api_endpoints)])

	# asset_list will only include false if there was a problem
	# accessing one of the datasets used to form the asset_list
	if False in asset_list:
		return False

	# asset_list is returned to be used in lamdba_handler function
	return asset_list