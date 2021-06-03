from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import logging
import pandas as pd
import numpy as np
from csv import reader
import matplotlib.pyplot as plt
import io
import urllib, base64
import json

import time
import os
from django.conf import settings


# Create your views here.
#@login_required
def analytics(request):
    return render(request,'analytics/home.html',)




def get_file_data(request, disp_param,disp_param2=0):

	df = pd.read_csv(request.session['file_save_path'])
	print("THe files name is ", request.session['file_save_path'])

	columns = df.columns.tolist()	# file headers
	rows=np.arange(1,df.shape[0],1)
	if disp_param =='ShowAll':
		df_rows = df.values.tolist()    # data as list of list for top 5 rows
	elif disp_param =='Top10':
		df_rows = df.iloc[:10].values.tolist()    # data as list of list for top 5 rows
	elif disp_param =='Bottom5':
		df_rows = df.iloc[-5:].values.tolist()    # data as list of list for top 5 rows
	else:
		df_rows = df.iloc[:settings.TOP_N_ROWS].values.tolist()    # data as list of list for top 5 rows
	return columns, rows, df_rows				#columns returns column names; rows will display rows from 1 to df.shape[0]; df_rows returns selected rows from html select option whereby default is TOP_N_ROWS(5)


# helper function used by other functions when user clicks on uploading a file, this is invoked to upload the file 
def upload_file(request):
	if request.FILES:
		# there is a file upload
		for files in request.FILES:
			logging.debug('result, a file upload was detected')
			file_name = str(request.FILES[files])

			if 'csv' not in file_name.lower():
				return render(request, 'analytics/home.html', {'file_error':True})
			print('Reading file: {}'.format(file_name))

			# file save
			current_timestamp = time.strftime("%y%m%d-%H%M%S")
			file_name = current_timestamp+'_'+ file_name
			file_save_path = os.path.join(settings.MEDIA_ROOT, file_name)
			with open(file_save_path, 'wb') as destination:
				for file_chunk in request.FILES[files].chunks():
					destination.write(file_chunk)  

				# storing file path in django session
				request.session['file_save_path'] = file_save_path
				request.session['file_columns_renamed_yet']=False
				print("The session is " , request.session['file_save_path'])


#@login_required
def result(request):
	# Handle file upload
	if request.FILES:
		# there is a file to upload
		upload_file(request)

	#disp_param1 = request.GET.get('disp1', settings.TOP_N_ROWS)
	disp_param1 = request.GET.get('disp1', 'Top5')			
	disp_param2 = request.GET.get('disp2', 0)
	print(disp_param1)
	print(disp_param2)
	
	if 'file_save_path' in request.session:
		columns, rows, df_rows= get_file_data(request, disp_param1, disp_param2=disp_param2)
		print("number of rows is" , type(columns))
		logging.debug('request, after get_file_data')
	else:
		return render(request, 'analytics/nofile.html', )

	# file read
	context = {
				'columns' : columns, 	#columns returns column names;
				'data_rows' : df_rows, 	#df_rows returns selected rows from html select option whereby default is TOP_N_ROWS(5)
				'rows': rows, 			#rows will display rows from 1 to df.shape[0];
				'disp2':disp_param2,	#select option for number
				'disp1':disp_param1,		#select option for op, bottom, top5, etc
			  }	
	return render(request, 'analytics/home.html', context)





def loadJson(param):
	json_records=param.reset_index().to_json(orient='records')
	data=[]
	data=json.loads(json_records)
	return data



