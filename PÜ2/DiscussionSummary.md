## Project background

### Purpose of project
Ziel dieses Projektes ist es eine Leistungsfeststellung mittels eines Fahrradergometers.
Dabei wird nur ein Test-Typ gefahren (3 Minuten).
Es wird der Puls und die Leistung des Probanden erfasst.
Diese Daten sollen ausgewertet und visualisiert werden.

### Scope of project
Das Programm soll die ausgewerteten Daten speichern und als Diagramme ausgeben.

### Other background information
Es gibt einige Abbruchkriterien die ebenfalls berücksichtig werden müssen.
Diese Tests (Daten) sollen in einem separaten Ordner gespeichert werden. 


## Perspectives
### Who will use the system?
Bedient wird dieses System nur von dem Diagnostiker.
Dieser kann mit den geplotteten Werten eine Diagnose erstellen.

### Who can provide input about the system?
Den Input liefert der Proband, der Mittels diversen Sensoren überwacht wird.


## Project Objectives
### Known business rules
Die gesamten Messwerte die während des Tests entstanden sind, werden an das Programm übermittelt.
Dann werden die Informationen des Probanden eingegeben (Name, Technische ID und Geburtsdatum).
Anschließend wertet das Programm die erfassten Daten aus, welche dann bei erfolgreichen Abschluss des Tools in einem eigenen Ordner gespeichert werden.
Hierbei wird noch mittels Unterordner zwischen erfolgreichen und abgebrochen Durchlauf unterschieden.

### System information and/or diagrams


![](ekg_example.png)

Beispiel von aufgezeichneten EKG-Daten.
Diese Daten werden vom Programm weiter ausgewertet und von dem Diagnostiker begutachtet.

### Assumptions and dependencies
In den csv-Dateien sind die EKG-Daten der verschiedenen Patienten gespeichert. Für jeden Datenpunkt wird die gemessene Spannung in mV angegeben. Alle EKG-Daten haben eine zeitliche Auflösung von 1kHz, es werden also pro Sekunde 1.000 Datenpunkte geschrieben. 

- In den txt-Dateien sind die Leistungsdaten der einzelnen Patienten beschrieben, hierbei wird für jede Zeile (was den Sekunden entspricht) die entsprechende Leistung in Watt gespeichert. Die zeitliche Auflösung entpricht 1Hz.
- Sowohl bei den EKG-, als auch den Leistungsdaten haben die Tests einen zeitlichen Umfang von 180 Sekunden.
- In den json-Dateien sind zusätzliche Daten zum Patienten, wie zum Beispiel sein Geburtsjahr, und dessen Leistungstest (Dauer und vorgegebene Leistung) hinterlegt.

NOTE-JHU: Gut, ahbs noch mit Bulletpoints strukturiert, damit es ein so Textbrei ist.

### Design and implementation constraints
Es ist eine feste Zeit von 3 min pro Test vorgegeben.
Außerdem gibt es Abbruchkriterien:
- Herzfrequenz über 90% (220-Lebensalter).
- Andere Kriterien die vom Diagnostiker eingegeben werden können.

## Risks
Das größte Risiko ist ein Datenverlust der bearbeiteten beziehungsweiße anfänglichen Daten.

## Known future enhancements
In näherer Zukunft könnten auch noch die Auswertung anderer Test-Typen und ein grafisches Nutzerinterface implementiert werden.


## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues
Für mehr Sicherheit wäre es sinnvoll, die gespeicherten Daten mit einer Cloud laufend zu synchronisieren um einen Datenverlust zu vermeiden.

