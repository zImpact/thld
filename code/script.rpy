init python:
    class ThldFunctionCallback(Action):
        def __init__(self, function, *arguments):
            self.function = function
            self.arguments = arguments

        def __call__(self):
            return self.function(self.arguments)
    
    def thld_on_load_callback(slot):
        try:
            if persistent.thld_on_save_timeofday[slot]:
                persistent.timeofday = persistent.thld_on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.thld_on_save_timeofday[slot][1]
                persistent.font_size = persistent.thld_on_save_timeofday[slot][2]
                _preferences.volumes["music"] = persistent.thld_on_save_timeofday[slot][3]
                _preferences.volumes["sfx"] = persistent.thld_on_save_timeofday[slot][4]
                _preferences.volumes["voice"] = persistent.thld_on_save_timeofday[slot][5]
                thld_set_dynamic_cursor("timeofday")
        
        except:
            pass
    
    def thld_on_save_callback(slot):
        if not persistent.thld_on_save_timeofday:
            persistent.thld_on_save_timeofday = {}

        persistent.thld_on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes["music"], _preferences.volumes["sfx"], _preferences.volumes["voice"])
        
    def thld_screen_save():
        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[("thld_old_" + screen_name, None)] = renpy.display.screen.screens[(screen_name, None)]
        
    def thld_screen_act():
        config.window_title = u"Преддверие"
        config.name = "thld"
        config.version = "1.0"

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("thld_" + screen_name, None)]

        layout.LOADING = "Потерять несохраненные данные?"
            
        config.main_menu_music = "thld/sounds/music/thld_reef_inevitability.mp3"
        config.linear_saves_page_size = None
        persistent._file_page = "thld_FilePage_1"  

    def thld_screens_diact():
        config.window_title = u"Бесконечное лето"
        config.name = "Everlasting_Summer"
        config.version = "1.2"

        for screen_name in ["main_menu", "quit", "say", "nvl", "game_menu_selector", "yesno_prompt", "choice", "help"]:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("thld_old_" + screen_name, None)]
         
        layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
        
        config.overlay_functions.remove(thld_set_timeofday_cursor)
        config.mouse_displayable = MouseDisplayable("images/misc/mouse/1.png", 0, 0)
        config.main_menu_music = "sound/music/blow_with_the_fires.ogg"

        persistent._file_page = 1

        for channel in ["ambience", "music", "sound", "sound_loop"]:
            renpy.music.stop(channel)

        renpy.play(music_list["blow_with_the_fires"], channel = "music")

    def thld_screens_save_act():
        thld_screen_save()
        thld_screen_act()