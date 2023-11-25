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

define config.default_fullscreen = True

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
    #play sound ...
    #play music ...

    call firstAct from _call_firstAct
    call secondAct from _call_secondAct
    call thirdAct from _call_thirdAct
    call fourthAct

    return

label firstAct:
    play music музыка_начало

    scene bg_start_scene_street

    ggDenis "Бывают такие дни… {w}Я бы сказал, неважные…"
    ggDenis "Серые, рутинные, ничем не запоминающиеся будни, тянущиеся один за другим, каждый из которых ценен не больше, чем предыдущий."
    ggDenis "Однако, сейчас не такой день… {w}Во всяком случае не совсем."
    ggDenis "Сегодня заканчивается мой контракт на работу. {w}Очередная компания позади, по крайней мере для меня."
    ggDenis "(с иронией) Тестировщик и уже 8 лет… {w}Многовато для такой должности."
    ggDenis "В нынешней ситуации крупной компании легче заключить контракт с работником на определённый срок, чтобы не тратиться на мед страховку, премии и прочее, что может причитаться полноценному работнику."
    ggDenis "А что мне остаётся делать, кроме как играть по таким правилам? {w}Идти на постоянную работу? {w}Но в таком случае я буду получать меньше."
    ggDenis "Может заняться собственным проектом, перестать искать чужие ошибки и заявить о себе? {w}За 8-то лет я обзавёлся каким никаким опытом. {w}Можно, да только с кем? А если найду с кем, то чем займёмся?"
    ggDenis "\"Много вопросов, мало дела\" – как говорит мама. Трудно с ней не согласиться. {w}Прозябать всю жизнь, как наёмник, такое себе решение для \"дипломированного специалиста\", но куда в таком случае податься?"
    ggDenis "Иногда кажется, что стоит относиться к всему проще, брать то, что даёт судьба и \"плыть по течению\". {w}Тем более и так не плохо живу – есть крыша над головой, не голодаю. {w}Но ведь хочется чего-то большего…"

    scene bg_white

    stop music
    play sound ультразвук

    ggDenis "Аааа.. {w}Голова.... {w}Как.. {w}боль..но"
    
    scene bg_interference with dissolve

    ggDenis "Ааа.. {w}Не вижу?... {w}Ничего не вижу."

    stop sound

    Marat "Ёу чел, смотри этот очнулся."
    SanyaBefore "Не нравится мне он, трупы просто так не оживают."
    ggDenis "Какие трупы? {w}Я живой, помогите."

    # Звуки приближающихся шагов
    play sound звук_приближающихся_шагов

    Marat "Нифига се, он ещё и говорить может."
    ggDenis "<Видимо, они подошли ко мне>"

    SanyaBefore "Говорю я тебе, здесь что-то не чисто. Он здесь почти неделю лежит, подстава какая-то."
    "Те же голоса, только звук сверху"

    stop sound

    Marat "Ёу, \"потерпевший\" , есть чё-нить ценное с собой?"
    SanyaBefore "Ты меня вообще слушаешь?"
    Marat "Сань, не ссы ты, что он нам может сделать?"

    Sanya "В таком состоянии ничего."
    Marat "Правильно. {w}Но, как мне кажется, он может нам чё-нить дать."
    Marat "Верно, потерпевший?"

    menu:
        "..."
        "У меня ничего с собой нет.":
            call firstBeating from _call_firstBeating
        "Для тебя у меня ничего нет.":
            call secondBeating from _call_secondBeating

    UrgenBefore "Эй утырки, отошли от него!"
    Sanya "А я говорил же тебе, что до добра это не доведёт!"
    Marat "Чё тоже хочешь получить?"

    play sound звук_удара
    "(удар)"
    Marat "АААААЙ"

    play sound удар_о_землю

    "(Удар о землю)"
    ggDenis "<Он меня бросил>"

    stop sound

    Marat "Чёрт, руку отпусти!!!"
    MurusBefore "Отпущу, если пообещаешь, что больше не будешь грабить и избивать."
    Marat "Сделаю чё хочешь, братан! {w}Без проблем!"
    Marat "МММ Как болит то. Саня сматываемся от сюда."

    play sound звук_удаляющихся_шагов
    ggDenis "<Ну хоть эти двое ушли>"
    
    play sound звук_резкого_поднятия_персонажа

    "(Рывок вверх)"
    ggDenis "<Снова я кому-то понадобился>"

    stop sound

    menu:
        "..."
        "Вы тоже грабить пришли?":
            call thirdBeating from _call_thirdBeating
        "Отпустите меня, у меня ничего нет.":
            call thirdBeating from _call_thirdBeating_1

    return

label secondAct:
    # Звук закрытия дверей
    play sound звук_закрытия_двери_в_машине

    ggDenis "<Двери закрылись>"
    ggDenis "<И куда он меня притащил?>"

    stop sound

    # Гул двигателя
    play sound гул_двигателя

    "(Резкое ускорение)"
    ggDenis "<Естественно, в машину.{w} Чтобы увести куда подальше>"

    stop sound

    "(Тычок в затылок)"
    ggDenis "Ай, что такое?"

    show person_mira_calm at holo(), brightness(.25), color("#cdf")

    MiraBefore "Спокойно. Не дёргайся и всё будет хорошо."
    ggDenis "<Что? Откуда исходит звук? {w} Будто в голове кто-то говорит>"

    $ persistent.dict0 = True

    MiraBefore "Так и есть. Я у тебя в голове, а если быть точнее в интерфейсе твоих {a=glossary:Имплант}имплантов{/a}."
    ggDenis "<Моих чего?>"
    MiraBefore "Сейчас будет немного щипать."
    "(Появляется раздражение в области глаз)"

    # ((Появляется изображение кузова фургона))
    scene bg_garage
    show person_mira_calm at holo(), brightness(.25), color("#cdf")

    ggDenis "Я… Я вижу."
    MiraBefore "Можешь не благодарить, также подключила тебя к закрытой сети."
    MiraBefore "Там только базовая информация, но подойдёт, чтобы освежить память. {w}До встречи, \"редактор\"."

    hide person_mira_calm

    "(Покалывание в затылке)"
    ggDenis "<Какой редактор? Что за сюр?>"
    ggDenis "Что… Что это было?"

    # ((Появляется моделька Юргена, его фразы пока что без подписи))
    show person_urgen_calm

    $ persistent.dict1 = True

    UrgenWithoutSign "Это была Мира. Наш {a=glossary:Сетевик}сетевик{/a}."
    ggDenis "Простите, кто?"
    UrgenWithoutSign "Ми-ра, Се-те-вик, человек, что копается в сети за нас."
    ggDenis "<Всё равно ничего не понял>"
    ggDenis "А вы кто?"
    UrgenWithoutSign "Я Юрген. Главный в отряде. Это Мурус – человек, полный сюрпризов и добра."

    show person_urgen_calm:
        xpos 960 ypos 1080
        linear .3 xpos 880 ypos 1090
        linear .3 xpos 780 ypos 1080
        linear .3 xpos 680 ypos 1090
        linear .3 xpos 580 ypos 1080

    # ((Появляется моделька Муруса))
    show person_murus_calm at right1

    Murus "Приветствую."
    Urgen "За рулём сидит Тодд."
    "(Звук позади)"
    Todd "Привет \"редактор\", или как тебя там."
    ggDenis "Стоп, стоп, стоп. Вы меня с кем-то путаете. {w}Я – Денис, тестировщик, а не \"редактор\"."
    Urgen "Очень сомневаюсь, что мы тебя с кем-то спутали. {w}Резидента TNN не встретишь на каждом углу."
    ggDenis "Резидента чего?"

    $ persistent.dict2 = True

    Todd "{a=glossary:Team New Net}Team New Net{/a}. {w}Ты один из тех, кто создал и запустил новую сеть. {w}Не прикидывайся дураком, мы всю твою подноготную знаем."
    ggDenis "Ладно, это давно начало переходить все возможные границы. {w}Ещё раз вам говорю, что я ничего не запускал, не основывал, не… не редактировал. {w}Я шёл домой, потом…"
    ggDenis "Потом каким-то образом оказался здесь… {w}Меня избили, хотели ограбить… {w}Теперь похитили и… {w}и везут не понятно куда. {w}Это нарушение моих гражданских прав, я требую отпустить меня и вызвать полицию."

    # ((Моделька Юргена с красным глазом))
    hide person_urgen_calm
    show person_urgen_irritated at left1
    
    Urgen "Ты меня уже порядком подзадолбал. {w}Хватит ныть, мы тебе жизнь спасли, так что будь добр хотя бы не критиковать наши способы работы, в противном случае можешь возвращаться к своим друганам из переулка."
    ggDenis "<Я в ступоре, с одной стороны он прав, а с другой это не отменяет того, что меня похитили>"
    Murus "Прекратите оба. {w}Мы все в одной лодке плывём."
    Todd "Ну как скажешь."
    Murus "Так что лучше разобраться с проблемами."
    Urgen "Отлично, можешь начинать."
    Murus "Так, Денис, верно? {w}Что самое последнее ты помнишь до того, как оказался здесь?"
    ggDenis "Помню, как домой шёл."
    Murus "А когда это было?"
    ggDenis "Осенью, в начале октября 2023."
    Murus "Стоп, а после ничего не помнишь?"
    ggDenis "После мне что-то ударило в голову, я ослеп и меня пришли грабить."
    Todd "Погодь, какой сейчас по твоему год?"
    ggDenis "Ну по-моему сейчас 2023."
    Todd "Вот и приплыли. Юрг, у нас проблемы."

    $ persistent.dict3 = True

    Urgen "Без тебя вижу. Твой \"хороший профессионал\" решил нас кинуть и достал нам {a=glossary:Образ}образ{/a} какого идиота."
    Murus "Постой, не руби с плеча. {w}Денис, а кем ты работал и сколько?"
    ggDenis "Тестировщик, работал на разных специальностях чуть более 8 лет."
    Todd "Как и \"редактор\" в своё время. Юрг, видишь, никто нас не кидал."
    Urgen "Спасибо, утешил. {w}У нас тут испорченный {a=glossary:Образ}образ{/a} человека, который когда-то был \"редактором\", но сам он об этом ничего не помнит и не знает. {w}Как раз так и планировал."
    Murus "Предлагаю…"
    Urgen "Помолчи, хватит с тебя."
    Urgen "Ладно. Доедем до базы, там дадим Мире покопаться в нём, а ты, Тодд, организуешь мне встречу со своим \"профессионалом\"."
    Todd "Но…"
    Urgen "Без но, он обещал мне {a=glossary:Образ}образ{/a} \"редактора\", а не нюни."
    Murus "Юрген, оставь его, не усугубляй."
    Urgen "Сдался он мне."
    Murus "Денис, не сердись на него. {w} Он сейчас на взводе, как и все мы."
    ggDenis "<Мда… {w}Хотел я чего-то большего, но чтоб настолько… {w}Оказаться не в своём времени, не в своём теле, так как у меня точно не было никаких {a=glossary:Имплант}имплантов{/a}, так ещё с меня требуют не понятно что… {w}По видимому остаётся только ждать>"

    hide person_urgen_irritated
    hide person_murus_calm
    return

label thirdAct:
    # ((Вид гаража с машиной – такой надеюсь будет))

    show person_mira_irritated at left1
    show person_todd_excited at right1

    Mira "Тодд, назови хоть одну причину тебя не обнулять!"
    ggDenis "<Вот и здравствуйте>"
    Todd "Тише, тише, сестрёнка, не перед новеньким ведь."
    Mira "Юрген, теперь косяки стали для нас нормой или что?"
    Murus "Давай не будем усугуб…"
    Mira "Даже не начинай. {w}Не сейчас."

    # ((Злой Юрген проходит по экрану))
    show person_urgen_irritated at offscreenright
    show person_urgen_irritated:
        xpos 1800 ypos 1080
        linear .5 xpos 1400 ypos 1090
        linear .5 xpos 1000 ypos 1080
        linear .5 xpos 600 ypos 1090
        linear .5 xpos 200 ypos 1080
        linear .5 xpos -200 ypos 1090
        linear .5 xpos -600 ypos 1080
        linear .5 xpos -1000 ypos 1090

    Mira "Юрген, не молчи, второй раз так накосячить нельзя. {w}Куда… {w}куда ты?"

    hide person_urgen_irritated

    Todd "А что ты сразу на меня всё валишь? Я лишь свёл вас с ним и потом забрал {a=glossary:Образ}образ{/a}."
    
    $ persistent.dict4 = True

    Mira "Именно, забрал повреждённый {a=glossary:Образ}образ{/a}, даю сто {a=glossary:Univency}univency{/a}, что ты знал об этом."
    Todd "Думай, что хочешь, а сотку можешь перевести."
    Murus "Так, Денис, лучше пошли отсюда. {w}Это надолго."
    
    hide person_mira_irritated
    hide person_todd_excited

    #((Вид комнаты с двумя двухъярусными кроватями, надеюсь, что он также будет готов))

    show person_murus_calm

    Murus "Вот здесь будет поспокойнее. {w}Кстати, ты об этом не переживай, они часто так."
    menu:
        "..."
        "Она сказала, что это второй косяк. Что она имела в виду?":
            play music музыка_истории_муруса
            call firstMurusStory from _call_firstMurusStory
            ggDenis "О ком они говорили? С \"кем\" встречался Тодд?"
            call secondMurusStory from _call_secondMurusStory
        "О ком они говорили? С \"кем\" встречался Тодд?":
            play music музыка_истории_муруса
            call secondMurusStory from _call_secondMurusStory_1
            ggDenis "Она сказала, что это второй косяк. Что она имела в виду?"
            call firstMurusStory from _call_firstMurusStory_1
    
    stop music
    ggDenis "Кажется, эти двое успокоились, у меня есть пара вопросов к ним и к Юргену. {w}Кстати, а где он?"
    Murus "Не знаю, знать не хочу и тебе не рекомендую узнавать. {w}Он сейчас в плохом настроении, лучше его таким не видеть."
    ggDenis "Понял, спасибо за разговор."

    hide person_murus_calm

    return

label fourthAct:
    #((Вид гаража с машиной внутри))
    ggDenis "<Кажется, где-то здесь должен быть Тодд>"

    show person_todd_excited

    Todd "Что, пришла извиняться?"
    ggDenis "Не совсем."
    Todd "А, так это ты. Что, старина Мурус, так сказать, выболтал тебя?"
    ggDenis "Можно и так сказать. А если честно, то хочется с тобой пообщаться, позадавать вопросы."
    Todd "Если у великого \"редактора\" есть ко мне вопросы, то пускай задаёт их."
    ggDenis "Как давно ты знаешь Муруса и Юргена?"
    Todd "Юргена знаю года два, может три. {w}А с Мурусом очень давно знаком, ещё до того, как он на фронт попал."
    ggDenis "Стоп, стоп, стоп. {w}Мурус, как и Юрген - бывший военный?"
    Todd "Конечно, а ты думаешь, как они ещё могли познакомиться?"
    ggDenis "Странно, Мурус совсем не похож на Юргена."
    Todd "Так война на каждого по-разному влияет. {w}Кто-то, как Юрген, продолжает быть \"военным\" и в жизни, {w}а кто-то замыкается в себе, строит из себя \"мистера добро\" и лезет, куда попало."
    ggDenis "<Кажется, что у Тодда есть какие-то претензии к Мурусу>"
    ggDenis "Ясно, а зачем мы все здесь? {w}Хотел у Муруса спросить, да боюсь, что он мне до вечера рассказывать будет."
    Todd "Молодец, быстро понял, кто тебе всё пояснит без воды и нравоучений."
    Todd "В общем, у Юргена есть претензии к содружеству корпораций \"Newborn Old World\"*, {w}которые сейчас контролируют почти всю Евразию."
    Todd "Наш доблестный командир хочет выставить все их грязные секретики на всемирное обозрение, {w}возможно, желая освободить континент от фирм и сделать снова свободным."
    ggDenis "<Высокие замашки, особенно для обычного военного. Хотя, кем был Юрген на фронте?>"
    Todd "А возможно, что Юрг просто тронулся умом и тащит всех нас на верную гибель."
    ggDenis "А кем был Юрген на фронте?"
    Todd "Ээм… Командиром, большим и важным. {w}Не спрашивай об этом, не знаю, не помню."
    ggDenis "<Что-то мой собеседник растерялся>"
    ggDenis "Понял, спасибо. {w}Тогда зачем я понадобился Юргену?"
    Todd "О, вот это правильный вопрос. {w} Смотри, Юргену был нужен человек, что будет толкать всю команду вперёд. {w}Поэтому здесь есть Мурус – человек-мораль."
    Todd "Юргену нужен был специалист по Сети, что защитит от треклятых {a=glossary:Офисник}офисников{/a}. {w}Вот он и нашёл Миру, а может и не искал, тут не буду утверждать точно."
    Todd "Юргену нужен был один из талантливейших механиков и инженеров современности. {w}Мурус и привёл ему меня."
    Todd "И тут, Юргену потребовался человек, что сможет вынести всё \"грязное бельё\" NOW*. {w}Вот тут появляется потребность в человеке, вроде тебя. {w}Но как ты можешь понять, не всё пошло по плану."
    ggDenis "Спасибо за ответ, наверное."
    Todd "Так, у меня ещё есть одно дело, так что давай ещё один вопрос, а то я не успею до завтрашнего выезда."
    ggDenis "А что за дело?"
    Todd "Ну раз тебе интересно, то нужно починить радио из машины. {w}Оно исправно, по крайней мере с технической точки зрения, но не с программной. {w}Короче, радио не выводит звук."
    ggDenis "Я мог бы подключиться и посмотреть, что с ним не так, не зря же я великий \"редактор\"."
    Todd "Без проблем, главное, ещё хуже не сделай."
    ggDenis "<Я погляжу, что их подкоды не сильно далеко ушли от кодов моего времени>"
    ggDenis "Можешь включить?"
    Todd "А то."

    # Старт игры
    call startFirstMiniGame

    # Звук радиопомех
    play sound звук_радиопомех

    Todd "Харош, оно работает. Может Юрген ошибается, и ты и правда тот, кто нам нужен?"
    ggDenis "Спасибо, если понадобится что-нибудь ещё, то обращайся."

    stop sound

    ggDenis "Я кое-что ещё хотел у тебя спросить."
    menu:
        "..."
        # Негативный вариант
        "Что за вирус был на том роботе?":
            call firstToddStory
        # Нейтральный вариант
        "Не знаешь, где сейчас Мира?":
            call secondToddStory

    hide person_todd_excited

    # ((Вид комнаты с проводами))

    show person_mira_irritated

    ggDenis "Привет."
    Mira "Стой там."
    ggDenis "Что? Что-то не так."
    Mira "Конечно. {w}Всё не так, начиная с тебя, заканчивая твоей грязной обувью."
    ggDenis "То есть, нужно разуться?"
    Mira "Ну как минимум."
    ggDenis "Вообще я хотел расспросить тебя про новую сеть."

    show person_mira_calm
    hide person_mira_irritated

    Mira "Ох… Ну давай, начинай. {w}Чувствую, что я с тобой и твоими вопросами надолго."
    ggDenis "Можешь максимально просто рассказать, что из себя представляет ваша Сеть?"
    Mira "Ну… {w}В общем, Сеть представляет собой объёмное виртуальное пространство, напоминающее город."
    Mira "Где каждый дом – есть место сосредоточения информации по определённой теме и ссылок, ведущих к другим домам, связанным с темой первого дома."
    ggDenis "Ох… {w}То есть, теперь вся информация, относящаяся к определённой теме, представляет собой какой-то дом. Но как в нём располагается вся информация и как её находить?"
    Mira "Всё довольно просто. Тебя буквально кидает между домами и информацией внутри каждого дома. {w}Можно сказать, что тебя телепортирует либо между домами, либо между этажами или комнатами определённого здания."
    ggDenis "Но как это использовать? Как, скажу так, сделать запрос?"
    Mira "Подумать об этом и тебя кинет туда, куда нужно."
    ggDenis "А если я думаю о доступе к какой-нибудь секретной информации, например, о паролях или идентификаторе?"
    Mira "Подобная информация называется \"подвалом\", то есть она является сокрытой и доступна только обладателям \"ключей\"."
    ggDenis "Ключей?"
    Mira "Обладать ключом – находится в списке тех, чей идентификатор находится в списках доступа к данной информации."
    ggDenis "Примерно уловил смысл. {w}А как не теряться во всём этом?"
    Mira "Вот тут и начинаются сложности, ведь некоторым с трудом даётся одно ссылочное перемещение, а кто-то скачет сразу по нескольким ссылкам и перебирает тонны информации за час."
    ggDenis "Стоп, если ты скачешь по нескольким ссылкам, то получается, что в Сети ты есть в нескольких местах одновременно?"
    Mira "Именно, и для такого трюка использую дополнительные образы. {w}То есть, у обычного пользователя есть один образ, с которым он полностью себя ассоциирует."
    Mira "У {a=glossary:Сетевик}сетевиков{/a} образов тьма тьмущая, и все они посылают информацию ему в голову."
    ggDenis "А как можно хранить в голове столько информации? {w}С помощью имплантов?"
    Mira "Да, бывалые сетевики нарочно сращивают себя с серверами и суперкомпьютерами."
    Mira "Некоторые настолько увлекаются, что забывают о своём настоящем теле и иногда умирают, сидя в метре от еды и воды. {w}Но могут остаться живыми в Сети, как куча образов, привязанных к определённой вычислительной системе."
    ggDenis "Звучит немного жутко."
    Mira "Ну это их выбор, так что не стоит их осуждать за это."
    ggDenis "А как создавать локальные сети?"
    Mira "Вот для этого нужна независимая система из серверов, полный контроль над которой доступен сетевику, её создавшему, или тому, у кого есть \"ключи\"."
    Mira "После установки и настройки серверов сетевик должен создать пространство, прописать правила ссылок и \"прыжков\", возможно даже прописать \"подвалы\"."
    Mira "И вот только сделав всё это, можно пользоваться, добавлять и расширять свою сеть."
    ggDenis "Можно ли в таком случае сказать, что вся Сеть – это очень-очень огромная локальная сеть {a=glossary:Team New Net}TNN{/a}?"
    Mira "Так и есть. {w}Ну или по крайней мере было, до того, как TNN распалась и была перебита."
    ggDenis "А почему {a=glossary:Team New Net}TNN{/a} распалась?"
    Mira "Вы, вроде бы, разделились в плане мнений о будущем развитии Сети. {w}Но тут тайна, покрытая мраком. {w}Следов в Сети об распаде крайне мало, а в Сетях {a=glossary:Офисник}офисников{/a} об этом вообще ничего не сказано."
    ggDenis "Ясно, а что касательно языка программирования, на котором всё пишется?"
    Mira "Если коротко, то нынешний язык – огромный набор методов, циклов и вариантов написания всесторонних задач и действий, составленный и построенный на твоём древнем языке программирования."
    ggDenis "Для меня он всё равно актуален и скажу даже больше, благодаря моему знанию этого \"древнего\" языка, я помог Тодду."
    Mira "Не велика заслуга."
    ggDenis "<Похоже, что Мира всё ещё обижается на Тодда>"
    Mira "Ещё есть вопросы?"
    menu:
        "..."
        "Что связывает тебя с Юргеном?":
            call firstMiraStory
        "Технически возможно восстановить мой образ?":
            call secondMiraStory
    
    ggDenis "<Что ж пойду обратно к Мурусу, кажется завтра большой день, нужно отдохнуть>"

    return

# Выборы

# Первая стычка с Маратом
label firstBeating:
    play sound звук_резкого_поднятия_персонажа

    "(Рывок вверх)"
    ggDenis "<Он меня поднял>"

    stop sound

    Marat "Это мы сейчас проверим, Саня, подержи-ка его."
    ggDenis "<Он выворачивает мне карманы.{w} Да что же это происходит то?>"
    ggDenis "Я же говорю, что ничего у меня нет."

    # Экран мигает красным
    play sound звук_удара
    "(Удар в живот)"

    ggDenis "....Ой"
    Marat "Молчать! Без тебя разберусь."
    return

# Вторая стычка с Маратом
label secondBeating:
    play sound звук_резкого_поднятия_персонажа

    "(Рывок вверх)"
    ggDenis "<Он меня поднял>"

    stop sound

    Marat "Саня, подержи-ка его, сейчас я научу его общаться с заместителем Рекса."

    play sound звук_череды_ударов
    "(Череда беспорядочных ударов в грудь и живот)"

    ggDenis "Кхе... {w}Согласен.. {w}по удару ты на директора не тянешь!"

    stop sound

    Marat "Ты чё бессмертный?"
    return

# Спасение Лениса
label thirdBeating:
    MurusBefore "Успокойся ты, я тебя не обижу."
    UrgenBefore "Хватит сюсюкаться, погнали отсюда, нам нельзя здесь светиться."
    MurusBefore "Понял, понял."
    ggDenis "<Он меня куда-то тащит>"
    ggDenis "Это похищение? Куда вы меня тащите?"
    MurusBefore "Спокойно, просто жди. {w}Скоро сам всё поймёшь."

    return

# Первая история Муруса
label firstMurusStory:
    Murus "До этого из-за Тодда пришлось срочно менять расположение базы."
    ggDenis "А что он такого учудил?"
    Murus "Ну тут долгая история… {w}Хотя лучше тебе я всё расскажу, рано или поздно ты бы узнал, но только начну издалека."
    Murus "Раньше мы дислоцировались на заброшенном когда-то грузовом, а после и военном корабле. {w}Его наскоро переделали под воздушный транспортник, а после сбили ещё во времена, когда войны вели государства, а не фирмы."
    Murus "Впоследствии корабль был разграблен, а неподалёку возник военный городок, что ныне разросся до целого селения."
    Murus "После с войны вернулся Юрген, привёл остатки корабля в удобоваримый вид, а там всё \"это\" и завертелось…  {w}А точно, Тодд."
    Murus "Он однажды весь в грязи и копоти ворвался в рубку с какой-то картонкой, на которой написал, чтобы мы все заткнулись."
    Murus "Я и Мира подумали, что это шутка какая-то, а Юрген хотел отчитать его за нарушение субординации."
    Murus "Только он открыл рот, как Тодд кинул картонку, бросился к рубильнику и обесточил базу."
    Murus "Ой, как после на него орала Мира…"
    ggDenis "А зачем он это сделал?"
    Murus "Не спеши, и так много важного опускаю. {w}Так о чём это я? {w}Точно."
    Murus "Ещё до того, как мы все собрались, Мира, как опытный {a=glossary:Сетевик}сетевик{/a}, возвела локальную сеть, в которой хранилась куча информации."
    $ persistent.dict5 = True
    Murus "Через неё велось управление всем имеющимся оборудованием, а самое важное, что через неё можно было безопасно пользоваться общей сетью, не боясь попасться {a=glossary:Офисник}офисникам{/a}."
    Murus "Так вот, однажды я и Тодд на свалке нашли почти рабочего робота, привезли на базу, Тодд не удержался и подключил его к нашей сети."
    Murus "После радовался, как ребёнок, когда железяка прошла пару метров. {w}Сказал, что заставит её работать за двоих, и уселся за работу."
    Murus "Через несколько часов произошла эта ситуация с рубильником."
    Murus "Как оказалось, в роботе сидел опасный вирус, который понемногу начал подчинять себе всё наше оборудование, мог завладеть нашей сетью, а после и нами."
    Murus "Пришлось срочно перебираться, оставлять кучу оборудования и нашу сеть, что очень сильно задело Миру."
    ggDenis "Я одного не понял, зачем он просил вас замолчать?"
    Murus "Я тоже, но лучше тебе спросить у него."

    return
    
# Вторая история Муруса
label secondMurusStory:
    Murus "Скажем так, Тодд встречался с человеком-легендой, с тем единственным, что уже много лет обворовывает фирмы и остаётся живым."
    ggDenis "И получается, что эта \"легенда\" выкрала меня у какой-то фирмы?"
    Murus "Именно, но как ты уже понял, у \"профессионала\" что-то пошло не так, из-за этого уже Юргену придётся пообщаться с ним."
    ggDenis "А кем я был? Все говорят, что каким-то \"редактором\"."
    Murus "Именно, ты был человеком, благодаря которому новая сеть смогла запуститься и стабильно работать."
    ggDenis "Класс, а теперь я… {w}А кто я?"
    Murus "Если быть честным, то ты сейчас в теле бывшего работника местной горнодобывающей компании \"Richground\". {w}Насколько я помню, у прошлого владельца этого тела остановилось сердце, и он погиб в реанимации."
    ggDenis "Мило, тогда почему я ещё жив?"
    Murus "Нынче тела, напичканные {a=glossary:Имплант}имплантами{/a}, не хоронят, а буквально восстанавливают, вставляя ещё больше \"железок\", чтобы загружать на них {a=glossary:Образ}образы{/a} ценных работников."
    ggDenis "То есть, я жив только благодаря модификациям чужого мёртвого тела?"
    Murus "Да, ты бывший легендарный тестировщик-разработчик, запертый в чужом полуроботизированном теле с огромной дырой в памяти."
    ggDenis "<Вот так поднял настроение, нечего сказать>"
    Murus "Но не расстраивайся, держи универсальную схему подкодов, которые сейчас используются везде. {w}Даже микроволновка благодаря ним работает."
    ggDenis "Спасибо, пригодится."

    return

# Негативный вариант распроса Тодда
label firstToddStory:
    Todd "… {w}Вот это вопрос, так вопрос."
    ggDenis "<Что-то он опять растерялся>"
    Todd "Тебе ведь Мурус об этом рассказал?"
    ggDenis "Да, он. А что?"
    Todd "Да так, ничего. {w}Просто, не верь всему, что он говорит, часто ты видишь не полную картину событий."
    Todd "Я… Не смогу ответить на этот вопрос, {w}лучше спроси у Миры, {w}она в сетевой сейчас."
    ggDenis "<Мурус был прав, не стоило у Тодда спрашивать об этом вирусе>"
    ggDenis "Понял. Удачи тебе."

    return

# Нейтральный вариант распроса Тодда
label secondToddStory:
    Todd "Мира в сетевой – комнате с кучей проводов, серверов и с постоянным проветриванием."
    Todd "О, вот ещё что. {w}Не ляпни ничего лишнего про Юргена, когда к ней придёшь, {w}у них какие-то близкие отношения или что-то в этом роде."
    ggDenis "Спасибо. Удачи тебе."
    Todd "И тебе."

    return

# Негативный вариант выбора распроса Миры
label firstMiraStory:
    show person_mira_irritated
    hide person_mira_calm
    
    Mira "Тебе-то какая разница?"
    ggDenis "Интересно откуда он тебя знает. {w}Тодда он знает благодаря Мурусу, с которым знаком с фронта."
    Mira "А я погляжу, что ты уже много чего знаешь. {w}Он помог мне тогда, когда меня все бросили, и с тех пор я с ним."
    ggDenis "Понял, спасибо за ответ."
    Mira "Ладно, выметайся, не до тебя сейчас."

    hide person_mira_irritated

    return

# Нейтральный вариант выбора распроса Миры
label secondMiraStory:
    Mira "Скорее всего, только перезаписью текущего образа, то есть, \"нынешний ты\" будешь утерян."
    ggDenis "А нельзя дополнить текущий образ?"
    Mira "Образ невероятно сложная структура, копаться и корректно перестраивать которую под силу только нескольким очень опытным {a=glossary:Сетевик}сетевикам{/a}."
    ggDenis "Печально как-то выходит."
    Mira "Соглашусь, но грустить ты можешь и в другом месте, так что на выход."

    hide person_mira_calm

    return

label startFirstMiniGame:
    # определим фон игры, время игры в секундах
    # и зададим параметры игры - спрайты и положение для собираемых предметов
    $ bgForGame = "bg_quest"
    $ nameMistake = "mistake"
    $ ox = 445
    $ oy = 530
    $ hf_init(bgForGame, (nameMistake, ox, oy, _(nameMistake)))
    
    # покажем вместе с фоном и фигурки на нём
    $ hf_bg()
    with dissolve
    
    "Мне кажется, что здесь есть ошибка."

    # запустим игру
    $ hf_start()
    # жёсткая пауза, чтобы игрок перестал кликать и не пропустил результаты
    $ renpy.pause(1, hard=True)

    # результаты
    if hf_return == 0:
        "Все ошибки исправлены!"

    $ hf_hide()
    with dissolve
    return

# Координаты для расположения персонажей
init:
    $ left1 = Position(xalign=0.2)
    $ right1 = Position(xalign=0.8)

init python:
    def glossary_handler(target):
        x, y = renpy.get_mouse_pos()
        if (y > 925):
            y -= 130
        renpy.show_screen("glossary", target, x, y)
        renpy.restart_interaction()

    config.hyperlink_handlers["glossary"] = glossary_handler

# голограмма
init:
    # мерцание голограммы
    transform holo(a1=.75, a2=.5, z1=.5, z2=.55, t1=.15, t2=1.25):
        parallel:
            yanchor 1. ypos config.screen_height xpos 680
        # мерцание прозрачности
        parallel:
            alpha a1
            ease .015 alpha a2
            ease .005 alpha a1
            .05
            ease .01 alpha a2
            ease .01 alpha a1
            .025
            ease .005 alpha a2
            ease .015 alpha a1
            .05
            ease .02 alpha a2
            ease .001 alpha a1
            .035
            ease .015 alpha a2
            ease .005 alpha a1
            .05
            ease .01 alpha a2
            ease .01 alpha a1
            .015
            repeat
        # несколько рандомных вытягиваний по вертикали,
        # имитирующих неполадки и сбои в связи (с шипением)
        parallel:
            rndf(t1, t2)
            ease .01 
            .01
            ease .01 
            .01
            rndf(t1, t2)
            ease .01 
            .01
            ease .01 
            .01
            rndf(t1, t2)
            ease .01 
            .01
            ease .01 
            .01
            rndf(t1, t2)
            ease .01 
            .01
            ease .01
            .01
            rndf(t1, t2)
            ease .01 
            .01
            ease .01 
            .01
            rndf(t1, t2)
            repeat

# Для добавления новых слов {a=glossary:Имплант}импланты{/a}
default glossary_dict = {
    "Имплант": "механическая модификация тела.",
    "Сетевик": "опытный пользователь новой сети.",
    "Team New Net": "команда создателей новой сети.",
    "Образ": "оцифрованная личность человека.",
    "Univency": "валюта нового времени.",
    "Офисник": "сетевик, работающий на фирму.",
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