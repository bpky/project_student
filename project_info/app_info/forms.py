from .forms import forms

class StudentDetailForm(Forms.ModelForm):
    passport = forms.CharField(widget=passwordInput)
    class Meta:
        #fields = "__all__" - to load all fields
        fields = "__all__"
        fields = ("First_name", "middle_name","contact","email","passport")
        model = StudentDetail

class StudentLoginForm(forms.ModelForm):
    class Meta:
        field = ("email", "password")
        model = StudentDetail