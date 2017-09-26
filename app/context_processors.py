from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings


def site(request):
    site = get_current_site(request)
    protocol = 'https' if request.is_secure() else 'http'
    return {
        'site': site,
        'site_root': "{0}://{1}".format(protocol, site.domain),
        'settings': settings,
    }
