screen thld_main_menu():
    tag menu
    modal True

    key "game_menu":
        action NullAction()

    key "K_F1":
        action NullAction()

    add "thld_main_menu_background"

    add "thld_main_menu_particles" at thld_main_menu_particles_anim

    if thld_main_menu_var:
        add "thld_main_menu_logo" xalign 0.5 yalign 0.1

        imagebutton:
            auto "thld_start_button_%s"
            xalign 0.5
            yalign 0.35
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [
                Stop("sound_loop"),
                Hide("thld_main_menu", Dissolve(2.0)),
                SetVariable("thld_lock_quit_game_main_menu_var", False),
                Start("thld_scenario")
            ]

        imagebutton:
            auto "thld_load_button_%s"
            xalign 0.5
            yalign 0.475
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [
                Stop("sound_loop"),
                SetVariable("thld_main_menu_var", False),
                ShowMenu("thld_load_main_menu")
            ]

        imagebutton:
            auto "thld_extra_button_%s"
            xalign 0.5
            yalign 0.6
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [
                Stop("sound_loop"),
                SetVariable("thld_main_menu_var", False),
                ShowMenu("thld_extra")
            ]

        imagebutton:
            auto "thld_preferences_button_%s"
            xalign 0.5
            yalign 0.725
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [
                Stop("sound_loop"),
                SetVariable("thld_main_menu_var", False),
                ShowMenu("thld_preferences_main_menu")
            ]

        imagebutton:
            auto "thld_exit_button_%s"
            xalign 0.5
            yalign 0.85
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [
                Stop("sound_loop"),
                SetVariable("thld_main_menu_var", False),
                ShowMenu("thld_quit_main_menu")
            ]

        imagebutton:
            auto "thld_logowhite_%s"
            xpos 1520
            ypos 800
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action OpenURL("https://vk.com/public176281709")

screen thld_load_main_menu():
    modal True

    key "K_F1":
        action NullAction()

    if not thld_main_menu_var:
        add "thld_main_menu_options_frame" xalign 0.5 yalign 0.5

        text "Загрузка":
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
                SetVariable("thld_main_menu_var", True),
                Hide("thld_load_main_menu"),
                ShowMenu("thld_main_menu")
            ]

        if selected_slot != "_" and FileLoadable(selected_slot):
            imagebutton:
                auto "thld_load_button_%s_"
                xalign 0.5
                ypos 970
                hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
                unhovered Stop("sound_loop")
                action [
                    Stop("sound_loop"),
                    ThldFunctionCallback(thld_on_load_callback, selected_slot),
                    FileLoad(selected_slot, confirm=False)
                ]

            imagebutton:
                auto "thld_delete_button_%s"
                xalign 0.9
                ypos 970
                hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
                unhovered Stop("sound_loop")
                action [
                    Stop("sound_loop"),
                    FileDelete(selected_slot, confirm=False)
                ]

        else:
            text "Загрузить игру":
                font thld_main_menu_font
                color "#d1d1d1"
                size 60
                xalign 0.5
                ypos 970

            text "Удалить":
                font thld_main_menu_font
                color "#d1d1d1"
                size 60
                xalign 0.9
                ypos 970

        grid 4 3:
            xpos 0.11
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True

            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "thld_save_load_button_main_menu"

                        fixed:
                            text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" Пусто") + "\n" + FileSaveName(i)):
                                style "thld_text_save_load_main_menu"
                                xpos 15
                                ypos 15

screen thld_extra():
    modal True

    key "K_F1":
        action NullAction()

    if not thld_main_menu_var:
        add "thld_main_menu_options_frame" xalign 0.5 yalign 0.5

        text "Дополнительно":
            font thld_main_menu_font
            size 90
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        imagebutton:
            auto "thld_music_button_%s"
            xalign 0.5
            yalign 0.3
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [
                Stop("sound_loop"),
                Hide("thld_extra"),
                ShowMenu("thld_music_room")
            ]

        imagebutton:
            auto "thld_gallery_button_%s"
            xalign 0.5
            yalign 0.5
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [
                Stop("sound_loop"),
                Hide("thld_extra"),
                ShowMenu("thld_background_gallery")
            ]

        imagebutton:
            auto "thld_return_button_%s"
            xalign 0.1
            ypos 970
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [
                Stop("sound_loop"),
                SetVariable("thld_main_menu_var", True),
                Hide("thld_extra"),
                ShowMenu("thld_main_menu")
            ]

screen thld_preferences_main_menu():
    modal True

    key "K_F1":
        action NullAction()

    if not thld_main_menu_var:
        add "thld_main_menu_options_frame" xalign 0.5 yalign 0.5

        text "Настройки":
            font thld_main_menu_font
            size 90
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        text "Режим экрана":
            font thld_main_menu_font
            size 60
            xalign 0.5
            ypos 200

        textbutton "Во весь экран":
            style "thld_button_none"
            text_style "thld_settings_header_main_menu_preferences"
            xalign 0.15
            ypos 280
            action Preference("display", "fullscreen")

        textbutton "В окне":
            style "thld_button_none"
            text_style "thld_settings_header_main_menu_preferences"
            xalign 0.85
            ypos 280

            if not _preferences.fullscreen:
                text_style "thld_settings_header_main_menu_preferences_inverse"

            else:
                text_style "thld_settings_header_main_menu_preferences"

            action Preference("display", "window")

        text "Размер шрифта":
            font thld_main_menu_font
            size 60
            xalign 0.5
            ypos 360

        textbutton "Обычный":
            style "thld_button_none"
            text_style "thld_settings_header_main_menu_preferences"
            xalign 0.15
            ypos 440
            action SetField(persistent, "font_size", "small")

        textbutton "Крупный":
            style "thld_button_none"
            text_style "thld_settings_header_main_menu_preferences"
            xalign 0.85
            ypos 440
            action SetField(persistent, "font_size", "large")

        text "Пропускать":
            font thld_main_menu_font
            size 60
            xalign 0.5
            ypos 520

        if not _preferences.skip_unseen:
            textbutton "Виденное ранее":
                style "thld_button_none"
                text_style "thld_settings_header_main_menu_preferences"
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "Всё":
                style "thld_button_none"
                text_style "thld_settings_header_main_menu_preferences"
                xalign 0.85
                ypos 600
                action Preference("skip", "all")

        if _preferences.skip_unseen:
            textbutton "Виденное ранее":
                style "thld_button_none"
                text_style "thld_settings_header_main_menu_preferences"
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "Всё":
                style "thld_button_none"
                text_style "thld_settings_header_main_menu_preferences"
                xalign 0.85
                ypos 600
                action Preference("skip", "all")

        text "Громкость музыки":
            font thld_main_menu_font
            size 60
            xpos 380
            ypos 820

        bar:
            value Preference("music volume")
            right_bar THLD_GUI_PATH + "preferences/main_menu/bar_full.png"
            left_bar "thld_main_menu_bar_null_glitched"
            thumb THLD_GUI_PATH + "misc/main_menu_thumb.png"
            xpos 960
            ypos 813
            xmaximum 400
            ymaximum 85

        imagebutton:
            auto "thld_return_button_%s"
            xalign 0.1
            ypos 970
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [
                Stop("sound_loop"),
                SetVariable("thld_main_menu_var", True),
                Hide("thld_preferences_main_menu"),
                ShowMenu("thld_main_menu")
            ]

screen thld_quit_main_menu():
    modal True

    key "K_F1":
        action NullAction()

    if not thld_main_menu_var:
        add "thld_main_menu_options_frame" xalign 0.5 yalign 0.5

        text "Вы действительно хотите выйти?":
            font thld_main_menu_font
            size 80
            text_align 0.5
            xalign 0.5
            yalign 0.33
            antialias True
            kerning 2

        imagebutton:
            auto "thld_yes_button_%s"
            xpos 493
            ypos 600
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [
                Stop("sound_loop"),
                Hide("thld_quit_main_menu"),
                Function(thld_screens_diact),
                ShowMenu("main_menu")
            ]

        imagebutton:
            auto "thld_no_button_%s"
            xpos 1230
            ypos 600
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [
                Stop("sound_loop"),
                SetVariable("thld_main_menu_var", True),
                Hide("thld_quit_main_menu"),
                ShowMenu("thld_main_menu")
            ]
