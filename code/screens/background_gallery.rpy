init python:
    thld_gallery = Gallery()
    thld_gallery_page = 0
    thld_gallery.transition = fade
    thld_gallery.locked_button = THLD_GUI_PATH + "save_load/main_menu/thumbnail_idle.png"
    thld_gallery.navigation = False

    thld_rows = 4
    thld_cols = 3
    thld_cells  = thld_rows * thld_cols

    def thld_gallery_page_counter(n, k):
        l = float(n) / float(k)

        if l - int(l) > 0:
            return int(l) + 1

        else:
            return l

    thld_gallery_bg_list = [
        "thld_int_catacombs_living_celling",
        "thld_ext_tribune_night",
        "thld_ext_tribune_day",
        "thld_ext_hill_day",
        "thld_ext_railway_day",
        "thld_ext_railway_day_train",
        "thld_int_dining_hall_damaged",
        "thld_ext_houses_night",
        "thld_ext_playground_night_battle",
    ]

    for bg in thld_gallery_bg_list:
        thld_gallery.button(bg)
        thld_gallery.image("bg " + bg)
        thld_gallery.unlock("bg " + bg)

screen thld_background_gallery():
    modal True

    if not thld_main_menu_var:
        add "thld_main_menu_options_frame" xalign 0.5 yalign 0.5

        $ thld_gallery_table = thld_gallery_bg_list

        $ thld_len_table = len(thld_gallery_table)

        text "Галерея":
            font thld_main_menu_font
            size 90
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        imagebutton:
            auto "thld_return_button_%s"
            xalign 0.1
            ypos 970
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [
                Stop("sound_loop"),
                Hide("thld_background_gallery"),
                ShowMenu("thld_extra")
            ]

        grid thld_rows thld_cols xpos 0.1 ypos 0.18:
            $ thld_bg_displayed = 0
            $ thld_next_page = thld_gallery_page + 1

            if thld_next_page > int(thld_len_table / thld_cells):
                $ thld_next_page = 0

            for n in range(thld_len_table):
                if n < (thld_gallery_page + 1) * thld_cells and n >= thld_gallery_page * thld_cells:
                    $ _thld_t = im.Crop(
                        "thld/images/bg/" + thld_gallery_table[n][len(thld_prefix):] + ".png",
                        (0, 0, 1920, 1080)
                    )

                    $ _thld_img_scaled = im.Scale(_thld_t, 320, 180)

                    $ thld_img = im.Composite(
                        (336, 196),
                        (8, 8),
                        im.Alpha(_thld_img_scaled, 0.9),
                        (0, 0),
                        im.Image(THLD_GUI_PATH + "save_load/main_menu/thumbnail_idle.png")
                    )

                    $ thld_imgh = im.Composite(
                        (336, 196),
                        (8, 8),
                        _thld_img_scaled,
                        (0, 0),
                        im.Image(THLD_GUI_PATH + "save_load/main_menu/thumbnail_hover.png")
                    )

                    add thld_gallery.make_button(
                        thld_gallery_table[n],
                        get_image("gui/gallery/blank.png"),
                        None,
                        thld_imgh,
                        thld_img,
                        style="blank_button",
                        bottom_margin=50,
                        right_margin=50
                    )

                    $ thld_bg_displayed += 1

                    if n + 1 == thld_len_table:
                        $ thld_next_page = 0

            for j in range(0, thld_cells - thld_bg_displayed):
                null

        if thld_gallery_page != 0:
            imagebutton:
                auto THLD_GUI_PATH + "misc/gallery_previous_%s.png"
                yalign 0.5
                xalign 0.04
                action [
                    SetVariable("thld_gallery_page", thld_gallery_page - 1),
                    ShowMenu("thld_background_gallery")
                ]

        if thld_gallery_page != int(thld_gallery_page_counter(thld_len_table, thld_cells)) - 1:
            imagebutton:
                auto THLD_GUI_PATH + "misc/gallery_next_%s.png"
                yalign 0.5
                xalign 0.96
                action [
                    SetVariable("thld_gallery_page", thld_next_page),
                    ShowMenu("thld_background_gallery")
                ]
