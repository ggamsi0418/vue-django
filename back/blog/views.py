from django.shortcuts import render
from django.views.generic import DetailView, ListView
from blog.models import Post


class PostLV(ListView):
    model = Post
    # template_name을 따로 설정하지 않아도 다음과 같은 규칙으로 파일명을 정의한다.
    # opts.app_label + opts.model_name + self.template_name_suffix
    # (앱 이름/)+(모델명)+(_url 접미사).html
    # blog/post_list.html
    

class PostDV(DetailView):
    model = Post
    

