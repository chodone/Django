from django import forms
from .models import Travel



class TravelForm(forms.ModelForm):

    location = forms.CharField(
        label='Location',
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'ex)제주도',


            }
        )
    )
    
    plan = forms.CharField(
        label='Plan',
        widget=forms.Textarea(
            attrs={
                'placeholder' : 'ex)슈슉,슉',
                'rows' : 5,
                'cols' : 50,

            }
        ),
        error_messages={
            'required' : 'please enter your content',
        }
    )

    start_date = forms.DateField(
        label='Start date',
        widget=forms.TextInput(
            attrs={
                'PlaceHolder' : 'ex)2022-02-22'
            }
        )
    )

    end_date = forms.DateField(
        label='End date',
        widget=forms.TextInput(
            attrs={
                'PlaceHolder' : 'ex)2022-02-22'
            }
        )
    )




    class Meta:
        model = Travel # 어떤 모델을 기반으로 할지
        fields = '__all__' # 사용자로부터 입력받은 모든 필드들