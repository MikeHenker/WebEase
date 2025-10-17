# Data Visualization Example

set_title("Data Dashboard")
set_background("#ffffff")
add_google_font("Inter")
set_font("Inter, sans-serif", "16px")

create_navbar("Data Dashboard", [{"url": "#charts", "text": "Charts"}, {"url": "#stats", "text": "Statistics"}], "nav")

create_container("", "dashboard", True)

add_title("Sales Dashboard", 1)
add_text("Visualize your data with beautiful charts")

add_spacer("40px")

add_title("Monthly Sales", 2)
create_bar_chart([450, 380, 520, 490, 610, 580], ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "Sales by Month", "sales-chart")

add_spacer("40px")

add_title("Market Share", 2)
create_pie_chart([35, 25, 20, 15, 5], ["Product A", "Product B", "Product C", "Product D", "Others"], ["#667eea", "#764ba2", "#f093fb", "#4facfe", "#fa709a"], "market-pie")

add_spacer("40px")

add_title("Performance Metrics", 2)
create_row("", "metrics")
create_card("Revenue", "$125,000", "metric-card")
create_card("Customers", "1,234", "metric-card")
create_card("Growth", "+25%", "metric-card")
create_card("Satisfaction", "98%", "metric-card")
end_flex_container()

add_spacer("40px")

add_title("Progress Tracking", 2)
add_text("Q1 Goals:")
add_progress_bar(75, 100, "goal-1")
add_br(1)
add_text("Q2 Goals:")
add_progress_bar(60, 100, "goal-2")
add_br(1)
add_text("Q3 Goals:")
add_progress_bar(40, 100, "goal-3")

add_custom_css(".metrics { gap: 20px; justify-content: center; flex-wrap: wrap; }")
add_custom_css(".metric-card { min-width: 200px; }")
