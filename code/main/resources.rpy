init python:
    from os import path
    from random import randint, uniform
    from math import sqrt, pow

    for file_name in renpy.list_files():
        if THLD_MOD_NAME in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith(THLD_MOD_NAME + "/images/bg/"):
                renpy.image("bg " + THLD_PREFIX + file_path, file_name)

            elif file_name.startswith(THLD_MOD_NAME + "/images/sprites/"):
                renpy.image(
                    THLD_PREFIX + file_path,
                    ConditionSwitch(
                        "persistent.sprite_time=='sunset'", im.MatrixColor(file_name, im.matrix.tint(0.94, 0.82, 1.0)),
                        "persistent.sprite_time=='night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)),
                        True, file_name
                    )
                )

            elif file_name.startswith(THLD_MOD_NAME + "/sounds/"):
                globals()[THLD_PREFIX + file_path] = file_name

    store.thld_colors = {}
    store.thld_names = {}
    store.thld_names_list = []
    thld_speaker_color = "speaker_color"

    store.thld_names_list.append("thld_narrator")

    store.thld_names_list.append("thld_th")

    thld_colors["thld_me"] = {"speaker_color": THLD_PACIFIST_NAME_COLOR}
    thld_names["thld_me"] = "Я"
    store.thld_names_list.append("thld_me")

    thld_colors["thld_pacifist"] = {"speaker_color": THLD_PACIFIST_NAME_COLOR}
    thld_names["thld_pacifist"] = "Пацифист"
    store.thld_names_list.append("thld_pacifist")

    thld_colors["thld_pi_arena"] = {"speaker_color": THLD_PI_ARENA_NAME_COLOR}
    thld_names["thld_pi_arena"] = "Пионер"
    store.thld_names_list.append("thld_pi_arena")

    thld_colors["thld_pi_teapot"] = {"speaker_color": THLD_TEAPOT_NAME_COLOR}
    thld_names["thld_pi_teapot"] = "Пионер"
    store.thld_names_list.append("thld_pi_teapot")

    thld_colors["thld_teapot"] = {"speaker_color": THLD_TEAPOT_NAME_COLOR}
    thld_names["thld_teapot"] = "Чайник"
    store.thld_names_list.append("thld_teapot")

    thld_colors["thld_pi_railway"] = {"speaker_color": THLD_PI_RAILWAY_NAME_COLOR}
    thld_names["thld_pi_railway"] = "Пионер"
    store.thld_names_list.append("thld_pi_railway")

    thld_colors["thld_pi_preacher"] = {"speaker_color": THLD_PREACHER_NAME_COLOR}
    thld_names["thld_pi_preacher"] = "Пионер в халате"
    store.thld_names_list.append("thld_pi_preacher")

    thld_colors["thld_preacher"] = {"speaker_color": THLD_PREACHER_NAME_COLOR}
    thld_names["thld_preacher"] = "Проповедник"
    store.thld_names_list.append("thld_preacher")

    thld_colors["thld_third"] = {"speaker_color": THLD_THIRD_NAME_COLOR}
    thld_names["thld_third"] = "Третий"
    store.thld_names_list.append("thld_third")

    thld_colors["thld_pi_announcer"] = {"speaker_color": THLD_PI_ANNOUNCER_NAME_COLOR}
    thld_names["thld_pi_announcer"] = "Распорядитель"
    store.thld_names_list.append("thld_pi_announcer")

    thld_colors["thld_butcher"] = {"speaker_color": THLD_BUTCHER_NAME_COLOR}
    thld_names["thld_butcher"] = "Мясник"
    store.thld_names_list.append("thld_butcher")

    thld_colors["thld_pi_pharos"] = {"speaker_color": THLD_PI_PHAROS_NAME_COLOR}
    thld_names["thld_pi_pharos"] = "Пионер"
    store.thld_names_list.append("thld_pi_pharos")

    thld_colors["thld_pharos"] = {"speaker_color": THLD_PI_PHAROS_NAME_COLOR}
    thld_names["thld_pharos"] = "Маяк"
    store.thld_names_list.append("thld_pharos")

    thld_colors["thld_engi"] = {"speaker_color": THLD_ENGI_NAME_COLOR}
    thld_names["thld_engi"] = "Инженер"
    store.thld_names_list.append("thld_engi")

    thld_colors["thld_gensek"] = {"speaker_color": THLD_GENSEK_NAME_COLOR}
    thld_names["thld_gensek"] = "Генсек"
    store.thld_names_list.append("thld_gensek")

    thld_colors["thld_crowd"] = {"speaker_color": THLD_CROWD_NAME_COLOR}
    thld_names["thld_crowd"] = "Толпа"
    store.thld_names_list.append("thld_crowd")

    thld_colors["thld_pi_guide"] = {"speaker_color": THLD_PI_GUIDE_NAME_COLOR}
    thld_names["thld_pi_guide"] = "Проводник"
    store.thld_names_list.append("thld_pi_guide")

    def thld_char_define(character_name, is_nvl=False):
        global DynamicCharacter
        global nvl
        global thld_store
        global thld_speaker_color
        thld_gl = globals()

        if character_name == "thld_narrator":
            if is_nvl:
                thld_gl["thld_narrator"] = Character(
                    None,
                    kind=nvl,
                    what_style="thld_text_style"
                )

            else:
                thld_gl["thld_narrator"] = Character(
                    None,
                    what_style="thld_text_style"
                )

            return

        if character_name == "thld_th":
            if is_nvl:
                thld_gl["thld_th"] = Character(
                    None,
                    kind=nvl,
                    what_style="thld_text_style",
                    what_prefix="~ ",
                    what_suffix=" ~"
                )

            else:
                thld_gl["thld_th"] = Character(
                    None,
                    what_style="thld_text_style",
                    what_prefix="~ ",
                    what_suffix=" ~"
                )

            return

        if is_nvl:
            thld_gl[character_name] = DynamicCharacter(
                "%s_name" % character_name,
                color=store.thld_colors[character_name][thld_speaker_color],
                kind=nvl,
                what_style="thld_text_style",
                who_suffix=":"
            )
            thld_gl["%s_name" % character_name] = store.thld_names[character_name]

        else:
            thld_gl[character_name] = DynamicCharacter(
                "%s_name" % character_name,
                color=store.thld_colors[character_name][thld_speaker_color],
                what_style="thld_text_style"
            )
            thld_gl["%s_name" % character_name] = store.thld_names[character_name]

    def thld_set_mode_adv():
        nvl_clear()

        global menu
        menu = renpy.display_menu

        global thld_store

        for character_name in store.thld_names_list:
            thld_char_define(character_name)

    def thld_set_mode_nvl():
        nvl_clear()

        global menu
        menu = nvl_menu

        global thld_narrator
        global thld_th
        thld_narrator_nvl = thld_narrator
        th_nvl = thld_th

        global thld_store

        for character_name in store.thld_names_list:
            thld_char_define(character_name, True)

    def thld_reload_names():
        global thld_store

        for character_name in store.thld_names_list:
            thld_char_define(character_name)

    def thld_onload(type):
        global thld_lock_quit
        global thld_lock_quick_menu

        if type == "lock":
            renpy.config.skipping = None
            thld_lock_quit = True
            thld_lock_quick_menu = True
            config.allow_skipping = False

        elif type == "unlock":
            thld_lock_quit = False
            thld_lock_quick_menu = False
            config.allow_skipping = True

    def thld_set_timeofday_cursor():
        config.mouse_displayable = MouseDisplayable(THLD_GUI_PATH + "cursors/" + persistent.timeofday + "/cursor.png", 0, 0)

    def thld_set_dynamic_cursor(state):
        if thld_set_timeofday_cursor in config.overlay_functions:
            config.overlay_functions.remove(thld_set_timeofday_cursor)

        if state == "timeofday":
            config.overlay_functions.append(thld_set_timeofday_cursor)

        elif state == "main_menu":
            config.mouse_displayable = MouseDisplayable(THLD_GUI_PATH + "cursors/main_menu/cursor.png", 0, 0)

        elif state == "null":
            config.mouse_displayable = MouseDisplayable(Null(0, 0), 0, 0)

    def thld_set_time(timeofday, sprite_time=None):
        if sprite_time is None:
            sprite_time = timeofday

        renpy.block_rollback()
        persistent.timeofday = timeofday
        persistent.sprite_time = sprite_time

    def thld_blink(blink_pause):
        renpy.show("blink")
        renpy.pause(blink_pause, hard=True)

    def thld_unblink(scene_name, unblink_pause):
        renpy.hide("blink")
        renpy.scene()
        renpy.show(scene_name)
        renpy.show("unblink")
        renpy.pause(unblink_pause, hard=True)

    def thld_get_image_offsets(tag, zoom_factor, width, height):
        pos = renpy.get_image_bounds(tag)

        zoom_xoffset = (width * (zoom_factor - 1)) / 2
        zoom_yoffset = (height * (zoom_factor - 1)) / 2

        initial_xoffset = pos[0] + zoom_xoffset
        initial_yoffset = pos[1] + zoom_yoffset
        return initial_xoffset, initial_yoffset

    class ThldVector(renpy.object.Object):
        def __init__(self, *data):
            self.data = data

        def __repr__(self):
            return repr(self.data)

        def __add__(self, other):
            return tuple((a + b for a, b in zip(self.data, other.data)))

        def __sub__(self, other):
            return tuple((a - b for a, b in zip(self.data, other.data)))

    class ThldSingleDustParticle(renpy.object.Object):
        def __init__(self, sp, fp, t, rt, ft, zoom, alpha, st):
            self.start_pos = sp
            self.finish_pos = fp
            self.part_time = t
            self.rise_time = rt
            self.fall_time = ft
            self.max_zoom = zoom
            self.max_alpha = alpha
            self.oldst = st
            self.pos = self.start_pos
            self.zoom = .0
            self.alpha = .0

    class ThldDustParticles(renpy.Displayable, NoRollback):
        def __init__(self, part_img, parts_count=300):
            super(ThldDustParticles, self).__init__()
            self.part_img = renpy.displayable(part_img)
            self.w, self.h = (config.screen_width, config.screen_height)
            self.particles = [self.make_particle() for i in xrange(parts_count)]

        def get_rand_cord(self, w, h):
            return randint(-100, w + 100), randint(-100, h + 100)

        def progress_calc(self, oldst, t, st):
            target = oldst + t
            anim_time = target - st
            res = 1.0 - anim_time / t

            if res < .0:
                return .0

            elif .0 <= res <= 1.0:
                return res

            else:
                return 1.0

        def make_particle(self, st=float()):
            w, h, = self.w, self.h

            start_pos = self.get_rand_cord(w, h)
            finish_pos = self.get_rand_cord(w, h)
            xdist, ydist = ThldVector(*finish_pos) - ThldVector(*start_pos)

            speed = uniform(110, 130)

            part_time = sqrt(pow(xdist, 2) + pow(ydist, 2)) / speed
            rise_time = part_time * uniform(.1, .25)
            fall_time = part_time * uniform(.1, .25)

            max_alpha = uniform(.25, .75)
            max_zoom = uniform(.25, .75)

            part = ThldSingleDustParticle(
                            start_pos,
                            finish_pos,
                            part_time,
                            rise_time,
                            fall_time,
                            max_zoom,
                            max_alpha,
                            st
                            )
            return part

        def update_particle(self, part_idx, st):
            part = self.particles[part_idx]

            t = part.part_time
            rt = part.rise_time
            ft = part.fall_time

            start_time = part.oldst
            rise_time = start_time + rt
            fall_time = start_time + t - ft

            anim_progress = self.progress_calc(start_time, t, st)
            rise_progress = self.progress_calc(rise_time, rt, st)
            fall_progress = self.progress_calc(fall_time, ft, st)

            rise_vs_fall = rise_progress - fall_progress

            part.pos = renpy.atl.interpolate(
                                        anim_progress,
                                        part.start_pos,
                                        part.finish_pos,
                                        (int, int)
                                        )

            part.alpha = part.max_alpha * rise_vs_fall
            part.zoom = part.max_zoom * rise_vs_fall

            if anim_progress >= 1.0:
                self.particles.pop(part_idx)
                self.particles.append(self.make_particle(st))

        def visit(self):
            return [self.part_img for i in self.particles]

        def render(self, w, h, st, at):
            rv = renpy.Render(w, h)

            for idx, part in enumerate(self.particles):
                self.update_particle(idx, st)
                xpos, ypos = part.pos

                if 0 < xpos < w and 0 < ypos < h:
                    t = Transform(
                            child=self.part_img,
                            alpha=part.alpha,
                            zoom=part.zoom
                            )

                    tr = t.render(w, h, st, at)
                    rv.blit(tr, (xpos, ypos))

            renpy.redraw(self, .0)
            return rv

    class ThldGlitchEffect(renpy.Displayable):
        def __init__(self, child, randomkey=None, *args , **kwargs):
            super(ThldGlitchEffect, self).__init__(**kwargs)
            self.child = renpy.displayable(child)
            self.args = args
            self.randomkey = randomkey
            self.kwargs = kwargs

        def render(self, width, height, st, at):
            cwidth, cheight = renpy.render(self.child, width, height, st, at).get_size()
            return renpy.render(self.glitch(self.child,
                                            cwidth, cheight, renpy.random.Random(self.randomkey),
                                            *self.args, **self.kwargs),
                                width, height,
                                st, at)

        @staticmethod
        def glitch(child, cwidth, cheight, randomobj, chroma=True, minbandheight=1, offset=10, crop=False):
            chroma &= renpy.display.render.models
            if not (cwidth and cheight):
                return child
            lizt = []
            offt = 0
            theights = sorted(randomobj.randint(0, cheight) for k in range(min(cheight, randomobj.randint(10, 20))))
            fheight = 0

            while fheight < cheight:
                if theights:
                    theight = max(theights.pop(0) - fheight, minbandheight)

                else:
                    theight = cheight - theight

                band = Transform(child, crop=(0, fheight, cwidth, theight))

                if chroma:
                    band = thld_chromatic_offset(band, chzoom=1.0 + .5 * offt / cwidth)

                band = Transform(band, pos=(offt, absolute(fheight)), subpixel=True)
                lizt.append(band)
                fheight += theight

                if offt:
                    offt = 0

                else:
                    offt = randomobj.randint(-offset, offset)

            crop = crop or None

            return Fixed(Transform(child, alpha=.0),
                        *lizt,
                        fit_first=True,
                        crop_relative=crop or False,
                        crop=crop and (0, 0, 1.0, 1.0)
                        )

        def __eq__(self, other):
            return (type(self) == type(other)) and (self.args == other.args) and (self.kwargs == other.kwargs)

    class ThldRectangle(renpy.Displayable):
        def __init__(self, width, height, alpha, **kwargs):
            super(ThldRectangle, self).__init__(**kwargs)
            self.width = width
            self.height = height
            self.alpha = alpha
            self.frame = Solid("#000000", xsize=self.width, ysize=self.height)

        def render_frame(self, width, height, st, at):
            t = Transform(child=self.frame, alpha=self.alpha)
            obj = renpy.render(t, width, height, st, at)
            render = renpy.Render(self.width, self.height)
            render.blit(obj, (0, 0))
            return render

    class ThldBlackRectangle(ThldRectangle):
        def __init__(self, width, height, alpha, **kwargs):
            super(ThldBlackRectangle, self).__init__(width, height, alpha, **kwargs)

        def render(self, width, height, st, at):
            return self.render_frame(width, height, st, at)

    class ThldTextRectangle(ThldRectangle):
        def __init__(self, padding, alpha, text, font=None, size=20, **kwargs):
            self.padding = padding
            self.text = text
            self.font = font
            self.size = size
            self.text_displayable = Text(self.text, font=self.font, size=self.size, xalign=0.5, yalign=0.5)
            super(ThldTextRectangle, self).__init__(0, 0, alpha, **kwargs)

        def render(self, width, height, st, at):
            text_render = renpy.render(self.text_displayable, width, height, st, at)
            text_width, text_height = text_render.get_size()

            self.width = int(text_width + self.padding * 2)
            self.height = int(text_height + self.padding * 2)
            self.frame = Solid("#000000", xsize=self.width, ysize=self.height)

            render = self.render_frame(self.width, self.height, st, at)
            render.blit(text_render, (self.width / 2 - text_render.get_size()[0] / 2,
                                    self.height / 2 - text_render.get_size()[1] / 2))
            return render

init:
    $ thld_reload_names()

    $ thld_main_menu_font = THLD_GUI_PATH + "fonts/gotham_pro_light.ttf"
    $ thld_main_menu_buttons_padding = 20
    $ thld_main_menu_buttons_alpha = 0.6
    $ thld_main_menu_buttons_size = 60

    $ thld_main_menu_var = True
    $ thld_lock_quit_game_main_menu_var = True
    $ thld_lock_quit = False
    $ thld_lock_quick_menu = False

    image thld_main_menu_particles = ThldDustParticles("thld/images/effects/particle_dust.png", 300)
    image thld_sunset_dust = ThldDustParticles("thld/images/effects/sunset_particle_dust.png", 300)
    image thld_ext_lake_day = "thld/images/effects/ext_lake_day.png"
    image thld_ext_boat_day = "thld/images/effects/ext_boat_day.png"
    image thld_vingette = "thld/images/effects/vingette.png"

    image thld_blank_skip = renpy.display.behavior.ImageButton(Null(1920, 1080), Null(1920, 1080), clicked=[Jump("thld_after_intro")])

    image thld_intro_logo = THLD_GUI_PATH + "misc/intro_logo.png"
    image thld_main_menu_background = THLD_GUI_PATH + "main_menu/main_menu_background.png"
    image thld_logowhite_idle = THLD_GUI_PATH + "misc/logowhite_idle.png"
    image thld_main_menu_bar_null = THLD_GUI_PATH + "preferences/main_menu/bar_null.png"
    image thld_main_menu_vbar_null = THLD_GUI_PATH + "main_menu/vbar_null.png"
    image thld_main_menu_options_frame = ThldBlackRectangle(width=1804, height=1028, alpha=0.6)

    transform thld_main_menu_particles_anim:
        ease 1 xoffset -10 rotate -0.3 alpha 0.7
        ease 1 xoffset 10 rotate 0 alpha 1
        ease 1 xoffset 0 rotate 0.3 alpha 0.5
        repeat

    transform thld_chromatic_offset(child, chzoom=1.01):
        Fixed(
            Transform(child, alpha=.0),
            Transform(child, xalign=.0, xzoom=chzoom, gl_color_mask=(False, False, True, True)),
            Transform(child, xalign=.5, xzoom=chzoom, gl_color_mask=(False, True, False, True)),
            Transform(child, xalign=1.0, xzoom=chzoom, gl_color_mask=(True, False, False, True)),
            fit_first=True
            )
        crop(.0, .0, 1.0, 1.0)
        crop_relative True

    transform thld_boat_moving():
        subpixel True
        truecenter
        zoom 1.03

        parallel:
            linear 0.5 xoffset -2
            linear 0.5 xoffset 3
            linear 0.5 xoffset -1
            linear 0.5 xoffset 2
            repeat

        parallel:
            linear 0.8 yoffset -6
            linear 0.8 yoffset 12
            linear 0.8 yoffset -6
            repeat

    image thld_logowhite_hover:
        ThldGlitchEffect("thld_logowhite_idle")
        pause 0.2
        ThldGlitchEffect("thld_logowhite_idle")
        pause 0.2
        repeat

    image thld_main_menu_logo = ThldTextRectangle(
        padding=thld_main_menu_buttons_padding,
        alpha=thld_main_menu_buttons_alpha,
        text="Преддверие",
        font=thld_main_menu_font,
        size=100
    )

    image thld_start_button_idle = ThldTextRectangle(
        padding=thld_main_menu_buttons_padding,
        alpha=thld_main_menu_buttons_alpha,
        text="Начать игру",
        font=thld_main_menu_font,
        size=thld_main_menu_buttons_size
    )

    image thld_start_button_hover:
        ThldGlitchEffect("thld_start_button_idle")
        pause 0.2
        ThldGlitchEffect("thld_start_button_idle")
        pause 0.2
        repeat

    image thld_load_button_idle = ThldTextRectangle(
        padding=thld_main_menu_buttons_padding,
        alpha=thld_main_menu_buttons_alpha,
        text="Загрузить",
        font=thld_main_menu_font,
        size=thld_main_menu_buttons_size
    )

    image thld_load_button_hover:
        ThldGlitchEffect("thld_load_button_idle")
        pause 0.2
        ThldGlitchEffect("thld_load_button_idle")
        pause 0.2
        repeat

    image thld_extra_button_idle = ThldTextRectangle(
        padding=thld_main_menu_buttons_padding,
        alpha=thld_main_menu_buttons_alpha,
        text="Дополнительно",
        font=thld_main_menu_font,
        size=thld_main_menu_buttons_size
    )

    image thld_extra_button_hover:
        ThldGlitchEffect("thld_extra_button_idle")
        pause 0.2
        ThldGlitchEffect("thld_extra_button_idle")
        pause 0.2
        repeat

    image thld_preferences_button_idle = ThldTextRectangle(
        padding=thld_main_menu_buttons_padding,
        alpha=thld_main_menu_buttons_alpha,
        text="Настройки",
        font=thld_main_menu_font,
        size=thld_main_menu_buttons_size
    )

    image thld_preferences_button_hover:
        ThldGlitchEffect("thld_preferences_button_idle")
        pause 0.2
        ThldGlitchEffect("thld_preferences_button_idle")
        pause 0.2
        repeat

    image thld_exit_button_idle = ThldTextRectangle(
        padding=thld_main_menu_buttons_padding,
        alpha=thld_main_menu_buttons_alpha,
        text="Выход",
        font=thld_main_menu_font,
        size=thld_main_menu_buttons_size
    )

    image thld_exit_button_hover:
        ThldGlitchEffect("thld_exit_button_idle")
        pause 0.2
        ThldGlitchEffect("thld_exit_button_idle")
        pause 0.2
        repeat

    image thld_return_button_idle = Text("Назад", font=thld_main_menu_font, size=thld_main_menu_buttons_size)

    image thld_return_button_hover:
        ThldGlitchEffect("thld_return_button_idle")
        pause 0.2
        ThldGlitchEffect("thld_return_button_idle")
        pause 0.2
        repeat

    image thld_load_button_idle_ = Text("Загрузить игру", font=thld_main_menu_font, size=thld_main_menu_buttons_size)

    image thld_load_button_hover_:
        ThldGlitchEffect("thld_load_button_idle_")
        pause 0.2
        ThldGlitchEffect("thld_load_button_idle_")
        pause 0.2
        repeat

    image thld_delete_button_idle = Text("Удалить", font=thld_main_menu_font, size=thld_main_menu_buttons_size)

    image thld_delete_button_hover:
        ThldGlitchEffect("thld_delete_button_idle")
        pause 0.2
        ThldGlitchEffect("thld_delete_button_idle")
        pause 0.2
        repeat

    image thld_yes_button_idle = Text("Да", font=thld_main_menu_font, size=thld_main_menu_buttons_size)

    image thld_yes_button_hover:
        ThldGlitchEffect("thld_yes_button_idle")
        pause 0.2
        ThldGlitchEffect("thld_yes_button_idle")
        pause 0.2
        repeat

    image thld_no_button_idle = Text("Нет", font=thld_main_menu_font, size=thld_main_menu_buttons_size)

    image thld_no_button_hover:
        ThldGlitchEffect("thld_no_button_idle")
        pause 0.2
        ThldGlitchEffect("thld_no_button_idle")
        pause 0.2
        repeat

    image thld_music_button_idle = Text("Музыка", font=thld_main_menu_font, size=thld_main_menu_buttons_size)

    image thld_music_button_hover:
        ThldGlitchEffect("thld_music_button_idle")
        pause 0.2
        ThldGlitchEffect("thld_music_button_idle")
        pause 0.2
        repeat

    image thld_gallery_button_idle = Text("Галерея", font=thld_main_menu_font, size=thld_main_menu_buttons_size)

    image thld_gallery_button_hover:
        ThldGlitchEffect("thld_gallery_button_idle")
        pause 0.2
        ThldGlitchEffect("thld_gallery_button_idle")
        pause 0.2
        repeat

    image thld_main_menu_bar_null_glitched:
        ThldGlitchEffect("thld_main_menu_bar_null")
        pause 0.2
        ThldGlitchEffect("thld_main_menu_bar_null")
        pause 0.2
        repeat

    image thld_main_menu_vbar_null_glitched:
        ThldGlitchEffect("thld_main_menu_vbar_null")
        pause 0.2
        ThldGlitchEffect("thld_main_menu_vbar_null")
        pause 0.2
        repeat
