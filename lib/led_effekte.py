# led_effekte.py – LED-Effekte für NeoPixel-Streifen (makerSpaceOS)
#
# Dünne Hülle um adafruit_led_animation: Ein gestarteter Effekt läuft im
# Hintergrund, während das Programm weitermacht. Mehrere Streifen laufen
# gleichzeitig, je Streifen höchstens ein Effekt.
#
# Muss nach CIRCUITPY/lib/ kopiert werden, zusammen mit adafruit_led_animation/.
#
# Verwendung (so erzeugt der Generator den Code):
#   from led_effekte import effekte_einrichten, effekt_start, effekt_stopp
#   effekte_einrichten()                                   # einmal je Programm
#   effekt_start(_npx_GP14, "komet", (128, 0, 255), 3, 2)  # Tempo 1–4, 2 mal
#   effekt_start(_npx_GP15, "regenbogen", (0, 0, 0), 2)    # endlos
#   effekt_stopp(_npx_GP14)
import asyncio

from makerspaceos import immer, im_hintergrund

_laufend = {}  # id(streifen) -> (einstellung, animation, anzahl)

# Tempo 1 (langsam) … 4 (sehr schnell)
_SCHRITT = (0.1, 0.05, 0.02, 0.01)   # Komet, Lauflicht: Sekunden je Schritt
_BLINKEN = (1.0, 0.5, 0.25, 0.1)     # Sekunden an bzw. aus
_PERIODE = (5, 3, 1.5, 0.8)          # Pulsieren, Regenbogen: Sekunden je Runde


# Die Effekte werden erst bei Bedarf geladen – spart Speicher auf dem Board.
def _neu(streifen, art, farbe, tempo):
    stufe = min(max(int(tempo), 1), 4) - 1
    if art == "komet":
        from adafruit_led_animation.animation.comet import Comet
        return Comet(streifen, _SCHRITT[stufe], farbe,
                     tail_length=max(2, len(streifen) // 2))
    if art == "lauflicht":
        from adafruit_led_animation.animation.chase import Chase
        return Chase(streifen, _SCHRITT[stufe] * 2, farbe, size=2, spacing=3)
    if art == "blinken":
        from adafruit_led_animation.animation.blink import Blink
        return Blink(streifen, _BLINKEN[stufe], farbe)
    if art == "pulsieren":
        from adafruit_led_animation.animation.pulse import Pulse
        return Pulse(streifen, 0.02, farbe, period=_PERIODE[stufe])
    if art == "regenbogen":
        from adafruit_led_animation.animation.rainbow import Rainbow
        # step so wählen, dass der ganze Regenbogen auf den Streifen passt
        return Rainbow(streifen, 0.02, period=_PERIODE[stufe],
                       step=max(1, 256 // len(streifen)))
    raise ValueError("Unbekannter Effekt: " + art)


def effekt_start(streifen, art, farbe, tempo, anzahl=None):
    """Startet einen Effekt (anzahl=None: endlos).

    Läuft auf dem Streifen schon genau dieser Effekt, passiert nichts – so
    fängt er in FÜR IMMER oder bei erneutem Tastendruck nicht von vorne an.
    """
    if anzahl is not None and anzahl < 1:
        effekt_stopp(streifen)
        return
    einstellung = (art, farbe, tempo, anzahl)
    alt = _laufend.get(id(streifen))
    if alt and alt[0] == einstellung:
        return
    streifen.fill((0, 0, 0))
    _laufend[id(streifen)] = (einstellung, _neu(streifen, art, farbe, tempo), anzahl)


def effekt_stopp(streifen):
    """Beendet den Effekt und schaltet den Streifen aus."""
    _laufend.pop(id(streifen), None)
    streifen.fill((0, 0, 0))
    streifen.show()


async def _abspielen():
    while True:
        for _, animation, anzahl in list(_laufend.values()):
            animation.animate()
            if anzahl is not None and animation.cycle_count >= anzahl:
                effekt_stopp(animation.pixel_object)
        await asyncio.sleep(0.005)


async def _wach_bleiben():
    await asyncio.sleep(1)


def effekte_einrichten():
    """Einmal pro Programmlauf aufrufen (macht der erzeugte Code)."""
    _laufend.clear()  # Modul bleibt zwischen zwei Läufen geladen
    im_hintergrund(_abspielen)  # läuft auch schon während BEIM START
    immer(_wach_bleiben)  # Programm nicht beenden, solange Effekte laufen können
