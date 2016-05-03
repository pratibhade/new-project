from django.http import HttpResponse
import MySQLdb
import json
from django.template.loader import get_template
from django.db import connection
from django.shortcuts import render_to_response
import simplejson as json

def get_fname(request):
	cursor = connection.cursor()
	cursor.execute ("select * from faculty")
	results=cursor.fetchall()
	x=cursor.description
	resultsList = []   
	for r in results:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)
	my_template="test33.html"
	#return HttpResponse(json.dumps(resultsList))
	return render_to_response(my_template, {"results":resultsList})
	

