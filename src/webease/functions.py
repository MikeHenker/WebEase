"""
Webease Function Library - 230+ beginner-friendly functions for web creation
"""

class WebeaseContext:
    def __init__(self):
        self.html_parts = []
        self.css_rules = []
        self.js_code = []
        self.head_parts = []
        self.body_classes = []
        self.imported_libraries = []
        self.custom_functions = {}
        
    def add_html(self, html):
        self.html_parts.append(html)
    
    def add_css(self, css):
        self.css_rules.append(css)
    
    def add_js(self, js):
        self.js_code.append(js)
    
    def add_head(self, head):
        self.head_parts.append(head)

# Global context
ctx = WebeaseContext()

# ==================== BASIC HTML ELEMENTS ====================

def add_title(text, level=1):
    """Add a heading (h1-h6)"""
    ctx.add_html(f'<h{level}>{text}</h{level}>')

def add_text(text):
    """Add a paragraph of text"""
    ctx.add_html(f'<p>{text}</p>')

def add_heading(text, level=1):
    """Add a heading (alias for add_title)"""
    add_title(text, level)

def add_paragraph(text):
    """Add a paragraph (alias for add_text)"""
    add_text(text)

def add_div(content="", css_class="", element_id=""):
    """Add a div container"""
    class_attr = f' class="{css_class}"' if css_class else ''
    id_attr = f' id="{element_id}"' if element_id else ''
    ctx.add_html(f'<div{class_attr}{id_attr}>{content}</div>')

def add_span(content="", css_class=""):
    """Add an inline span"""
    class_attr = f' class="{css_class}"' if css_class else ''
    ctx.add_html(f'<span{class_attr}>{content}</span>')

def add_link(url, text, target="_self"):
    """Add a hyperlink"""
    ctx.add_html(f'<a href="{url}" target="{target}">{text}</a>')

def add_image(src, alt="", width="", height=""):
    """Add an image"""
    width_attr = f' width="{width}"' if width else ''
    height_attr = f' height="{height}"' if height else ''
    ctx.add_html(f'<img src="{src}" alt="{alt}"{width_attr}{height_attr}>')

def add_list(items, ordered=False):
    """Add a list (ordered or unordered)"""
    tag = 'ol' if ordered else 'ul'
    list_html = f'<{tag}>'
    for item in items:
        list_html += f'<li>{item}</li>'
    list_html += f'</{tag}>'
    ctx.add_html(list_html)

def add_ordered_list(items):
    """Add an ordered list"""
    add_list(items, ordered=True)

def add_unordered_list(items):
    """Add an unordered list"""
    add_list(items, ordered=False)

# ==================== TEXT FORMATTING ====================

def add_bold(text):
    """Add bold text"""
    ctx.add_html(f'<strong>{text}</strong>')

def add_italic(text):
    """Add italic text"""
    ctx.add_html(f'<em>{text}</em>')

def add_underline(text):
    """Add underlined text"""
    ctx.add_html(f'<u>{text}</u>')

def add_strikethrough(text):
    """Add strikethrough text"""
    ctx.add_html(f'<s>{text}</s>')

def add_code(text):
    """Add inline code"""
    ctx.add_html(f'<code>{text}</code>')

def add_code_block(code, language=""):
    """Add a code block"""
    lang_class = f' class="language-{language}"' if language else ''
    ctx.add_html(f'<pre><code{lang_class}>{code}</code></pre>')

def add_superscript(text):
    """Add superscript text"""
    ctx.add_html(f'<sup>{text}</sup>')

def add_subscript(text):
    """Add subscript text"""
    ctx.add_html(f'<sub>{text}</sub>')

def add_quote(text):
    """Add a blockquote"""
    ctx.add_html(f'<blockquote>{text}</blockquote>')

def add_small(text):
    """Add small text"""
    ctx.add_html(f'<small>{text}</small>')

def add_mark(text):
    """Add highlighted/marked text"""
    ctx.add_html(f'<mark>{text}</mark>')

# ==================== LINE BREAKS & SEPARATORS ====================

def add_br(count=1):
    """Add line breaks"""
    ctx.add_html('<br>' * count)

def add_hr():
    """Add a horizontal rule"""
    ctx.add_html('<hr>')

def add_space(count=1):
    """Add non-breaking spaces"""
    ctx.add_html('&nbsp;' * count)

# ==================== TABLES ====================

def create_table(headers, rows, css_class=""):
    """Create a table"""
    class_attr = f' class="{css_class}"' if css_class else ''
    table_html = f'<table{class_attr}><thead><tr>'
    for header in headers:
        table_html += f'<th>{header}</th>'
    table_html += '</tr></thead><tbody>'
    for row in rows:
        table_html += '<tr>'
        for cell in row:
            table_html += f'<td>{cell}</td>'
        table_html += '</tr>'
    table_html += '</tbody></table>'
    ctx.add_html(table_html)

def add_table_row(cells):
    """Add a table row (use within table context)"""
    row_html = '<tr>'
    for cell in cells:
        row_html += f'<td>{cell}</td>'
    row_html += '</tr>'
    ctx.add_html(row_html)

# ==================== FORMS & INPUTS ====================

def create_form(action="", method="post", form_id=""):
    """Start a form"""
    id_attr = f' id="{form_id}"' if form_id else ''
    ctx.add_html(f'<form action="{action}" method="{method}"{id_attr}>')

def end_form():
    """End a form"""
    ctx.add_html('</form>')

def add_input(input_type="text", name="", placeholder="", value="", required=False):
    """Add an input field"""
    required_attr = ' required' if required else ''
    ctx.add_html(f'<input type="{input_type}" name="{name}" placeholder="{placeholder}" value="{value}"{required_attr}>')

def add_text_input(name, placeholder="", value=""):
    """Add a text input"""
    add_input("text", name, placeholder, value)

def add_email_input(name, placeholder="", value=""):
    """Add an email input"""
    add_input("email", name, placeholder, value)

def add_password_input(name, placeholder=""):
    """Add a password input"""
    add_input("password", name, placeholder)

def add_number_input(name, placeholder="", min_val="", max_val=""):
    """Add a number input"""
    min_attr = f' min="{min_val}"' if min_val else ''
    max_attr = f' max="{max_val}"' if max_val else ''
    ctx.add_html(f'<input type="number" name="{name}" placeholder="{placeholder}"{min_attr}{max_attr}>')

def add_textarea(name, placeholder="", rows=4, cols=50):
    """Add a textarea"""
    ctx.add_html(f'<textarea name="{name}" placeholder="{placeholder}" rows="{rows}" cols="{cols}"></textarea>')

def add_button(text, button_type="button", onclick=""):
    """Add a button"""
    onclick_attr = f' onclick="{onclick}"' if onclick else ''
    ctx.add_html(f'<button type="{button_type}"{onclick_attr}>{text}</button>')

def add_submit_button(text="Submit"):
    """Add a submit button"""
    add_button(text, "submit")

def add_checkbox(name, label, value="", checked=False):
    """Add a checkbox"""
    checked_attr = ' checked' if checked else ''
    ctx.add_html(f'<label><input type="checkbox" name="{name}" value="{value}"{checked_attr}> {label}</label>')

def add_radio(name, label, value, checked=False):
    """Add a radio button"""
    checked_attr = ' checked' if checked else ''
    ctx.add_html(f'<label><input type="radio" name="{name}" value="{value}"{checked_attr}> {label}</label>')

def add_select(name, options, selected=""):
    """Add a select dropdown"""
    select_html = f'<select name="{name}">'
    for option in options:
        if isinstance(option, dict):
            value = option.get('value', option.get('label'))
            label = option.get('label', value)
        else:
            value = label = option
        selected_attr = ' selected' if value == selected else ''
        select_html += f'<option value="{value}"{selected_attr}>{label}</option>'
    select_html += '</select>'
    ctx.add_html(select_html)

def add_label(text, for_id=""):
    """Add a label"""
    for_attr = f' for="{for_id}"' if for_id else ''
    ctx.add_html(f'<label{for_attr}>{text}</label>')

def add_file_input(name, accept=""):
    """Add a file input"""
    accept_attr = f' accept="{accept}"' if accept else ''
    ctx.add_html(f'<input type="file" name="{name}"{accept_attr}>')

def add_date_input(name, value=""):
    """Add a date input"""
    add_input("date", name, "", value)

def add_color_input(name, value="#000000"):
    """Add a color picker"""
    add_input("color", name, "", value)

def add_range_input(name, min_val=0, max_val=100, value=50):
    """Add a range slider"""
    ctx.add_html(f'<input type="range" name="{name}" min="{min_val}" max="{max_val}" value="{value}">')

# ==================== STYLING FUNCTIONS ====================

def set_background(color):
    """Set page background color"""
    ctx.add_css(f'body {{ background-color: {color}; }}')

def set_background_gradient(color1, color2, direction="to bottom"):
    """Set background gradient"""
    ctx.add_css(f'body {{ background: linear-gradient({direction}, {color1}, {color2}); }}')

def set_font(family, size="16px"):
    """Set page font"""
    ctx.add_css(f'body {{ font-family: {family}; font-size: {size}; }}')

def set_text_color(color):
    """Set page text color"""
    ctx.add_css(f'body {{ color: {color}; }}')

def set_page_margin(margin):
    """Set page margin"""
    ctx.add_css(f'body {{ margin: {margin}; }}')

def set_page_padding(padding):
    """Set page padding"""
    ctx.add_css(f'body {{ padding: {padding}; }}')

def add_custom_css(css):
    """Add custom CSS"""
    ctx.add_css(css)

def add_style_to_element(selector, property_name, value):
    """Add a style to an element"""
    ctx.add_css(f'{selector} {{ {property_name}: {value}; }}')

# ==================== LAYOUT UTILITIES ====================

def create_container(content="", css_class="container", centered=True):
    """Create a container"""
    center_css = "margin: 0 auto;" if centered else ""
    ctx.add_css(f'.{css_class} {{ max-width: 1200px; padding: 20px; {center_css} }}')
    ctx.add_html(f'<div class="{css_class}">{content}</div>')

def create_section(content="", css_class="section"):
    """Create a section"""
    ctx.add_html(f'<section class="{css_class}">{content}</section>')

def create_row(content="", css_class="row"):
    """Create a flex row"""
    ctx.add_css(f'.{css_class} {{ display: flex; flex-wrap: wrap; }}')
    ctx.add_html(f'<div class="{css_class}">{content}</div>')

def create_column(content="", width="", css_class="column"):
    """Create a column"""
    width_css = f'flex: 0 0 {width}; max-width: {width};' if width else 'flex: 1;'
    ctx.add_css(f'.{css_class} {{ {width_css} padding: 10px; box-sizing: border-box; }}')
    ctx.add_html(f'<div class="{css_class}">{content}</div>')

def create_grid(columns=3, gap="20px", css_class="grid"):
    """Create a grid container"""
    ctx.add_css(f'.{css_class} {{ display: grid; grid-template-columns: repeat({columns}, 1fr); gap: {gap}; }}')
    ctx.add_html(f'<div class="{css_class}">')

def end_grid():
    """End a grid container"""
    ctx.add_html('</div>')

def create_flex_container(direction="row", justify="flex-start", align="stretch", css_class="flex-container"):
    """Create a flexbox container"""
    ctx.add_css(f'.{css_class} {{ display: flex; flex-direction: {direction}; justify-content: {justify}; align-items: {align}; }}')
    ctx.add_html(f'<div class="{css_class}">')

def end_flex_container():
    """End a flexbox container"""
    ctx.add_html('</div>')

def add_spacer(height="20px"):
    """Add vertical space"""
    ctx.add_html(f'<div style="height: {height};"></div>')

# ==================== CARDS & CONTENT BOXES ====================

def create_card(title="", content="", css_class="card", shadow=True):
    """Create a card"""
    shadow_css = "box-shadow: 0 4px 6px rgba(0,0,0,0.1);" if shadow else ""
    ctx.add_css(f'.{css_class} {{ background: white; border-radius: 8px; padding: 20px; margin: 10px; {shadow_css} }}')
    card_html = f'<div class="{css_class}">'
    if title:
        card_html += f'<h3>{title}</h3>'
    card_html += f'{content}</div>'
    ctx.add_html(card_html)

def create_info_box(content, css_class="info-box"):
    """Create an info box"""
    ctx.add_css(f'.{css_class} {{ background: #e3f2fd; border-left: 4px solid #2196F3; padding: 15px; margin: 10px 0; border-radius: 4px; }}')
    ctx.add_html(f'<div class="{css_class}">{content}</div>')

def create_warning_box(content, css_class="warning-box"):
    """Create a warning box"""
    ctx.add_css(f'.{css_class} {{ background: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; margin: 10px 0; border-radius: 4px; }}')
    ctx.add_html(f'<div class="{css_class}">{content}</div>')

def create_success_box(content, css_class="success-box"):
    """Create a success box"""
    ctx.add_css(f'.{css_class} {{ background: #d4edda; border-left: 4px solid #28a745; padding: 15px; margin: 10px 0; border-radius: 4px; }}')
    ctx.add_html(f'<div class="{css_class}">{content}</div>')

def create_error_box(content, css_class="error-box"):
    """Create an error box"""
    ctx.add_css(f'.{css_class} {{ background: #f8d7da; border-left: 4px solid #dc3545; padding: 15px; margin: 10px 0; border-radius: 4px; }}')
    ctx.add_html(f'<div class="{css_class}">{content}</div>')

def create_panel(title, content, css_class="panel"):
    """Create a panel with header"""
    ctx.add_css(f'.{css_class} {{ border: 1px solid #ddd; border-radius: 4px; margin: 10px 0; }} .{css_class}-header {{ background: #f5f5f5; padding: 10px 15px; border-bottom: 1px solid #ddd; font-weight: bold; }} .{css_class}-body {{ padding: 15px; }}')
    ctx.add_html(f'<div class="{css_class}"><div class="{css_class}-header">{title}</div><div class="{css_class}-body">{content}</div></div>')

# ==================== NAVIGATION ====================

def create_navbar(brand="", links=None, css_class="navbar"):
    """Create a navigation bar"""
    links = links or []
    ctx.add_css(f'.{css_class} {{ background: #333; padding: 15px; display: flex; align-items: center; }} .{css_class} a {{ color: white; text-decoration: none; padding: 0 15px; }} .{css_class} a:hover {{ color: #ddd; }} .{css_class}-brand {{ font-weight: bold; margin-right: auto; }}')
    navbar_html = f'<nav class="{css_class}">'
    if brand:
        navbar_html += f'<span class="{css_class}-brand">{brand}</span>'
    for link in links:
        if isinstance(link, dict):
            navbar_html += f'<a href="{link.get("url", "#")}">{link.get("text", "Link")}</a>'
        else:
            navbar_html += f'<a href="#">{link}</a>'
    navbar_html += '</nav>'
    ctx.add_html(navbar_html)

def create_menu(items, css_class="menu"):
    """Create a vertical menu"""
    ctx.add_css(f'.{css_class} {{ list-style: none; padding: 0; margin: 0; }} .{css_class} li {{ padding: 10px; border-bottom: 1px solid #ddd; }} .{css_class} li:hover {{ background: #f5f5f5; cursor: pointer; }}')
    menu_html = f'<ul class="{css_class}">'
    for item in items:
        menu_html += f'<li>{item}</li>'
    menu_html += '</ul>'
    ctx.add_html(menu_html)

def create_breadcrumbs(items, css_class="breadcrumbs"):
    """Create breadcrumbs navigation"""
    ctx.add_css(f'.{css_class} {{ display: flex; list-style: none; padding: 10px 0; }} .{css_class} li::after {{ content: " / "; margin: 0 8px; }} .{css_class} li:last-child::after {{ content: ""; }}')
    breadcrumb_html = f'<ul class="{css_class}">'
    for item in items:
        breadcrumb_html += f'<li>{item}</li>'
    breadcrumb_html += '</ul>'
    ctx.add_html(breadcrumb_html)

def create_tabs(tabs, css_class="tabs"):
    """Create tabs"""
    ctx.add_css(f'.{css_class} {{ display: flex; border-bottom: 2px solid #ddd; }} .{css_class} button {{ background: none; border: none; padding: 10px 20px; cursor: pointer; }} .{css_class} button.active {{ border-bottom: 2px solid #007bff; color: #007bff; }}')
    tabs_html = f'<div class="{css_class}">'
    for i, tab in enumerate(tabs):
        active = ' class="active"' if i == 0 else ''
        tabs_html += f'<button{active}>{tab}</button>'
    tabs_html += '</div>'
    ctx.add_html(tabs_html)

def create_accordion(items, css_class="accordion"):
    """Create an accordion"""
    ctx.add_css(f'.{css_class}-item {{ border: 1px solid #ddd; margin: 5px 0; }} .{css_class}-header {{ background: #f5f5f5; padding: 15px; cursor: pointer; font-weight: bold; }} .{css_class}-header:hover {{ background: #e0e0e0; }} .{css_class}-body {{ padding: 15px; display: none; }} .{css_class}-body.active {{ display: block; }}')
    for item in items:
        if isinstance(item, dict):
            header = item.get('header', 'Accordion Item')
            body = item.get('body', '')
        else:
            header = body = item
        ctx.add_html(f'<div class="{css_class}-item"><div class="{css_class}-header">{header}</div><div class="{css_class}-body">{body}</div></div>')

# ==================== MODALS & DIALOGS ====================

def create_modal(modal_id, title, content, css_class="modal"):
    """Create a modal dialog"""
    ctx.add_css(f'.{css_class} {{ display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); }} .{css_class}-content {{ background: white; margin: 10% auto; padding: 20px; border-radius: 8px; width: 80%; max-width: 500px; position: relative; }} .{css_class}-close {{ position: absolute; right: 15px; top: 10px; font-size: 28px; cursor: pointer; }}')
    modal_html = f'<div id="{modal_id}" class="{css_class}"><div class="{css_class}-content"><span class="{css_class}-close">&times;</span><h2>{title}</h2><p>{content}</p></div></div>'
    ctx.add_html(modal_html)

def add_alert(message, alert_type="info"):
    """Add an alert message"""
    colors = {
        'info': '#2196F3',
        'success': '#4CAF50',
        'warning': '#ff9800',
        'error': '#f44336'
    }
    color = colors.get(alert_type, '#2196F3')
    ctx.add_css(f'.alert-{alert_type} {{ background: {color}; color: white; padding: 15px; margin: 10px 0; border-radius: 4px; }}')
    ctx.add_html(f'<div class="alert-{alert_type}">{message}</div>')

def add_toast(message, duration=3000):
    """Add a toast notification"""
    ctx.add_css('.toast { position: fixed; bottom: 20px; right: 20px; background: #333; color: white; padding: 15px 20px; border-radius: 4px; z-index: 1000; }')
    ctx.add_html(f'<div class="toast">{message}</div>')
    ctx.add_js(f'setTimeout(() => {{ document.querySelector(".toast").remove(); }}, {duration});')

# ==================== ANIMATIONS ====================

def add_fade_in(selector, duration="1s"):
    """Add fade-in animation"""
    ctx.add_css(f'{selector} {{ animation: fadeIn {duration}; }} @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}')

def add_slide_in(selector, direction="left", duration="0.5s"):
    """Add slide-in animation"""
    transform_from = {
        'left': 'translateX(-100%)',
        'right': 'translateX(100%)',
        'top': 'translateY(-100%)',
        'bottom': 'translateY(100%)'
    }.get(direction, 'translateX(-100%)')
    ctx.add_css(f'{selector} {{ animation: slideIn{direction.capitalize()} {duration}; }} @keyframes slideIn{direction.capitalize()} {{ from {{ transform: {transform_from}; }} to {{ transform: translateX(0); }} }}')

def add_bounce(selector, duration="1s"):
    """Add bounce animation"""
    ctx.add_css(f'{selector} {{ animation: bounce {duration}; }} @keyframes bounce {{ 0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }} 40% {{ transform: translateY(-30px); }} 60% {{ transform: translateY(-15px); }} }}')

def add_rotate(selector, degrees=360, duration="2s"):
    """Add rotation animation"""
    ctx.add_css(f'{selector} {{ animation: rotate {duration} infinite linear; }} @keyframes rotate {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate({degrees}deg); }} }}')

def add_scale(selector, scale=1.1, duration="0.3s"):
    """Add scale animation"""
    ctx.add_css(f'{selector} {{ transition: transform {duration}; }} {selector}:hover {{ transform: scale({scale}); }}')

def add_shake(selector, duration="0.5s"):
    """Add shake animation"""
    ctx.add_css(f'{selector} {{ animation: shake {duration}; }} @keyframes shake {{ 0%, 100% {{ transform: translateX(0); }} 10%, 30%, 50%, 70%, 90% {{ transform: translateX(-10px); }} 20%, 40%, 60%, 80% {{ transform: translateX(10px); }} }}')

def add_pulse(selector, duration="1s"):
    """Add pulse animation"""
    ctx.add_css(f'{selector} {{ animation: pulse {duration} infinite; }} @keyframes pulse {{ 0% {{ transform: scale(1); }} 50% {{ transform: scale(1.05); }} 100% {{ transform: scale(1); }} }}')

# ==================== HOVER & INTERACTION EFFECTS ====================

def add_hover_effect(selector, property_name, value, duration="0.3s"):
    """Add hover effect"""
    ctx.add_css(f'{selector} {{ transition: {property_name} {duration}; }} {selector}:hover {{ {property_name}: {value}; }}')

def add_hover_color(selector, color):
    """Add hover color change"""
    add_hover_effect(selector, 'color', color)

def add_hover_background(selector, color):
    """Add hover background change"""
    add_hover_effect(selector, 'background-color', color)

def add_click_effect(element_id, effect):
    """Add click effect with JavaScript"""
    ctx.add_js(f'document.getElementById("{element_id}").addEventListener("click", function() {{ {effect} }});')

# ==================== RESPONSIVE DESIGN ====================

def set_mobile_breakpoint(max_width="768px"):
    """Set mobile breakpoint"""
    ctx.add_css(f'@media (max-width: {max_width}) {{ .container {{ padding: 10px; }} .row {{ flex-direction: column; }} }}')

def add_responsive_text(selector, mobile_size="14px", desktop_size="16px"):
    """Add responsive text sizing"""
    ctx.add_css(f'{selector} {{ font-size: {desktop_size}; }} @media (max-width: 768px) {{ {selector} {{ font-size: {mobile_size}; }} }}')

def hide_on_mobile(selector):
    """Hide element on mobile"""
    ctx.add_css(f'@media (max-width: 768px) {{ {selector} {{ display: none; }} }}')

def hide_on_desktop(selector):
    """Hide element on desktop"""
    ctx.add_css(f'@media (min-width: 769px) {{ {selector} {{ display: none; }} }}')

# ==================== MEDIA ====================

def add_video(src, width="", height="", controls=True):
    """Add a video"""
    width_attr = f' width="{width}"' if width else ''
    height_attr = f' height="{height}"' if height else ''
    controls_attr = ' controls' if controls else ''
    ctx.add_html(f'<video src="{src}"{width_attr}{height_attr}{controls_attr}></video>')

def add_audio(src, controls=True):
    """Add audio"""
    controls_attr = ' controls' if controls else ''
    ctx.add_html(f'<audio src="{src}"{controls_attr}></audio>')

def add_iframe(src, width="100%", height="400px"):
    """Add an iframe"""
    ctx.add_html(f'<iframe src="{src}" width="{width}" height="{height}"></iframe>')

def add_embed(src, width="", height=""):
    """Add embedded content"""
    width_attr = f' width="{width}"' if width else ''
    height_attr = f' height="{height}"' if height else ''
    ctx.add_html(f'<embed src="{src}"{width_attr}{height_attr}>')

# ==================== ADVANCED STYLING ====================

def add_box_shadow(selector, shadow="0 4px 6px rgba(0,0,0,0.1)"):
    """Add box shadow"""
    ctx.add_css(f'{selector} {{ box-shadow: {shadow}; }}')

def add_text_shadow(selector, shadow="2px 2px 4px rgba(0,0,0,0.3)"):
    """Add text shadow"""
    ctx.add_css(f'{selector} {{ text-shadow: {shadow}; }}')

def add_border(selector, width="1px", style="solid", color="#ddd"):
    """Add border"""
    ctx.add_css(f'{selector} {{ border: {width} {style} {color}; }}')

def add_border_radius(selector, radius="4px"):
    """Add border radius"""
    ctx.add_css(f'{selector} {{ border-radius: {radius}; }}')

def set_opacity(selector, opacity=1.0):
    """Set opacity"""
    ctx.add_css(f'{selector} {{ opacity: {opacity}; }}')

def add_transform(selector, transform):
    """Add CSS transform"""
    ctx.add_css(f'{selector} {{ transform: {transform}; }}')

def add_transition(selector, property_name="all", duration="0.3s", timing="ease"):
    """Add CSS transition"""
    ctx.add_css(f'{selector} {{ transition: {property_name} {duration} {timing}; }}')

# ==================== UTILITY FUNCTIONS ====================

def set_title(title):
    """Set page title"""
    ctx.add_head(f'<title>{title}</title>')

def add_favicon(href):
    """Add favicon"""
    ctx.add_head(f'<link rel="icon" href="{href}">')

def add_meta(name, content):
    """Add meta tag"""
    ctx.add_head(f'<meta name="{name}" content="{content}">')

def add_external_css(href):
    """Add external CSS"""
    ctx.add_head(f'<link rel="stylesheet" href="{href}">')

def add_external_js(src):
    """Add external JavaScript"""
    ctx.add_head(f'<script src="{src}"></script>')

def add_google_font(font_name):
    """Add Google Font"""
    font_url = font_name.replace(' ', '+')
    ctx.add_head(f'<link href="https://fonts.googleapis.com/css2?family={font_url}&display=swap" rel="stylesheet">')

# ==================== ICONS & SYMBOLS ====================

def add_icon(icon_class, size="24px"):
    """Add an icon (FontAwesome or similar)"""
    ctx.add_html(f'<i class="{icon_class}" style="font-size: {size};"></i>')

def add_emoji(emoji):
    """Add emoji"""
    ctx.add_html(emoji)

# ==================== PROGRESS & LOADING ====================

def add_progress_bar(value=50, max_val=100, css_class="progress"):
    """Add a progress bar"""
    percentage = (value / max_val) * 100
    ctx.add_css(f'.{css_class} {{ width: 100%; background: #f0f0f0; border-radius: 4px; overflow: hidden; }} .{css_class}-bar {{ height: 20px; background: #007bff; transition: width 0.3s; }}')
    ctx.add_html(f'<div class="{css_class}"><div class="{css_class}-bar" style="width: {percentage}%;"></div></div>')

def add_spinner(size="40px", color="#007bff"):
    """Add a loading spinner"""
    ctx.add_css(f'.spinner {{ border: 4px solid #f3f3f3; border-top: 4px solid {color}; border-radius: 50%; width: {size}; height: {size}; animation: spin 1s linear infinite; }} @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}')
    ctx.add_html('<div class="spinner"></div>')

def add_skeleton_loader(width="100%", height="20px"):
    """Add skeleton loader"""
    ctx.add_css(f'.skeleton {{ background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%); background-size: 200% 100%; animation: loading 1.5s infinite; width: {width}; height: {height}; border-radius: 4px; }} @keyframes loading {{ 0% {{ background-position: 200% 0; }} 100% {{ background-position: -200% 0; }} }}')
    ctx.add_html('<div class="skeleton"></div>')

# ==================== BADGES & LABELS ====================

def add_badge(text, color="#007bff"):
    """Add a badge"""
    ctx.add_css(f'.badge {{ display: inline-block; padding: 4px 8px; background: {color}; color: white; border-radius: 12px; font-size: 12px; }}')
    ctx.add_html(f'<span class="badge">{text}</span>')

def add_pill(text, color="#6c757d"):
    """Add a pill badge"""
    ctx.add_css(f'.pill {{ display: inline-block; padding: 6px 16px; background: {color}; color: white; border-radius: 20px; font-size: 14px; }}')
    ctx.add_html(f'<span class="pill">{text}</span>')

# ==================== TOOLTIPS ====================

def add_tooltip(text, tooltip_text):
    """Add tooltip to text"""
    ctx.add_css('.tooltip { position: relative; display: inline-block; } .tooltip .tooltiptext { visibility: hidden; background-color: #555; color: #fff; text-align: center; border-radius: 6px; padding: 5px 10px; position: absolute; z-index: 1; bottom: 125%; left: 50%; transform: translateX(-50%); opacity: 0; transition: opacity 0.3s; } .tooltip:hover .tooltiptext { visibility: visible; opacity: 1; }')
    ctx.add_html(f'<span class="tooltip">{text}<span class="tooltiptext">{tooltip_text}</span></span>')

# ==================== CAROUSEL & SLIDER ====================

def create_carousel(images, css_class="carousel"):
    """Create an image carousel"""
    ctx.add_css(f'.{css_class} {{ position: relative; width: 100%; overflow: hidden; }} .{css_class}-item {{ display: none; width: 100%; }} .{css_class}-item.active {{ display: block; }}')
    for i, img in enumerate(images):
        active = ' active' if i == 0 else ''
        ctx.add_html(f'<div class="{css_class}-item{active}"><img src="{img}" style="width: 100%;"></div>')

# ==================== PRICING TABLES ====================

def create_pricing_card(title, price, features, button_text="Choose Plan"):
    """Create a pricing card"""
    ctx.add_css('.pricing-card { border: 1px solid #ddd; border-radius: 8px; padding: 30px; text-align: center; margin: 10px; } .pricing-card h3 { margin-bottom: 20px; } .pricing-card .price { font-size: 36px; font-weight: bold; margin: 20px 0; } .pricing-card ul { list-style: none; padding: 0; margin: 20px 0; } .pricing-card li { padding: 10px 0; border-bottom: 1px solid #f0f0f0; }')
    card_html = f'<div class="pricing-card"><h3>{title}</h3><div class="price">{price}</div><ul>'
    for feature in features:
        card_html += f'<li>{feature}</li>'
    card_html += f'</ul><button>{button_text}</button></div>'
    ctx.add_html(card_html)

# ==================== TIMELINE ====================

def create_timeline(events, css_class="timeline"):
    """Create a timeline"""
    ctx.add_css(f'.{css_class} {{ position: relative; padding: 20px 0; }} .{css_class}::before {{ content: ""; position: absolute; left: 50%; width: 2px; background: #ddd; top: 0; bottom: 0; }} .{css_class}-item {{ position: relative; margin: 20px 0; }} .{css_class}-content {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 45%; }} .{css_class}-item:nth-child(odd) .{css_class}-content {{ margin-left: 55%; }} .{css_class}-item:nth-child(even) .{css_class}-content {{ margin-right: 55%; }}')
    for event in events:
        if isinstance(event, dict):
            content = f"<strong>{event.get('title', '')}</strong><p>{event.get('description', '')}</p>"
        else:
            content = event
        ctx.add_html(f'<div class="{css_class}-item"><div class="{css_class}-content">{content}</div></div>')

# ==================== SCROLL EFFECTS ====================

def add_parallax(selector, speed=0.5):
    """Add parallax scroll effect"""
    ctx.add_js(f'''
    window.addEventListener('scroll', function() {{
        const elem = document.querySelector('{selector}');
        if (elem) {{
            const scrolled = window.pageYOffset;
            elem.style.transform = 'translateY(' + (scrolled * {speed}) + 'px)';
        }}
    }});
    ''')

def add_scroll_reveal(selector):
    """Add scroll reveal animation"""
    ctx.add_css(f'{selector} {{ opacity: 0; transform: translateY(50px); transition: opacity 0.6s, transform 0.6s; }} {selector}.revealed {{ opacity: 1; transform: translateY(0); }}')
    ctx.add_js(f'''
    window.addEventListener('scroll', function() {{
        document.querySelectorAll('{selector}').forEach(elem => {{
            const rect = elem.getBoundingClientRect();
            if (rect.top < window.innerHeight * 0.8) {{
                elem.classList.add('revealed');
            }}
        }});
    }});
    ''')

def add_sticky_header(selector):
    """Make header sticky on scroll"""
    ctx.add_css(f'{selector} {{ position: sticky; top: 0; z-index: 100; background: white; }}')

# ==================== DARK MODE ====================

def enable_dark_mode():
    """Enable dark mode"""
    ctx.add_css('body.dark-mode { background: #1a1a1a; color: #f0f0f0; } body.dark-mode a { color: #64b5f6; }')
    ctx.add_js('document.body.classList.add("dark-mode");')

def add_dark_mode_toggle():
    """Add dark mode toggle button"""
    ctx.add_html('<button id="dark-mode-toggle">Toggle Dark Mode</button>')
    ctx.add_js('''
    document.getElementById('dark-mode-toggle').addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
    });
    ''')
    ctx.add_css('body.dark-mode { background: #1a1a1a; color: #f0f0f0; transition: background 0.3s, color 0.3s; }')

# ==================== ADVANCED COMPONENTS ====================

def create_dropdown_menu(trigger_text, items, css_class="dropdown"):
    """Create dropdown menu"""
    ctx.add_css(f'.{css_class} {{ position: relative; display: inline-block; }} .{css_class}-content {{ display: none; position: absolute; background: white; min-width: 160px; box-shadow: 0 8px 16px rgba(0,0,0,0.2); z-index: 1; }} .{css_class}-content a {{ color: black; padding: 12px 16px; text-decoration: none; display: block; }} .{css_class}-content a:hover {{ background: #f1f1f1; }} .{css_class}:hover .{css_class}-content {{ display: block; }}')
    dropdown_html = f'<div class="{css_class}"><button>{trigger_text}</button><div class="{css_class}-content">'
    for item in items:
        if isinstance(item, dict):
            dropdown_html += f'<a href="{item.get("url", "#")}">{item.get("text", "Link")}</a>'
        else:
            dropdown_html += f'<a href="#">{item}</a>'
    dropdown_html += '</div></div>'
    ctx.add_html(dropdown_html)

def create_sidebar(content, position="left", width="250px", css_class="sidebar"):
    """Create a sidebar"""
    position_css = f'{position}: 0;' if position in ['left', 'right'] else 'left: 0;'
    ctx.add_css(f'.{css_class} {{ position: fixed; {position_css} top: 0; width: {width}; height: 100%; background: #f8f9fa; padding: 20px; overflow-y: auto; box-shadow: 2px 0 5px rgba(0,0,0,0.1); }}')
    ctx.add_html(f'<aside class="{css_class}">{content}</aside>')

def create_footer(content, css_class="footer"):
    """Create a footer"""
    ctx.add_css(f'.{css_class} {{ background: #333; color: white; padding: 30px 20px; margin-top: 50px; text-align: center; }}')
    ctx.add_html(f'<footer class="{css_class}">{content}</footer>')

def create_hero_section(title, subtitle, background_image="", css_class="hero"):
    """Create a hero section"""
    bg_css = f'background-image: url({background_image});' if background_image else 'background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);'
    ctx.add_css(f'.{css_class} {{ {bg_css} background-size: cover; background-position: center; color: white; padding: 100px 20px; text-align: center; }} .{css_class} h1 {{ font-size: 48px; margin-bottom: 20px; }} .{css_class} p {{ font-size: 20px; }}')
    ctx.add_html(f'<div class="{css_class}"><h1>{title}</h1><p>{subtitle}</p></div>')

# ==================== LIBRARY SYSTEM ====================

def import_library(library_name):
    """Import a .wl library"""
    ctx.imported_libraries.append(library_name)

def define_component(name, html_template):
    """Define a custom component"""
    ctx.custom_functions[name] = html_template

def use_component(name, **kwargs):
    """Use a custom component"""
    if name in ctx.custom_functions:
        template = ctx.custom_functions[name]
        for key, value in kwargs.items():
            template = template.replace(f'{{{{{key}}}}}', str(value))
        ctx.add_html(template)

# ==================== IMAGE GALLERY ====================

def create_image_gallery(images, columns=3, gap="10px", css_class="gallery"):
    """Create an image gallery"""
    ctx.add_css(f'.{css_class} {{ display: grid; grid-template-columns: repeat({columns}, 1fr); gap: {gap}; }} .{css_class} img {{ width: 100%; height: 200px; object-fit: cover; border-radius: 8px; cursor: pointer; transition: transform 0.3s; }} .{css_class} img:hover {{ transform: scale(1.05); }}')
    gallery_html = f'<div class="{css_class}">'
    for img in images:
        if isinstance(img, dict):
            src = img.get('src', '')
            alt = img.get('alt', '')
        else:
            src = img
            alt = ''
        gallery_html += f'<img src="{src}" alt="{alt}">'
    gallery_html += '</div>'
    ctx.add_html(gallery_html)

def create_masonry_gallery(images, css_class="masonry"):
    """Create a masonry-style gallery"""
    ctx.add_css(f'.{css_class} {{ column-count: 3; column-gap: 15px; }} .{css_class} img {{ width: 100%; margin-bottom: 15px; border-radius: 8px; }} @media (max-width: 768px) {{ .{css_class} {{ column-count: 2; }} }} @media (max-width: 480px) {{ .{css_class} {{ column-count: 1; }} }}')
    gallery_html = f'<div class="{css_class}">'
    for img in images:
        gallery_html += f'<img src="{img}">'
    gallery_html += '</div>'
    ctx.add_html(gallery_html)

def add_lightbox(image_selector=".gallery img"):
    """Add lightbox effect to images"""
    ctx.add_css('.lightbox { display: none; position: fixed; z-index: 9999; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9); } .lightbox img { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); max-width: 90%; max-height: 90%; } .lightbox-close { position: absolute; top: 20px; right: 40px; color: white; font-size: 40px; cursor: pointer; }')
    ctx.add_html('<div class="lightbox"><span class="lightbox-close">&times;</span><img src="" alt=""></div>')
    ctx.add_js(f'''
    document.querySelectorAll('{image_selector}').forEach(img => {{
        img.addEventListener('click', function() {{
            const lightbox = document.querySelector('.lightbox');
            const lightboxImg = lightbox.querySelector('img');
            lightboxImg.src = this.src;
            lightbox.style.display = 'block';
        }});
    }});
    document.querySelector('.lightbox-close').addEventListener('click', function() {{
        document.querySelector('.lightbox').style.display = 'none';
    }});
    document.querySelector('.lightbox').addEventListener('click', function(e) {{
        if (e.target === this) this.style.display = 'none';
    }});
    ''')

# ==================== ADVANCED SLIDERS ====================

def create_image_slider(images, auto_play=True, interval=3000, css_class="slider"):
    """Create an image slider with controls"""
    ctx.add_css(f'.{css_class} {{ position: relative; width: 100%; max-width: 800px; margin: 0 auto; overflow: hidden; border-radius: 12px; }} .{css_class}-track {{ display: flex; transition: transform 0.5s ease; }} .{css_class}-slide {{ min-width: 100%; height: 400px; }} .{css_class}-slide img {{ width: 100%; height: 100%; object-fit: cover; }} .{css_class}-btn {{ position: absolute; top: 50%; transform: translateY(-50%); background: rgba(255,255,255,0.8); border: none; padding: 15px; cursor: pointer; font-size: 20px; border-radius: 50%; }} .{css_class}-prev {{ left: 20px; }} .{css_class}-next {{ right: 20px; }} .{css_class}-dots {{ text-align: center; padding: 15px 0; }} .{css_class}-dot {{ display: inline-block; width: 12px; height: 12px; border-radius: 50%; background: #ddd; margin: 0 5px; cursor: pointer; }} .{css_class}-dot.active {{ background: #667eea; }}')
    
    slider_html = f'<div class="{css_class}"><div class="{css_class}-track">'
    for img in images:
        slider_html += f'<div class="{css_class}-slide"><img src="{img}"></div>'
    slider_html += f'</div><button class="{css_class}-btn {css_class}-prev">&#10094;</button><button class="{css_class}-btn {css_class}-next">&#10095;</button><div class="{css_class}-dots">'
    for i in range(len(images)):
        active = ' active' if i == 0 else ''
        slider_html += f'<span class="{css_class}-dot{active}" data-slide="{i}"></span>'
    slider_html += '</div></div>'
    ctx.add_html(slider_html)
    
    ctx.add_js(f'''
    (function() {{
        const slider = document.querySelector('.{css_class}');
        const track = slider.querySelector('.{css_class}-track');
        const slides = slider.querySelectorAll('.{css_class}-slide');
        const prev = slider.querySelector('.{css_class}-prev');
        const next = slider.querySelector('.{css_class}-next');
        const dots = slider.querySelectorAll('.{css_class}-dot');
        let current = 0;
        
        function goToSlide(n) {{
            current = (n + slides.length) % slides.length;
            track.style.transform = `translateX(-${{current * 100}}%)`;
            dots.forEach((dot, i) => dot.classList.toggle('active', i === current));
        }}
        
        prev.addEventListener('click', () => goToSlide(current - 1));
        next.addEventListener('click', () => goToSlide(current + 1));
        dots.forEach((dot, i) => dot.addEventListener('click', () => goToSlide(i)));
        
        {'setInterval(() => goToSlide(current + 1), ' + str(interval) + ');' if auto_play else ''}
    }})();
    ''')

# ==================== CHARTS & DATA VISUALIZATION ====================

def create_bar_chart(data, labels, title="", css_class="bar-chart"):
    """Create a simple bar chart"""
    max_val = max(data) if data else 1
    ctx.add_css(f'.{css_class} {{ max-width: 600px; margin: 20px auto; }} .{css_class}-title {{ text-align: center; font-size: 20px; font-weight: bold; margin-bottom: 20px; }} .{css_class}-bar {{ display: flex; align-items: center; margin: 10px 0; }} .{css_class}-label {{ width: 100px; text-align: right; padding-right: 15px; }} .{css_class}-bar-fill {{ height: 30px; background: linear-gradient(90deg, #667eea, #764ba2); border-radius: 4px; transition: width 0.5s; }} .{css_class}-value {{ margin-left: 10px; font-weight: bold; }}')
    
    chart_html = f'<div class="{css_class}">'
    if title:
        chart_html += f'<div class="{css_class}-title">{title}</div>'
    for i, (label, value) in enumerate(zip(labels, data)):
        percentage = (value / max_val * 100) if max_val > 0 else 0
        chart_html += f'<div class="{css_class}-bar"><div class="{css_class}-label">{label}</div><div class="{css_class}-bar-fill" style="width: {percentage}%;"></div><div class="{css_class}-value">{value}</div></div>'
    chart_html += '</div>'
    ctx.add_html(chart_html)

def create_pie_chart(data, labels, colors=None, css_class="pie-chart"):
    """Create a simple pie chart using CSS conic gradient"""
    if not colors:
        colors = ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#43e97b', '#fa709a']
    
    total = sum(data)
    percentages = [val/total*100 for val in data] if total > 0 else [0]*len(data)
    
    gradient_stops = []
    cumulative = 0
    for i, pct in enumerate(percentages):
        color = colors[i % len(colors)]
        gradient_stops.append(f'{color} {cumulative}% {cumulative + pct}%')
        cumulative += pct
    
    gradient = ', '.join(gradient_stops)
    
    ctx.add_css(f'.{css_class} {{ width: 300px; height: 300px; border-radius: 50%; background: conic-gradient({gradient}); margin: 20px auto; }} .{css_class}-legend {{ max-width: 300px; margin: 20px auto; }} .{css_class}-legend-item {{ display: flex; align-items: center; margin: 8px 0; }} .{css_class}-legend-color {{ width: 20px; height: 20px; border-radius: 4px; margin-right: 10px; }}')
    
    chart_html = f'<div class="{css_class}"></div><div class="{css_class}-legend">'
    for i, (label, value) in enumerate(zip(labels, data)):
        color = colors[i % len(colors)]
        chart_html += f'<div class="{css_class}-legend-item"><div class="{css_class}-legend-color" style="background: {color};"></div><span>{label}: {value}</span></div>'
    chart_html += '</div>'
    ctx.add_html(chart_html)

# ==================== COUNTDOWN TIMER ====================

def create_countdown(target_date, css_class="countdown"):
    """Create a countdown timer"""
    ctx.add_css(f'.{css_class} {{ display: flex; justify-content: center; gap: 30px; padding: 30px; }} .{css_class}-item {{ text-align: center; }} .{css_class}-number {{ font-size: 48px; font-weight: bold; color: #667eea; }} .{css_class}-label {{ font-size: 14px; color: #666; text-transform: uppercase; }}')
    
    ctx.add_html(f'<div class="{css_class}"><div class="{css_class}-item"><div class="{css_class}-number" id="days">0</div><div class="{css_class}-label">Days</div></div><div class="{css_class}-item"><div class="{css_class}-number" id="hours">0</div><div class="{css_class}-label">Hours</div></div><div class="{css_class}-item"><div class="{css_class}-number" id="minutes">0</div><div class="{css_class}-label">Minutes</div></div><div class="{css_class}-item"><div class="{css_class}-number" id="seconds">0</div><div class="{css_class}-label">Seconds</div></div></div>')
    
    ctx.add_js(f'''
    const targetDate = new Date('{target_date}').getTime();
    function updateCountdown() {{
        const now = new Date().getTime();
        const distance = targetDate - now;
        
        if (distance < 0) {{
            document.getElementById('days').innerHTML = '0';
            document.getElementById('hours').innerHTML = '0';
            document.getElementById('minutes').innerHTML = '0';
            document.getElementById('seconds').innerHTML = '0';
            return;
        }}
        
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
        document.getElementById('days').innerHTML = days;
        document.getElementById('hours').innerHTML = hours;
        document.getElementById('minutes').innerHTML = minutes;
        document.getElementById('seconds').innerHTML = seconds;
    }}
    updateCountdown();
    setInterval(updateCountdown, 1000);
    ''')

# ==================== VIDEO BACKGROUNDS ====================

def add_video_background(video_src, css_class="video-bg"):
    """Add a video background"""
    ctx.add_css(f'.{css_class} {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: -1; }} .{css_class}-overlay {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: -1; }}')
    ctx.add_html(f'<video class="{css_class}" autoplay muted loop><source src="{video_src}" type="video/mp4"></video><div class="{css_class}-overlay"></div>')

# ==================== SOCIAL MEDIA EMBEDS ====================

def embed_youtube(video_id, width="560", height="315"):
    """Embed a YouTube video"""
    ctx.add_html(f'<iframe width="{width}" height="{height}" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')

def embed_twitter_timeline(username):
    """Embed Twitter timeline"""
    ctx.add_html(f'<a class="twitter-timeline" href="https://twitter.com/{username}">Tweets by {username}</a>')
    ctx.add_head('<script async src="https://platform.twitter.com/widgets.js"></script>')

def add_social_share_buttons(url="", text=""):
    """Add social media share buttons"""
    share_url = url or "window.location.href"
    share_text = text or "document.title"
    
    ctx.add_css('.social-share { display: flex; gap: 10px; margin: 20px 0; } .social-share button { padding: 10px 20px; border: none; border-radius: 4px; color: white; cursor: pointer; font-size: 14px; } .social-share .twitter { background: #1DA1F2; } .social-share .facebook { background: #4267B2; } .social-share .linkedin { background: #0077B5; }')
    
    ctx.add_html(f'<div class="social-share"><button class="twitter" onclick="window.open(\'https://twitter.com/intent/tweet?url=\'+encodeURIComponent({share_url})+\'&text=\'+encodeURIComponent({share_text}), \'_blank\')">Share on Twitter</button><button class="facebook" onclick="window.open(\'https://www.facebook.com/sharer/sharer.php?u=\'+encodeURIComponent({share_url}), \'_blank\')">Share on Facebook</button><button class="linkedin" onclick="window.open(\'https://www.linkedin.com/sharing/share-offsite/?url=\'+encodeURIComponent({share_url}), \'_blank\')">Share on LinkedIn</button></div>')

# ==================== MAPS ====================

def embed_google_map(address, width="100%", height="400px"):
    """Embed Google Map"""
    encoded_address = address.replace(' ', '+')
    ctx.add_html(f'<iframe width="{width}" height="{height}" frameborder="0" src="https://www.google.com/maps?q={encoded_address}&output=embed"></iframe>')

# ==================== ADVANCED ANIMATIONS ====================

def add_typing_effect(selector, text, speed=100):
    """Add typing animation effect"""
    ctx.add_js(f'''
    const element = document.querySelector('{selector}');
    const text = '{text}';
    let i = 0;
    element.innerHTML = '';
    function typeWriter() {{
        if (i < text.length) {{
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(typeWriter, {speed});
        }}
    }}
    typeWriter();
    ''')

def add_fade_in_on_scroll(selector):
    """Add fade-in animation on scroll"""
    ctx.add_css(f'{selector} {{ opacity: 0; transform: translateY(30px); transition: opacity 0.6s, transform 0.6s; }} {selector}.visible {{ opacity: 1; transform: translateY(0); }}')
    ctx.add_js(f'''
    const observer = new IntersectionObserver(entries => {{
        entries.forEach(entry => {{
            if (entry.isIntersecting) {{
                entry.target.classList.add('visible');
            }}
        }});
    }});
    document.querySelectorAll('{selector}').forEach(el => observer.observe(el));
    ''')

def add_float_animation(selector, duration="3s"):
    """Add floating animation"""
    ctx.add_css(f'{selector} {{ animation: float {duration} ease-in-out infinite; }} @keyframes float {{ 0%, 100% {{ transform: translateY(0px); }} 50% {{ transform: translateY(-20px); }} }}')

def add_glow_effect(selector, color="#667eea"):
    """Add glowing effect"""
    ctx.add_css(f'{selector} {{ animation: glow 2s ease-in-out infinite alternate; }} @keyframes glow {{ from {{ box-shadow: 0 0 10px {color}, 0 0 20px {color}, 0 0 30px {color}; }} to {{ box-shadow: 0 0 20px {color}, 0 0 30px {color}, 0 0 40px {color}; }} }}')

# ==================== ADVANCED FORMS ====================

def add_form_validation(form_id):
    """Add form validation"""
    ctx.add_js(f'''
    document.getElementById('{form_id}').addEventListener('submit', function(e) {{
        const inputs = this.querySelectorAll('input[required], textarea[required]');
        let valid = true;
        inputs.forEach(input => {{
            if (!input.value.trim()) {{
                input.style.borderColor = 'red';
                valid = false;
            }} else {{
                input.style.borderColor = '';
            }}
        }});
        if (!valid) {{
            e.preventDefault();
            alert('Please fill in all required fields');
        }}
    }});
    ''')

def add_password_strength_meter(input_id):
    """Add password strength indicator"""
    ctx.add_css(f'#{input_id}-strength {{ height: 5px; margin-top: 5px; border-radius: 3px; transition: all 0.3s; }} .strength-weak {{ background: #ff4444; width: 33%; }} .strength-medium {{ background: #ffaa00; width: 66%; }} .strength-strong {{ background: #00C851; width: 100%; }}')
    ctx.add_html(f'<div id="{input_id}-strength"></div>')
    ctx.add_js(f'''
    document.getElementById('{input_id}').addEventListener('input', function(e) {{
        const password = e.target.value;
        const strength = document.getElementById('{input_id}-strength');
        let score = 0;
        if (password.length >= 8) score++;
        if (/[A-Z]/.test(password)) score++;
        if (/[0-9]/.test(password)) score++;
        if (/[^A-Za-z0-9]/.test(password)) score++;
        
        strength.className = '';
        if (score <= 1) strength.className = 'strength-weak';
        else if (score <= 3) strength.className = 'strength-medium';
        else strength.className = 'strength-strong';
    }});
    ''')

# ==================== STICKY ELEMENTS ====================

def make_sticky(selector, top="0px"):
    """Make element sticky on scroll"""
    ctx.add_css(f'{selector} {{ position: sticky; top: {top}; z-index: 100; }}')

def add_sticky_cta(text, link="#", position="bottom-right"):
    """Add sticky call-to-action button"""
    positions = {
        'bottom-right': 'bottom: 20px; right: 20px;',
        'bottom-left': 'bottom: 20px; left: 20px;',
        'top-right': 'top: 20px; right: 20px;',
        'top-left': 'top: 20px; left: 20px;'
    }
    pos_css = positions.get(position, positions['bottom-right'])
    
    ctx.add_css(f'.sticky-cta {{ position: fixed; {pos_css} z-index: 1000; padding: 15px 30px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; text-decoration: none; border-radius: 50px; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4); transition: transform 0.3s; }} .sticky-cta:hover {{ transform: scale(1.05); }}')
    ctx.add_html(f'<a href="{link}" class="sticky-cta">{text}</a>')

# ==================== COLOR UTILITIES ====================

def create_color_palette(colors, css_class="color-palette"):
    """Display a color palette"""
    ctx.add_css(f'.{css_class} {{ display: flex; gap: 10px; margin: 20px 0; }} .{css_class}-color {{ width: 100px; height: 100px; border-radius: 8px; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 10px; color: white; font-size: 12px; font-family: monospace; }}')
    palette_html = f'<div class="{css_class}">'
    for color in colors:
        palette_html += f'<div class="{css_class}-color" style="background: {color};">{color}</div>'
    palette_html += '</div>'
    ctx.add_html(palette_html)

# ==================== TYPOGRAPHY ====================

def add_dropcap(selector):
    """Add drop cap to first letter"""
    ctx.add_css(f'{selector}::first-letter {{ float: left; font-size: 75px; line-height: 60px; padding: 8px 8px 0 0; font-weight: bold; color: #667eea; }}')

def add_text_gradient(selector, color1="#667eea", color2="#764ba2"):
    """Add gradient text effect"""
    ctx.add_css(f'{selector} {{ background: linear-gradient(90deg, {color1}, {color2}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }}')

# ==================== CONTEXT MANAGEMENT ====================

def reset_context():
    """Reset the context"""
    global ctx
    ctx = WebeaseContext()

def get_context():
    """Get the current context"""
    return ctx
