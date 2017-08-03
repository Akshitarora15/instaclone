from django import forms
from models import UserModel,PostModel,LikeModel,CommentModel


class SignUpForm(forms.ModelForm): #creating signup form
    class Meta:
        model = UserModel
        fields=['email','username','name','password']

class LoginForm(forms.ModelForm):  #creating login form
    class Meta:
        model = UserModel
        fields = ['username', 'password']

class PostForm(forms.ModelForm):  #creaing form for posting an image
    class Meta:
        model=PostModel
        fields=['image','caption']

class LikeForm(forms.ModelForm):  #creating form for liking a pic
    class Meta:
        model = LikeModel
        fields=['post']


class CommentForm(forms.ModelForm):  #creating form for commenting a pic

    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']