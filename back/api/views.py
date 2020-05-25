from django.views.generic.list import BaseListView
from django.http import JsonResponse

from blog.models import Post
from api.views_util import obj_to_post

class ApiPostLV(BaseListView):
    model = Post

    def get_queryset(self):
        paramTag = self.request.GET.get('tag')
        if paramTag:
            qs = Post.objects.filter(tags__name=paramTag)
        else:
            qs = Post.objects.all()
        return qs

    def render_to_response(self, context, **response_kwargs):
        postList = [obj_to_post(obj) for obj in context['object_list']]
        return JsonResponse(data=postList, safe=False, status=200)