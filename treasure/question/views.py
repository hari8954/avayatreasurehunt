from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .forms import DynamicAnswerForm
from .models import Question,Clue

# Create your views here.
def submit_answers(request):
    questions = Question.objects.all()

    if request.method == 'POST':
        form = DynamicAnswerForm(request.POST, questions=questions)
        if form.is_valid():
            name = form.cleaned_data['name']

            for q in questions:
                answer = form.cleaned_data[f'answer_{q.id}']
                question = Question.objects.get(question=q.question)
                actualAns = str(question.answer)
                if answer.casefold() != actualAns.casefold():
                    messages.error(request,"Wrong answers, Please give correct answer to get the clue")
                    return render(request,"question/question.html",{'form':form})
            clue = Clue.objects.filter(assigned=False).first()
            if clue is not None:
                clue.teamName=name
                clue.assigned=True
                clue.save()
                return render(request,"question/display.html", {'object':clue.clue})
            else :
                return HttpResponse("Thanks for participating!!!")

    else:
        form = DynamicAnswerForm(questions=questions)
    return render(request,"question/question.html",{'form':form})