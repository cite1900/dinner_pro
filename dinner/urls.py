from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'dinner.views.first_page'),
    url(r'^register', 'dinner.views.dinner_register'),
)
