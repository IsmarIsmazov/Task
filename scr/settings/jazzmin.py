JAZZMIN_SETTINGS = {
    "site_title": "Task",
    "site_header": "Task",
    "site_brand": "Task",
    "welcome_sign": "Task",
    "copyright": "Task",
    "search_model": ["auth.User", "auth.Group"],

    "topmenu_links": [

        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        {"model": "auth.User"},

        {"app": "books"},
    ],
    "show_sidebar": True,

    "changeform_format": "horizontal_tabs",

}
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": True,
    "brand_small_text": True,
    "brand_colour": "navbar-success",
    "accent": "accent-teal",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-info",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": True,

    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "cyborg",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}
