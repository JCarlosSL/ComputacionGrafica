from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from .models import Post,Post1
from .forms import PostForm,Post1Form
from django.core.files import File
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from .PointOperator.PointOperator import PointOperator as PO

#direccion a operadores punto#
from .HistogramEqual.HistogramEqual import HistogramEqual as HE
from .Lab2.contrastStretching import ConstS as CS
from .LogarithmOperator.pointOperator import pointOperator as _PO
from .Threasholding.th import Threshold as TH
from .OperadorExponencial.OpExp import pointOperator as POO
from .Sustraccion.subtraccion import subtraccion as SO
from .Addition.Addition import AdditionOperator as AO
from .Blending.Blending import blendingOperator as BO
from .Division.Division import divisionOperator as DO
from .multiplication.Multiplication import MultiplicationOperator as MO
# Create your views here.

def resize(img1,img2):
	size1=img1.shape[0]+img1.shape[1]
	size2=img2.shape[0]+img2.shape[1]
	
	if(size1 > size2):
		img1 = cv.resize(img1,img2.shape[1::-1])
	else:
		img2 = cv.resize(img2,img1.shape[1::-1])
	return img1,img2

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{
        'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def post_scale(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            data = PO(img)
            newimg = data.contrastStretching()
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})

def post_save(request,pk):
    post1 = get_object_or_404(Post1,pk=pk)
    post2 = get_object_or_404(Post, pk=post1.post.pk)
    post2.imagen.delete()
    direccion = post1.result.url
    ropen=open(direccion[1:],'rb')
    post2.imagen.save(direccion[14:],File(ropen),save=True)
    post2.save()
    return redirect('post_detail',pk=post2.pk)

def post_show(request,pk,pk1):
    post1 = get_object_or_404(Post, pk=pk)
    post2 = get_object_or_404(Post1, pk=pk1)
    return render(request, 'blog/post_show.html', {'post': post1,
        'post1': post2})
        
def post_thresholding(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            data = TH(img)
            l=0
            r=255
            if post1.limite_a:
            	l=int(post1.limite_a)
            if post1.limite_b:
           		r=int(post1.limite_b)
            
            newimg = data.thresholding(l,r)
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_contrast(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            data = CS(img)
            
            d=15
            if post1.limite_a:
            	d=int(post1.limite_a)
            
            data.CDlimit(d)
            newimg = data.Stretch()
            
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_equalizer(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            data = HE(img)
            newimg = data.Equalization()
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_logaritmo(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            data = _PO(img)
            
            d=15
            if post1.limite_a:
            	d=int(post1.limite_a)
            
            newimg = data.logarithmOperator(d)
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_raiz(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            data = _PO(img)
            
            d=15
            if post1.limite_a:
            	d=int(post1.limite_a)
            newimg = data.raizOperator(d)
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_exponencial(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            data = POO(img)
            b=1.005
            c=5
            if post1.limite_a:
            	b=post1.limite_a
            if post1.limite_b:
            	c=post1.limite_b
            
            newimg = data.expoOperator(b,c)
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})

def post_raizpower(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            data = POO(img)
            
            b=1.005
            c=5
            if post1.limite_a:
            	b=post1.limite_a
            if post1.limite_b:
            	c=post1.limite_b
            
            newimg = data.raiseOperator(b,c)
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        

def post_adicion(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            
            verbose=False
            r=1
            if post1.limite_a:
            	verbose=True
            	r=int(post1.limite_a)
            if post1.imagen:
            	direc = post1.imagen.url
            	img1 = cv.imread('media/images/'+direc[7:],0)
            	img,img1 = resize(img,img1)
            	
            data = AO(img)
            if verbose:
            	newimg=data.additionC(r)
            else:
            	newimg=data.additionImg(img1)
            	
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_sustraccion(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            
            verbose=False
            r=1
            if post1.limite_a:
            	verbose=True
            	r=int(post1.limite_a)
            if post1.imagen:
            	direc = post1.imagen.url
            	img1 = cv.imread('media/images/'+direc[7:],0)
            	img,img1 = resize(img,img1)
            	
            data = SO(img)
            if verbose:
            	newimg=data.subtraccionC(r)
            else:
            	newimg=data.subtraccionImg(img1)
            
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_multiplicacion(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:])  
            
            verbose=False
            r=1
            if post1.limite_a:
            	verbose=True
            	r=int(post1.limite_a)
            if post1.imagen:
            	direc = post1.imagen.url
            	img1 = cv.imread('media/images/'+direc[7:],0)
            	img,img1 = resize(img,img1)
            	
            data = MO(img)
            if verbose:
            	newimg=data.MultiplicacionC(r)
            else:
            	newimg=data.multiplicacionImg(img1)
            
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_division(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            
            verbose=False
            r=1
            if post1.limite_a:
            	verbose=True
            	r=int(post1.limite_a)
            if post1.imagen:
            	direc = post1.imagen.url
            	img1 = cv.imread('media/images/'+direc[7:],0)
            	img,img1 = resize(img,img1)
            	
            data = DO(img)
            if verbose:
            	newimg=data.divisionC(r)
            else:
            	newimg=data.divisionImg(img1)
            
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_blending(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:])
            
            verbose=False
            r=0.25
            if post1.limite_a:
            	verbose=True
            	r=float(post1.limite_a)
            direc = post1.imagen.url
            img1 = cv.imread('media/images/'+direc[7:])
            img,img1 = resize(img,img1)
            	
            data = BO(img)
            newimg=data.blending(img1,float(r))
              

            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_invert_log_not(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            data = PO(img)
            newimg = data.contrastStretching()
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_log_and_nand(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            data = PO(img)
            newimg = data.contrastStretching()
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_log_or_nor(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            data = PO(img)
            newimg = data.contrastStretching()
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
        
def post_log_xor_xnor(request,pk):
    post = get_object_or_404(Post,pk=pk)
    pageTitle="scale"
    if request.method == "POST":
        form = Post1Form(request.POST,request.FILES)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author = request.user
            post1.post=post

            direccion = post.imagen.url
            img = cv.imread(direccion[1:],0)  
            data = PO(img)
            newimg = data.contrastStretching()
            name = 'images/scale_'+post.imagen.name[7:]
            cv.imwrite('media/'+name,newimg)

            nameh = 'images/sc_h'+post.imagen.name[7:]
            cv.imwrite('media/'+nameh,newimg)
            ropen = open('media/'+name,'rb')
            hopen = open('media/'+nameh,'rb')

            post1.result.save('scale_'+post.imagen.name[7:],File(ropen),save=True)
            post1.histogram.save('sc_h'+post.imagen.name[7:],File(hopen),save=True)
            post1.save()
            return redirect('post_show',pk=post.pk,pk1=post1.pk)

    else:
        form = Post1Form()
    return render(request,'blog/post_scale.html',{'form': form,
        'post':post,
        'pageTitle':pageTitle})
