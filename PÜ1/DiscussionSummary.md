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
Das Tool soll per Kommandozeile bedient werden und besitzt anfänglich kein Nutzerinterface.



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
Für mehr Sicherheit wäre es sinnvoll die gespeicherten Daten mit einer Cloud laufend zu synchronisieren um einen Datenverlust zu vermeiden.

