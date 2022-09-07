from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'jp'

#     NATION_CHOICES = [ 
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]
    

#     title = forms.CharField(max_length=10) #form에서는 max_length값이 필수는 아니다
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=NATION_CHOICES, widget=forms.RadioSelect)

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article # 어떤 모델을 기반으로 할지
        fields = '__all__' # 사용자로부터 입력받은 모든 필드들
