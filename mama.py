import streamlit as st
import time

# --- Configuración de la Página ---
st.set_page_config(
    page_title="¡Feliz Día, Mamá!",
    page_icon="💖",
    layout="centered", # o "wide"
    initial_sidebar_state="expanded" # O "collapsed"
)

# --- Funciones Auxiliares para Emojis y Pausas ---
def mostrar_mensaje(texto, pausa=1.5):
    """Muestra un texto y espera un momento."""
    st.write(texto)
    time.sleep(pausa)

# --- Título y Mensaje Inicial ---
st.title("💖 ¡Feliz Día de la Madre! 💖")
st.header("Para la mujer más especial del mundo...")

# --- Sidebar con la Foto ---
with st.sidebar:
    st.image("mama_foto.jpg", caption="¡Mi Mamá, mi todo!", use_container_width=True) 
    st.write("---")
    st.write("Un regalo de tu pollito más grande 🥰")

# --- Contenido Principal ---
st.write("---")

# 1. Bienvenida Especial
if 'etapa' not in st.session_state:
    st.session_state.etapa = 0
    st.session_state.mate_intento = 0 # Para el juego del mate

if st.session_state.etapa == 0:
    st.write("¡Hola Mamá! 🎉 Hoy celebramos a la mejor, con la mejor banda sonora. 🎶")
    st.write("Preparate para un 'Matetour' especial, lleno de **Azul y Mar** y mucha música... ¡Vamos a jugar un rato! 😉")
    if st.button("Empezar la celebración ✨"):
        st.session_state.etapa = 1
        st.rerun()

elif st.session_state.etapa == 1:
    # 2. La Academia y el Mar
    st.write("---")
    st.write("Tu corazón es **Azul** como el mar que tanto adoras, y **Blanco** como la espuma de la ola. 🌊")
    st.write("Pero tu pasión más grande está en el Cilindro... ¡La dueña del sentimiento **Académico**, siempre de **Racing Club**! 💙🤍")
    st.write("El mar puede ser inmenso, pero mi amor por vos es más grande. ¡Infinito! ✨")
    if st.button("¿Lista para el mate? 🧉"):
        st.session_state.etapa = 2
        st.rerun()

elif st.session_state.etapa == 2:
    # 3. Desafío del Mate Ajustado (Iterativo)
    st.write("---")
    st.write("Es la hora sagrada del mate. Yo me ofrezco a cebar, pero necesito tu crítica honesta. 😉")
    
    # 1. Mostrar el intento actual de mate
    if st.session_state.mate_intento == 0:
        st.session_state.mate_intento = 1
    
    st.subheader(f"Mate #{st.session_state.mate_intento}:")
    st.write(f"Cebo el mate número {st.session_state.mate_intento}... 🧉")
    time.sleep(0.5) # Pausa visual ligera

    # 2. Pregunta interactiva para el mate
    respuesta_mate = st.radio(
        "¿Cómo está el agua en este mate? 🤔",
        ('Frío', 'Caliente', 'Perfecto'),
        key=f"radio_mate_{st.session_state.mate_intento}" # Clave única por intento
    )
    
    # Inicializamos las variables para el feedback
    mensaje_madre = None
    texto_boton = None
    siguiente_etapa = None
    
    # 3. Determinar el mensaje de la madre
    if "Frío" in respuesta_mate:
        mensaje_madre = "🥶 Ah, dirías: 'Le falta un grado al agua'. ¡Tenés toda la razón! Y bueno, se me pasó."
    elif "Caliente" in respuesta_mate:
        mensaje_madre = "😬 Uhm, dirías: 'Ay, estás tomando matecocido'. se te paso algunos grados."
    elif "Perfecto" in respuesta_mate:
        mensaje_madre = "🤩 ¡Wow! ¡Un mate perfecto! ✨"

    # 4. Lógica para la acción del botón (Intento 1 o 2)
    if st.session_state.mate_intento < 3:
        if "Perfecto" in respuesta_mate:
            texto_boton = f"Cebar el {['segundo', 'tercer'][st.session_state.mate_intento-1]} mate"
        else:
            texto_boton = "Cebar el siguiente mate ☕"
        
        siguiente_etapa = st.session_state.mate_intento + 1

    # 5. Lógica para el intento 3 (Finaliza el juego del mate)
    elif st.session_state.mate_intento == 3:
        st.write(mensaje_madre) # Mostramos su mensaje final

        if "Perfecto" in respuesta_mate:
            # Si el tercer mate es perfecto, pasamos a la siguiente etapa de la app
            st.session_state.etapa = 3
            st.rerun()
            
        # Lógica final del termo si no fue perfecto el intento 3
        st.write("Ya tomamos los 3 reglamentarios... ¿Finalizamos el termo porque estaban muy ricos? 🤔")
        terminar_termo = st.radio(
            "Tu veredicto final: ",
            ('Sí, el termo está vacío', 'No, que quede para después'),
            key="final_termo"
        )
        if terminar_termo:
            if "Sí" in terminar_termo:
                st.write("🎉 ¡Eso es un éxito matero! El termo vacío es la mejor aprobación. ¡Gracias por la paciencia! 😉")
            else:
                st.write("😄 Bueno, al menos cumplimos la regla de los 3 mates ricos.")
            
            if st.button("¡Continuemos la celebración! 🥳"):
                st.session_state.etapa = 3
                st.rerun()
        
        # CORRECCIÓN FINAL: Usamos st.stop() para detener la ejecución y evitar el error de return.
        st.stop() 

    # 6. Mostrar el mensaje de la madre y el botón de acción (solo para intentos 1 y 2)
    if mensaje_madre and st.session_state.mate_intento < 3:
        st.write(mensaje_madre) # Muestra el feedback después de la pregunta

        if texto_boton:
            if st.button(texto_boton):
                st.session_state.mate_intento = siguiente_etapa # Avanzamos el contador de mate
                st.rerun() 

elif st.session_state.etapa == 3:
    # 4. Momento de Cultura Pop y Música
    st.write("---")
    st.write("Dejemos el mate y pasemos al entretenimiento... ¡tus verdaderas pasiones! 🎤💃")
    st.write("Sé que si en la radio suena una canción de **Ricky Martin** o **Carlos Rivera**, el volumen sube a tope. 🔊 ¡Fanclub presente desde casa! ✨")
    
    st.write("Pero si hablamos de películas...")
    st.write("Para vos, no hay demonio ni ángel que se resista. ¡El mismísimo **Constantine** nos enseña que el amor de mamá es la mejor protección! 😈😇")

    st.write("---")
    st.subheader("🎵 Una canción para vos, Mamá 🎵")
    st.write("Como sé que te encanta la música, te dejo un tema que encontré para vos. ¡Espero que te guste! 👇")
    
    # Para este ejemplo, usaremos un audio de stock o una URL de ejemplo si no tienes un mp3 directo
    try:
        st.audio("audio_mama.mp3", format="audio/mp3", start_time=0) # Asegúrate de tener "audio_mama.mp3" en tu carpeta
        st.write("**(te sorprendi ¿cierto?)**")
    except FileNotFoundError:
        st.warning("No se encontró el archivo de audio 'audio_mama.mp3'. Si quieres, puedes subirlo a la misma carpeta.")
        st.write("Mientras tanto, te invito a escuchar 'La Mujer Perfecta' de Carlos Rivera en tu reproductor favorito. ¡Pura emoción! ❤️")

    if st.button("El mensaje final... 💌"):
        st.session_state.etapa = 4
        st.rerun()

elif st.session_state.etapa == 4:
    # 5. Mensaje Final
    st.write("---")
    st.balloons() # ¡Globos de celebración!
    st.write("Mamá, con tus gustos, tus frases y tu inmensa dedicación...")
    st.write("### **Sos la mujer más especial y linda del mundo.**")
    st.write("Te amo con todo mi ser y te admiro por ser quien sos. ¡Gracias por tanto! ✨")
    st.write("\n\n## 💙🤍 ¡Feliz Día de la Madre! 🤍💙")
    st.write("---")
    st.write("Mamá, Si pudiera resumir en una sola palabra lo que siento al escribirte, sería admiración. Pero una palabra se queda cortísima, como una tribuna vacía.") 
    st.write("Sé que has pasado por esas tempestades de la vida, esas rachas bravas que te revuelven por dentro y que, a veces, duelen más que un gol anulado en el último minuto. Hemos visto tu barco zarandearse, y hemos sentido el frío del miedo. Pero, ¿sabes qué es lo increíble? Siempre, siempre, encontraste la forma de enderezarlo. Te pusiste al mando, firme, como la capitana que eres.")
    st.write("Y es que vos sos así. Tenés la fuerza inagotable del mar que tanto amás. Te golpean las olas y, en lugar de romperte, te haces más fuerte, más profunda, más inmensa. Cuando pienso en la calma que transmitís después de la tormenta, me imagino la inmensidad del océano al amanecer, con esa paz que lo cura todo.")
    st.write("También te miro y veo a la hinchada más fiel, la que nunca abandona. Sos nuestra Academia personificada: la que aguanta, la que lucha con garra, la que celebra la victoria con un amor que te desborda. Cuando el partido se pone difícil, cuando hay que meter, ahí estás vos, bancando, con ese corazón que late Celeste y Blanco por la vida y por los tuyos. No conozco a nadie más resiliente, ni con un amor tan incondicional.")
    st.write("Y por nosotros. Gracias por hacer de cada uno de nosotros un puerto seguro. Aunque seamos distintos, aunque cada uno traiga su propia marea, vos tenés una bandera izada para recibirnos. No importa qué tan lejos estemos o qué tan difícil la estemos pasando, tu amor es el ancla que nos mantiene a flote.")
    st.write("Quería que esta carta fuera sincera, de verdad. Y la verdad es que sos humana. Has llorado, has dudado, te has cansado. Te hemos visto. Y precisamente ahí, en esa vulnerabilidad, es donde reside tu grandeza más hermosa. No sos un robot de perfección, sos una mujer de carne y hueso que se levanta y vuelve a empezar, mil veces si hace falta, sin rendirse.")
    st.write("Sos nuestra roca, nuestro refugio, nuestro faro. Y sí, sos todo. Sos el primer sol en la mañana, la fuerza al mediodía y la paz al anochecer.")
    st.write("Hoy, simplemente quiero decirte que no estás sola. Que te merecés toda la calma del mar y toda la gloria del Cilindro.")
    st.write("Te quiero con toda el alma.")
    st.write("Con amor, tu hija. 🥰")
    
    if st.button("Volver a empezar (por si quieres jugar de nuevo)"):
        st.session_state.etapa = 0
        st.session_state.mate_intento = 0
        st.rerun()