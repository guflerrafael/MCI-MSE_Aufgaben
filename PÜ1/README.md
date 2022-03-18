# Leistungsdiagnostik

Tool zur automatisierten Auswertung der Daten eines Fahrradergometer-Leistungstests, welches als Ergebnis sowohl die Herzrate, als auch die erbrachte Leistung in Form eines Plots und deren zugrundeliegenden Daten, gespeichert in einer Datei, liefert.

## Installation

Für die Proof-Of-Concept-Version des Tools wird nur die Kommandozeile gebraucht, weshalb keine zusätzliche Installation nötig ist.

## Usage

Bevor das Tool gestartet wird, sollte zuerst geprüft werden, ob alle Daten, also der Puls und die erbrachte Leistung als Zeitreihe in Form mehrerer ".txt"-Dateien im Ordner "input_data" vorliegen. Anschließend wird das Tool über die Kommandozeile gestartet, indem ```python main.py``` als Befehl ausgeführt wird. Das Tool analysiert die Daten zuerst auf das Vorhandensein von Abbruchkriterien und markiert die Daten gegebenenfalls als ungültig. Dies kann in einem weiteren Schritt auch von der Diagnostikerin selbst vermerkt werden. Des weiteren kann zu den Daten der Name, die technische ID und das Geburtsdatum der Versuchsperson hinzugefügt werden.

Als Ergebnis erstellt das Tool einen Plot der Herzrate und Leistung über den gewählten Zeitraum und speichert diesen Plot, zusammen mit den verarbeiteten Daten, im Ordner "output_data". Hier wird mittels Unterordnern zudem noch unterscheiden, ob es ein erfolgreicher oder abgebrochenen Versuch war.

## Contributing

- Gufler Rafael, 12037580, gr2601@mci4me.at
- Gruber Richard, 52110057, richi24091996@hotmail.com

## License
[MIT](https://choosealicense.com/licenses/mit/)
