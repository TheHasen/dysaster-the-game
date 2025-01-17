﻿# Guión del juego.

# Tamaño de la pantalla.
define width  = 1280
define height = 720

# Personajes principales.
# Don Nacho
define color_nombre_narco = "#FF8200"
define anon_n = Character("???", color=color_nombre_narco)
define narco = Character("Don Nacho", color=color_nombre_narco) # Ignacio Villanueva Alcallaga

# Los demás.
define naufrago = Character("Naufrago", color="#5599ff")
define empresario = Character("Harrison", color="#5599ff") # Robert Bobby harrison
define waton = Character("Jimeno") # Jimeno Montoya
define mecanica = Character("Lili") # Liliana Oliviera

# Personajes secundarios.
define guardia_1 = Character("Guardia 1", color="#584f63")
define guardia_2 = Character("Guardia 2", color="#aaa")
define guardia_3 = Character("Guardia 3", color="#a52c2b")
define guardia_4 = Character("Guardia 4", color="#a7a223")

# Fondos de cada escena.
# Escala de las imágenes.
# Modelo a seguir: image bg NOMBRE = im.Scale('bg NOMBRE.EXT', width, height)
image bg guard_1 = im.Scale('bg guard_1.png', width, height)
image bg guard_2 = im.Scale('bg guard_2.png', width, height)
image bg guard_3 = im.Scale('bg guard_3.png', width, height)
image bg guard_4 = im.Scale('bg guard_4.png', width, height)
image bg prison = im.Scale('bg prison.jpg', width, height)
image bg norte_sur = im.Scale('bg norte_sur.png', width, height)
image bg zombies = im.Scale('bg zombies.jpg', width, height)
image bg boat = im.Scale('bg boat.jpg', width, height)
image bg bodega = im.Scale('bg bodega.png', width, height)

# Otras variables
default items_bodega = set()

# Textos del narrador & el contexto.
define texto_centrado = Character(None, what_xalign=0.5, what_text_align=0.5, text_xpos=0.5, window_yalign=0.5)
define contexto = Character(None, what_xalign=0.5, what_text_align=0.5, text_xpos=0.5, window_yalign=0.5, what_color="#e79600")
define warning_box = Character(None, window_xalign=0.5, window_yalign=0.5, what_xalign=0.5, what_yalign=0.5, text_xpos=0.5, text_ypos=0.5, what_text_align=0.5, interact=False)
define warning_title = "{b}{color=#f00}Disclaimer{/color}{/b}"

# Helpers
#texto_centrado "{i}{/i}"

# Se inicia el juego.
label start:

    # Detener la música del menú principal.
    stop music fadeout 2.0

    # Al inicio el fondo es de color negro.
    # Disclaimer
    warning_box "[warning_title]\n\
    El Siguiente trabajo es una obra de ficción que\
    puede contener material sensible y/u ofensivo\
    para algunas personas, cualquier parecido con\
    la realidad sobre personajes, diálogos, elementos\
    y/o historia es pura coincidencia. Todo el contenido\
    presentado en este juego es total y completamente\
    ficticio. Al haber iniciado el archivo ejecutable\
    del juego (dysaster.exe), usted renuncia automaticamente a\
    toda posible demanda u otra acción legal en contra\
    del Team Walala y a todos sus integrantes.\
    \n© 2021 Team Walala"

    pause(1.0)
    
    # Fondo prisión.
    scene bg prison

    # Hablado por narrador, centrado en el eje X e Y.
    texto_centrado "{i}Prisión de Guantanamo, Cuba{/i}"

    # Personajes secundarios comienzan el diálogo.
    scene bg guard_1
    guardia_1 "¡Los infectados están entrando por el muro este!"
    scene bg guard_2
    guardia_2 "¡Invadieron la zona norte, el muro practicamente ya no existe!"
    scene bg guard_3
    guardia_3 "¡Estamos teniendo una fuga de reclusos en la zona sur!"
    scene bg guard_4
    guardia_4 "Acaban de confirmar que {b}ÉL{/b} esta entre los que se han fugado."

    # Fondo inicial.
    scene bg forest

    # Aparece uno de los protagonistas.
    show fugitive one:
        ease 1 zoom 1.5 xoffset 500 yoffset 50

    # Personaje principal inicia su diálogo.
    anon_n "¡Finalmente, después de 6 años, soy libre!"
    anon_n "¡Había estado esperando por este momento!"

    #contexto "Contexto: \n{i}Observando a lo lejos{/i}"

    anon_n "¡Dios, ya sabía acerca de esto, pero verlo en persona va más allá de mi imaginación!"

    scene bg zombies
    #contexto "Contexto: \n{i}Se acerca una horda de infectados{/i}"
    scene bg norte_sur
    menu:
        "¿Hacia dónde debería correr?"
        "Correr hacia el norte":
            jump ir_al_norte
        "Correr hacia el sur":
            jump ir_al_sur

    label ir_al_norte:
        # Bad ending
        texto_centrado "{i}Los guardias suponían que escaparía por el norte{/i}"
        extend "{p}{i}No logró llegar muy lejos y quedó rodeado de guardias{/i}"
        texto_centrado "{i}Prefirió entregarse y volver a prisión{/i}"
        "Bad Ending."
        return

    label ir_al_sur:
        scene bg boat

        #contexto "Contexto: \n{i}Llega a un pequeño muelle...{/i}"
        show lancha agua:
            ease 1 zoom 1.0 xoffset 300 yoffset 300

        anon_n "¡Perfecto, esto me será útil!"

        #contexto "Contexto: \n{i}Encuentra una lancha{/i}"

        menu:
            "¿Debería revisar las provisiones?"
            "Revisar ahora provisiones y nivel de combustible":
                jump revisar_provisiones
            "Revisar mas tarde":
                # Bad Ending
                contexto "Contexto: \n{i}Se sube a una lancha y arranca{/i}"
                anon_n "¡Hasta nunca, Idiotas!"
                contexto "Contexto: \n{i}se aleja en la lancha{/i}"
                texto_centrado "{i}No las revisa y se adentra en altamar{p}Al tercer día se queda sin provisiones{p}{/i}"
                texto_centrado "{i}Una semana después muere por el hambre y la insolación{/i}"
                "Bad Ending."
                return

    label revisar_provisiones:
        "Con esto podré vivir algunos días más"

        #contexto "Contexto: \n{i}Se sube a una lancha y arranca{/i}"

        anon_n "¡Hasta nunca, Idiotas!"

        #contexto "Contexto: \n{i}se aleja en la lancha{/i}"

        texto_centrado "{i}2 Días después...{/i}"

        menu:
            "El combustible esta empezando a escasear"
            "Aumentar Velocidad":
                # Bad ending
                texto_centrado "{i}Acelera la velocidad y queda sin combustible en altamar{/i}"
                texto_centrado "{i}Días después muere por falta de provisiones{/i}"
                "Bad Ending."
                return
            "Disminuir Velocidad":
                contexto "Contexto: \n{i}Observa un objeto a cierta distancia en el oceano...{/i}"
                # contexto "Contexto: \n{i}{/i}"
                menu:
                    "¿Pero qué es eso?, ¿será posible...?"
                    "Acercarse a examinar":
                        contexto "Contexto: \n{i}Apenas logra distinguir lo que parece una persona que él conocía...{/i}"
                        menu:
                            "¿Y este como logró llegar hasta aquí?"
                            "Rescatarlo":
                                contexto "{i}Rescata a una persona que flotaba aún con vida en el mar...{/i}"
                                contexto "{i}Algunos minutos después el naufrago despierta...{/i}"
                                show harrison one:
                                    ease .5 zoom 1.5 xoffset 700 yoffset 50
                                naufrago "¡No es posible! ¡¿{b}Ignacio Villanueva{/b}?!"
                                naufrago "¡Maldito Bastardo!"
                                show fugitive one:
                                    ease .5 zoom 1.5 xoffset 200 yoffset 50
                                anon_n "¡Es Don Nacho para tí!"
                                contexto "{i}Le da un puñetazo que lo hace caer{/i}"
                                naufrago "¡Me rompiste la nariz!"
                                narco "¡No exageres!, además, ¿quién se supone que eres tú?"
                                naufrago "¿Nunca has oido de mi?, Yo soy el gran {b}Robert \"Bobby\" Harrison{/b}"
                                narco "Ah, el loco de los barcos gigantes"
                                empresario "Prefiero el termino \"Excentrico\"... "
                                empresario "¡Hey!, ¿no se supone que deberías estar en prisión o algo?"
                                narco "Los tiempos han cambiado mi amigo, dime, ¿cómo es que alguien como tú terminó este lugar?"

                                empresario "Bueno..."
                                empresario "En verdad es algo vergonzoso de admitir..."
                                empresario "Pero como tú ya sabrás, hace 6 años cuando condenaste al mundo a este apocalipsis zombie, o algo así..."
                                narco "¡Que soy inocente maldita sea, y siempre lo he sido!"
                                empresario "Como sea, me di la tarea de intentar salvar la mayor cantidad de vidas posibles"
                                empresario "Construyendo una flota de super cruceros o ciudades flotantes como me gusta llamarlas a mí"
                                empresario "En donde la humanidad podría vivir tranquila y sin tener que preocuparse por esos infectados"
                                empresario "Pues es más que obvio que alguno de ellos jamás aparecería en medio del mar ..."

                                # Segunda parte
                                narco "¡Ve al grano de una vez y ya!"
                                empresario "Vaya tipo más impaciente, en fin, hace poco realizamos en mi crucero personal una gran celebración"
                                empresario "Debí de haber bebido mucho alcohol porque lo último que recuerdo es que estaba sentando en una baranda cantando"
                                empresario "Quizá perdí el equilibrio lo que llevó a que me cayera al mar"
                                narco "..."
                                narco "¿Aún tienen alcohol despues de todos estos años?"
                                empresario "Eh..."
                                empresario "Cambiando de tema, necesito regresar a mi barco así que voy a necesitar un aventón"
                                empresario "¿Qué me dices?, ¿podrías ayudarme a volver?"
                                empresario "Sería por unos buenos billetes o si lo prefieres puedo conseguirte una de las mejores habitaciones en mi barco"
                                empresario "¿Qué te parece?"
                                narco "Veo que ustedes los {i}snobs{/i} nunca salen de sus burbujas"
                                narco "Primero, el dinero en esta era no es nada más que un simple papel sin valor"
                                narco "Segundo, no tengo ni la menor idea en dónde pueda estar tu susodicho crucero y creo que tú tampoco"
                                narco "Y tercero, ahora que estás aquí, tanto mis provisiones como el combustible de esta lancha estan al mínimo"
                                narco "así que a menos que encontremos algo para reabastecernos, dudo que lleguemos con vida a la próxima semana"
                                empresario "..."

                                texto_centrado "Esa misma noche..."
                                contexto "Una feroz tormenta en altamar"
                                empresario "¡¡Vamos a morir!!"
                                narco "¡Cierra el hocico y sujétate de algo, no he llegado tan lejos solo para terminar muriendo por una maldita tormenta!"
                                narco "Como si algo como esto pudiera detenerme"
                                contexto "Una enorme ola está por golpear la lancha"
                                empresario "¡Gira!, ¡¡GIRA!!"
                                contexto "La ola hunde la lancha"

                                contexto "Contexto: Llegan a una playa pequeña"

                                # Tercera parte
                                empresario "Cómo me duele la cabeza"
                                empresario "Hmm... ¿en dónde está ese sujeto?"
                                contexto "Don Nacho a lo lejos observando hacia el horizonte"
                                narco "¿Sigues con vida, eh?"
                                empresario "¿Alguna idea de dónde estamos?"
                                narco "Colombia"
                                empresario "¿Y cómo lo sabes?"
                                narco "¿Ves ese lugar al otro lado del mar?"
                                narco "ese lugar es Puerto Bolivar, lo sé porque era uno de los puertos que solía usar en mi ruta de tráfico"
                                empresario "¿Y ahora qué?"
                                narco "Hay que ir para allá, pues de seguro debe haber comida o herramientas que nos puedan ser de utilidad"
                                menu:
                                    "Ir por Tierra":
                                        # Bad Ending
                                        "Se mueren"
                                        "Bad ending"
                                        return
                                    "Ir por Mar":
                                        contexto "Don Nacho se tira al mar"
                                        empresario "¿Qué estas haciendo?"
                                        narco "Es más seguro ir nadando hasta allí que ir por tierra, a menos que te quieras encontrar con algún infectado"
                                        empresario "¿Acaso no podemos ir en un bote o algo?"
                                        narco "Parece que no tenemos una embarcación ..."
                                        narco "Por si no lo has notado, la tormenta no solo hundió la lancha"
                                        narco "También se llevó las pocas provisiones que iban quedando, así que no hay de otra"
                                        narco "Pero si prefieres quedarte aquí, es cosa tuya"
                                        empresario "¡Espera un momento!"
                                        narco "¿Ahora qué quieres?, ¿acaso no sabes nadar?"
                                        empresario "¡Pues claro que si sé!"
                                        narco "¿Entonces...?"
                                        empresario "¡Al demonio con esto!"
                                        contexto "Harrison se lanza al mar"
                                        contexto "Ambos hombres comienzan a nadar en dirección a Puerto Bolivar"
                                        texto_centrado "Horas más tarde..."
                                        contexto "Puerto Bolivar, tras haber estado buscando por provisiones y herramientas por horas"
                                        empresario "¡Encontré algo!, ¡ayúdame a levantar esto!"
                                        narco "Vaya vaya, con que aquí se escondía"
                                        scene bg bodega
                                        show harrison one:
                                            ease .5 zoom 1.5 xoffset 700 yoffset 50
                                        show fugitive one:
                                            ease .5 zoom 1.5 xoffset 200 yoffset 50
                                        empresario "¿Sabes lo que es?"
                                        narco "La entrada secreta a una bodega subterránea que solían usar mis hombres en el pasado"
                                        narco "De seguro puede que aún deban haber algunos objetos interesantes allí dentro"
                                        empresario "Realmente está oscuro aquí"
                                        menu:
                                            "Usar una linterna":
                                                narco "Este lugar tiene demasiado olor a metano"
                                                narco  "¡Y con razón, estas latas de gas están rotas!"
                                                empresario "¡Tomemos lo que podamos y largémonos!"
                                                narco "¡No, es mejor revisarlo todo primero para después no tener que terminar cargando peso muerto!"

                                                $ items = 6
                                                while items:
                                                    $ items -= 1
                                                    menu:
                                                        set items_bodega
                                                        "Revisar cajas de madera":
                                                            texto_centrado "Alimentos en conserva y otras provisiones encontradas"
                                                        "Revisar cajas de carton":
                                                            texto_centrado "Botiquines y medicinas encontradas"
                                                        "Revisar pequeña caja de metal":
                                                            texto_centrado "Pistolas 9mm encontradas"
                                                            if "Revisar pequeño cilindro de metal" in items_bodega:
                                                                narco "¡Ahora si, con esto mejora nuestra suerte!"
                                                            else:
                                                                empresario "Muy lindo pero... ¿dónde estan las balas?"
                                                        "Revisar caja de plastico":
                                                            texto_centrado "Cuchillos encontrados"
                                                        "Revisar pequeño cilindro de metal":
                                                            texto_centrado "15 balas encontradas"
                                                            if "Revisar pequeña caja de metal" not in items_bodega:
                                                                empresario "¿Balas? ¡perfecto, sólo faltan las armas!"
                                                            else:
                                                                narco "No son muchas, pero aun asi servirán"
                                                        "Revisar hielera":
                                                            texto_centrado "Agua embotellada encontrada"

                                                narco "Con esto sera suficiente"
                                                empresario "Bien, mejor que nos largemos cuanto antes de aquí, este lugar me eseta dando escalofríos"
                                                narco "Primero hay que encontrar algún vehículo, sino dudo que podamos salir intactos de esta zona"
                                                contexto "Una horda de infectados se esta acercando al área"
                                                empresario "Ya anocheció"
                                                narco "¡Hay que andar con cautela, si hay infectados cerca, estamos bien jodidos, esos bastardos son más letales en la oscuridad!"
                                                contexto "Ambos hombres salen de la bodega"
                                                empresario "¡Oh,no! ¡Mira hacia allá, infectados!"
                                                scene bg zombies
                                                narco "Espera, no saben que nos encontramos aquí... Aun..."
                                                empresario "¡¡Estamos perdidos!!, ¡es nuestro fin!"
                                                scene black
                                                texto_centrado "Continuará...{p}(sólo si ganamos la DevJam ;) )"
                                                "Good Ending."
                                            "Usar un encendedor":
                                                # Bad Ending
                                                "Explotan"
                                                "Bad Ending"
                                                return
                            "Dejarlo a su suerte":
                                # Bad ending
                                texto_centrado "{i}Al alejarse se dió cuenta que iba directo a un huracán..."
                                extend "{p}Intentó saltar, pero fue peor, murió ahogado y su cuerpo fue arrastrado por el huracán.{/i}"
                                "Bad Ending."
                                return
                    "Seguir otro rumbo":
                        # Bad ending
                        texto_centrado "{i}Terminó llegando a tierra firme y se dió cuenta que había vuelto al punto de inicio...{/i}"
                        texto_centrado "{i}Rápidamente fue descubierto por uno de los guardias que disparó sin dudar{/i}"
                        texto_centrado "{i}No logró llegar muy lejos, fue capturado y llevado a otra penitenciaría.{/i}"
                        "Bad Ending."
                        return

    # Se acaba el juego.
    "{b}Fin de la demo 0.1{/b}"
    return