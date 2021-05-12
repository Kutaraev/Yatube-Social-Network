from django.forms import ModelForm

from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['group', 'text', 'image']
        labels = {'group': 'Сообщество',
                  'text': 'Сообщение',
                  'image': 'Картинка'}
        help_texts = {'group': 'Выбирайте с умом',
                      'text': 'Введите текст сообщения',
                      'image': 'Добавьте картинку'}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
