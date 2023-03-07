from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .forms import RegForm,DeptForm,ManagerForm
from .models import RegModel,Department,Manager
# Create your views here.

class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request):
        form_data=RegForm(request.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            name=form_data.cleaned_data.get('name')
            age=form_data.cleaned_data.get('age')
            em=form_data.cleaned_data.get('email')
            ex=form_data.cleaned_data.get('experiance')  
            RegModel.objects.create(name=name,age=age,email=em,experiance=ex)
            messages.success(request,"Registration success")
            return redirect('reg')
        else:
            messages.error(request,"Registration failed")
            return render(request,"registration.html",{"form":form_data})



    
# class Home(View):
#     def get(self,request):
#         return render(request,"home.html")   

        



class ViewEmp(View):
    def get(self,request):
        emp=RegModel.objects.all()
        return render(request,"viewemp.html",{'data':emp})




class DeleteEmp(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        #print(eid)
        eob=RegModel.objects.get(eid=id)
        eob.delete()
        return redirect('vemp')



class EditEmp(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        emp=RegModel.objects.get(eid=id)
        form=RegForm(initial={'name':emp.name,'age':emp.age,'email':emp.email,'experiance':emp.experiance})
        return render(request,"editemp.html",{'form':form})
    def post(self,request,*args,**kwargs):
        form=RegForm(request.POST)
        id=kwargs.get('id')
        if form.is_valid():
            name=form.cleaned_data.get('name')
            age=form.cleaned_data.get('age')
            em=form.cleaned_data.get('email')
            ex=form.cleaned_data.get('experiance')  
            RegModel.objects.filter(eid=id).update(name=name,age=age,email=em,experiance=ex)
            return redirect('vemp')
        else:
            return redirect('editemp')



class DeptView(View):
    def get(self,request,*args,**kwargs):
        form=DeptForm()
        return render(request,"deptreg.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form_data=DeptForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Department Added")
            return redirect('home')
        else:
            messages.error(request,"Department Registration Failed")
            return redirect('dept')



class ViewDept(View):
    def get(self,request):
        dep=Department.objects.all()
        return render(request,"viewdept.html",{'data':dep})




class DeleteDept(View):
    def get(self,request,*args,**kwargs):
        did=kwargs.get("did")
        dep=Department.objects.get(id=did)
        dep.delete()
        return redirect('dept1')



class DeptEdit(View):
    def get(self,request,*args,**kwargs):
        d_id=kwargs.get("did")
        dep=Department.objects.get(id=d_id)
        form=DeptForm(instance=dep)
        return render(request,"editdept.html",{'form':form})
    def post(self,request,*args,**kwargs):
        d_id=kwargs.get('did')
        dept=Department.objects.get(id=d_id)
        form_data=DeptForm(request.POST,instance=dept)
        if form_data.is_valid():
            form_data.save()
            return redirect('dept1')
        else:
            return redirect('editdept')


class MangerReg(View):
    def get(self,request):
        form=ManagerForm()
        return render(request,"addman.html",{'form':form})
    def post(self,request):
        form_data=ManagerForm(request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('home')
        else:
            return redirect('addman')




class ManagerList(View):
    def get(self,request):
        mng=Manager.objects.all()
        return render(request,"viewmangr.html",{'data':mng})



class DeleteMan(View):
    def get(self,request,*args,**kwargs):
        did=kwargs.get("did")
        dep=Manager.objects.get(id=did)
        dep.delete()
        return redirect('viewman')



class ManEdit(View):
    def get(self,request,*args,**kwargs):
        d_id=kwargs.get("did")
        dep=Manager.objects.get(id=d_id)
        form=ManagerForm(instance=dep)
        return render(request,"editman.html",{'form':form})
    def post(self,request,*args,**kwargs):
        d_id=kwargs.get('did')
        dept=Manager.objects.get(id=d_id)
        form_data=ManagerForm(request.POST,files=request.FILES,instance=dept)
        if form_data.is_valid():
            form_data.save()
            return redirect('viewman')
        else:
            return redirect('editman')




class Home(View):
  def get(self,request):
    return render(request,"home.html")   
