# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1602793189.9032485
_enable_loop = True
_template_filename = 'c:/users/mkond/anaconda3/lib/site-packages/nikola/data/themes/bootblog4/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content_header', 'before_content', 'content', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        math = _mako_get_namespace(context, 'math')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        is_frontmost_index = _import_ns.get('is_frontmost_index', context.get('is_frontmost_index', UNDEFINED))
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        theme_config = _import_ns.get('theme_config', context.get('theme_config', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        featured = _import_ns.get('featured', context.get('featured', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        pagination = _mako_get_namespace(context, 'pagination')
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        def before_content():
            return render_before_content(context._locals(__M_locals))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'before_content'):
            context['self'].before_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        __M_writer('\n        ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_before_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def before_content():
            return render_before_content(context)
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        is_frontmost_index = _import_ns.get('is_frontmost_index', context.get('is_frontmost_index', UNDEFINED))
        featured = _import_ns.get('featured', context.get('featured', UNDEFINED))
        theme_config = _import_ns.get('theme_config', context.get('theme_config', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'main_index' in pagekind and is_frontmost_index and featured and (theme_config.get('featured_large') or theme_config.get('featured_small')):
            if theme_config.get('featured_on_mobile'):
                __M_writer('            <div class="d-block">\n')
            else:
                __M_writer('            <div class="d-none d-md-block">\n')
            if featured and theme_config.get('featured_large'):
                __M_writer('        <div class="jumbotron p-0 text-white rounded bg-dark">\n            <div class="row bootblog4-featured-jumbotron-row">\n                <div class="col-md-6 p-3 p-md-4 pr-0 h-md-250 bootblog4-featured-text">\n                    <h1 class="display-4 font-italic"><a class="text-white" href="')
                __M_writer(str(featured[0].permalink()))
                __M_writer('">')
                __M_writer(str(featured[0].title()))
                __M_writer('</a></h1>\n')
                if featured[0].previewimage:
                    __M_writer('                            <div class="lead my-3 mb-0">')
                    __M_writer(str(featured[0].text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                        </div>\n')
                    if theme_config.get('featured_large_image_on_mobile'):
                        __M_writer('                        <div class="col-md-6 p-0 h-md-250 text-right">\n')
                    else:
                        __M_writer('                        <div class="col-md-6 p-0 h-md-250 text-right d-none d-md-block">\n')
                    __M_writer('                            <img class="bootblog4-featured-large-image" src="')
                    __M_writer(str(featured[0].previewimage))
                    __M_writer('" alt="')
                    __M_writer(str(featured.pop(0).title()))
                    __M_writer('">\n                        </div>\n')
                else:
                    __M_writer('                        <div class="lead my-3 mb-0">')
                    __M_writer(str(featured.pop(0).text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                        </div>\n')
                __M_writer('            </div>\n        </div>\n')
            __M_writer('\n')
            if featured and theme_config.get('featured_small'):
                __M_writer('            <div class="row mb-2">\n')
                if len(featured) == 1:
                    __M_writer('                <div class="col-md-12">\n')
                else:
                    __M_writer('                <div class="col-md-6">\n')
                __M_writer('                    <div class="card flex-md-row mb-4 box-shadow h-md-250">\n                       <div class="card-body d-flex flex-column align-items-start">\n                           <h3 class="mb-0">\n                               <a class="text-dark" href="')
                __M_writer(str(featured[0].permalink()))
                __M_writer('">')
                __M_writer(str(featured[0].title()))
                __M_writer('</a>\n                           </h3>\n')
                if featured[0].previewimage:
                    __M_writer('                               <div class="card-text mb-auto bootblog4-featured-text">')
                    __M_writer(str(featured[0].text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                               </div>\n                               <img class="card-img-right flex-auto d-none d-lg-block" src="')
                    __M_writer(str(featured[0].previewimage))
                    __M_writer('" alt="')
                    __M_writer(str(featured.pop(0).title()))
                    __M_writer('">\n')
                else:
                    __M_writer('                           <div class="card-text mb-auto bootblog4-featured-text">')
                    __M_writer(str(featured.pop(0).text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                           </div>\n')
                __M_writer('                    </div>\n                </div>\n\n')
                if featured:
                    __M_writer('               <div class="col-md-6">\n                    <div class="card flex-md-row mb-4 box-shadow h-md-250">\n                       <div class="card-body d-flex flex-column align-items-start">\n                           <h3 class="mb-0">\n                               <a class="text-dark" href="')
                    __M_writer(str(featured[0].permalink()))
                    __M_writer('">')
                    __M_writer(str(featured[0].title()))
                    __M_writer('</a>\n                           </h3>\n')
                    if featured[0].previewimage:
                        __M_writer('                               <div class="card-text mb-auto bootblog4-featured-text">')
                        __M_writer(str(featured[0].text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                        __M_writer('</div>\n                               </div>\n                               <img class="card-img-right flex-auto d-none d-lg-block" src="')
                        __M_writer(str(featured[0].previewimage))
                        __M_writer('" alt="')
                        __M_writer(str(featured.pop(0).title()))
                        __M_writer('">\n')
                    else:
                        __M_writer('                           <div class="card-text mb-auto bootblog4-featured-text">')
                        __M_writer(str(featured.pop(0).text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                        __M_writer('</div>\n                           </div>\n')
                    __M_writer('                    </div>\n                </div>\n')
                __M_writer('       </div>\n')
            __M_writer('    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        math = _mako_get_namespace(context, 'math')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        def content():
            return render_content(context)
        pagination = _mako_get_namespace(context, 'pagination')
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        def content_header():
            return render_content_header(context)
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('        ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('        ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer('    <div class="postindex">\n')
        for post in posts:
            __M_writer('            <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('" itemscope="itemscope" itemtype="http://schema.org/Article">\n            <header>\n                <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n                <div class="metadata">\n                    <p class="byline author vcard"><span class="byline-name fn" itemprop="author">\n')
            if author_pages_generated:
                __M_writer('                        <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                        ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('                    </span></p>\n            <p class="dateline">\n            <a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark">\n            <time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" itemprop="datePublished" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time>\n')
            if post.updated and post.updated != post.date:
                __M_writer('                <span class="updated"> (')
                __M_writer(str(messages("updated")))
                __M_writer('\n                    <time class="dt-updated" datetime="')
                __M_writer(str(post.formatted_updated('webiso')))
                __M_writer('" itemprop="dateUpdated" title="')
                __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
                __M_writer('</time>)</span>\n')
            __M_writer('            </a>\n            </p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                        <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('                </div>\n            </header>\n')
            if index_teasers:
                __M_writer('                <div class="p-summary entry-summary">\n                    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n                </div>\n')
            else:
                __M_writer('                <div class="e-content entry-content">\n                    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n                </div>\n')
            __M_writer('            </article>\n')
        __M_writer('    </div>\n    ')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n    ')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        math = _mako_get_namespace(context, 'math')
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.tmpl", "filename": "c:/users/mkond/anaconda3/lib/site-packages/nikola/data/themes/bootblog4/templates/index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 5, "26": 3, "29": 2, "32": 4, "35": 6, "41": 0, "83": 2, "84": 3, "85": 4, "86": 5, "87": 6, "88": 7, "93": 15, "98": 69, "103": 146, "109": 18, "119": 18, "120": 19, "121": 19, "127": 71, "140": 71, "141": 72, "142": 73, "143": 74, "144": 75, "145": 76, "146": 78, "147": 79, "148": 82, "149": 82, "150": 82, "151": 82, "152": 83, "153": 84, "154": 84, "155": 84, "156": 86, "157": 87, "158": 88, "159": 89, "160": 91, "161": 91, "162": 91, "163": 91, "164": 91, "165": 93, "166": 94, "167": 94, "168": 94, "169": 97, "170": 100, "171": 101, "172": 102, "173": 103, "174": 104, "175": 105, "176": 106, "177": 108, "178": 111, "179": 111, "180": 111, "181": 111, "182": 113, "183": 114, "184": 114, "185": 114, "186": 116, "187": 116, "188": 116, "189": 116, "190": 117, "191": 118, "192": 118, "193": 118, "194": 121, "195": 124, "196": 125, "197": 129, "198": 129, "199": 129, "200": 129, "201": 131, "202": 132, "203": 132, "204": 132, "205": 134, "206": 134, "207": 134, "208": 134, "209": 135, "210": 136, "211": 136, "212": 136, "213": 139, "214": 142, "215": 144, "221": 17, "251": 17, "256": 20, "257": 21, "258": 22, "259": 22, "260": 22, "261": 24, "262": 25, "263": 25, "264": 25, "265": 27, "266": 28, "267": 29, "268": 29, "269": 29, "270": 31, "271": 31, "272": 31, "273": 31, "274": 34, "275": 35, "276": 35, "277": 35, "278": 35, "279": 35, "280": 36, "281": 37, "282": 37, "283": 37, "284": 39, "285": 41, "286": 41, "287": 42, "288": 42, "289": 42, "290": 42, "291": 42, "292": 42, "293": 43, "294": 44, "295": 44, "296": 44, "297": 45, "298": 45, "299": 45, "300": 45, "301": 45, "302": 45, "303": 47, "304": 49, "305": 50, "306": 50, "307": 50, "308": 52, "309": 54, "310": 55, "311": 56, "312": 56, "313": 58, "314": 59, "315": 60, "316": 60, "317": 63, "318": 65, "319": 66, "320": 66, "321": 67, "322": 67, "323": 68, "324": 68, "330": 9, "343": 9, "344": 10, "345": 10, "346": 11, "347": 12, "348": 12, "349": 12, "350": 14, "351": 14, "352": 14, "358": 352}}
__M_END_METADATA
"""
