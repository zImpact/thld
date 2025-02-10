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
            action [Stop("sound_loop"), Hide("thld_main_menu", Dissolve(2.0)), SetVariable("thld_lock_quit_game_main_menu_var", False), Start("thld_1")]

        imagebutton:
            auto "thld_load_button_%s"
            xalign 0.5 
            yalign 0.475
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [Stop("sound_loop"), SetVariable("thld_main_menu_var", False), ShowMenu("thld_load_main_menu")]

        imagebutton:
            auto "thld_extra_button_%s"
            xalign 0.5 
            yalign 0.6
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [Stop("sound_loop"), SetVariable("thld_main_menu_var", False), ShowMenu("thld_extra")]

        imagebutton:
            auto "thld_preferences_button_%s"
            xalign 0.5
            yalign 0.725
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [Stop("sound_loop"), SetVariable("thld_main_menu_var", False), ShowMenu("thld_preferences_main_menu")]

        imagebutton:
            auto "thld_exit_button_%s"
            xalign 0.5 
            yalign 0.85
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [Stop("sound_loop"), SetVariable("thld_main_menu_var", False), ShowMenu("thld_quit_main_menu")]

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
            action [Stop("sound_loop"), SetVariable("thld_main_menu_var", True), Hide("thld_load_main_menu"), ShowMenu("thld_main_menu")]

        if selected_slot != "_" and FileLoadable(selected_slot):
            imagebutton:
                auto "thld_load_button_%s_"
                xalign 0.5
                ypos 970
                hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
                unhovered Stop("sound_loop")
                action [Stop("sound_loop"), ThldFunctionCallback(thld_on_load_callback, selected_slot), FileLoad(selected_slot, confirm=False)]
                        
            imagebutton:
                auto "thld_delete_button_%s"
                xalign 0.9
                ypos 970
                hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
                unhovered Stop("sound_loop")
                action [Stop("sound_loop"), FileDelete(selected_slot, confirm=False)]

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
                            text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" " + "Пусто") + "\n" + FileSaveName(i)):
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
            action [Stop("sound_loop"), Hide("thld_extra"), ShowMenu("thld_music_room")]

        imagebutton:
            auto "thld_gallery_button_%s"
            xalign 0.5
            yalign 0.5
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [Stop("sound_loop"), Hide("thld_extra"), ShowMenu("thld_backround_gallery")]

        imagebutton:
            auto "thld_return_button_%s"
            xalign 0.1
            ypos 970
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [Stop("sound_loop"), SetVariable("thld_main_menu_var", True), Hide("thld_extra"), ShowMenu("thld_main_menu")]

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
            
        text ["Громкость музыки"]:
            font thld_main_menu_font
            size 60
            xpos 380
            ypos 820

        bar:
            value Preference("music volume")
            right_bar "thld_main_menu_bar_full"
            left_bar "thld_main_menu_bar_null_glitched"
            thumb "thld_main_menu_thumb"
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
            action [Stop("sound_loop"), SetVariable("thld_main_menu_var", True), Hide("thld_preferences_main_menu"), ShowMenu("thld_main_menu")]

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
            action [Stop("sound_loop"), Hide("thld_quit_main_menu"), Function(thld_screens_diact), ShowMenu("main_menu")]

        imagebutton:
            auto "thld_no_button_%s"
            xpos 1230
            ypos 600
            hovered Play("sound_loop", thld_glitch, relative_volume=0.1)
            unhovered Stop("sound_loop")
            action [Stop("sound_loop"), SetVariable("thld_main_menu_var", True), Hide("thld_quit_main_menu"), ShowMenu("thld_main_menu")]
        
screen thld_preferences():
    tag menu
    modal True
    
    $ thld_bar_null = Frame((thld_gui_path + "preferences/" + persistent.timeofday + "/thld_bar_null.png"), 36, 36)
    $ thld_bar_full = Frame((thld_gui_path + "preferences/" + persistent.timeofday + "/thld_bar_full.png"), 36, 36)

    window background thld_gui_path + "preferences/" + persistent.timeofday + "/preferences_bg.jpg":
        text ["Настройки"]: 
            style "thld_settings_link"
            xalign 0.5 
            yalign 0.08 
            color "#ffffff"

        textbutton "Назад": 
            style "thld_log_button" 
            text_style "thld_settings_link" 
            xalign 0.015 
            yalign 0.92 
            action Return()

        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport id "preferences":
                mousewheel True
                scrollbars None

                has grid 1 16 xfill True spacing 15

                text ["Режим экрана"]:
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.fullscreen:
                            add thld_gui_path + "preferences/" + persistent.timeofday + "/thld_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Во весь экран"]: 
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action Preference("display", "fullscreen")

                    hbox xalign 0.5:
                        if not _preferences.fullscreen:
                            add thld_gui_path + "preferences/" + persistent.timeofday + "/thld_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["В окне"]: 
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action Preference("display", "window")

                text ["Пропускать"]:
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.skip_unseen:
                            add thld_gui_path + "preferences/" + persistent.timeofday + "/thld_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Всё"]: 
                            style "thld_log_button" 
                            text_style "thld_settings_text_" + persistent.timeofday
                            action Preference("skip", "all")

                    hbox xalign 0.5:
                        if not _preferences.skip_unseen:
                            add thld_gui_path + "preferences/" + persistent.timeofday + "/thld_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Виденное ранее"]: 
                            style "thld_log_button" 
                            text_style "thld_settings_text_" + persistent.timeofday
                            action Preference("skip", "seen")

                text ["Громкость"]:
                    style "thld_settings_header_" + persistent.timeofday                   
                    xalign 0.5

                grid 2 1 xfill True:
                    textbutton ["Музыка"]: 
                        style "thld_log_button"
                        text_style "thld_settings_text_" + persistent.timeofday
                        action NullAction()
                        xpos 0.1

                    bar:
                        value Preference("music volume")
                        left_bar thld_bar_full 
                        right_bar thld_bar_null 
                        thumb thld_gui_path + "preferences/" + persistent.timeofday + "/thld_htumb.png" 
                        hover_thumb thld_gui_path + "preferences/" + persistent.timeofday + "/thld_htumb.png" 
                        xmaximum 1.35 
                        ymaximum 36 
                        xpos -0.55

                grid 2 1 xfill True:
                    textbutton ["Звуки"]: 
                        style "thld_log_button"
                        text_style "thld_settings_text_" + persistent.timeofday
                        action NullAction()
                        xpos 0.1

                    bar: 
                        value Preference("sound volume") 
                        left_bar thld_bar_full 
                        right_bar thld_bar_null 
                        thumb thld_gui_path + "preferences/" + persistent.timeofday + "/thld_htumb.png" 
                        hover_thumb thld_gui_path + "preferences/" + persistent.timeofday + "/thld_htumb.png" 
                        xmaximum 1.35 
                        ymaximum 36
                        xpos -0.55

                grid 2 1 xfill True:
                    textbutton ["Эмбиент"]: 
                        style "thld_log_button"
                        text_style "thld_settings_text_" + persistent.timeofday
                        action NullAction()
                        xpos 0.1

                    bar: 
                        value Preference("voice volume") 
                        left_bar thld_bar_full 
                        right_bar thld_bar_null 
                        thumb thld_gui_path + "preferences/" + persistent.timeofday + "/thld_htumb.png" 
                        hover_thumb thld_gui_path + "preferences/" + persistent.timeofday + "/thld_htumb.png" 
                        xmaximum 1.35 
                        ymaximum 36 
                        xpos -0.55

                text ["Скорость текста"]:
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                bar: 
                    value Preference("text speed") 
                    left_bar thld_bar_full 
                    right_bar thld_bar_null 
                    thumb thld_gui_path + "preferences/" + persistent.timeofday + "/thld_htumb.png" 
                    hover_thumb thld_gui_path + "preferences/" + persistent.timeofday + "/thld_htumb.png" 
                    xalign 0.5 
                    xmaximum 0.8 
                    ymaximum 36

                text ["Автопереход"]:
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.afm_time != 0:
                            add thld_gui_path + "preferences/" + persistent.timeofday + "/thld_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Включить"]: 
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action Preference("auto-forward after click", "enable")

                    hbox xalign 0.5:
                        if _preferences.afm_time == 0:
                            add thld_gui_path + "preferences/" + persistent.timeofday + "/thld_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Выключить"]: 
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

                text ["Время автоперехода"]:
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                bar: 
                    value Preference("auto-forward time") 
                    left_bar thld_bar_full 
                    right_bar thld_bar_null 
                    thumb thld_gui_path + "preferences/" + persistent.timeofday + "/thld_htumb.png" 
                    hover_thumb thld_gui_path + "preferences/" + persistent.timeofday + "/thld_htumb.png" 
                    xalign 0.5 
                    xmaximum 0.8 
                    ymaximum 36

                text ["Размер шрифта"]:
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.font_size == "small":
                            add thld_gui_path + "preferences/" + persistent.timeofday + "/thld_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Обычный"]:
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action SetField(persistent, "font_size", "small")

                    hbox xalign 0.5:
                        if not persistent.font_size == "small":
                            add thld_gui_path + "preferences/" + persistent.timeofday + "/thld_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton ["Крупный"]: 
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action SetField(persistent, "font_size", "large")

            bar: 
                value XScrollValue("preferences") 
                left_bar "images/misc/none.png" 
                right_bar "images/misc/none.png" 
                thumb "images/misc/none.png" 
                hover_thumb "images/misc/none.png"

            vbar: 
                value YScrollValue("preferences") 
                bottom_bar "images/misc/none.png" 
                top_bar "images/misc/none.png" 
                thumb thld_gui_path + "preferences/" + persistent.timeofday + "/thld_vthumb.png" 
                thumb_offset -12

screen thld_save():
    tag menu
    modal True
    
    window background thld_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png":
        text ["Сохранение"]: 
            style "thld_settings_link" 
            xalign 0.5 
            yalign 0.08 
            color "#ffffff"

        textbutton ["Назад"]: 
            style "thld_log_button" 
            text_style "thld_settings_link" 
            xalign 0.015 
            yalign 0.92 
            action Return()

        textbutton ["Сохранить"]: 
            style "thld_log_button" 
            text_style "thld_settings_link"
            yalign 0.92 
            xalign 0.5 
            action (ThldFunctionCallback(thld_on_save_callback, selected_slot), FileSave(selected_slot))

        textbutton ["Удалить"]: 
            style "thld_log_button" 
            text_style "thld_settings_link" 
            yalign 0.92 
            xalign 0.97 
            action FileDelete(selected_slot)

        grid 4 3 xpos 0.108 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True

            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i) xpos 10 ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "thld_save_load_button_" + persistent.timeofday
                        has fixed
                        text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" " + "Пусто") + "\n" + FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15
    
screen thld_load():
    tag menu
    modal True
    
    window background thld_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png":
        text ["Загрузка"]: 
            style "thld_settings_link" 
            xalign 0.5 
            yalign 0.08 
            color "#ffffff"

        textbutton ["Назад"]: 
            style "thld_log_button" 
            text_style "thld_settings_link" 
            xalign 0.015 
            yalign 0.92 
            action Return()

        textbutton ["Загрузить"]: 
            style "thld_log_button" 
            text_style "thld_settings_link" 
            yalign 0.92 
            xalign 0.5
            action (ThldFunctionCallback(thld_on_load_callback, selected_slot), FileLoad(selected_slot, confirm=False))
            
        textbutton ["Удалить"]: 
            style "thld_log_button" 
            text_style "thld_settings_link"
            yalign 0.92
            xalign 0.97 
            action FileDelete(selected_slot)

        grid 4 3 xpos 0.108 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True

            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i) xpos 10 ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "thld_save_load_button_" + persistent.timeofday
                        has fixed
                        text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" " + "Пусто") + "\n" +FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15                  
                                
screen thld_say(what, who):    
    window background None id "window":
        if persistent.font_size == "large":
            add thld_gui_path + "dialogue_box/" + persistent.timeofday + "/dialogue_box_large.png" xpos 174 ypos 866

            imagebutton:
                auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/hide_%s.png" 
                xpos 1508 
                ypos 883 
                action HideInterface()

            imagebutton:
                auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/save_%s.png"
                xpos 1567
                ypos 883
                action ShowMenu("thld_save")

            imagebutton:
                auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/menu_%s.png"
                xpos 1625 
                ypos 883 
                action ShowMenu("thld_game_menu_selector")

            imagebutton:
                auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/load_%s.png"
                xpos 1682 
                ypos 883 
                action ShowMenu("thld_load")

            imagebutton:
                auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_%s.png" 
                xpos 38 
                ypos 924 
                action ShowMenu("thld_text_history")

            if not config.skipping:
                imagebutton:
                    auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_%s.png"
                    xpos 1768 
                    ypos 924 
                    action Skip()

            else:
                imagebutton: 
                    auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_%s.png"
                    xpos 1768 
                    ypos 924 
                    action Skip()

            text what:
                id "what" 
                xpos 194 
                ypos 914 
                xmaximum 1541 
                size 30
                line_spacing 1

            if who:
                text who:
                    id "who" 
                    xpos 194 
                    ypos 877 
                    size 35 
                    line_spacing 1

        elif persistent.font_size == "small":
            add thld_gui_path + "dialogue_box/" + persistent.timeofday + "/dialogue_box.png" xpos 174 ypos 916

            imagebutton:
                auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/hide_%s.png"
                xpos 1508
                ypos 933
                action HideInterface()

            imagebutton:
                auto thld_gui_path + "dialogue_box/" + persistent.timeofday+"/save_%s.png"
                xpos 1567
                ypos 933
                action ShowMenu("thld_save")

            imagebutton:
                auto thld_gui_path + "dialogue_box/" + persistent.timeofday+"/menu_%s.png"
                xpos 1625
                ypos 933
                action ShowMenu("thld_game_menu_selector")

            imagebutton:
                auto thld_gui_path + "dialogue_box/" + persistent.timeofday+"/load_%s.png"
                xpos 1682
                ypos 933
                action ShowMenu("thld_load")

            imagebutton:
                auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_%s.png" 
                xpos 38 
                ypos 949 
                action ShowMenu("thld_text_history")

            if not config.skipping:
                imagebutton:
                    auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_%s.png"
                    xpos 1768 
                    ypos 949 
                    action Skip()

            else:
                imagebutton:
                    auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_%s.png"
                    xpos 1768 
                    ypos 949 
                    action Skip()

            text what:
                id "what" 
                xpos 194 
                ypos 964 
                xmaximum 1541 
                size 25
                line_spacing 2

            if who:
                text who:
                    id "who" 
                    xpos 194 
                    ypos 931 
                    size 28 
                    line_spacing 2

screen thld_nvl(items, dialogue):
    window background Frame((thld_gui_path + "choice/" + persistent.timeofday + "/choice_box.png"), 50, 50) xfill True yfill True yalign 0.5 left_padding 175 right_padding 175 bottom_padding 150 top_padding 150:
        has vbox

        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10

                if persistent.font_size == "large":
                    if who is not None:
                        text who: 
                            id who_id 
                            size 35

                    text what:
                        id what_id 
                        size 35

                elif persistent.font_size == "small":
                    if who is not None:
                        text who: 
                            id who_id 
                            size 28

                    text what:
                        id what_id 
                        size 28

        if items:
            vbox:
                id "menu"

                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"

                    else:
                        text caption style "nvl_dialogue"

    imagebutton:
        auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_%s.png"
        xpos 38 
        ypos 924
        action ShowMenu("thld_text_history")

    if not config.skipping:
        imagebutton:
            auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_%s.png"
            xpos 1768
            ypos 949
            action Skip()

    else:
        imagebutton:
            auto thld_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_%s.png"
            xpos 1768
            ypos 949
            action Skip()

screen thld_game_menu_selector():
    tag menu
    modal True

    if thld_lock_quick_menu:
        timer 0.01 action Return()

    else:
        button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

        add thld_gui_path + "quick_menu/" + persistent.timeofday + "/quick_menu_ground.png" xalign 0.5 yalign 0.5

        imagemap:
            auto thld_gui_path + "quick_menu/" + persistent.timeofday + "/quick_menu_%s.png" xalign 0.5 yalign 0.5

            hotspot (0, 83, 660, 65) focus_mask None clicked [Function(thld_set_dynamic_cursor, "main_menu"), MainMenu(confirm=False)]

            hotspot (0, 148, 660, 65) focus_mask None clicked ShowMenu("thld_save")

            hotspot (0, 213, 660, 65) focus_mask None clicked ShowMenu("thld_load")

            hotspot (0, 278, 660, 65) focus_mask None clicked ShowMenu("thld_preferences")

            hotspot (0, 343, 660, 65) focus_mask None action [(Function(thld_screens_diact)), ShowMenu("main_menu")]

screen thld_quit():
    tag menu
    modal True

    if thld_lock_quit:
        timer 0.01 action Return()

    elif thld_lock_quit_game_main_menu_var:
        timer 0.01 action Quit(confirm=False)

    else:
        add thld_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png"
            
        text ["Вы действительно \nхотите выйти?"]:
            font thld_link_font
            size 100
            text_align 0.5
            xalign 0.5
            yalign 0.33
            antialias True
            kerning 2
            
        textbutton ["Да"]:
            style "thld_settings_header_quit"
            text_style "thld_settings_header_quit"
            xpos 493
            ypos 600
            action [(Function(thld_screens_diact)), ShowMenu("main_menu")]
            
        textbutton ["Нет"]:
            style "thld_settings_header_quit"
            text_style "thld_settings_header_quit"
            xpos 1230
            ypos 600
            action [Hide("thld_quit"), Return()]

screen thld_yesno_prompt(yes_action, message, no_action):
    modal True

    add thld_gui_path + "yes_no/" + persistent.timeofday + "/yes_no.png"

    text _(message):
        font thld_header_font
        text_align 0.5 
        yalign 0.46 
        xalign 0.5

        if persistent.timeofday == "day":
            color "#64483c"

        elif persistent.timeofday == "night":
            color "#161d3d"

        elif persistent.timeofday == "prologue":
            color "#008193"

        elif persistent.timeofday == "sunset":
            color "#5a3525"

        size 30

    textbutton ["Да"]: 
        text_size 60 
        style "thld_log_button" 
        text_style "thld_settings_link" 
        yalign 0.65 
        xalign 0.3 
        action yes_action

    textbutton ["Нет"]: 
        text_size 60 
        style "thld_log_button" 
        text_style "thld_settings_link" 
        yalign 0.65 
        xalign 0.7 
        action no_action

screen thld_text_history():
    tag menu

    predict False

    $ xmax = 1600
    $ xposition = 100

    $ history_text_size = 21
    $ history_name_size = 22

    if persistent.font_size == "small":
        $ history_text_size = 28
        $ history_name_size = 29

    elif persistent.font_size == "large":
        $ history_text_size = 36
        $ history_name_size = 37

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    window background Frame(thld_gui_path + "choice/" + persistent.timeofday + "/choice_box.png") left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:
        viewport id "thld_text_history_screen":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0

            has vbox

            for h in _history_list:
                if h.who:
                    text h.who:
                        ypos 0
                        xpos xposition
                        xalign 0.0
                        size history_name_size
                        
                        if "color" in h.who_args:
                            color h.who_args["color"]

                textbutton h.what:
                    text_size history_text_size
                    style "thld_log_button" 
                    text_style "thld_text_history" 
                    xpos 100                    
                    xmaximum xmax

                    if persistent.timeofday == "day":
                        text_hover_color "#40e138"

                    elif persistent.timeofday == "night":
                        text_hover_color "#008193"

                    elif persistent.timeofday == "prologue":
                        text_hover_color "#00c6ff"

                    elif persistent.timeofday == "sunset":
                        text_hover_color "#636840"
                    
                    action RollbackToIdentifier(h.rollback_identifier) 
        
        vbar value YScrollValue("thld_text_history_screen") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb thld_gui_path + "preferences/" + persistent.timeofday + "/thld_vthumb.png" xoffset 1700  

screen thld_choice(items):
    modal True
    
    python:
        thld_choice_colors = {
        "day": "#466123",
        "night": "#145644",
        "sunset": "#69652f",
        "prologue": "#496463"
                            }

        thld_choice_colors_hover = {                        
        "day": "#9dcd55",
        "night": "#3ccfa2",
        "sunset": "#dcd168",
        "prologue": "#98d8da"
                            }

        thld_choice_colors_selected = {                        
        "day": "#2a3b15",
        "night": "#0b3027",
        "sunset": "#42401e",
        "prologue": "#2d3d3d"
                            }

    window background Frame(("thld/images/gui/choice/" + persistent.timeofday + "/choice_box.png"), 50, 50) xfill True yalign 0.5 left_padding 75 right_padding 75 bottom_padding 50 top_padding 50:
        has vbox xalign 0.5

        for caption, action, chosen in items:
            if action and caption:
                button background None:
                    xalign 0.5
                    action action

                    if persistent.licensed:
                        if caption in persistent.choices and caption != "Налево" and caption != "Направо" and caption != "Go left" and caption != "Go right" and caption != "Ir a la izquierda" and caption != "Ir a la derecha":
                            text caption font header_font size 37 hover_size 37 color thld_choice_colors_selected[persistent.timeofday] hover_color thld_choice_colors_hover[persistent.timeofday] xcenter 0.5 text_align 0.5
                            
                        else:
                            text caption font header_font size 37 hover_size 37 color thld_choice_colors[persistent.timeofday] hover_color thld_choice_colors_hover[persistent.timeofday] xcenter 0.5 text_align 0.5

                    else:
                        text caption font header_font size 37 hover_size 37 color thld_choice_colors[persistent.timeofday] hover_color thld_choice_colors_hover[persistent.timeofday] xalign 0.5

            else:
                if persistent.licensed:
                    text caption font header_font size 60 color thld_choice_colors[persistent.timeofday] text_align 0.5 xcenter 0.5

                else:
                    text caption font header_font size 40 color thld_choice_colors[persistent.timeofday] xalign 0.5 text_align 0.5 xcenter 0.5

screen thld_help():
    tag menu
    modal True
    
    add thld_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png"
    
    text ["Информация"]:
        font thld_link_font
        size 70
        xalign 0.5
        ypos 33
        antialias True
        kerning 2
            
    textbutton ["Группа VK"]:
        style "thld_log_button" 
        text_style "thld_settings_header_quit"
        xalign 0.5
        ypos 350
        action OpenURL("https://vk.com/public176281709")

    textbutton ["Под холодным небом"]:
        style "thld_log_button" 
        text_style "thld_settings_header_quit"
        xalign 0.5
        ypos 500
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2262867309")

    textbutton ["Сон"]:
        style "thld_log_button" 
        text_style "thld_settings_header_quit"
        xalign 0.5
        ypos 650
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2663197411")

    add "thld_logowhite_hover" xpos 1520 ypos 890

    textbutton "Назад": 
        style "thld_log_button" 
        text_style "thld_settings_link" 
        xalign 0.015 
        yalign 0.92 
        action Return()