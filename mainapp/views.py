from django.http import request, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.
def index(request):
    siteform = SiteForm(initial={"created_by":request.user})
    siteusers = Siteuserroles.objects.filter(user=request.user)
    site = Site.objects.all()
    context = {'siteform':siteform, 'siteusers':siteusers, 'site':site}
    return render(request, 'page/index.html', context)

def repository(request):
    faculties = Faculty.objects.all()
    departments = Department.objects.all()
    folders = Folder.objects.filter(is_rep=True)
    files = File.objects.filter(is_rep=True)
    create_folder = FolderForm(initial={'created_by':request.user, 'is_rep':True})
    fileform = FileForm(initial={'uploaded_by':request.user, 'is_rep':True})
    context = {
        'faculties':faculties, 'departments':departments, 'create_folder':create_folder, 'folders':folders,
        'form':fileform, 'files':files,
    }
    return render(request, 'page/repository.html', context)

def mysite(request):
    folders = Folder.objects.filter(is_rep=False, created_by=request.user, main_folder=None, department=None, faculty=None)
    files = File.objects.filter(is_rep=False, uploaded_by=request.user, folder=None, department=None, faculty=None, task_name=None)
    create_folder = FolderForm(initial={'created_by':request.user})
    fileform = FileForm(initial={'uploaded_by':request.user})
    context = {
        'create_folder':create_folder, 'folders':folders,
        'form':fileform, 'files':files,
    }
    return render(request, 'page/mysite.html', context)

def open_site(request, pk):
    site = Site.objects.get(site_url=pk)
    files = File.objects.filter(site=site)
    create_folder = FolderForm(initial={'created_by':request.user, 'site':site})
    folders = Folder.objects.filter(site=site)
    fileform = FileForm(initial={'uploaded_by':request.user, 'site':site})
    context = {
        'site':site, 'files':files, 'create_folder':create_folder, 'form':fileform, 'folders':folders,
    }
    return render(request, 'page/mysite.html', context)

def faculty(request, pk):
    faculty = Faculty.objects.get(id=pk)
    files = File.objects.filter(faculty=faculty)
    folders = Folder.objects.filter(faculty=faculty)
    create_folder = FolderForm(initial={'created_by':request.user, 'faculty':faculty})
    fileform = FileForm(initial={'uploaded_by':request.user, 'faculty':faculty})
    context ={
        'facul':faculty, 'files':files, 'create_folder':create_folder, 'form':fileform, 'folders':folders,
    }
    return render(request, 'page/mysite.html', context)

def department(request, pk):
    department = Department.objects.get(id=pk)
    files = File.objects.filter(department=department)
    folders = Folder.objects.filter(department=department)
    create_folder = FolderForm(initial={'created_by':request.user, 'department':department})
    fileform = FileForm(initial={'uploaded_by':request.user, 'department':department})
    context = {
        'depart':department, 'files':files, 'folders':folders, 'create_folder':create_folder, 'form':fileform,
    }
    return render(request, 'page/mysite.html', context)

def folder(request, pk):
    folder = Folder.objects.get(folder_url=pk)
    files = File.objects.filter(folder=folder)
    folders = Folder.objects.filter(main_folder=folder)
    create_folder = FolderForm(initial={'created_by':request.user, 'main_folder':folder})
    fileform = FileForm(initial={'uploaded_by':request.user, 'folder':folder})
    context = {
        'folders':folders, 'files':files, 'create_folder':create_folder, 'form':fileform, 'fold':folder,
    }
    return render(request, 'page/mysite.html', context)

def savefolder(request):
    folder = FolderForm(request.POST)
    url = request.POST.get('request')
    if folder.is_valid():
        folder.save()
        return redirect(f'{url}')

def save_file(request):
    form = FileForm(request.POST, request.FILES)
    url = request.POST.get('request')
    if form.is_valid():
        form.save()
        return redirect(f'{url}')

def docview(request, pk):
    file = File.objects.get(file_url=pk)
    context = {'file':file}
    return render(request, 'page/docview.html', context)

def add_site_members(request, pk):
    site = Site.objects.get(site_url=pk)
    users = MyUser.objects.all()
    siteusers = Siteuserroles.objects.filter(site=site)
    context = {'users':users, 'site':site, 'siteusers':siteusers}
    return render(request, 'page/add_site_members.html', context)

def add_site_member_ajax(request):
    user = request.POST.get('username')
    selvalue = request.POST.get('selvalue')
    site = request.POST.get('site')
    print(f"{user}, {selvalue}, {site}")
    siteuser = MyUser.objects.get(username = user)
    siteid = Site.objects.get(site_name=site)  
    ifexist = Siteuserroles.objects.filter(site=siteid, user=siteuser)
    if ifexist:
        data = {
            "message":"error"
        }
        return JsonResponse(data)
    else:
        siteUserRole = Siteuserroles(site=siteid, user=siteuser, role="selvalue")
        siteUserRole.save()
        saved = f"{user} saved"
        data = {
            "message":f"{saved}"
        }
        return JsonResponse(data)
        

def save_siteform(request):
    siteform = SiteForm(request.POST)
    site = request.POST.get('site_url')
    if siteform.is_valid():
        print(siteform)
        siteform.save()
        sites = Site.objects.get(site_url=site)
        siteusers = Siteuserroles(user=request.user, site=sites, role="manager")
        siteusers.save()
        return redirect('mainapp:add_site_members', site)
    else: 
        print(siteform.errors)

def userexists(request):
    data = {

    }
    return JsonResponse(data)