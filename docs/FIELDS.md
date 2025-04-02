## 📋 Übersicht: UI-Felder für `get_X_field`-Methoden

Diese Tabelle zeigt alle geplanten oder möglichen UI-Felder, die sich gut in das modulare Event-basierte System von StudyFrog integrieren lassen.

### 🔤 Textfelder

| Methode                         | Typ              | Beschreibung                                | Spezialfunktionen                                   |
|----------------------------------|------------------|---------------------------------------------|-----------------------------------------------------|
| `get_single_line_text_field`   | `Entry`          | Einzeilige Texteingabe                       | Validierung, Placeholder, max Länge                |
| `get_multi_line_text_field`    | `Text`           | Mehrzeilige Texteingabe                     | Scrollbar, Formatierung, Auto-Resize               |
| `get_password_field`           | `Entry`          | Maskierte Texteingabe (Passwort)            | `show="*"`, Sichtbarkeit umschaltbar               |

---

### 🔘 Auswahlfelder

| Methode                            | Typ                     | Beschreibung                             | Spezialfunktionen                                   |
|-----------------------------------|--------------------------|------------------------------------------|-----------------------------------------------------|
| `get_radiobutton_field_group`    | `Radiobutton`            | Auswahl **einer** Option                 | Horizontal/Vertikal, dynamisch erzeugbar            |
| `get_combobox_field`             | `Combobox`               | Auswahl aus Dropdown                     | Clear-Button, freie Eingabe optional                |
| `get_listbox_field`              | `Listbox`                | Auswahl mehrerer Elemente                | `single`, `multiple`, Scrollbar                     |
| `get_checkbutton_field_group`    | `Checkbutton`            | Auswahl mehrerer Optionen                | Callback, Selektion erzwingen (`single`-Modus)      |

---

### 🌺 Numerische Felder

| Methode                         | Typ              | Beschreibung                                | Spezialfunktionen                                |
|----------------------------------|------------------|---------------------------------------------|--------------------------------------------------|
| `get_scale_field`              | `Scale (int)`    | Schieberegler für Ganzzahlen                | Min/Max, Live-Update                             |
| `get_float_scale_field`        | `Scale (float)`  | Schieberegler für Kommazahlen               | z. B. Schrittweite 0.1                           |
| `get_spinbox_field`            | `Spinbox`        | Inkrementelle Auswahl per Klick             | Min/Max, int/float                               |
| `get_slider_field_group`       | `Frame`          | Kombination mehrerer Skalen                 | z. B. zur Bewertung                              |

---

### 🗖 Datum/Zeit

| Methode                          | Typ               | Beschreibung                                | Spezialfunktionen                                |
|----------------------------------|-------------------|---------------------------------------------|--------------------------------------------------|
| `get_date_picker_field`         | `Custom`          | Datumsauswahl mit Kalender                  | Nutzung von `tkcalendar` o. ä. möglich           |
| `get_time_picker_field`         | `Custom`          | Uhrzeit-Auswahl                             | Dropdown oder manuelle Eingabe                   |
| `get_datetime_field`            | `Custom`          | Kombination aus Datum + Zeit                | Modular aus Picker-Methoden zusammensetzbar      |

---

### ⏱️ Zeit-/Timer-Felder

| Methode                          | Typ               | Beschreibung                                | Spezialfunktionen                                |
|----------------------------------|-------------------|---------------------------------------------|--------------------------------------------------|
| `get_countdown_timer_field`     | `Custom`          | Countdown mit visueller Anzeige             | Integriert in Speed-Test-Session                 |
| `get_countup_timer_field`       | `Custom`          | Timer ab 0, z. B. für Daueranzeige          | Start/Stop möglich                               |
| `get_duration_field`            | `Slider/Spinbox`  | Feste Dauer wählen (z. B. 5–120 min)        | Kombinierbar mit Session-Planung                 |

---

### 🎨 Spezialfelder

| Methode                          | Typ               | Beschreibung                                | Spezialfunktionen                                |
|----------------------------------|-------------------|---------------------------------------------|--------------------------------------------------|
| `get_color_picker_field`        | `Custom`          | Farbwahl über Dialog                        | Hex/RGB-Ausgabe, Farbvorschau                    |
| `get_file_picker_field`         | `askopenfilename` | Auswahl einer Datei                         | Dateifilter, Pfadanzeige                         |
| `get_directory_picker_field`    | `askdirectory`    | Auswahl eines Ordners                       | Pfadanzeige, Validierung                         |
| `get_toggle_switch_field`       | `Custom`          | Toggle im Stil eines modernen Switches      | ttk.Style oder Canvas-Design                     |
| `get_rating_field`              | `Custom`          | Sterne/Emoji-Bewertung                      | z. B. 1–5 Sterne, Emojis oder Farben             |

---

### 💡 Erweiterte/Komplexe Felder

| Methode                          | Typ               | Beschreibung                                | Spezialfunktionen                                |
|----------------------------------|-------------------|---------------------------------------------|--------------------------------------------------|
| `get_tag_selector_field`        | `Entry + Tags`    | Tags hinzufügen, entfernen, vorschlagen     | Autocomplete, frei oder vorgegeben               |
| `get_object_reference_field`    | `Combobox + ID`   | Auswahl eines Objekts im System             | Verknüpfung zu `Flashcard`, `Stack`, etc.        |
| `get_progress_field`            | `Progressbar`     | Visualisierung des Fortschritts             | `determinate` oder `indeterminate`              |

---

### ↺ Sonstiges

| Methode                          | Typ               | Beschreibung                                | Spezialfunktionen                                |
|----------------------------------|-------------------|---------------------------------------------|--------------------------------------------------|
| `get_boolean_field`             | `Checkbutton`     | Alias für ja/nein-Felder                    | ggf. stilistisch als Switch                      |
| `get_readonly_field`            | `Label/Entry`     | Zeigt Werte an, aber keine Eingabe          | Ideal für Infoanzeigen                           |
| `get_json_field`                | `Text (JSON)`     | Bearbeitung komplexer strukturierter Daten  | JSON-Formatierung + Validierung                  |

