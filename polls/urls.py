from django.conf.urls import url
from polls import views as view

urlpatterns = [
    # Tip: the 'name' value as called by the {% url %} template tag
    url(r'^$', view.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', view.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', view.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', view.vote, name='vote'),
]
