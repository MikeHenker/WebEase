# Library Demo - Using Custom Components from .wl file

import_library("ui_components")

set_title("Webease Library Demo")
set_background("#f5f7fa")
add_google_font("Poppins")
set_font("Poppins, sans-serif", "16px")

create_hero_section("Component Library Demo", "Reusable components with .wl files", "")

create_container("", "main-content", True)

add_title("Custom Feature Cards", 2)
add_text("These cards are defined in the ui_components.wl library file:")

create_row("", "features")
use_component("feature_card", title="Easy to Use", description="Simple syntax anyone can learn")
use_component("feature_card", title="Reusable", description="Create components once, use everywhere")
use_component("feature_card", title="Powerful", description="Build complex websites with ease")
end_flex_container()

add_spacer("40px")

add_title("Call-to-Action Button", 2)
use_component("cta_button", text="Get Started Now")

add_spacer("40px")

add_title("Testimonials", 2)
use_component("testimonial", quote="Webease made building my first website so easy!", author="Sarah J.")
use_component("testimonial", quote="I love how simple and powerful Webease is.", author="Mike T.")

add_spacer("40px")

add_title("Statistics", 2)
create_row("", "stats")
use_component("stat_box", number="230+", label="Functions")
use_component("stat_box", number="100%", label="Beginner Friendly")
use_component("stat_box", number="0", label="HTML Knowledge Needed")
end_flex_container()

create_footer("Built with Webease & Custom Libraries", "demo-footer")

add_custom_css(".features { justify-content: center; gap: 20px; flex-wrap: wrap; }")
add_custom_css(".stats { justify-content: center; gap: 30px; flex-wrap: wrap; max-width: 800px; margin: 0 auto; }")
