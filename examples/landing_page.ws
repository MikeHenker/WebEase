# Product Launch Landing Page

set_title("Product Launch - Coming Soon")
set_background("#ffffff")
add_google_font("Poppins")
set_font("Poppins, sans-serif", "16px")

create_navbar("LaunchApp", [{"url": "#features", "text": "Features"}, {"url": "#pricing", "text": "Pricing"}, {"url": "#contact", "text": "Contact"}], "top-nav")

create_hero_section("Revolutionary Product Launch", "Something amazing is coming December 31, 2025", "")

create_container("", "content", True)

add_title("Countdown to Launch", 2)
create_countdown("2025-12-31 00:00:00", "launch-countdown")

add_spacer("60px")

add_title("What We're Building", 2)
create_row("", "features-row")
create_card("Fast", "Lightning-fast performance that scales", "feature-box")
create_card("Secure", "Bank-level security for your data", "feature-box")
create_card("Simple", "Intuitive design anyone can use", "feature-box")
end_flex_container()

add_spacer("60px")

add_title("Early Bird Pricing", 2)
create_row("", "pricing-section")
create_pricing_card("Starter", "$9/mo", ["5 Projects", "10 GB Storage", "Email Support"], "Reserve Now")
create_pricing_card("Professional", "$29/mo", ["Unlimited Projects", "100 GB Storage", "Priority Support", "Advanced Analytics"], "Reserve Now")
create_pricing_card("Enterprise", "$99/mo", ["Everything in Pro", "Unlimited Storage", "24/7 Support", "Custom Solutions"], "Contact Sales")
end_flex_container()

add_spacer("60px")

add_title("Join the Waitlist", 2)
create_form("", "post", "waitlist-form")
add_text_input("email", "Enter your email")
add_br(1)
add_submit_button("Join Waitlist")
end_form()

add_spacer("40px")

add_social_share_buttons("", "")

add_sticky_cta("Reserve Your Spot", "#waitlist-form", "bottom-right")

create_footer("© 2024 LaunchApp. Built with Webease.", "page-footer")

add_fade_in(".feature-box", "1s")
add_hover_effect(".feature-box", "transform", "translateY(-10px)", "0.3s")
add_pulse(".launch-countdown")

add_custom_css(".features-row { gap: 30px; justify-content: center; flex-wrap: wrap; }")
add_custom_css(".pricing-section { gap: 30px; justify-content: center; flex-wrap: wrap; }")
add_custom_css("#waitlist-form { max-width: 400px; margin: 0 auto; text-align: center; }")
add_custom_css("#waitlist-form input { width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 4px; margin-bottom: 10px; }")
