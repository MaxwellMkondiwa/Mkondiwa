# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1546921224.6785147
_enable_loop = True
_template_filename = 'c:/users/mkond/anaconda3/lib/site-packages/nikola/data/themes/bootblog4/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content_header', 'content', 'before_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

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
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        def before_content():
            return render_before_content(context._locals(__M_locals))
        featured = _import_ns.get('featured', context.get('featured', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        math = _mako_get_namespace(context, 'math')
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        is_frontmost_index = _import_ns.get('is_frontmost_index', context.get('is_frontmost_index', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        theme_config = _import_ns.get('theme_config', context.get('theme_config', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
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


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        math = _mako_get_namespace(context, 'math')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        def content():
            return render_content(context)
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        def content_header():
            return render_content_header(context)
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        math = _mako_get_namespace(context, 'math')
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
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


def render_before_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        def before_content():
            return render_before_content(context)
        featured = _import_ns.get('featured', context.get('featured', UNDEFINED))
        is_frontmost_index = _import_ns.get('is_frontmost_index', context.get('is_frontmost_index', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        theme_config = _import_ns.get('theme_config', context.get('theme_config', UNDEFINED))
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"23": 5, "26": 4, "29": 3, "32": 2, "35": 6, "41": 0, "83": 2, "84": 3, "85": 4, "86": 5, "87": 6, "88": 7, "93": 15, "98": 69, "103": 146, "109": 9, "122": 9, "123": 10, "124": 10, "125": 11, "126": 12, "127": 12, "128": 12, "129": 14, "130": 14, "131": 14, "137": 18, "147": 18, "148": 19, "149": 19, "155": 17, "185": 17, "190": 20, "191": 21, "192": 22, "193": 22, "194": 22, "195": 24, "196": 25, "197": 25, "198": 25, "199": 27, "200": 28, "201": 29, "202": 29, "203": 29, "204": 31, "205": 31, "206": 31, "207": 31, "208": 34, "209": 35, "210": 35, "211": 35, "212": 35, "213": 35, "214": 36, "215": 37, "216": 37, "217": 37, "218": 39, "219": 41, "220": 41, "221": 42, "222": 42, "223": 42, "224": 42, "225": 42, "226": 42, "227": 43, "228": 44, "229": 44, "230": 44, "231": 45, "232": 45, "233": 45, "234": 45, "235": 45, "236": 45, "237": 47, "238": 49, "239": 50, "240": 50, "241": 50, "242": 52, "243": 54, "244": 55, "245": 56, "246": 56, "247": 58, "248": 59, "249": 60, "250": 60, "251": 63, "252": 65, "253": 66, "254": 66, "255": 67, "256": 67, "257": 68, "258": 68, "264": 71, "277": 71, "278": 72, "279": 73, "280": 74, "281": 75, "282": 76, "283": 78, "284": 79, "285": 82, "286": 82, "287": 82, "288": 82, "289": 83, "290": 84, "291": 84, "292": 84, "293": 86, "294": 87, "295": 88, "296": 89, "297": 91, "298": 91, "299": 91, "300": 91, "301": 91, "302": 93, "303": 94, "304": 94, "305": 94, "306": 97, "307": 100, "308": 101, "309": 102, "310": 103, "311": 104, "312": 105, "313": 106, "314": 108, "315": 111, "316": 111, "317": 111, "318": 111, "319": 113, "320": 114, "321": 114, "322": 114, "323": 116, "324": 116, "325": 116, "326": 116, "327": 117, "328": 118, "329": 118, "330": 118, "331": 121, "332": 124, "333": 125, "334": 129, "335": 129, "336": 129, "337": 129, "338": 131, "339": 132, "340": 132, "341": 132, "342": 134, "343": 134, "344": 134, "345": 134, "346": 135, "347": 136, "348": 136, "349": 136, "350": 139, "351": 142, "352": 144, "358": 352}, "filename": "c:/users/mkond/anaconda3/lib/site-packages/nikola/data/themes/bootblog4/templates/index.tmpl", "uri": "index.tmpl"}
__M_END_METADATA
"""
