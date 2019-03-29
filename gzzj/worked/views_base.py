import json

from django.core import serializers
from django.http import JsonResponse
from django.views.generic.base import View

from worked.models import Gzzj


class GzzjListView(View):
    def get(self, request):
        gzzj = Gzzj.objects.all()
        json_data = serializers.serialize('json', gzzj)
        json_data = json.loads(json_data)

        return JsonResponse(json_data, safe=False)
