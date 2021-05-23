from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=11, label='Please Enter Mobile Number',
                               widget=forms.widgets.TextInput(
                                   attrs={'class': 'layui-input', 'placeholder': 'Please Enter Mobile Number',
                                          'lay-verify': 'required|phone', 'id': 'username'}), )
    password = forms.CharField(max_length=20, label='Please Enter Password',
                               widget=forms.widgets.PasswordInput(
                                   attrs={'class': 'layui-input', 'placeholder': 'Please Enter Password',
                                          'lay-verify': 'required|password', 'id': 'password'}), )

    # 自定义表单字段username的数据清洗
    def clean_username(self):
        if len(self.cleaned_data['username']) == 11:
            return self.cleaned_data['username']
        else:
            raise ValidationError('Please Enter Mobile Number')


class LoginModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': 'Please Enter Mobile Number',
            'password': 'Please Enter Password',
        }
        error_messages = {
            '__all__': {'required': '请输入内容',
                        'invalid': '请检查输入内容'},
        }
        # 定义widgets，设置表单字段对应HTML元素控件的属性
        widgets = {
            'username': forms.widgets.TextInput(
                                   attrs={'class': 'layui-input', 'placeholder': 'Please Enter Mobile Number',
                                          'lay-verify': 'required|phone', 'id': 'username'}),
            'password': forms.widgets.PasswordInput(
                                   attrs={'class': 'layui-input', 'placeholder': 'Please Enter Password',
                                          'lay-verify': 'required|password', 'id': 'password'})
        }

    # 自定义表单字段username的数据清洗
    def clean_username(self):
        if len(self.cleaned_data['username']) == 11:
            return self.cleaned_data['username']
        else:
            raise ValidationError('Please Enter Mobile Number')
