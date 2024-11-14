from django_hosts import patterns, host

host_patterns = patterns(
    '',
    # host(r'', 'restaurant_branding.urls', name='default'),
    host(r'localhost', 'restaurant_branding.urls', name='default_local'), 
    host(r'(?P<brand_name>\w+)', 'restaurants.urls', name='restauranturls'),
    
)
