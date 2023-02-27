from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpRequest, request, HttpResponse
from django.core.files.storage import default_storage
import os
import subprocess


# Create your views here.

# Handle home route
def home(request):
      return render(request, 'filemgmt/home.html')

# Handle dashboard route
def dashboard(request):
    context = {
        "current_working_directory": os.getcwd(),
        "file_list": subprocess.check_output('ls', shell=True).decode('utf-8').split('\n')
    }
    return render(request, 'filemgmt/dashboard.html', context)

# Handle 'change directory' route
def cd(request):
    # runs command to change to directory specified by path
    os.chdir(request.GET['path'])

    # redirect to file manager root page
    return redirect('/dashboard/')

# handle 'make directory' route
def md(request):
    # create new folder
    os.mkdir(request.GET['folder'])

    # redirect to file manager
    return redirect('/dashboard/')

# handle 'make file' command
def mf(request):
    # create new file
    os.system('touch -f ' + request.GET['file'] + '.txt')

    return redirect('/dashboard/')

# handle 'remove directory' command
def rmdir(request):
    # remove specified directory
    os.system('rm -f -r ' + request.GET['dir'])

    # redirect to file manager
    return redirect('/dashboard/')

# handle 'remove file' command
def rm(request):
    # remove specified file
    os.system('rm -f ' + request.GET['file'])

    # redirect to file manager
    return redirect('/dashboard')    

# view text files
def view(request):
    # return the file content
    resp = subprocess.check_output('cat ' + request.GET['file'], shell=True).decode('utf-8').replace('\n', '<br>')
    return HttpResponse(resp)

# Sending the file to the user
def upload(request):
    if request.method == 'POST':
       file = request.FILES['file']
       file_name = default_storage.save(file.name,file)
       res = file

    return redirect('/dashboard')











