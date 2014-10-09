from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^question$', 'questions.views.get_question', name='get_question'),
    url(r'^credentials$', 'users.views.get_credentials', name='get_credentials'),

    url(r'^admin/', include(admin.site.urls)),
)