# hf - HiddenFolks (поиск предметов)
# используется в паре с модулем 7dots.rpy

# затем будет вызов игры:
    # $ hf_start() 
# количество несобранных предметов будет в hf_return

init python:
    # автоматическое объявление спрайтов (включая webp)
    images_auto()

# НАСТРОЙКИ

    # нужно ли выводить подсказку
    hf_hint = False

    # имя папки со спрайтами игры в директории images плюс пробел
    hf_dir = "quest"

# ВНУТРЕННИЕ ПЕРЕМЕННЫЕ

    # режим игры (False - режим фона)
    hf_game_mode = False

    # предметы, которые нужно найти
    hf_needed = []

    # предметы, которые уже нашли
    hf_picked = []

    # фон игры
    hf_back = "black"

    # количество несобранных предметов
    hf_return = 0

    # изначальное количество предметов
    hf_max_count = 0

    # инициализация игры
    def hf_init(bg, *args, **kwargs):
        global hf_needed, hf_picked, hf_back, hf_max_count
        # обнуляем списки и переменные
        hf_needed = []
        hf_picked = []
        hf_back = bg
        # добавляем в список предметы, которые нужно найти
        for item, x, y, h in args:
            hf_needed.append((item, x, y, h))
        hf_max_count = len(hf_needed)
        # применяем необязательные параметры игры
        # по сути меняем значения похожих переменных,
        # но только они должны начинаться с hf_
        for k, v in kwargs.items():
            kk = "hf_" + k
            if kk in globals().keys():
                globals()[kk] = kwargs.get(k)

    # показать игру в виде фона на слое master
    def hf_bg():
        store.hf_game_mode = False
        show_s("HiddenFolks")

    # спрятать игру-фон
    # но сначала показать, если игра экран скрыт
    def hf_hide():
        hf_bg()
        renpy.with_statement(None)
        hide_s("HiddenFolks")

    # запустить игру
    # если задан какой-то эффект, то сначала показать игру с ним
    def hf_start(effect=None):
        store.hf_game_mode = False
        hf_bg()
        renpy.with_statement(effect)
        store.hf_game_mode = True
        store.hf_return = len(hf_needed)
        renpy.call_screen("HiddenFolks")
        hf_bg()

    # клик по предмету (перенести его в инвентарь или убрать оттуда)
    def hf_click(item, x, y, h):
        store.hf_picked.append(store.hf_needed.pop(hf_needed.index((item, x, y, h))))
        splay("sound/click")
        renpy.restart_interaction()
        # осталось собрать
        store.hf_return = len(hf_needed)
    HFClick = renpy.curry(hf_click)

    # текст подсказки
    hf_hint_text = ""

    # меняем текст подсказки
    def hf_set_hint(t=""):
        if hf_hint and hf_hint_text != t:
            store.hf_hint_text = t
            renpy.restart_interaction()
    SetHint = renpy.curry(hf_set_hint)

screen HiddenFolks():
    # фон игры
    add hf_back
    image nameAnswer at truecenter
    # все предметы на экране
    for i, x, y, h in hf_needed:

        $ item = hf_dir + " " + i
        # предмет-кнопка
        imagebutton:
            style "empty"
            # спрайт предмета
            idle item
            # положение предмета (координаты его центра)
            pos(x, y)
            # наведение на пиксель
            focus_mask True
            # все действия только в режиме игры
            if hf_game_mode:
                # обработка клика
                action HFClick(i, x, y, h)

    # анимация таймера
    if hf_game_mode:
        # всё собрали, уходим (Return()() из def больше не работает)
        if hf_return < 1:
            timer .01 repeat True action SetHint(), SPlay("sound/gamewin"), Return()