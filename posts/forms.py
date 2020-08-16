from django import forms
from .models import Post, Comment
from tinymce.widgets import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail', 
        'categories', 'featured', 'previous_post', 'next_post', 'file')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'

    }))
    class Meta:
        model = Comment
        fields = ('content', 'asset_offered')

    # def __init__(self, user, *args, **kwargs):
    #     super(CommentForm, self). __init__(*args, **kwargs)
    #     self.fields['asset_offered'].queryset=Post.objects.filter(author__user=self.request.user)