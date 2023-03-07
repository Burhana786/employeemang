from django import forms
from.models import Department,Manager

class RegForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter name","class":"form-control"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter age","class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Enter e-mail","class":"form-control"}))
    experiance=forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Enter experiance","class":"form-control"}))
    def clean(self):
        cleaned_data=super().clean()
        exp=cleaned_data.get('experiance')
        if exp<0:
            msg="Invalid experiance"
            self.add_error('experiance',msg)



class DeptForm(forms.ModelForm):
    class Meta:
        model=Department
        fields="__all__"
        widgets={
            'dept_name':forms.TextInput(attrs={'placeholder':'Enter department name','class':'form-control'}),
            'dept_no':forms.TextInput(attrs={'placeholder':'Enter department no:','class':'form-control'}),
            'dept_description':forms.TextInput(attrs={'placeholder':'Enter department description','class':'form-control'})
            }


class ManagerForm(forms.ModelForm):
    class Meta:
        model=Manager
        fields="__all__"
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'pic':forms.FileInput(attrs={'class':'form-control'})
            }