# Webease

**A beginner-friendly programming language for creating beautiful websites**

Webease makes web development simple and fun! Write `.ws` files using intuitive commands, compile them to HTML, and launch your website instantly. No HTML, CSS, or JavaScript knowledge required!

## 🌟 Features

- **150+ Built-in Functions** - From basic HTML to advanced animations
- **Super Beginner-Friendly** - Simple, intuitive Python-like syntax
- **Library System** - Create reusable components with `.wl` files
- **Instant Preview** - Compiles and launches in your browser automatically
- **Beautiful by Default** - Responsive, modern designs out of the box
- **No Configuration** - Just write and run!

## 🚀 Quick Start

### Installation

```bash
# Clone this repository
git clone https://github.com/MikeHenker/WebEase
cd webease

# Install dependencies (already included)
# Python 3.11+ required
```

### Your First Website

Create a file called `hello.ws`:

```python
set_title("My First Website")

add_title("Hello, World!", 1)
add_text("Welcome to Webease!")

add_list(["Easy to learn", "Fun to use", "Powerful features"], False)

set_background("#f0f0f0")
set_font("Arial, sans-serif", "16px")
```

Compile and launch:

```bash
python webease.py hello.ws
```
or if you want to use a gui use compile_gui.py

Your browser will automatically open with your new website!

## 📚 Function Categories

### Basic HTML Elements
- `add_title(text, level)` - Add headings (h1-h6)
- `add_text(text)` - Add paragraphs
- `add_link(url, text)` - Add hyperlinks
- `add_image(src, alt)` - Add images
- `add_list(items, ordered)` - Add lists
- `create_table(headers, rows)` - Create tables

### Text Formatting
- `add_bold(text)` - Bold text
- `add_italic(text)` - Italic text
- `add_underline(text)` - Underlined text
- `add_code(text)` - Inline code
- `add_code_block(code)` - Code blocks
- `add_quote(text)` - Blockquotes

### Styling
- `set_background(color)` - Set background color
- `set_background_gradient(color1, color2)` - Gradient backgrounds
- `set_font(family, size)` - Set page font
- `set_text_color(color)` - Set text color
- `add_custom_css(css)` - Add custom CSS

### Layout
- `create_container(content)` - Responsive containers
- `create_row()` / `end_flex_container()` - Flexbox rows
- `create_grid(columns, gap)` / `end_grid()` - Grid layouts
- `create_column(content, width)` - Grid columns
- `add_spacer(height)` - Vertical spacing

### Forms & Inputs
- `create_form(action, method)` / `end_form()` - Forms
- `add_text_input(name, placeholder)` - Text inputs
- `add_email_input(name)` - Email inputs
- `add_password_input(name)` - Password inputs
- `add_textarea(name, placeholder)` - Text areas
- `add_button(text)` - Buttons
- `add_checkbox(name, label)` - Checkboxes
- `add_radio(name, label, value)` - Radio buttons
- `add_select(name, options)` - Dropdowns

### Cards & Content Boxes
- `create_card(title, content)` - Card components
- `create_info_box(content)` - Info boxes (blue)
- `create_success_box(content)` - Success boxes (green)
- `create_warning_box(content)` - Warning boxes (yellow)
- `create_error_box(content)` - Error boxes (red)
- `create_panel(title, content)` - Panels with headers

### Navigation
- `create_navbar(brand, links)` - Navigation bars
- `create_menu(items)` - Vertical menus
- `create_breadcrumbs(items)` - Breadcrumb navigation
- `create_tabs(tabs)` - Tab components
- `create_accordion(items)` - Accordion panels

### Modals & Dialogs
- `create_modal(id, title, content)` - Modal dialogs
- `add_alert(message, type)` - Alert messages
- `add_toast(message, duration)` - Toast notifications

### Animations
- `add_fade_in(selector, duration)` - Fade in animation
- `add_slide_in(selector, direction)` - Slide in animation
- `add_bounce(selector)` - Bounce animation
- `add_rotate(selector, degrees)` - Rotation animation
- `add_scale(selector, scale)` - Scale/zoom animation
- `add_shake(selector)` - Shake animation
- `add_pulse(selector)` - Pulse animation
- `add_float_animation(selector)` - Floating effect
- `add_glow_effect(selector, color)` - Glowing effect

### Hover Effects
- `add_hover_effect(selector, property, value)` - Custom hover effects
- `add_hover_color(selector, color)` - Hover color change
- `add_hover_background(selector, color)` - Hover background change

### Image Galleries
- `create_image_gallery(images, columns)` - Grid gallery
- `create_masonry_gallery(images)` - Masonry layout
- `add_lightbox(selector)` - Lightbox/popup viewer

### Sliders & Carousels
- `create_carousel(images)` - Basic carousel
- `create_image_slider(images, auto_play, interval)` - Advanced slider with controls

### Charts & Data Visualization
- `create_bar_chart(data, labels, title)` - Bar charts
- `create_pie_chart(data, labels, colors)` - Pie charts

### Advanced Components
- `create_countdown(target_date)` - Countdown timer
- `add_video_background(video_src)` - Video backgrounds
- `embed_youtube(video_id)` - YouTube embeds
- `embed_google_map(address)` - Google Maps
- `add_social_share_buttons()` - Social sharing
- `create_pricing_card(title, price, features)` - Pricing cards
- `create_timeline(events)` - Timeline component
- `create_dropdown_menu(trigger, items)` - Dropdown menus
- `create_sidebar(content, position)` - Sidebars
- `create_footer(content)` - Footers
- `create_hero_section(title, subtitle)` - Hero sections

### Typography & Effects
- `add_dropcap(selector)` - Drop cap first letter
- `add_text_gradient(selector, color1, color2)` - Gradient text
- `add_typing_effect(selector, text, speed)` - Typing animation
- `add_fade_in_on_scroll(selector)` - Scroll reveal animation
- `add_scroll_reveal(selector)` - Scroll-based reveal
- `add_sticky_header(selector)` - Sticky header
- `make_sticky(selector, top)` - Make element sticky
- `add_sticky_cta(text, link, position)` - Sticky CTA button

### Utilities
- `set_title(title)` - Set page title
- `add_favicon(href)` - Add favicon
- `add_meta(name, content)` - Add meta tags
- `add_google_font(font_name)` - Load Google Fonts
- `add_external_css(href)` - Load external CSS
- `add_external_js(src)` - Load external JavaScript
- `enable_dark_mode()` - Enable dark mode
- `add_dark_mode_toggle()` - Dark mode toggle button
- `create_color_palette(colors)` - Display color palette

### Responsive Design
- `set_mobile_breakpoint(max_width)` - Set breakpoints
- `add_responsive_text(selector, mobile_size, desktop_size)` - Responsive text
- `hide_on_mobile(selector)` - Hide on mobile
- `hide_on_desktop(selector)` - Hide on desktop

### Progress & Loading
- `add_progress_bar(value, max)` - Progress bars
- `add_spinner(size, color)` - Loading spinners
- `add_skeleton_loader(width, height)` - Skeleton loaders

### Badges & Labels
- `add_badge(text, color)` - Badge labels
- `add_pill(text, color)` - Pill badges
- `add_tooltip(text, tooltip_text)` - Tooltips

### Advanced Forms
- `add_form_validation(form_id)` - Form validation
- `add_password_strength_meter(input_id)` - Password strength
- `add_file_input(name, accept)` - File uploads
- `add_date_input(name, value)` - Date pickers
- `add_color_input(name, value)` - Color pickers
- `add_range_input(name, min, max, value)` - Range sliders

## 📦 Library System

Create reusable components with `.wl` files!

### Creating a Library (`components.wl`)

```
component my_button {
<button style="background: blue; color: white; padding: 10px 20px;">
    {{text}}
</button>
}

component feature_box {
<div style="border: 1px solid #ddd; padding: 20px; border-radius: 8px;">
    <h3>{{title}}</h3>
    <p>{{description}}</p>
</div>
}
```

### Using Libraries in `.ws` files

```python
import_library("components")

use_component("my_button", text="Click Me")
use_component("feature_box", title="Feature 1", description="Amazing feature")
```

## 📝 Examples

Check the `examples/` directory for complete examples:

- `hello.ws` - Basic introduction
- `advanced.ws` - Advanced features showcase
- `portfolio.ws` - Portfolio website
- `library_demo.ws` - Library system demo
- `gallery.ws` - Image galleries and sliders
- `data_viz.ws` - Charts and data visualization
- `landing_page.ws` - Product launch page with countdown

## 🎨 Styling Best Practices

### Color Schemes
```python
# Gradient backgrounds
set_background_gradient("#667eea", "#764ba2", "to bottom right")

# Color palette display
create_color_palette(["#667eea", "#764ba2", "#f093fb", "#4facfe"])
```

### Responsive Design
```python
# Mobile-first approach
set_mobile_breakpoint("768px")
hide_on_mobile(".desktop-only")
hide_on_desktop(".mobile-only")
```

### Animations
```python
# Combine animations
add_fade_in(".card", "0.5s")
add_hover_effect(".card", "transform", "translateY(-5px)", "0.3s")
```

## 🔧 Command-Line Options

```bash
# Compile and auto-open in browser (default)
python webease.py myfile.ws

# Compile and save without opening
python webease.py myfile.ws --save

# Custom output directory
python webease.py myfile.ws --output custom_folder

# Help
python webease.py --help
```

## 🗂️ Project Structure

```
webease/
├── src/
│   └── webease/
│       ├── __init__.py
│       ├── functions.py      # 150+ functions
│       ├── compiler.py        # .ws file compiler
│       └── cli.py            # Command-line interface
├── examples/                  # Example .ws files
├── libraries/                 # Reusable .wl components
├── output/                    # Compiled HTML files
├── webease.py                # Main entry point
└── README.md
```

## 🐛 Error Handling

Webease provides beginner-friendly error messages:

```
╔══════════════════════════════════════════════════════════════╗
║  WEBEASE ERROR                                               ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Error Type: NameError                                       ║
║                                                              ║
║  Message: Function 'add_titl' is not defined                 ║
║                                                              ║
║  💡 Suggestion:                                             ║
║  Check if the function name is spelled correctly.            ║
║  Available functions are listed in the documentation.        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

## 🚀 Advanced Usage

### Custom CSS and JavaScript

```python
# Add custom CSS
add_custom_css(".my-class { color: red; font-weight: bold; }")

# Add custom JavaScript
add_js_code("console.log('Hello from Webease!');")
```

### Component Definition

```python
# Define components programmatically
define_component("alert_box", "<div class='alert'>{{message}}</div>")
use_component("alert_box", message="Hello!")
```

## 💡 Tips for Beginners

1. **Start Simple** - Begin with `hello.ws` and gradually add features
2. **Use Examples** - Learn from the examples in the `examples/` directory
3. **Experiment** - Try different functions and see what they do
4. **Build Libraries** - Create `.wl` files for components you use often
5. **Read Errors** - Error messages guide you to fix issues
6. **Combine Functions** - Mix and match functions for unique designs

## 🎯 Common Use Cases

### Personal Portfolio
```python
create_navbar("Your Name", links)
create_hero_section("Hi, I'm Your Name", "Web Developer")
create_card("Project 1", "Description")
create_footer("© 2024")
```

### Landing Page
```python
create_hero_section("Product Name", "Tagline")
create_countdown("2025-12-31 00:00:00")
create_pricing_card("Basic", "$9/mo", features)
```

### Blog Post
```python
add_title("Blog Post Title", 1)
add_text("Introduction paragraph")
add_image("image.jpg", "Description")
add_quote("Important quote")
```

### Data Dashboard
```python
create_bar_chart(data, labels, "Sales Chart")
create_pie_chart(data, labels)
add_progress_bar(75, 100)
```

## 🔄 Workflow

1. **Write** - Create `.ws` file with Webease functions
2. **Compile** - Run `python webease.py yourfile.ws`
3. **Preview** - Browser opens automatically with your website
4. **Refine** - Edit `.ws` file and recompile
5. **Deploy** - Use generated HTML from `output/` folder

## 🌐 Browser Compatibility

All generated HTML/CSS/JS works in:
- Chrome
- Firefox  
- Safari
- Edge
- Mobile browsers

## 📄 License

Open source - feel free to use, modify, and share!

## 🤝 Contributing

Create your own functions and library components! The codebase is designed to be extensible.

## 💬 Support

- Check examples for inspiration
- Read error messages carefully - they guide you to solutions
- Experiment with functions - they're designed to be intuitive!

---

**Made with ❤️ for beginners learning web development**

Start creating beautiful websites today with Webease! 🚀
