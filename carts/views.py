from django.http import JsonResponse
from .models import CartLine


def _get_data_from_request(request):
    return request.POST.dict()


def cart_detail(request):
    lines = CartLine.objects.all()
    return JsonResponse({"lines": [line.to_dict() for line in lines]})
