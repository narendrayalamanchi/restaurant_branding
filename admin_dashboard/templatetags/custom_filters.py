from django import template
from django.conf import settings

register = template.Library()

# Initialize an empty dictionary to hold the previous value
@register.simple_tag(takes_context=True)
def update_previous_category(context, current_category):
    context['previous_category'] = current_category
    return ""

@register.simple_tag
def get_aws_s3_base_url():
    print("HELLO",settings.AWS_S3_BASE_URL)
    return settings.AWS_S3_BASE_URL

@register.filter
def get(dict_data, key):
    return dict_data.get(key, None)