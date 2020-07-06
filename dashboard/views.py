from django.shortcuts import render

# Create your views here.

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)