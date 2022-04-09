from django.shortcuts import render

# Create your views here.
def Calculator(request):
    result=''
    try:
        if request.method=='POST':
            num1=eval(request.POST.get('first'))
            num2=eval(request.POST.get('second'))
            operation=request.POST.get('but')
            if operation=='Add':
                result=num1+num2
            elif operation=='Sub':
                result=num1-num2
            elif operation=='Mul':
                result=num1*num2
            elif operation=='Div':
                result=num1/num2
    except (ZeroDivisionError,TypeError,NameError,AttributeError,SyntaxError):
        result='Invaild Operation...'
    return render(request,'calculator.html',{'result':result})