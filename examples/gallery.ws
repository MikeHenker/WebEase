# Image Gallery Example

set_title("Photo Gallery")
set_background("#f8f9fa")
add_google_font("Raleway")
set_font("Raleway, sans-serif", "16px")

create_hero_section("My Photo Gallery", "Beautiful memories captured in time", "")

create_container("", "main", True)

add_title("Grid Gallery", 2)
create_image_gallery(["https://picsum.photos/400/300?random=1", "https://picsum.photos/400/300?random=2", "https://picsum.photos/400/300?random=3", "https://picsum.photos/400/300?random=4", "https://picsum.photos/400/300?random=5", "https://picsum.photos/400/300?random=6"], 3, "15px", "photo-gallery")

add_lightbox(".photo-gallery img")

add_spacer("40px")

add_title("Image Slider", 2)
create_image_slider(["https://picsum.photos/800/400?random=10", "https://picsum.photos/800/400?random=11", "https://picsum.photos/800/400?random=12"], True, 3000, "main-slider")

add_spacer("40px")

add_title("Masonry Layout", 2)
create_masonry_gallery(["https://picsum.photos/400/500?random=20", "https://picsum.photos/400/300?random=21", "https://picsum.photos/400/400?random=22", "https://picsum.photos/400/600?random=23", "https://picsum.photos/400/350?random=24", "https://picsum.photos/400/450?random=25"], "masonry-gallery")

create_footer("Photo Gallery powered by Webease", "gallery-footer")
