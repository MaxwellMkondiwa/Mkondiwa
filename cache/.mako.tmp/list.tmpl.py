# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1603194516.3055365
_enable_loop = True
_template_filename = 'c:/users/mkond/anaconda3/lib/site-packages/nikola/data/themes/base/templates/list.tmpl'
_template_uri = 'list.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

    ns = runtime.TemplateNamespace('archive_nav', context._clean_inheritance_tokens(), templateuri='archive_navigation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'archive_nav')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        has_no_feeds = _import_ns.get('has_no_feeds', context.get('has_no_feeds', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content():
            return render_content(context._locals(__M_locals))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content():
            return render_content(context)
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<article class="listpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n    </header>\n    ')
        __M_writer(str(archive_nav.archive_navigation()))
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n')
        if items:
            __M_writer('    <ul class="postlist">\n')
            for text, link, count in items:
                __M_writer('        <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(text)))
                __M_writer('</a>\n')
                if count:
                    __M_writer('            (')
                    __M_writer(str(count))
                    __M_writer(')\n')
            __M_writer('    </ul>\n')
        else:
            __M_writer('    <p>')
            __M_writer(str(messages("Nothing found.")))
            __M_writer('</p>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'archive_nav')._populate(_import_ns, ['*'])
        has_no_feeds = _import_ns.get('has_no_feeds', context.get('has_no_feeds', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(kind=kind, rss_override=False, has_no_feeds=has_no_feeds)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "c:/users/mkond/anaconda3/lib/site-packages/nikola/data/themes/base/templates/list.tmpl", "line_map": {"128": 7, "96": 20, "69": 10, "134": 128, "23": 4, "26": 3, "84": 10, "85": 13, "86": 13, "87": 15, "88": 15, "89": 16, "90": 16, "91": 17, "92": 18, "93": 19, "94": 20, "95": 20, "32": 0, "97": 20, "98": 20, "99": 21, "100": 22, "101": 22, "102": 22, "103": 25, "104": 26, "105": 27, "106": 27, "107": 27, "108": 29, "114": 6, "51": 2, "52": 3, "53": 4, "58": 8, "127": 7, "126": 6, "63": 30}, "source_encoding": "utf-8", "uri": "list.tmpl"}
__M_END_METADATA
"""
