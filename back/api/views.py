from django.http import JsonResponse
from django.views.generic.edit import BaseCreateView
from django.views.generic.list import BaseListView

from api.views_util import obj_to_post
from blog.models import Post


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



class ApiPostCV(BaseCreateView):
    model = Post
    fields = '__all__'

    def form_valid(self, form):
        # form.instance.owner = self.request.user
        self.object = form.save()
        post = obj_to_post(self.object)
        return JsonResponse(data=post, safe=True, status=201)

    def form_invalid(self, form):
        print(vars(form))
        return JsonResponse(data=form.errors, safe=True, status=400)