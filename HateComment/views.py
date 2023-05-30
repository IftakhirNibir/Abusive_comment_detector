from django.shortcuts import render
import AbusiveCmt as ac
from django.http import FileResponse
import os
import pandas as pd
import csv 

# Create your views here.

def home(request):
    if request.method == 'POST':
        cmt = request.POST['input_text']
        comment = str(cmt)
        output = ac.abusive_comment(comment)
        a =  "The Comment is not Abusive "
        b = "The Comment is Abusive "
        good = ""
        bad = ""
        if output == a:
            good = a
        else:
            bad = b
       
        return render(request,'index.html',{'good':good,'bad':bad,'cmt':comment})
        # return JsonResponse({'cmt':output}) 
    return render(request, 'index.html')

def homepage(request):
    return render(request,'main.html')

def package(request):
    return render(request,'package.html')

def data(request):
    if request.method == 'POST':
        cmt = request.POST['input_text']
        type = request.POST['cars']
        df = pd.read_csv('data.csv')
        new_row = {'comment_text': cmt, 'abusive': type}
        a = len(df['comment_text'])
        df.loc[a] = new_row
        df.to_csv('data.csv', index=False)
    return render(request, 'data.html')       

def packagepage(request):
    filename = 'D:\Cancer Treatment Aid\My_Django_Projects\Final\Final\Abusive_Comment_Detector\package.zip'
    file = open(filename, 'rb')
    response = FileResponse(file, content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(filename)}"'
    return response

def checker(request):
    if request.method == 'POST':
        cmt = request.POST['input_text']
        comment = str(cmt)
        output = ac.abusive_comment(comment)
        a =  "The Comment is not Abusive "
        b = "The Comment is Abusive "
        good = ""
        bad = ""
        if output == a:
            good = a
        else:
            bad = b
       
        return render(request,'checker.html',{'good':good,'bad':bad,'cmt':comment})
    return render(request, 'checker.html')