# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1546926038.2791753
_enable_loop = True
_template_filename = 'c:/users/mkond/anaconda3/lib/site-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl'
_template_uri = 'feeds_translations_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['_head_feed_link', '_head_atom', '_head_rss', '_html_translation_link', 'head', '_html_feed_link', 'feed_link', 'translation_link']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('        <link rel="alternate" type="')
            __M_writer(str(link_type))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(link_name)))
            __M_writer(' (')
            __M_writer(str(language))
            __M_writer(')" hreflang="')
            __M_writer(str(language))
            __M_writer('" href="')
            __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
            __M_writer('">\n')
        else:
            __M_writer('        <link rel="alternate" type="')
            __M_writer(str(link_type))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(link_name)))
            __M_writer('" hreflang="')
            __M_writer(str(language))
            __M_writer('" href="')
            __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__head_atom(context,classification=None,kind='index'):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        all_languages = context.get('all_languages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def _head_feed_link(link_type,link_name,link_postfix,classification,kind,language):
            return render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if generate_atom:
            if len(translations) > 1 and has_other_languages and classification and kind != 'index':
                for language, classification, name in all_languages:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom for ')
                    __M_writer(str(kind))
                    __M_writer(' ')
                    __M_writer(filters.html_escape(str(name)))
                    __M_writer(' (')
                    __M_writer(str(language))
                    __M_writer(')" hreflang="')
                    __M_writer(str(language))
                    __M_writer('" href="')
                    __M_writer(str(_link(kind + "_atom", classification, language)))
                    __M_writer('">\n')
            else:
                for language in sorted(translations):
                    if (classification or classification == '') and kind != 'index':
                        __M_writer('                    ')
                        __M_writer(str(_head_feed_link('application/atom+xml', 'Atom for ' + kind + ' ' + classification, 'atom', classification, kind, language)))
                        __M_writer('\n')
                    else:
                        __M_writer('                    ')
                        __M_writer(str(_head_feed_link('application/atom+xml', 'Atom', 'atom', classification, 'index', language)))
                        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__head_rss(context,classification=None,kind='index',rss_override=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        all_languages = context.get('all_languages', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        def _head_feed_link(link_type,link_name,link_postfix,classification,kind,language):
            return render__head_feed_link(context,link_type,link_name,link_postfix,classification,kind,language)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link and rss_override:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        if generate_rss and not (rss_link and rss_override) and kind != 'archive':
            if len(translations) > 1 and has_other_languages and classification and kind != 'index':
                for language, classification, name in all_languages:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS for ')
                    __M_writer(str(kind))
                    __M_writer(' ')
                    __M_writer(filters.html_escape(str(name)))
                    __M_writer(' (')
                    __M_writer(str(language))
                    __M_writer(')" hreflang="')
                    __M_writer(str(language))
                    __M_writer('" href="')
                    __M_writer(str(_link(kind + "_rss", classification, language)))
                    __M_writer('">\n')
            else:
                for language in sorted(translations):
                    if (classification or classification == '') and kind != 'index':
                        __M_writer('                    ')
                        __M_writer(str(_head_feed_link('application/rss+xml', 'RSS for ' + kind + ' ' + classification, 'rss', classification, kind, language)))
                        __M_writer('\n')
                    else:
                        __M_writer('                    ')
                        __M_writer(str(_head_feed_link('application/rss+xml', 'RSS', 'rss', classification, 'index', language)))
                        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__html_translation_link(context,classification,kind,language,name=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if name and kind != "archive" and kind != "author":
            __M_writer('        <a href="')
            __M_writer(str(_link(kind, classification, language)))
            __M_writer('" hreflang="')
            __M_writer(str(language))
            __M_writer('" rel="alternate">')
            __M_writer(str(messages("LANGUAGE", language)))
            __M_writer(' (')
            __M_writer(filters.html_escape(str(name)))
            __M_writer(')</a>\n')
        else:
            __M_writer('        <a href="')
            __M_writer(str(_link(kind, classification, language)))
            __M_writer('" hreflang="')
            __M_writer(str(language))
            __M_writer('" rel="alternate">')
            __M_writer(str(messages("LANGUAGE", language)))
            __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,classification=None,kind='index',feeds=True,other=True,rss_override=True,has_no_feeds=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        other_languages = context.get('other_languages', UNDEFINED)
        def _head_atom(classification=None,kind='index'):
            return render__head_atom(context,classification,kind)
        _link = context.get('_link', UNDEFINED)
        def _head_rss(classification=None,kind='index',rss_override=True):
            return render__head_rss(context,classification,kind,rss_override)
        __M_writer = context.writer()
        __M_writer('\n')
        if feeds and not has_no_feeds:
            __M_writer('        ')
            __M_writer(str(_head_rss(classification, 'index' if (kind == 'archive' and rss_override) else kind, rss_override)))
            __M_writer('\n        ')
            __M_writer(str(_head_atom(classification, kind)))
            __M_writer('\n')
        if other and has_other_languages and other_languages:
            for language, classification, _ in other_languages:
                __M_writer('            <link rel="alternate" hreflang="')
                __M_writer(str(language))
                __M_writer('" href="')
                __M_writer(str(_link(kind, classification, language)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__html_feed_link(context,link_type,link_name,link_postfix,classification,kind,language,name=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            if name and kind != "archive" and kind != "author":
                __M_writer('            <a href="')
                __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="')
                __M_writer(str(link_type))
                __M_writer('">')
                __M_writer(str(messages(link_name, language)))
                __M_writer(' (')
                __M_writer(filters.html_escape(str(name)))
                __M_writer(', ')
                __M_writer(str(language))
                __M_writer(')</a>\n')
            else:
                __M_writer('            <a href="')
                __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="')
                __M_writer(str(link_type))
                __M_writer('">')
                __M_writer(str(messages(link_name, language)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')</a>\n')
        else:
            if name and kind != "archive" and kind != "author":
                __M_writer('            <a href="')
                __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="')
                __M_writer(str(link_type))
                __M_writer('">')
                __M_writer(str(messages(link_name, language)))
                __M_writer(' (')
                __M_writer(filters.html_escape(str(name)))
                __M_writer(')</a>\n')
            else:
                __M_writer('            <a href="')
                __M_writer(str(_link(kind + '_' + link_postfix, classification, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="')
                __M_writer(str(link_type))
                __M_writer('">')
                __M_writer(str(messages(link_name, language)))
                __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_feed_link(context,classification,kind):
    __M_caller = context.caller_stack._push_frame()
    try:
        def _html_feed_link(link_type,link_name,link_postfix,classification,kind,language,name=None):
            return render__html_feed_link(context,link_type,link_name,link_postfix,classification,kind,language,name)
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        all_languages = context.get('all_languages', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if generate_atom or generate_rss:
            if len(translations) > 1 and has_other_languages and kind != 'index':
                for language, classification, name in all_languages:
                    __M_writer('                <p class="feedlink">\n')
                    if generate_atom:
                        __M_writer('                        ')
                        __M_writer(str(_html_feed_link('application/atom+xml', 'Atom feed', 'atom', classification, kind, language, name)))
                        __M_writer('\n')
                    if generate_rss and kind != 'archive':
                        __M_writer('                        ')
                        __M_writer(str(_html_feed_link('application/rss+xml', 'RSS feed', 'rss', classification, kind, language, name)))
                        __M_writer('\n')
                    __M_writer('                </p>\n')
            else:
                for language in sorted(translations):
                    __M_writer('                <p class="feedlink">\n')
                    if generate_atom:
                        __M_writer('                        ')
                        __M_writer(str(_html_feed_link('application/atom+xml', 'Atom feed', 'atom', classification, kind, language)))
                        __M_writer('\n')
                    if generate_rss and kind != 'archive':
                        __M_writer('                        ')
                        __M_writer(str(_html_feed_link('application/rss+xml', 'RSS feed', 'rss', classification, kind, language)))
                        __M_writer('\n')
                    __M_writer('                </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_translation_link(context,kind):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_other_languages = context.get('has_other_languages', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def _html_translation_link(classification,kind,language,name=None):
            return render__html_translation_link(context,classification,kind,language,name)
        other_languages = context.get('other_languages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if has_other_languages and other_languages:
            __M_writer('        <div class="translationslist translations">\n            <h3 class="translationslist-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for language, classification, name in other_languages:
                __M_writer('            <p>')
                __M_writer(str(_html_translation_link(classification, kind, language, name)))
                __M_writer('</p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "21": 2, "22": 9, "23": 25, "24": 33, "25": 54, "26": 72, "27": 85, "28": 113, "29": 124, "35": 3, "42": 3, "43": 4, "44": 5, "45": 5, "46": 5, "47": 5, "48": 5, "49": 5, "50": 5, "51": 5, "52": 5, "53": 5, "54": 5, "55": 6, "56": 7, "57": 7, "58": 7, "59": 7, "60": 7, "61": 7, "62": 7, "63": 7, "64": 7, "70": 56, "83": 56, "84": 57, "85": 58, "86": 59, "87": 60, "88": 60, "89": 60, "90": 60, "91": 60, "92": 60, "93": 60, "94": 60, "95": 60, "96": 60, "97": 60, "98": 62, "99": 63, "100": 64, "101": 65, "102": 65, "103": 65, "104": 66, "105": 67, "106": 67, "107": 67, "113": 35, "127": 35, "128": 36, "129": 37, "130": 37, "131": 37, "132": 39, "133": 40, "134": 41, "135": 42, "136": 42, "137": 42, "138": 42, "139": 42, "140": 42, "141": 42, "142": 42, "143": 42, "144": 42, "145": 42, "146": 44, "147": 45, "148": 46, "149": 47, "150": 47, "151": 47, "152": 48, "153": 49, "154": 49, "155": 49, "161": 27, "167": 27, "168": 28, "169": 29, "170": 29, "171": 29, "172": 29, "173": 29, "174": 29, "175": 29, "176": 29, "177": 29, "178": 30, "179": 31, "180": 31, "181": 31, "182": 31, "183": 31, "184": 31, "185": 31, "191": 75, "202": 75, "203": 76, "204": 77, "205": 77, "206": 77, "207": 78, "208": 78, "209": 80, "210": 81, "211": 82, "212": 82, "213": 82, "214": 82, "215": 82, "221": 11, "229": 11, "230": 12, "231": 13, "232": 14, "233": 14, "234": 14, "235": 14, "236": 14, "237": 14, "238": 14, "239": 14, "240": 14, "241": 14, "242": 14, "243": 14, "244": 14, "245": 15, "246": 16, "247": 16, "248": 16, "249": 16, "250": 16, "251": 16, "252": 16, "253": 16, "254": 16, "255": 16, "256": 16, "257": 18, "258": 19, "259": 20, "260": 20, "261": 20, "262": 20, "263": 20, "264": 20, "265": 20, "266": 20, "267": 20, "268": 20, "269": 20, "270": 21, "271": 22, "272": 22, "273": 22, "274": 22, "275": 22, "276": 22, "277": 22, "278": 22, "279": 22, "285": 87, "298": 87, "299": 88, "300": 89, "301": 90, "302": 91, "303": 92, "304": 93, "305": 93, "306": 93, "307": 95, "308": 96, "309": 96, "310": 96, "311": 98, "312": 100, "313": 101, "314": 102, "315": 103, "316": 104, "317": 104, "318": 104, "319": 106, "320": 107, "321": 107, "322": 107, "323": 109, "329": 115, "338": 115, "339": 116, "340": 117, "341": 118, "342": 118, "343": 119, "344": 120, "345": 120, "346": 120, "347": 122, "353": 347}, "filename": "c:/users/mkond/anaconda3/lib/site-packages/nikola/data/themes/base/templates/feeds_translations_helper.tmpl", "uri": "feeds_translations_helper.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
