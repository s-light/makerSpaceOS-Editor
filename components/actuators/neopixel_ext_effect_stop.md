---
id: neopixel_ext_effect_stop
blockCategory: Lichter
component: neopixel_strip
subCategory: "Streifen"
label: "✨ Streifen-Effekt stoppen"
label_en: "✨ Stop strip effect"
colour: "#EC4899"
tooltip: "Beendet den Effekt auf dem LED-Streifen und schaltet ihn aus."
tooltip_en: "Ends the effect on the LED strip and turns it off."
blockType: statement
inline: true
inputs:
  - label: "Effekt stoppen  Port:"
    label_en: "stop effect  port:"
    name: PORT
    fieldType: grove_dropdown
    groveRole: strip
valueInputs:
  - name: COUNT
    label: "LEDs gesamt"
    label_en: "total LEDs"
    check: Number
    defaultValue: 20
hardware:
  commonName: "NeoPixel-Streifen (extern) / WS2812B"
  verbrauch3j: 0
  kitStandard: false
legacyGenerator: true
---

# LED-Streifen – Effekt stoppen

Beendet den laufenden Effekt und schaltet den Streifen aus.

<!-- lang:en -->

# LED strip – stop effect

Ends the running effect and turns the strip off.
