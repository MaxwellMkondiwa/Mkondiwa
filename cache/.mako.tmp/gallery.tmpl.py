# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1571405200.8649268
_enable_loop = True
_template_filename = 'c:/users/mkond/anaconda3/lib/site-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'extra_js', 'extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='ui_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        enable_comments = context.get('enable_comments', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        lang = context.get('lang', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        post = context.get('post', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        _link = context.get('_link', UNDEFINED)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        photo_array = context.get('photo_array', UNDEFINED)
        len = context.get('len', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        def extra_js():
            return render_extra_js(context)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<script src="/assets/js/justified-layout.min.js"></script>\n<script src="/assets/js/gallery.min.js"></script>\n<script>\nvar jsonContent = ')
        __M_writer(str(photo_array_json))
        __M_writer(';\nvar thumbnailSize = ')
        __M_writer(str(thumbnail_size))
        __M_writer(";\nrenderGallery(jsonContent, thumbnailSize);\nwindow.addEventListener('resize', renderGallery);\n</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        lang = context.get('lang', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n<style type="text/css">\n    #gallery_container {\n        position: relative;\n    }\n    .image-block {\n        position: absolute;\n    }\n</style>\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang:
                    __M_writer('             <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(_link('gallery', gallery_path, langname)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        enable_comments = context.get('enable_comments', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def content():
            return render_content(context)
        folders = context.get('folders', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        post = context.get('post', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(ui.breadcrumbs(crumbs)))
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        if post:
            __M_writer('    <p>\n        ')
            __M_writer(str(post.text()))
            __M_writer('\n    </p>\n')
        if folders:
            __M_writer('    <ul>\n')
            for folder, ftitle in folders:
                __M_writer('        <li><a href="')
                __M_writer(str(folder))
                __M_writer('">📂&nbsp;')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('\n<div id="gallery_container"></div>\n')
        if photo_array:
            __M_writer('<noscript>\n<ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer('        <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('">\n            <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('" /></a>\n')
            __M_writer('</ul>\n</noscript>\n')
        if site_has_comments and enable_comments:
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "c:/users/mkond/anaconda3/lib/site-packages/nikola/data/themes/bootstrap4/templates/gallery.tmpl", "source_encoding": "utf-8", "uri": "gallery.tmpl", "line_map": {"192": 30, "132": 41, "133": 42, "134": 42, "135": 52, "136": 53, "137": 54, "138": 55, "139": 55, "140": 55, "141": 55, "142": 55, "148": 7, "23": 4, "26": 3, "32": 0, "164": 7, "165": 8, "166": 8, "167": 9, "168": 10, "169": 10, "170": 10, "171": 12, "172": 13, "173": 14, "174": 14, "175": 17, "176": 18, "177": 19, "178": 20, "179": 20, "180": 20, "181": 20, "182": 20, "183": 22, "184": 24, "185": 26, "186": 27, "187": 29, "188": 30, "189": 30, "190": 30, "63": 2, "64": 3, "65": 4, "194": 31, "195": 31, "196": 31, "197": 33, "70": 5, "199": 37, "200": 37, "75": 39, "206": 200, "80": 59, "193": 31, "85": 70, "91": 5, "198": 36, "102": 61, "110": 61, "111": 65, "112": 65, "113": 66, "114": 66, "120": 41, "191": 30}}
__M_END_METADATA
"""
