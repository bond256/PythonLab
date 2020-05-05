from django.shortcuts import render
from django.views import View
from .models import Link
from django.http import Http404, JsonResponse


class Index(View):
    def get(self, request):
        all_links = Link.objects.all()
        context = {
            'all_links':all_links
        }
        return render(request, 'Lab1/index.html', context=context)

class LinkView(View):
    def get(self, request, id):
        link = Link.objects.get(id=id)
        context = {
            'link':link
        }
        return render(request, 'Lab1/link.html', context=context)

class AjaxAddVisit(View):
    def get(self, request):
        if request.is_ajax():
            id = request.GET.get('id')
            link = Link.objects.get(id=id)
            link.add_visit()
            link.save()
            return JsonResponse({'message':'Success'})
        else:
            raise 404

class AdminStatistics(View):
    def get(self, request):
        if request.user.is_superuser:
            all_links = Link.objects.all()
            context = {
                'all_links':all_links,
            }
            return render(request,'Lab1/admin-stat.html', context=context)
        else:
            raise 404