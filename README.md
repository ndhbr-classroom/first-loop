# Aufgabe 2: Erste Schleife
An diesem Zeitpunkt hast du deine erste Aufgabe bereits erledigt. Du hast also schon dein erstes Python-Programm geschrieben. In dieser Aufgabe werden wir die Funktionsweisen von einfachen `for`-Schleifen kennenlernen.

Eine Python `for`-Schleife ist eine Kontrollstruktur, mit der man eine Gruppe von Anweisungen in einem Block der `for`-Schleife mit einer bestimmten Anzahl von Wiederholungen bzw. Listen-Argumenten ausführen kann.

Wir wollen nun beispielsweise folgende Ausgabe erreichen:
```
Andreas 0
Andreas 1
Andreas 2
Andreas 3
Andreas 4
```

Dies machen wir mithilfe einer `for`-Schleife. Das heißt wir schreiben nicht explizit fünf mal ein `print("Andreas n")`. Wir benötigen nur einen einzigen Aufruf von `print()`, welcher schließlich im `for`-Block ist und deshalb n-mal ausgeführt wird. Soll etwas wiederholt ausgeführt werden, sind Schleifen nämlich ein gutes Mittel, Schreibarbeit zu sparen.

## Schritt 1: for-Schleife
`for`-Schleifen bestehen aus vier Teilen.
- Teil 1: Das Keyword `for`
- Teil 2: Die Variable
- Teil 3: Das Keyword `in`
- Teil 4: Der Bereich (Runde oder Sequenz)

### Variable
Die `for`-Schleife beginnt offensichtlich immer mit dem Keyword `for`. Als nächstes folgt in diesem Fall die Variable. Die Variable ist bei einer Runde immer der aktuelle Wert. Wenn du beispielsweise von 0 bis auf 10 zählst, ist die Variable immer der aktuell gezählte Wert. Bei einer Sequenz wiederrum ist es immer das aktuell ausgewählte Objekt. Das wird jetzt etwas verwirrend für dich sein, du wirst es aber gleich besser verstehen.

### Bereich
#### Runde
Wenn du willst, dass dein Block genau n-mal ausgeführt werden soll, kannst du auch nach dem `for` das Keyword `in` verwenden. Du kannst so dann deinen Code beispielsweise 5 mal ausführen lassen:

```python
for i in range(5):
       print('Hallo Welt')
```

Das `i` ist ein Zähler, welcher innerhalb des Blocks verfügbar ist. Der Zähler beinhaltet immer den aktuellen Index. Wenn du nun also beispielsweise "Hallo Welt n" ausgeben möchtest, kannst du folgendes tun:

```python
for i in range(5):
       print(f'Hallo Welt {i}')
```

Um Variablen mit geschweiften Klammern innerhalb eines Strings (Zeichenkette) zu verwenden, musst du das kleine `f` voranstellen.

#### Sequenz
Wenn du beispielsweise eine Liste an Werten durchiterieren möchtest, kannst du in diesem Fall eine Sequenz (deine Liste) angeben. Python wird dann für jedes Element der Liste deinen Block innerhalb der `for`-Schleife ausführen. Dies bedeutet: Wenn du eine Liste mit Namen hast, welche acht Namen enthält, wird dein Block auch acht mal ausgeführt.

Beispiel:
```python
for name in namensliste:
       print(f'Mein Name ist {name}')
```

Verstehst du jetzt den Sinn der Variable? Bei einer Sequenz ist die Variable das aktuelle Objekt. In diesem Fall ein String der Liste namensliste.

## Schritt 2: Die Aufgabe
Öffne nun die Datei `loop.py` und sieh dir den Code an. Der bereits gegebenen Funktion `print_name` werden zwei Parameter übergeben: `name` und `count`. Die Variable `count` gibt an, wie oft du den Namen ausgeben sollst.

Löse nun die Aufgabe mit dem neu erlernten Wissen. Dein Programmablauf soll später so aussehen:

```python
Wie ist dein Name? Andi
Wie oft soll der Name ausgegeben werden? 5
Andi 0
Andi 1
Andi 2
Andi 3
Andi 4
```

## Schritt 3: Bonus
Wenn du dich bereits etwas sicherer fühlst, ist dir aufgefallen, dass die `for`-Loop bei 0 anfängt zu zählen. Probier doch mal aus, ob du es schaffst, dass die Ausgabe immer bereits bei 1 beginnt. Hier hast du die Möglichkeit die Schleife oder die Ausgabe zu modifizieren.

>Achtung: Für die Abgabe, muss die Ausgabe der Aufgabe trotzdem bei 0 beginnen.

## Schritt 4: Ausprobieren
Glückwunsch, das war's.

Wenn alles geklappt hat, ist die Aufgabe nun bereit zum abgeben. Teste sie doch gleich aus. Die Prozedur ist dieselbe. Starte die Anwendung mit:

```bash
python main.py
```

und probier aus! :)

## Lösung
<details>
  <summary>Nur aufklappen, wenn du wirklich Hilfe brauchst! Probiere es zuerst ohne Lösung.</summary>
  
  ### loop.py
  ```python
    for i in range(count):
        print(f'{name} {count}')
  ```

>Tipp: Achte immer darauf, dass die Zeilen richtig eingerückt sind!

</details>