# Advanced Webease Example - Showcasing 100+ Functions

set_title("Advanced Webease Demo")
add_google_font("Poppins")
set_font("Poppins, sans-serif", "16px")
set_background_gradient("#667eea", "#764ba2", "to bottom right")

create_hero_section("Advanced Webease Demo", "Explore the power of 230+ functions", "")

create_container("", "main-container", True)

add_title("Beautiful Cards", 2)
create_row("", "card-row")
create_card("Feature 1", "Amazing features at your fingertips", "card-1", True)
create_card("Feature 2", "No coding experience needed", "card-2", True)
create_card("Feature 3", "Instant website creation", "card-3", True)
end_flex_container()

add_spacer("40px")

add_title("Alert Boxes", 2)
create_info_box("This is an info box with important information!")
create_success_box("Success! Your action was completed.")
create_warning_box("Warning: Please review this information.")
create_error_box("Error: Something went wrong.")

add_spacer("40px")

add_title("Interactive Elements", 2)
create_form("", "post", "demo-form")
add_label("Your Name:")
add_text_input("name", "Enter your name")
add_br(1)
add_label("Your Email:")
add_email_input("email", "Enter your email")
add_br(1)
add_label("Message:")
add_textarea("message", "Type your message here", 4, 50)
add_br(1)
add_submit_button("Send Message")
end_form()

add_spacer("40px")

add_title("Navigation Components", 2)
create_tabs(["Tab 1", "Tab 2", "Tab 3"], "demo-tabs")

add_spacer("30px")

create_breadcrumbs(["Home", "Products", "Category", "Item"], "demo-breadcrumbs")

add_spacer("40px")

add_title("Progress & Loading", 2)
add_text("Progress Bar:")
add_progress_bar(75, 100, "demo-progress")
add_spacer("20px")
add_text("Loading Spinner:")
add_spinner("40px", "#667eea")

add_spacer("40px")

add_title("Badges & Labels", 2)
add_text("Status: ")
add_badge("New", "#28a745")
add_space(2)
add_badge("Featured", "#007bff")
add_space(2)
add_pill("Premium", "#6f42c1")

add_spacer("40px")

add_title("Pricing Table", 2)
create_row("", "pricing-row")
create_pricing_card("Basic", "$9/mo", ["10 Projects", "5 GB Storage", "Email Support"], "Get Started")
create_pricing_card("Pro", "$29/mo", ["Unlimited Projects", "50 GB Storage", "Priority Support", "Advanced Features"], "Upgrade Now")
create_pricing_card("Enterprise", "$99/mo", ["Everything in Pro", "Unlimited Storage", "Dedicated Support", "Custom Solutions"], "Contact Us")
end_flex_container()

add_spacer("60px")

create_footer("Made with ❤️ using Webease | © 2024", "demo-footer")

add_fade_in(".card-1", "0.5s")
add_fade_in(".card-2", "0.7s")
add_fade_in(".card-3", "0.9s")
add_hover_effect(".card-1", "transform", "translateY(-5px)", "0.3s")
add_hover_effect(".card-2", "transform", "translateY(-5px)", "0.3s")
add_hover_effect(".card-3", "transform", "translateY(-5px)", "0.3s")

add_custom_css(".main-container { margin-top: -50px; position: relative; z-index: 10; }")
add_custom_css(".card-row { justify-content: center; gap: 20px; flex-wrap: wrap; }")
add_custom_css(".pricing-row { justify-content: center; gap: 20px; flex-wrap: wrap; }")
