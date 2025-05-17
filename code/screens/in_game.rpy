screen thld_preferences():
    tag menu
    modal True

    $ thld_bar_null = Frame((THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/bar_null.png"), 36, 36)
    $ thld_bar_full = Frame((THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/bar_full.png"), 36, 36)

    window:
        background THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/preferences_bg.jpg"

        text "Настройки":
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

                text "Режим экрана":
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.fullscreen:
                            add THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/leaf.png":
                                ypos 0.12

                        else:
                            null width 22

                        textbutton "Во весь экран":
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action Preference("display", "fullscreen")

                    hbox xalign 0.5:
                        if not _preferences.fullscreen:
                            add THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/leaf.png":
                                ypos 0.12

                        else:
                            null width 22

                        textbutton "В окне":
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action Preference("display", "window")

                text "Пропускать":
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.skip_unseen:
                            add THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/leaf.png":
                                ypos 0.12

                        else:
                            null width 22

                        textbutton "Всё":
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action Preference("skip", "all")

                    hbox xalign 0.5:
                        if not _preferences.skip_unseen:
                            add THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/leaf.png":
                                ypos 0.12

                        else:
                            null width 22

                        textbutton "Виденное ранее":
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action Preference("skip", "seen")

                text "Громкость":
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    textbutton "Музыка":
                        style "thld_log_button"
                        text_style "thld_settings_text_" + persistent.timeofday
                        action NullAction()
                        xpos 0.1

                    bar:
                        value Preference("music volume")
                        left_bar thld_bar_full
                        right_bar thld_bar_null
                        thumb THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/htumb.png"
                        hover_thumb THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/htumb.png"
                        xmaximum 1.35
                        ymaximum 36
                        xpos -0.55

                grid 2 1 xfill True:
                    textbutton "Звуки":
                        style "thld_log_button"
                        text_style "thld_settings_text_" + persistent.timeofday
                        action NullAction()
                        xpos 0.1

                    bar:
                        value Preference("sound volume")
                        left_bar thld_bar_full
                        right_bar thld_bar_null
                        thumb THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/htumb.png"
                        hover_thumb THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/htumb.png"
                        xmaximum 1.35
                        ymaximum 36
                        xpos -0.55

                grid 2 1 xfill True:
                    textbutton "Эмбиент":
                        style "thld_log_button"
                        text_style "thld_settings_text_" + persistent.timeofday
                        action NullAction()
                        xpos 0.1

                    bar:
                        value Preference("voice volume")
                        left_bar thld_bar_full
                        right_bar thld_bar_null
                        thumb THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/htumb.png"
                        hover_thumb THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/htumb.png"
                        xmaximum 1.35
                        ymaximum 36
                        xpos -0.55

                text "Скорость текста":
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                bar:
                    value Preference("text speed")
                    left_bar thld_bar_full
                    right_bar thld_bar_null
                    thumb THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/htumb.png"
                    hover_thumb THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/htumb.png"
                    xalign 0.5
                    xmaximum 0.8
                    ymaximum 36

                text "Автопереход":
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.afm_time != 0:
                            add THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/leaf.png":
                                ypos 0.12

                        else:
                            null width 22

                        textbutton "Включить":
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action Preference("auto-forward after click", "enable")

                    hbox xalign 0.5:
                        if _preferences.afm_time == 0:
                            add THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/leaf.png":
                                ypos 0.12

                        else:
                            null width 22

                        textbutton "Выключить":
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action [
                                Preference("auto-forward time", 0),
                                Preference("auto-forward after click", "disable")
                            ]

                text "Время автоперехода":
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                bar:
                    value Preference("auto-forward time")
                    left_bar thld_bar_full
                    right_bar thld_bar_null
                    thumb THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/htumb.png"
                    hover_thumb THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/htumb.png"
                    xalign 0.5
                    xmaximum 0.8
                    ymaximum 36

                text "Размер шрифта":
                    style "thld_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.font_size == "small":
                            add THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/leaf.png":
                                ypos 0.12

                        else:
                            null width 22

                        textbutton "Обычный":
                            style "thld_log_button"
                            text_style "thld_settings_text_" + persistent.timeofday
                            action SetField(persistent, "font_size", "small")

                    hbox xalign 0.5:
                        if not persistent.font_size == "small":
                            add THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/leaf.png":
                                ypos 0.12

                        else:
                            null width 22

                        textbutton "Крупный":
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
                thumb THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/vthumb.png"
                thumb_offset -12

screen thld_save():
    tag menu
    modal True

    window:
        background THLD_GUI_PATH + "save_load/" + persistent.timeofday + "/load_bg.png"

        text "Сохранение":
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

        textbutton "Сохранить":
            style "thld_log_button"
            text_style "thld_settings_link"
            yalign 0.92
            xalign 0.5
            action [
                ThldFunctionCallback(thld_on_save_callback, selected_slot),
                FileSave(selected_slot)
            ]

        textbutton "Удалить":
            style "thld_log_button"
            text_style "thld_settings_link"
            yalign 0.92
            xalign 0.97
            action FileDelete(selected_slot)

        grid 4 3:
            xpos 0.108
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
                        style "thld_save_load_button_" + persistent.timeofday
                        has fixed
                        text "%s." % i + FileTime(i, format=THLD_SAVE_LOAD_FORMAT, empty=THLD_SAVE_LOAD_EMPTY_LABEL) + "\n" + FileSaveName(i):
                            style "file_picker_text"
                            xpos 15
                            ypos 15

screen thld_load():
    tag menu
    modal True

    window:
        background THLD_GUI_PATH + "save_load/" + persistent.timeofday + "/load_bg.png"

        text "Загрузка":
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

        textbutton "Загрузить":
            style "thld_log_button"
            text_style "thld_settings_link"
            yalign 0.92
            xalign 0.5
            action [
                ThldFunctionCallback(thld_on_load_callback, selected_slot),
                FileLoad(selected_slot, confirm=False)
            ]

        textbutton "Удалить":
            style "thld_log_button"
            text_style "thld_settings_link"
            yalign 0.92
            xalign 0.97
            action FileDelete(selected_slot)

        grid 4 3:
            xpos 0.108
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
                        style "thld_save_load_button_" + persistent.timeofday
                        has fixed
                        text "%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" Пусто") + "\n" +FileSaveName(i):
                            style "file_picker_text"
                            xpos 15
                            ypos 15

screen thld_say(what, who):
    window:
        background None
        id "window"

        if persistent.font_size == "large":
            add THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/dialogue_box_large.png":
                xpos 174
                ypos 866

            imagebutton:
                auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/hide_%s.png"
                xpos 1508
                ypos 883
                action HideInterface()

            imagebutton:
                auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/save_%s.png"
                xpos 1567
                ypos 883
                action ShowMenu("thld_save")

            imagebutton:
                auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/menu_%s.png"
                xpos 1625
                ypos 883
                action ShowMenu("thld_game_menu_selector")

            imagebutton:
                auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/load_%s.png"
                xpos 1682
                ypos 883
                action ShowMenu("thld_load")

            imagebutton:
                auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/backward_%s.png"
                xpos 38
                ypos 924
                action ShowMenu("thld_text_history")

            if not config.skipping:
                imagebutton:
                    auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/forward_%s.png"
                    xpos 1768
                    ypos 924
                    action Skip()

            else:
                imagebutton:
                    auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/fast_forward_%s.png"
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
            add THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/dialogue_box.png":
                xpos 174
                ypos 916

            imagebutton:
                auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/hide_%s.png"
                xpos 1508
                ypos 933
                action HideInterface()

            imagebutton:
                auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday+"/save_%s.png"
                xpos 1567
                ypos 933
                action ShowMenu("thld_save")

            imagebutton:
                auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday+"/menu_%s.png"
                xpos 1625
                ypos 933
                action ShowMenu("thld_game_menu_selector")

            imagebutton:
                auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday+"/load_%s.png"
                xpos 1682
                ypos 933
                action ShowMenu("thld_load")

            imagebutton:
                auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/backward_%s.png"
                xpos 38
                ypos 949
                action ShowMenu("thld_text_history")

            if not config.skipping:
                imagebutton:
                    auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/forward_%s.png"
                    xpos 1768
                    ypos 949
                    action Skip()

            else:
                imagebutton:
                    auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/fast_forward_%s.png"
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
    window:
        background Frame((THLD_GUI_PATH + "choice/" + persistent.timeofday + "/choice_box.png"), 50, 50)
        xfill True
        yfill True
        yalign 0.5
        left_padding 175
        right_padding 175
        bottom_padding 150
        top_padding 150
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
                            text caption:
                                style "nvl_menu_choice"

                    else:
                        text caption:
                            style "nvl_dialogue"

    imagebutton:
        auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/backward_%s.png"
        xpos 38
        ypos 924
        action ShowMenu("thld_text_history")

    if not config.skipping:
        imagebutton:
            auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/forward_%s.png"
            xpos 1768
            ypos 949
            action Skip()

    else:
        imagebutton:
            auto THLD_GUI_PATH + "dialogue_box/" + persistent.timeofday + "/fast_forward_%s.png"
            xpos 1768
            ypos 949
            action Skip()

screen thld_game_menu_selector():
    tag menu
    modal True

    if thld_lock_quick_menu:
        timer 0.01 action Return()

    else:
        button:
            style "blank_button"
            xpos 0
            ypos 0
            xfill True
            yfill True
            action Return()

        add THLD_GUI_PATH + "quick_menu/" + persistent.timeofday + "/quick_menu_ground.png":
            xalign 0.5
            yalign 0.5

        imagemap:
            auto THLD_GUI_PATH + "quick_menu/" + persistent.timeofday + "/quick_menu_%s.png" xalign 0.5 yalign 0.5

            hotspot(0, 83, 660, 65):
                focus_mask None
                clicked [
                    Function(thld_set_dynamic_cursor, "main_menu"),
                    MainMenu(confirm=False)
                ]

            hotspot(0, 148, 660, 65):
                focus_mask None
                clicked ShowMenu("thld_save")

            hotspot(0, 213, 660, 65):
                focus_mask None
                clicked ShowMenu("thld_load")

            hotspot(0, 278, 660, 65):
                focus_mask None
                clicked ShowMenu("thld_preferences")

            hotspot(0, 343, 660, 65):
                focus_mask None
                action [
                    Function(thld_screens_diact),
                    ShowMenu("main_menu")
                ]

screen thld_quit():
    tag menu
    modal True

    if thld_lock_quit:
        timer 0.01 action Return()

    elif thld_lock_quit_game_main_menu_var:
        timer 0.01 action Quit(confirm=False)

    else:
        add THLD_GUI_PATH + "save_load/" + persistent.timeofday + "/load_bg.png"

        text "Вы действительно \nхотите выйти?":
            font thld_link_font
            size 100
            text_align 0.5
            xalign 0.5
            yalign 0.33
            antialias True
            kerning 2

        textbutton "Да":
            style "thld_settings_header_quit"
            text_style "thld_settings_header_quit"
            xpos 493
            ypos 600
            action [
                Function(thld_screens_diact),
                ShowMenu("main_menu")
            ]

        textbutton "Нет":
            style "thld_settings_header_quit"
            text_style "thld_settings_header_quit"
            xpos 1230
            ypos 600
            action [
                Hide("thld_quit"),
                Return()
            ]

screen thld_yesno_prompt(yes_action, message, no_action):
    modal True

    add THLD_GUI_PATH + "yes_no/" + persistent.timeofday + "/yes_no.png"

    text _(message):
        font thld_header_font
        text_align 0.5
        yalign 0.46
        xalign 0.5
        color THLD_YESNO_PROMPT_MESSAGE_COLOR[persistent.timeofday]
        size 30

    textbutton "Да":
        text_size 60
        style "thld_log_button"
        text_style "thld_settings_link"
        yalign 0.65
        xalign 0.3
        action yes_action

    textbutton "Нет":
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

    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Return()

    window:
        background Frame(THLD_GUI_PATH + "choice/" + persistent.timeofday + "/choice_box.png")
        left_padding 75
        right_padding 75
        bottom_padding 120
        top_padding 120

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
                    text_hover_color THLD_TEXT_HISTORY_WHAT_COLOR_HOVER[persistent.timeofday]
                    action RollbackToIdentifier(h.rollback_identifier)

        vbar:
            value YScrollValue("thld_text_history_screen")
            bottom_bar "images/misc/none.png"
            top_bar "images/misc/none.png"
            thumb THLD_GUI_PATH + "preferences/" + persistent.timeofday + "/vthumb.png"
            xoffset 1700

screen thld_choice(items):
    modal True

    window:
        background Frame((THLD_GUI_PATH + "choice/" + persistent.timeofday + "/choice_box.png"), 50, 50)
        xfill True
        yalign 0.5
        left_padding 75
        right_padding 75
        bottom_padding 50
        top_padding 50

        has vbox xalign 0.5

        for caption, action, chosen in items:
            if action and caption:
                button background None:
                    xalign 0.5
                    action action

                    $ action_color = THLD_CHOICE_COLORS_SELECTED[persistent.timeofday] if caption in persistent.choices else THLD_CHOICE_COLORS[persistent.timeofday]

                    text caption:
                        font header_font
                        size 37
                        hover_size 37
                        color action_color
                        hover_color THLD_CHOICE_COLORS_HOVER[persistent.timeofday]
                        xcenter 0.5
                        text_align 0.5

            else:
                text caption:
                    font header_font
                    size 60
                    color THLD_CHOICE_COLORS[persistent.timeofday]
                    text_align 0.5
                    xcenter 0.5

screen thld_help():
    tag menu
    modal True

    add THLD_GUI_PATH + "save_load/" + persistent.timeofday + "/load_bg.png"

    text "Информация":
        font thld_link_font
        size 70
        xalign 0.5
        ypos 33
        antialias True
        kerning 2

    textbutton "Группа VK":
        style "thld_log_button"
        text_style "thld_settings_header_quit"
        xalign 0.5
        ypos 350
        action OpenURL("https://vk.com/public176281709")

    textbutton "Под холодным небом":
        style "thld_log_button"
        text_style "thld_settings_header_quit"
        xalign 0.5
        ypos 500
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2262867309")

    textbutton "Сон":
        style "thld_log_button"
        text_style "thld_settings_header_quit"
        xalign 0.5
        ypos 650
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2663197411")

    add "thld_logowhite_hover":
        xpos 1520
        ypos 890

    textbutton "Назад":
        style "thld_log_button"
        text_style "thld_settings_link"
        xalign 0.015
        yalign 0.92
        action Return()
