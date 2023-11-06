﻿# Определение персонажей игры.
define ggDenis = Character("Денис", color="#34ebe8")
define Marat = Character("Первый голос", color="#73a65b")
define SanyaBefore = Character("Второй голос", color="#88c8eb")
define Sanya = Character("Саня", color="#88c8eb")
define MurusBefore = Character("Третий голос", color="#57cf27")
define Murus = Character("Мурус", color="#57cf27")
define UrgenBefore = Character("Голос из далека", color="#d9453f")
define UrgenWithoutSign = Character("", color="#d9453f")
define Urgen = Character("Юрген", color="#d9453f")
define Todd = Character("Тодд", color="#d9ab57")
define MiraBefore = Character("Женский голос", color="#e691eb")
define Mira = Character("Мира", color="#e691eb")
define Zagan = Character("Заган", color="#917776")

# Заставка
#label splashscreen:
#    scene black with dissolve
#    show text "Velius представляет" with dissolve
#    pause(1)
#    scene black with dissolve
#    show text "The mistake of the future" with dissolve
#    pause(1)
#    scene black with dissolve
#    return

# Игра начинается здесь:
label start:

    #scene bg room
    #show eileen happy

    call firstAct
    call secondAct

    return

label firstAct:
    scene bg_start_scene_street

    ggDenis "Бывают такие дни… {w} Я бы сказал, неважные…"
    ggDenis "Серые, рутинные, ничем не запоминающиеся будни, тянущиеся один за другим, каждый из которых ценен не больше, чем предыдущий."
    ggDenis "Однако, сейчас не такой день… {w} Во всяком случае не совсем."
    ggDenis "Сегодня заканчивается мой контракт на работу. {w} Очередная компания позади, по крайней мере для меня."
    ggDenis "(с иронией) Тестировщик и уже 8 лет… {w} Многовато для такой должности."
    ggDenis "В нынешней ситуации крупной компании легче заключить контракт с работником на определённый срок, чтобы не тратиться на мед страховку, премии и прочее, что может причитаться полноценному работнику."
    ggDenis "А что мне остаётся делать, кроме как играть по таким правилам? {w} Идти на постоянную работу? {w} Но в таком случае я буду получать меньше."
    ggDenis "Может заняться собственным проектом, перестать искать чужие ошибки и заявить о себе? {w} За 8-то лет я обзавёлся каким никаким опытом. {w} Можно, да только с кем? А если найду с кем, то чем займёмся?"
    ggDenis "“Много вопросов, мало дела” – как говорит мама. Трудно с ней не согласиться. {w} Прозябать всю жизнь, как наёмник, такое себе решение для “дипломированного специалиста”, но куда в таком случае податься?"
    ggDenis "Иногда кажется, что стоит относиться к всему проще, брать то, что даёт судьба и “плыть по течению”. {w} Тем более и так не плохо живу – есть крыша над головой, не голодаю. {w} Но ведь хочется чего-то большего…"

    scene bg_white

    ggDenis "Аааа..{w} Голова....{w} Как ..{w} боль..но"

    scene bg_grey with dissolve

    ggDenis "Ааа..{w} Не вижу?...{w} Ничего не вижу."
    Marat "Ёу чел, смотри этот очнулся."
    SanyaBefore "Не нравится мне он, трупы просто так не оживают."
    ggDenis "Какие трупы?{w} Я живой, помогите."
    # Звуки приближающихся шагов
    Marat "Нифига се, он ещё и говорить может."
    SanyaBefore "Говорю я тебе, здесь что-то не чисто. Он здесь почти неделю лежит, подстава какая-то."
    "Те же голоса, только звук сверху"
    Marat "Ёу, \"потерпевший\" , есть чё-нить ценное с собой?"
    SanyaBefore "Ты меня вообще слушаешь?"
    Marat "Сань, не ссы ты, что он нам может сделать?"

    Sanya "В таком состоянии ничего."
    Marat "Правильно.{w} Но, как мне кажется, он может нам чё-нить дать."
    Marat "Верно, потерпевший?"

    menu:
        "..."
        "У меня ничего с собой нет.":
            call firstBeating
        "Для тебя у меня ничего нет.":
            call secondBeating

    UrgenBefore "Эй утырки, отошли от него!"
    Sanya "А я говорил же тебе, что до добра это не доведёт!"
    Marat "Чё тоже хочешь получить?"
    "(удар)"
    Marat "АААААЙ"
    "(Удар о землю)"
    ggDenis "<Он меня бросил>"
    Marat "Чёрт, руку отпусти!!!"
    MurusBefore "Отпущу, если пообещаешь, что больше не будешь грабить и избивать."
    Marat "Сделаю чё хочешь, братан!{w} Без проблем!"
    Marat "МММ Как болит то. Саня сматываемся от сюда."
    "(Звуки удаляющихся шагов)"
    "(Рывок вверх)"
    ggDenis "<Снова я кому-то понадобился>"

    menu:
        "..."
        "Вы тоже грабить пришли?":
            call thirdBeating
        "Отпустите меня, у меня ничего нет.":
            call thirdBeating

    return

label secondAct:
    # Звук закрытия дверей
    "(Звук закрытия дверей)"
    ggDenis "<И куда он меня притащил?>"
    # Гул двигателя
    "(Резкое ускорение, гул двигателя)"
    ggDenis "<Естественно, в машину.{w} Чтобы увести куда подальше>"
    "(Тычок в затылок)"
    ggDenis "Ай, что такое?"
    MiraBefore "Спокойно. Не дёргайся и всё будет хорошо."
    ggDenis "<Что? Откуда исходит звук? {w} Будто в голове кто-то говорит>"
    $ persistent.dict0 = True
    MiraBefore "Так и есть. {w} Я у тебя в голове, а если быть точнее в интерфейсе твоих {a=glossary:Имплант}имплантов{/a}."
    ggDenis "<Моих чего?>"
    MiraBefore "Сейчас будет немного щипать."
    "(Появляется раздражение в области глаз)"
    # ((Появляется изображение кузова фургона))
    ggDenis "Я… Я вижу."
    MiraBefore "Можешь не благодарить, также подключила тебя к закрытой сети. {w} До встречи, ‘редактор’."
    "(Покалывание в затылке)"
    ggDenis "<Какой редактор? Что за сюр?>"
    ggDenis "Что… Что это было?"
    # ((Появляется моделька Юргена, его фразы пока что без подписи))
    $ persistent.dict1 = True
    UrgenWithoutSign "Это была Мира. Наш {a=glossary:Сетевик}‘сетевик’{/a}."
    ggDenis "Простите, кто?"
    UrgenWithoutSign "Ми-ра, Се-те-вик, человек, что копается в сети за нас."
    ggDenis "<Всё равно ничего не понял>"
    ggDenis "А вы кто?"
    UrgenWithoutSign "Я Юрген. Главный в отряде. Это Мурус – человек, полный сюрпризов и добра."
    # ((Появляется моделька Муруса))
    Murus "Приветствую."
    Urgen "За рулём сидит Тодд."
    "(Звук позади)"
    Todd "Привет ‘редактор’, или как тебя там."
    ggDenis "Стоп, стоп, стоп. Вы меня с кем-то путаете. {w} Я – Денис, тестировщик, а не ‘редактор’."
    Urgen "Очень сомневаюсь, что мы тебя с кем-то спутали. {w} Резидента TNN не встретишь на каждом углу."
    ggDenis "Резидента чего?"
    $ persistent.dict2 = True
    Todd "{a=glossary:Team New Net}Team New Net{/a}. {w} Ты один из тех, кто создал и запустил новую сеть. {w} Не прикидывайся дураком, мы всю твою подноготную знаем."
    ggDenis "Ладно, это давно начало переходить все возможные границы. {w} Ещё раз вам говорю, что я ничего не запускал, не основывал, не… не редактировал. {w} Я шёл домой, потом…"
    ggDenis "Потом каким-то образом оказался здесь… {w} Меня избили, хотели ограбить… {w} Теперь похитили и… {w} и везут не понятно куда. {w} Это нарушение моих гражданских прав, я требую отпустить меня и вызвать полицию."
    # ((Моделька Юргена с красным глазом))
    Urgen "Ты меня уже порядком подзадолбал. {w} Хватит ныть, мы тебе жизнь спасли, так что будь добр хотя бы не критиковать наши способы работы, в противном случае можешь возвращаться к своим друганам из переулка."
    ggDenis "<Я в ступоре, с одной стороны он прав, а с другой это не отменяет того, что меня похитили>"
    Murus "Прекратите оба. {w} Мы все в одной лодке плывём."
    Todd "Ну как скажешь."
    Murus "Так что лучше разобраться с проблемами."
    Urgen "Отлично, можешь начинать."
    Murus "Так, Денис, верно? {w} Что самое последнее ты помнишь до того, как оказался здесь?"
    ggDenis "Помню, как домой шёл."
    Murus "А когда это было?"
    ggDenis "Осенью, в начале октября 2023."
    Murus "Стоп, а после ничего не помнишь?"
    ggDenis "После мне что-то ударило в голову, я ослеп и меня пришли грабить."
    Todd "Погодь, какой сейчас по твоему год?"
    ggDenis "Ну по-моему сейчас 2023."
    Todd "Вот и приплыли. Юрг, у нас проблемы."
    $ persistent.dict3 = True
    Urgen "Без тебя вижу. {w} Твой “хороший профессионал” решил нас кинуть и достал нам {a=glossary:Образ}‘образ’{/a} какого идиота."
    Murus "Постой, не руби с плеча. {w} Денис, а кем ты работал и сколько?"
    ggDenis "Тестировщик, работал на разных специальностях чуть более 8 лет."
    Todd "Как и ‘редактор’ в своё время. Юрг, видишь, никто нас не кидал."
    Urgen "Спасибо, утешил. {w} У нас тут испорченный образ человека, который когда-то был ‘редактором’, но сам он об этом ничего не помнит и не знает. {w} Как раз так и планировал."
    Murus "Предлагаю…"
    Urgen "Помолчи, хватит с тебя."
    Urgen "Ладно. Доедем до базы, там дадим Мире покопаться в нём, а ты, Тодд, организуешь мне встречу со своим “профессионалом”."
    Todd "Но…"
    Urgen "Без но, он обещал мне образ ‘редактора’, а не нюни."
    Murus "Юрген, оставь его, не усугубляй."
    Urgen "Сдался он мне."
    Murus "Денис, не сердись на него. {w} Он сейчас на взводе, как и все мы."
    ggDenis "<Мда… {w} Хотел я чего-то большего, но чтоб настолько… {w} Оказаться не в своём времени, не в своём теле, так как у меня точно не было никаких имплантов, так ещё с меня требуют не понятно что… {w} По видимому остаётся только ждать>"
    return

label firstBeating:
    "(Рывок вверх)"
    ggDenis "<Он меня поднял>"
    Marat "Это мы сейчас проверим, Саня, подержи-ка его."
    ggDenis "<Он выворачивает мне карманы.{w} Да что же это происходит то?>"
    ggDenis "Я же говорю, что ничего у меня нет."
    # Экран мигает красным
    "(Удар в живот)"
    ggDenis "....Ой"
    Marat "Молчать! Без тебя разберусь."
    return

label secondBeating:
    "(Рывок вверх)"
    ggDenis "<Он меня поднял>"
    Marat "Саня, подержи-ка его, сейчас я научу его общаться с заместителем Рекса."
    "(Череда беспорядочных ударов в грудь и живот)"
    ggDenis "Кхе...{w} Согласен..{w} по удару ты на директора не тянешь!"
    Marat "Ты чё бессмертный?"
    return

label thirdBeating:
    MurusBefore "Успокойся ты, я тебя не обижу."
    UrgenBefore "Хватит сюсюкаться, погнали отсюда, нам нельзя здесь светиться."
    MurusBefore "Понял, понял."
    ggDenis "<Он меня куда-то тащит>"
    ggDenis "Это похищение? Куда вы меня тащите?"
    MurusBefore "Спокойно, просто жди. {w} Скоро сам всё поймёшь."

init python:
    def glossary_handler(target):
        x, y = renpy.get_mouse_pos()
        renpy.show_screen("glossary", target, x, y)
        renpy.restart_interaction()

    config.hyperlink_handlers["glossary"] = glossary_handler

# Для добавления новых слов {a=glossary:имплант}импланты{/a}
default glossary_dict = {
    "Имплант":"это модификация тела.",
    "Сетевик": "тот, кто лазает по сетям.",
    "Team New Net": "TNN - те, кто сделал новую сеть.",
    "Образ": "это записанная душа человека",
}

screen glossary(target, x, y): # deleted styling elements but feel free to add them back
    zorder 250
    button background None action Hide("glossary")
    vbox:
        xpos x
        ypos y
        frame:
            xmaximum 400
            has vbox
            label target
            text glossary_dict[target]
