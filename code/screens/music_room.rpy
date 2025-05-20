init python:
    thld_music_box = {
        "Reef — Inevitability": thld_reef_inevitability,
    }

    thld_music_room = MusicRoom(fadeout=1.0)

    for music_name in thld_music_box.values():
        thld_music_room.add(music_name)

screen thld_music_room():
    modal True

    if not thld_main_menu_var:
        add "thld_main_menu_options_frame" xalign 0.5 yalign 0.5

        add THLD_GUI_PATH + "main_menu/music_room_frame.png"

        frame:
            background None

            side "c r":
                area (0.15, 0.22, 0.79, 0.73)

                viewport:
                    id "thld_music_box"
                    draggable True
                    mousewheel True
                    scrollbars None

                    grid 1 len(thld_music_box):
                        for name, track in sorted(thld_music_box.iteritems()):
                            $ thld_music_room_label_text = name if thld_music_room.is_unlocked(track) else "???"

                            textbutton thld_music_room_label_text:
                                style "thld_button_none"
                                text_style "music_link"
                                xalign 0.5
                                action thld_music_room.Play(track)

                vbar:
                    value YScrollValue("thld_music_box")
                    bottom_bar "thld_main_menu_vbar_null_glitched"
                    top_bar THLD_GUI_PATH + "main_menu/vbar_full.png"
                    thumb None
                    xmaximum 52

        text "Музыка":
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
                Hide("thld_music_room"),
                ShowMenu("thld_extra")
            ]

        on "replaced" action Play("music", thld_reef_inevitability)
