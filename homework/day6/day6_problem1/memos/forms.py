from django import forms
from .models import Memo



class MemoForm(forms.ModelForm):

    summary = forms.CharField(
        label='summary',
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'summary',


            }
        )
    )
    memo = forms.CharField(
        label='memo',
        widget=forms.Textarea(
            attrs={
                'placeholder' : 'memo',
                'rows' : 5,
                'cols' : 50,

            }
        ),
        error_messages={
            'required' : 'please enter your content',
        }
    )

    class Meta:
        model = Memo # 어떤 모델을 기반으로 할지
        fields = '__all__' # 사용자로부터 입력받은 모든 필드들