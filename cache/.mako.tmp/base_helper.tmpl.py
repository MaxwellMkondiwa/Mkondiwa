# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1546928532.7798502
_enable_loop = True
_template_filename = 'c:/users/mkond/anaconda3/lib/site-packages/nikola/data/themes/bootblog4/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_feedlinks', 'html_navigation_links', 'html_stylesheets', 'html_navigation_links_entries', 'html_headstart', 'html_translations']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js" integrity="sha256-EGs9T1xMHdvM1geM8jPpoo8EZ1V1VRsmcJz8OByENLA=" crossorigin="anonymous"></script>\n        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.11.0/baguetteBox.min.js" integrity="sha256-yQGjQhFs3LtyiN5hhr3k9s9TWZOh/RzCkD3gwwCKlkg=" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.2/moment-with-locales.min.js" integrity="sha256-VrmtNHAdGzjNsUNtWYG55xxE9xDTz4gF63x/prKXKH0=" crossorigin="anonymous"></script>\n')
        if use_bundles and use_cdn:
            __M_writer('        <script src="/assets/js/all.js"></script>\n')
        elif use_bundles:
            __M_writer('        <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if not use_cdn:
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/popper.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/baguetteBox.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n')
            __M_writer('        <script src="/assets/js/fancydates.min.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        navigation_links = context.get('navigation_links', UNDEFINED)
        def html_navigation_links_entries(navigation_links_source):
            return render_html_navigation_links_entries(context,navigation_links_source)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(html_navigation_links_entries(navigation_links)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">\n        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.11.0/baguetteBox.min.css" integrity="sha256-cKiyvRKpm8RaTdU71Oq2RUVgvfWrdIXjvVdQF2oZ1Y4=" crossorigin="anonymous" />\n')
        if use_bundles and use_cdn:
            __M_writer('        <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
        elif use_bundles:
            __M_writer('        <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if not use_cdn:
                __M_writer('            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n            <link href="/assets/css/baguetteBox.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/bootblog.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        __M_writer('    <link href="https://fonts.googleapis.com/css?family=Playfair+Display:700,900" rel="stylesheet">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links_entries(context,navigation_links_source):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text in navigation_links_source[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li class="nav-item dropdown"><a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">')
                __M_writer(str(text))
                __M_writer('</a>\n            <div class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <a href="')
                        __M_writer(str(permalink))
                        __M_writer('" class="dropdown-item active">')
                        __M_writer(str(text))
                        __M_writer(' <span class="sr-only">')
                        __M_writer(str(messages("(active)", lang)))
                        __M_writer('</span></a>\n')
                    else:
                        __M_writer('                    <a href="')
                        __M_writer(str(suburl))
                        __M_writer('" class="dropdown-item">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                __M_writer('            </div>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="nav-item active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('" class="nav-link">')
                    __M_writer(str(text))
                    __M_writer(' <span class="sr-only">')
                    __M_writer(str(messages("(active)", lang)))
                    __M_writer('</span></a>\n')
                else:
                    __M_writer('                <li class="nav-item"><a href="')
                    __M_writer(str(url))
                    __M_writer('" class="nav-link">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs_link = context.get('abs_link', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        description = context.get('description', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        title = context.get('title', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        meta_generator_tag = context.get('meta_generator_tag', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        comment_system = context.get('comment_system', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        url_type = context.get('url_type', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        __M_writer("prefix='")
        __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb# ')
        __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n    <head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width, initial-scale=1">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\n')
        if meta_generator_tag:
            __M_writer('    <meta name="generator" content="Nikola (getnikola.com)">\n')
        __M_writer('    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs_link = context.get('abs_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li class="nav-item"><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('" class="nav-link">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "c:/users/mkond/anaconda3/lib/site-packages/nikola/data/themes/bootblog4/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 63, "23": 88, "24": 118, "25": 122, "26": 145, "27": 170, "28": 178, "34": 65, "41": 65, "42": 66, "43": 67, "44": 73, "45": 74, "46": 75, "47": 76, "48": 77, "49": 78, "50": 79, "51": 85, "52": 87, "53": 87, "54": 87, "60": 149, "71": 149, "72": 150, "73": 151, "74": 151, "75": 151, "76": 152, "77": 153, "78": 154, "79": 155, "80": 155, "81": 155, "82": 155, "83": 155, "84": 157, "85": 158, "86": 158, "87": 158, "88": 161, "89": 162, "90": 163, "91": 164, "92": 164, "93": 164, "94": 164, "95": 164, "96": 166, "97": 167, "98": 167, "99": 167, "105": 120, "112": 120, "113": 121, "114": 121, "120": 91, "128": 91, "129": 92, "130": 93, "131": 96, "132": 97, "133": 98, "134": 99, "135": 100, "136": 101, "137": 102, "138": 105, "139": 109, "140": 110, "141": 113, "142": 114, "143": 117, "149": 124, "159": 124, "160": 125, "161": 126, "162": 127, "163": 127, "164": 127, "165": 129, "166": 130, "167": 131, "168": 131, "169": 131, "170": 131, "171": 131, "172": 131, "173": 131, "174": 132, "175": 133, "176": 133, "177": 133, "178": 133, "179": 133, "180": 136, "181": 137, "182": 138, "183": 139, "184": 139, "185": 139, "186": 139, "187": 139, "188": 139, "189": 139, "190": 140, "191": 141, "192": 141, "193": 141, "194": 141, "195": 141, "201": 3, "228": 3, "229": 7, "230": 8, "231": 9, "232": 10, "233": 12, "234": 13, "235": 14, "236": 17, "237": 17, "238": 17, "239": 20, "240": 21, "241": 21, "242": 21, "243": 23, "244": 24, "245": 25, "246": 25, "247": 25, "248": 26, "249": 27, "250": 27, "251": 27, "252": 27, "253": 27, "254": 29, "255": 30, "256": 30, "257": 31, "258": 31, "259": 32, "260": 33, "261": 35, "262": 35, "263": 35, "264": 36, "265": 36, "266": 38, "267": 39, "268": 40, "269": 40, "270": 40, "271": 40, "272": 40, "273": 40, "274": 40, "275": 43, "276": 44, "277": 45, "278": 45, "279": 45, "280": 47, "281": 48, "282": 49, "283": 49, "284": 49, "285": 51, "286": 52, "287": 52, "288": 52, "289": 54, "290": 55, "291": 55, "292": 56, "293": 57, "294": 58, "295": 59, "296": 59, "297": 59, "298": 61, "299": 62, "300": 62, "306": 172, "316": 172, "317": 173, "318": 174, "319": 175, "320": 175, "321": 175, "322": 175, "323": 175, "324": 175, "325": 175, "331": 325}}
__M_END_METADATA
"""
