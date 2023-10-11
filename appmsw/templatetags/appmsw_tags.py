from django import template
register = template.Library()
from appmsw.utl import get_env_appmsw, get_sidemenu

assignment_tag = register.assignment_tag if hasattr(register, 'assignment_tag') else register.simple_tag

@assignment_tag(takes_context=True)
def get_side_menu(context):
    return get_sidemenu(context)

# Create your views here.
@register.simple_tag
def appmsw_tags_get_env(name="", fieldname="",namereturn="",jsonkey=""):
    _ = get_env_appmsw("",name,fieldname,namereturn,jsonkey)
    #if not name:
    #    return _.get(name,"???")
    # Page from the theme 
    return _

# <p>Instance: {% piece iris_portal.instance delimiter="*" num=1 %}, dir: {% piece iris_portal.instance delimiter="*" num=0 %}
@register.simple_tag
def piece(value,  *args, **kwargs):
    if not value: return ""
    delimiter = kwargs['delimiter']
    num = kwargs['num']
    return value.split(delimiter)[num]  # $p(a,"*",num)

# <p>Instance: {% iris_piece iris_portal.instance "*" 1 %}, dir: {% iris_piece iris_portal.instance "*" 0 %} 
@register.simple_tag
def iris_piece(value, delim, num):
    if not value: return ""
    return value.split(delim)[num]  # txt.split(" ")[1::])) # $p(a," ",2,*)

def is_empty(value, alt):
   if value:
       return value
   return alt

register.filter('is_empty', is_empty)