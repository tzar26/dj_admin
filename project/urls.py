from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^categories$', 'questions.views.get_categories', name='get_categories'),
    url(r'^question$', 'questions.views.get_question', name='get_question'),
    url(r'^poll$', 'questions.views.get_poll', name='get_poll'),
    url(r'^credentials$', 'users.views.get_credentials', name='get_credentials'),

    url(r'^admin/', include(admin.site.urls)),
)
