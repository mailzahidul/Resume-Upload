from django import forms
from .models import Resume_info

STATE_CHOICE = {
    ('dhaka','Dhaka'),
    ('chitfagram','Chitfagram'),
    ('khunla','Khulna'),
    ('rajshahi','Rajshahi'),
    ('borishal','Borishal'),
    ('rangpur','Rangpur')
}
GENDER_CHOICE = {
    ('m', 'Male'),
    ('f','Female' ),
    ('o','Others'),
}

class Resume_info_forms(forms.ModelForm):
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER_CHOICE))
    class Meta:
        model = Resume_info
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin_code', 'state', 'mobile', 'email', 'job_city', 'profile_img', 'my_file']
        labels = {
            'name':'Full Name', 'dob':'Date Of Birth', 'job_city':'Prefferd Location', 'profile_img':'Profile Image', 'my_file':'Upload CV'
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'dob' : forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            # 'gender': forms.RadioSelect(choices=GENDER_CHOICE)    # Its shows an extra blank radio button
            'locality' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'pin_code' : forms.TextInput(attrs={'class':'form-control'}),
            'state' : forms.Select(attrs={'class':'form-control'}),
            'mobile' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'job_city' : forms.CheckboxSelectMultiple(attrs={}, choices=STATE_CHOICE)
        }