import json

from django.forms import model_to_dict
from django.http import HttpResponse,  JsonResponse
import sys
from .models import Results
from django.shortcuts import render
from .forms import MyForm


# Create your views here.
def greet(request):
    first_name = request.GET['first']
    last_name = request.GET['last']
    return HttpResponse(f"<h1>Hello {first_name} {last_name}</h1>")

def operation(request):
    # print(request.GET['num1'])
    # print("after request hello")
    # print(request.__dict__, file=sys.stderr)
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    action = request.GET['action']

    try:
        db_value = Results.objects.get(num1=num1, num2=num2, action=action)

        if db_value:
            print(db_value.result)
            return JsonResponse(model_to_dict(db_value), safe=False)

    except:
        if action == Results.ADD:
            result = num1+num2
        elif action == Results.SUB:
            result = num1-num2
        elif action == Results.MULTI:
            result = num1*num2
        elif action == Results.DIVIDE:
            try:
                result = num1/num2
            except ZeroDivisionError as e:
                result = e
        else:
            result = num1 + num2

        result_object = Results(num1=num1, num2=num2, action=action, result=result)
        result_object.save()
        return HttpResponse(result)


def assignment(request):

    assignment_result = {}
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    action = request.GET['action']
    was_avl_in_db = False
    check = Results.objects.all().values()
    assignment_result["past_results"] = list(check)
    try:
        db_value = Results.objects.get(num1=num1, num2=num2, action=action)
        if db_value:
            was_avl_in_db = True
            assignment_result["result"] = db_value.result
            assignment_result["was_avl_in_db"] = was_avl_in_db
            return JsonResponse(assignment_result, safe=False)

    except:
        print("result")
        if action == Results.ADD:
            result = num1 + num2
        elif action == Results.SUB:
            result = num1 - num2
        elif action == Results.MULTI:
            result = num1 * num2
        elif action == Results.DIVIDE:
            try:
                result = num1 / num2
            except ZeroDivisionError as e:
                result = e
        else:
            result = num1 + num2

        result_object = Results(num1=num1, num2=num2, action=action, result=result)
        result_object.save()
        assignment_result["result"] = result
        assignment_result["was_avl_in_db"] = was_avl_in_db
        return JsonResponse(assignment_result, safe=True)


def delete_record(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    action = request.GET['action']
    try:
        db_value = Results.objects.get(num1=num1, num2=num2, action=action)
        db_value.delete()
    except Results.DoesNotExist:
        return JsonResponse({"error":"No such value found in database"})


    return JsonResponse(model_to_dict(db_value), safe=False)


def update_record(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    action = request.GET['action']
    try:
        db_value = Results.objects.get(num1=num1, num2=num2, action=action)
    except:
        pass

    db_value.num1 = 4

    print(db_value)
    return JsonResponse(model_to_dict(db_value), safe=False)


def check(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            action = form.cleaned_data['action']
            if action == '1':
                result = num1 + num2
            elif action == '2':
                result = num1 - num2
            elif action == '3':
                result = num1 * num2
            elif action == '4':
                try:
                    result = num1 / num2
                except ZeroDivisionError as e:
                    result = e
            else:
                result = num1 + num2

            result_object = Results(num1=num1, num2=num2, action=action, result=result)
            result_object.save()

    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})
    # return HttpResponse("I am just checking is this is working or not")




