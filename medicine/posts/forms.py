from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea, label="Текст отзыва", help_text="Текст нового отзыва"
    )
    author = forms.CharField(label="Имя", help_text="Пожалуйста, представьтесь")

    class Meta:
        model = Post
        fields = ("author", "text", "image")
