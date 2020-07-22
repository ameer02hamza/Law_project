from templatetags.restart_tags import naturaltime
from django.contrib import admin
from django.core.cache import cache
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from models import RestartRequest
import os, os.path, time, datetime
import json

# Use reversion if installed
try:
    from reversion import VersionAdmin as ModelAdmin
except:
    from django.contrib.admin import ModelAdmin


def get_wsgi_path(return_invalid_path=False):
    wsgi_name = getattr(settings, 'WSGI_NAME', 'wsgi.py')
    site_root = getattr(settings, 'SITE_ROOT', os.path.abspath(os.path.dirname(__name__)))
    wsgi_path = "%s%s" % (site_root, wsgi_name)
    if (not os.path.isfile(wsgi_path)):
        if return_invalid_path:
            return wsgi_path
        return False
    return wsgi_path
    
def get_last_modified(wsgi_path):
    return datetime.datetime.strptime(time.ctime(os.path.getmtime(wsgi_path)), "%a %b %d %H:%M:%S %Y")

def get_can_write(wsgi_path):
    return os.access(wsgi_path, os.W_OK)

class RestartRequestAdmin(ModelAdmin):
    
    list_display = ('user', 'created_on',)
    list_filter = ('user',)
    date_hierarchy = 'created_on'
    actions = None
    
    def __init__(self, *args, **kwargs):
        super(RestartRequestAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
            
    def get_urls(self):
        urls = super(RestartRequestAdmin, self).get_urls()
        
        try:
            from django.conf.urls import patterns, url
        except:
            from django.conf.urls.defaults import patterns, url
        
        restart_urls = patterns('',
            url(r'^widget/$', self.admin_site.admin_view(self.widget), name='restart_widget'),
            url(r'^restart/$', self.admin_site.admin_view(self.restart), name='restart_widget_restart'),
            url(r'^updated/$', self.admin_site.admin_view(self.updated), name='restart_widget_updated')
        )
        return restart_urls + urls

    def widget(self, request):
        errors = []
        last_modified = False
        
        # custom view which should return an HttpResponse
        wsgi_path = get_wsgi_path()
        if (not wsgi_path):
            wsgi_path = get_wsgi_path(True)
            errors.append("WSGI file not found at '%s'.  <br/><br/>Please use the SITE_ROOT and WSGI_NAME swttings to define the correct location." % wsgi_path)
        else:
            last_modified = get_last_modified(wsgi_path)

            if not get_can_write(wsgi_path):
                errors.append("Unable to write to the WSGI file at '%s'.  <br/><br/>Please check the permissions." % wsgi_path)

        return render(request, 'restart/widget.html', {'errors': errors, 'wsgi_path':wsgi_path, 'last_modified':last_modified}, content_type="text/html")
        
    def restart(self, request):
        if request.is_ajax():
            wsgi_path = get_wsgi_path()
            if wsgi_path:
                with open(wsgi_path, 'a'):
                    os.utime(wsgi_path, None)
                    
                RestartRequest(user=request.user).save()
                    
                last_modified = get_last_modified(wsgi_path)
                last_modified = naturaltime(last_modified)
                json_return = {'last_modified': last_modified,}
                json_response = json.dumps(json_return)
                return HttpResponse(json_response, content_type="application/json")
        return HttpResponseForbidden
        
    def updated(self, request):
        if request.is_ajax():
            wsgi_path = get_wsgi_path()
            if wsgi_path:
                last_modified = get_last_modified(wsgi_path)
                return HttpResponse(naturaltime(last_modified), content_type="text/html")
        return HttpResponseForbidden
    
    # This method isint properly setup and is not yet used
    def clear_cache(self, request):
        cache.clear()
        json_return = {'html': "ere",}        
        json_response = json.dumps(json_return)
        return HttpResponse(json_response, content_type="application/json")
        
admin.site.register(RestartRequest, RestartRequestAdmin)
