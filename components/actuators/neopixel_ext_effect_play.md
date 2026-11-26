---
id: neopixel_ext_effect_play
blockCategory: Lichter
component: neopixel_strip
subCategory: "Streifen"
label: "✨ Streifen-Effekt abspielen"
label_en: "✨ Play strip effect"
colour: "#EC4899"
tooltip: "Spielt einen LED-Effekt einige Male ab, danach geht der Streifen aus. Das Programm läuft dabei weiter."
tooltip_en: "Plays an LED effect a few times, then the strip turns off. The program keeps running meanwhile."
blockType: statement
inline: false
inputs:
  - label: "abspielen"
    label_en: "play"
    name: EFFECT
    fieldType: options_dropdown
    options:
      - label: "Komet"
        label_en: "Comet"
        value: "komet"
      - label: "Lauflicht"
        label_en: "Chase"
        value: "lauflicht"
      - label: "Blinken"
        label_en: "Blink"
        value: "blinken"
      - label: "Pulsieren"
        label_en: "Pulse"
        value: "pulsieren"
      - label: "Regenbogen"
        label_en: "Rainbow"
        value: "regenbogen"
  - label: "Port:"
    label_en: "port:"
    name: PORT
    fieldType: grove_dropdown
    groveRole: strip
  - label: "Farbe:"
    label_en: "colour:"
    name: COLOR
    fieldType: colour_picker
    default: "#ff0000"
    newRow: true
  - label: "Tempo:"
    label_en: "speed:"
    name: SPEED
    fieldType: options_dropdown
    options:
      - label: "schnell"
        label_en: "fast"
        value: "3"
      - label: "sehr schnell"
        label_en: "very fast"
        value: "4"
      - label: "mittel"
        label_en: "medium"
        value: "2"
      - label: "langsam"
        label_en: "slow"
        value: "1"
valueInputs:
  - name: COUNT
    label: "LEDs gesamt"
    label_en: "total LEDs"
    check: Number
    defaultValue: 20
  - name: TIMES
    label: "wie oft (mal)"
    label_en: "repeat (times)"
    check: Number
    defaultValue: 2
hardware:
  commonName: "NeoPixel-Streifen (extern) / WS2812B"
  verbrauch3j: 0
  kitStandard: false
legacyGenerator: true
---

# LED-Streifen – Effekt abspielen

Startet einen Effekt (Komet, Lauflicht, Blinken, Pulsieren oder Regenbogen). Nach der gewählten Anzahl geht der Streifen aus.
Der Block wartet nicht: Das Programm läuft sofort weiter, und mehrere Streifen können gleichzeitig leuchten.
Läuft derselbe Effekt schon, fängt er nicht von vorne an. Regenbogen benutzt seine eigenen Farben.

Braucht `led_effekte.py` und `adafruit_led_animation` auf dem Board („Libs prüfen“).

<!-- lang:en -->

# LED strip – play effect

Starts an effect (comet, chase, blink, pulse or rainbow). After the chosen number of times the strip turns off.
The block does not wait: the program continues right away, and several strips can light up at the same time.
If the same effect is already running, it does not start over. Rainbow uses its own colours.

Needs `led_effekte.py` and `adafruit_led_animation` on the board (“Check libs”).
