# coding:utf-8
from django.shortcuts import render
from models import Question
# Create your views here.


def index(request):
    ques=Question.objects.all()
    return render(request,'index.html',{'Ques':ques})

def show(request,id):
    que=Question.objects.get(pk=id)
    choice=que.choices_set
    choices=choice.all()
    con={'Ques':que,'Chos':choices}
    return render(request,'show.html',con)

def showAction(request,id):
    que=Question.objects.get(pk=id)
    choice=que.choices_set
    choices=choice.all()
    try:
        num=request.POST['choice']
    except:
        return render(request,'show.html',{'Chos':choices,'Ques':que,'myERROR':'你还未投票，请重新投票！'})
    target=choices.get(pk=num)
    target.vote+=1
    target.save()
    que=Question.objects.get(pk=id)
    return render(request,'showresult.html',{'Que':que})


