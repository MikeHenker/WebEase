# Webease Library - UI Components
# This is a .wl library file with reusable components

component feature_card {
<div class="feature-card" style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; margin: 15px;">
    <h3 style="color: #667eea; margin-bottom: 15px;">{{title}}</h3>
    <p style="color: #666;">{{description}}</p>
</div>
}

component cta_button {
<button style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 15px 40px; border: none; border-radius: 30px; font-size: 18px; cursor: pointer; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4); transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
    {{text}}
</button>
}

component testimonial {
<div style="background: #f8f9fa; padding: 25px; border-radius: 8px; border-left: 4px solid #667eea; margin: 20px 0;">
    <p style="font-style: italic; margin-bottom: 15px;">"{{quote}}"</p>
    <p style="font-weight: bold; color: #667eea;">- {{author}}</p>
</div>
}

component stat_box {
<div style="text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border-radius: 12px; margin: 10px;">
    <h2 style="font-size: 48px; margin-bottom: 10px;">{{number}}</h2>
    <p style="font-size: 18px;">{{label}}</p>
</div>
}
