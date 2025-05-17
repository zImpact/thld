init python:
    thld_link_font = THLD_GUI_PATH + "fonts/gothic.ttf"
    thld_header_font = THLD_GUI_PATH + "fonts/corbel.ttf"
    thld_main_font = "fonts/calibri.ttf"
    thld_main_menu_font = THLD_GUI_PATH + "fonts/gotham_pro_light.ttf"

    style.thld_button_none = Style(style.button)
    style.thld_button_none.background = None
    style.thld_button_none.hover_background = None
    style.thld_button_none.selected_background = None
    style.thld_button_none.selected_hover_background = None
    style.thld_button_none.selected_idle_background = None

    style.thld_text_style = Style(style.default)
    style.thld_text_style.color = "#e2c778"
    style.thld_text_style.drop_shadow = (2, 2)
    style.thld_text_style.drop_shadow_color = "#000"

    style.thld_titles_style = Style(style.default)
    style.thld_titles_style.font = thld_link_font
    style.thld_titles_style.color = "#fff"
    style.thld_titles_style.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    style.thld_titles_style.drop_shadow_color = "#000"
    style.thld_titles_style.italic = False
    style.thld_titles_style.bold = False
    style.thld_titles_style.text_align = 0.5
    style.thld_titles_style.xmaximum = 0.8

    style.thld_save_load_button_main_menu = Style(style.button)
    style.thld_save_load_button_main_menu.background = THLD_GUI_PATH + "save_load/main_menu/thumbnail_idle.png"
    style.thld_save_load_button_main_menu.hover_background = THLD_GUI_PATH + "save_load/main_menu/thumbnail_hover.png"
    style.thld_save_load_button_main_menu.selected_background = THLD_GUI_PATH + "save_load/main_menu/thumbnail_selected.png"
    style.thld_save_load_button_main_menu.selected_hover_background = THLD_GUI_PATH + "save_load/main_menu/thumbnail_selected.png"
    style.thld_save_load_button_main_menu.selected_idle_background = THLD_GUI_PATH + "save_load/main_menu/thumbnail_selected.png"

    style.thld_save_load_button_day = Style(style.button)
    style.thld_save_load_button_day.background = THLD_GUI_PATH + "save_load/day/thumbnail_idle.png"
    style.thld_save_load_button_day.hover_background = THLD_GUI_PATH + "save_load/day/thumbnail_hover.png"
    style.thld_save_load_button_day.selected_background = THLD_GUI_PATH + "save_load/day/thumbnail_selected.png"
    style.thld_save_load_button_day.selected_hover_background = THLD_GUI_PATH + "save_load/day/thumbnail_selected.png"
    style.thld_save_load_button_day.selected_idle_background = THLD_GUI_PATH + "save_load/day/thumbnail_selected.png"

    style.thld_save_load_button_night = Style(style.button)
    style.thld_save_load_button_night.background = THLD_GUI_PATH + "save_load/night/thumbnail_idle.png"
    style.thld_save_load_button_night.hover_background = THLD_GUI_PATH + "save_load/night/thumbnail_hover.png"
    style.thld_save_load_button_night.selected_background = THLD_GUI_PATH + "save_load/night/thumbnail_selected.png"
    style.thld_save_load_button_night.selected_hover_background = THLD_GUI_PATH + "save_load/night/thumbnail_selected.png"
    style.thld_save_load_button_night.selected_idle_background = THLD_GUI_PATH + "save_load/night/thumbnail_selected.png"

    style.thld_save_load_button_prologue = Style(style.button)
    style.thld_save_load_button_prologue.background = THLD_GUI_PATH + "save_load/prologue/thumbnail_idle.png"
    style.thld_save_load_button_prologue.hover_background = THLD_GUI_PATH + "save_load/prologue/thumbnail_hover.png"
    style.thld_save_load_button_prologue.selected_background = THLD_GUI_PATH + "save_load/prologue/thumbnail_selected.png"
    style.thld_save_load_button_prologue.selected_hover_background = THLD_GUI_PATH + "save_load/prologue/thumbnail_selected.png"
    style.thld_save_load_button_prologue.selected_idle_background = THLD_GUI_PATH + "save_load/prologue/thumbnail_selected.png"

    style.thld_save_load_button_sunset = Style(style.button)
    style.thld_save_load_button_sunset.background = THLD_GUI_PATH + "save_load/sunset/thumbnail_idle.png"
    style.thld_save_load_button_sunset.hover_background = THLD_GUI_PATH + "save_load/sunset/thumbnail_hover.png"
    style.thld_save_load_button_sunset.selected_background = THLD_GUI_PATH + "save_load/sunset/thumbnail_selected.png"
    style.thld_save_load_button_sunset.selected_hover_background = THLD_GUI_PATH + "save_load/sunset/thumbnail_selected.png"
    style.thld_save_load_button_sunset.selected_idle_background = THLD_GUI_PATH + "save_load/sunset/thumbnail_selected.png"

    style.thld_base_font = Style(style.default)
    style.thld_base_font.font = thld_main_font
    style.thld_base_font.size = 28
    style.thld_base_font.line_spacing = 2

    style.thld_qte_text = Style(style.thld_base_font)
    style.thld_qte_text.font = thld_header_font
    style.thld_qte_text.size = 60
    style.thld_qte_text.kerning = 3
    style.thld_qte_text.color = "#cfd1d1"
    style.thld_qte_text.hover_color = "#ffffff"
    style.thld_qte_text.selected_color = "#ffffff"
    style.thld_qte_text.selected_idle_color = "#ffffff"
    style.thld_qte_text.selected_hover_color = "#ffffff"
    style.thld_qte_text.insensitive_color = "#ffffff"

    style.thld_settings_link = Style(style.thld_base_font)
    style.thld_settings_link.font = thld_link_font
    style.thld_settings_link.size = 60
    style.thld_settings_link.kerning = 3
    style.thld_settings_link.color = "#909ca3"
    style.thld_settings_link.hover_color = "#ffffff"
    style.thld_settings_link.selected_color = "#909ca3"
    style.thld_settings_link.selected_idle_color = "#909ca3"
    style.thld_settings_link.selected_hover_color = "#ffffff"
    style.thld_settings_link.insensitive_color = "#909ca3"

    style.thld_settings_link_main_menu = Style(style.thld_base_font)
    style.thld_settings_link_main_menu.font = thld_link_font
    style.thld_settings_link_main_menu.size = 60
    style.thld_settings_link_main_menu.kerning = 3
    style.thld_settings_link_main_menu.color = "#ffffff"
    style.thld_settings_link_main_menu.hover_color = "#ffffff"
    style.thld_settings_link_main_menu.selected_color = "#ffffff"
    style.thld_settings_link_main_menu.selected_idle_color = "#ffffff"
    style.thld_settings_link_main_menu.selected_hover_color = "#ffffff"
    style.thld_settings_link_main_menu.insensitive_color = "#ffffff"

    style.thld_settings_link_main_menu_preferences = Style(style.thld_base_font)
    style.thld_settings_link_main_menu_preferences.font = thld_link_font
    style.thld_settings_link_main_menu_preferences.size = 60
    style.thld_settings_link_main_menu_preferences.kerning = 3
    style.thld_settings_link_main_menu_preferences.color = "#d1d1d1"
    style.thld_settings_link_main_menu_preferences.hover_color = "#ffffff"
    style.thld_settings_link_main_menu_preferences.selected_color = "#d1d1d1"
    style.thld_settings_link_main_menu_preferences.selected_idle_color = "#d1d1d1"
    style.thld_settings_link_main_menu_preferences.selected_hover_color = "#ffffff"
    style.thld_settings_link_main_menu_preferences.insensitive_color = "#d1d1d1"

    style.thld_settings_header_main_menu_preferences = Style(style.thld_base_font)
    style.thld_settings_header_main_menu_preferences.font = thld_main_menu_font
    style.thld_settings_header_main_menu_preferences.size = 60
    style.thld_settings_header_main_menu_preferences.color = "#d1d1d1"
    style.thld_settings_header_main_menu_preferences.hover_color = "#ffffff"
    style.thld_settings_header_main_menu_preferences.selected_color = "#ffffff"

    style.thld_settings_header_main_menu_preferences_locked = Style(style.thld_base_font)
    style.thld_settings_header_main_menu_preferences_locked.font = thld_main_menu_font
    style.thld_settings_header_main_menu_preferences_locked.size = 60
    style.thld_settings_header_main_menu_preferences_locked.color = "#C0C0C0"
    style.thld_settings_header_main_menu_preferences_locked.hover_color = "#C0C0C0"
    style.thld_settings_header_main_menu_preferences_locked.selected_color = "#C0C0C0"

    style.thld_settings_header_quit = Style(style.thld_base_font)
    style.thld_settings_header_quit.font = thld_header_font
    style.thld_settings_header_quit.size = 60
    style.thld_settings_header_quit.color = "#d1d1d1"
    style.thld_settings_header_quit.hover_color = "#ffffff"

    style.thld_settings_header_main_menu_preferences_inverse = Style(style.thld_base_font)
    style.thld_settings_header_main_menu_preferences_inverse.font = thld_main_menu_font
    style.thld_settings_header_main_menu_preferences_inverse.size = 60
    style.thld_settings_header_main_menu_preferences_inverse.color = "#ffffff"
    style.thld_settings_header_main_menu_preferences_inverse.hover_color = "#ffffff"
    style.thld_settings_header_main_menu_preferences_inverse.selected_color = "#ffffff"

    style.thld_settings_header_day = Style(style.thld_base_font)
    style.thld_settings_header_day.font = thld_header_font
    style.thld_settings_header_day.size = 50
    style.thld_settings_header_day.color = "#4d2e19"
    style.thld_settings_header_day.hover_color = "#a27146"

    style.thld_settings_header_night = Style(style.thld_base_font)
    style.thld_settings_header_night.font = thld_header_font
    style.thld_settings_header_night.size = 50
    style.thld_settings_header_night.color = "#161d3d"
    style.thld_settings_header_night.hover_color = "#008193"

    style.thld_settings_header_prologue = Style(style.thld_base_font)
    style.thld_settings_header_prologue.font = thld_header_font
    style.thld_settings_header_prologue.size = 50
    style.thld_settings_header_prologue.color = "#161d3d"
    style.thld_settings_header_prologue.hover_color = "#008193"

    style.thld_settings_header_sunset = Style(style.thld_base_font)
    style.thld_settings_header_sunset.font = thld_header_font
    style.thld_settings_header_sunset.size = 50
    style.thld_settings_header_sunset.color = "#5a3525"
    style.thld_settings_header_sunset.hover_color = "#636840"

    style.thld_settings_text_day = Style(style.thld_settings_header_day)
    style.thld_settings_text_day.size = 36
    style.thld_settings_text_day.selected_color = "#4d2e19"
    style.thld_settings_text_day.hover_color = "#a27146"

    style.thld_settings_text_night = Style(style.thld_settings_header_night)
    style.thld_settings_text_night.size = 36
    style.thld_settings_text_night.selected_color = "#161d3d"
    style.thld_settings_text_night.hover_color = "#008193"

    style.thld_settings_text_prologue = Style(style.thld_settings_header_prologue)
    style.thld_settings_text_prologue.size = 36
    style.thld_settings_text_prologue.selected_color = "#161d3d"
    style.thld_settings_text_prologue.hover_color = "#008193"

    style.thld_settings_text_sunset = Style(style.thld_settings_header_sunset)
    style.thld_settings_text_sunset.size = 36
    style.thld_settings_text_sunset.selected_color = "#5a3525"
    style.thld_settings_text_sunset.hover_color = "#636840"

    style.thld_text_history = Style(style.thld_base_font)
    style.thld_text_history.color = "#e2c778"
    style.thld_text_history.drop_shadow = (2, 2)
    style.thld_text_history.drop_shadow_color = "#000"
