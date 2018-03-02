from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.http import HttpResponse

import csv


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['OBkEjbd81f7z5zLg9aa8TND4c0RTWP0xIfCREnnOMW8.qCtPt9nA3hRxpUcp0c_ob13Jy1cvZ9mWEt042rxdu94'])

    return response

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/new_home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    url(r'^.well-known/acme-challenge/4KhjSv2R9210j0B4ILK8ZiIKbc9x3fJikUlRPE1pZOw$', some_view, name=''),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('ifemun.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),


    # Your stuff: custom urls includes go here
    url(r'^blog/', include('ifemun.blog.urls', namespace='blog')),
    url(r'^conference/', include('ifemun.conference.urls', namespace='conference')),
    url(r'^committees/', include('ifemun.committees.urls', namespace='committees')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns


