# Portfolio Website Example

set_title("John Doe - Portfolio")
set_background("#ffffff")
set_font("Inter, sans-serif", "16px")
add_google_font("Inter")

create_navbar("John Doe", [{"url": "#about", "text": "About"}, {"url": "#projects", "text": "Projects"}, {"url": "#contact", "text": "Contact"}], "main-nav")

create_hero_section("Hi, I'm John Doe", "Web Developer & Designer", "")

create_container("", "content", True)

add_title("About Me", 2)
add_text("I'm a passionate web developer with 5 years of experience creating beautiful and functional websites.")

add_spacer("40px")

add_title("My Skills", 2)
create_row("", "skills")
create_card("Frontend", "HTML, CSS, JavaScript, React", "skill-card")
create_card("Backend", "Python, Node.js, Databases", "skill-card")
create_card("Design", "UI/UX, Figma, Adobe XD", "skill-card")
end_flex_container()

add_spacer("40px")

add_title("Projects", 2)
create_grid(2, "30px", "projects-grid")
create_panel("E-commerce Site", "Built a full-stack e-commerce platform with React and Node.js")
create_panel("Portfolio App", "Created a portfolio builder app for creatives")
create_panel("Task Manager", "Developed a collaborative task management tool")
create_panel("Blog Platform", "Built a modern blogging platform with CMS")
end_grid()

add_spacer("40px")

add_title("Contact Me", 2)
create_form("", "post", "contact-form")
add_text_input("name", "Your Name")
add_br(1)
add_email_input("email", "Your Email")
add_br(1)
add_textarea("message", "Your Message", 5, 50)
add_br(1)
add_submit_button("Send Message")
end_form()

create_footer("© 2024 John Doe. Built with Webease.", "site-footer")

add_hover_effect(".skill-card", "transform", "scale(1.05)", "0.3s")
add_custom_css("#about { scroll-margin-top: 80px; } #projects { scroll-margin-top: 80px; } #contact { scroll-margin-top: 80px; }")
add_custom_css(".skills { gap: 20px; }")
