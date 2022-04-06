#%% UC 2.0

# Importieren aller verwendeten Packete und globalen Variablen
import os
import pandas as pd
import neurokit2 as nk
import json

global termination
termination = False

#%% UC 2.1 Einlesen der Daten
## Überprüfen ob Dateien vorhanden sind und erstellen einer Liste von Tests, die zu verarbeiten sind


folder_input_data = os.path.join(os.path.dirname(__file__) , 'input_data')
    
def get_data(folder_input_data):
    """Funktion zum Einlesen und Speichern von Daten als Liste von panda_dataframes, Rückgabe: Liste der eingelesenen Tests
    

            Parameters:
                    folder_input_data (string): A path with input data as csv files
            
            Returns:
                    list_of_new_tests (array): a list of the test data
                
                    
    """
    list_of_new_tests = []


    ## Überprüfen ob Dateien vorhanden sind
    for file in os.listdir(folder_input_data):
        
        if file.endswith(".csv"):
            file_name = os.path.join(folder_input_data, file)
            print(file_name)
            subject_id = file_name.split(".")[0][-1]
            new_ecg_data= pd.read_csv(file_name)

            ## Erstellen einer Liste von Tests, die zu verarbeiten sind
            list_of_new_tests.append(new_ecg_data)
    
    return list_of_new_tests

list_of_new_tests = get_data()

#%% UC 2.2 Vorverarbeiten der Daten
## Anlegen einer Zeitreihe der Herzfrequenz aus den EKG-Daten für Subject_3

def analyze_data():
    """Funktion zum Finden der Peaks und Berechnung des moving_averages der Herzrate des Patienten, Rückgabe: Peaks und moving_average"""

    ekg_data=pd.DataFrame()
    new_ecg_data = list_of_new_tests[0]
    ekg_data["ECG"] = new_ecg_data["Subject_3"]

    # Finden der Peaks
    peaks, info = nk.ecg_peaks(ekg_data["ECG"], sampling_rate=1000)
    number_of_heartbeats = peaks["ECG_R_Peaks"].sum()
    duration_test_min = ekg_data.size/1000/60
    average_hr_test = number_of_heartbeats / duration_test_min

    ## Berechnung und plotten des moving_average der Herzfrequenz
    peaks['average_HR_10s'] = peaks.rolling(window=10000).mean()*60*1000
    peaks['average_HR_10s'].plot()

    return peaks, average_hr_test

heartrate, average_hr_test = analyze_data()

#%% UC 2.3 Analysieren der Daten auf Abbruch-Kriterium
## Vergleich der Maximalen Herzfrequenz mit Alter des Patienten (Subject_3)

def load_json(filename):
    """JSON Datei wird geöffnet und als dictionary zurückgegeben, Rückgabe: Daten der Testperson"""

    folder_input_data = os.path.join(os.path.dirname(__file__) , 'input_data')
    file_name = folder_input_data = os.path.join(folder_input_data, filename)
    f = open(file_name)
    subject_data = json.load(f)

    return subject_data

def check_data(subject_birthyear):
    """Daten werden auf Abbruchkriterium überprüft, falls postitiv termination auf true gesetzt, Rückgabe: Maximale Herzrate und zugelassene max. Herzrate"""

    maximum_hr = heartrate['average_HR_10s'].max()
    subject_max_hr = 220 - (2022 - subject_birthyear)

    if maximum_hr > subject_max_hr*0.90:
        termination = True

    return maximum_hr, subject_max_hr

subject_data = load_json("subject_3.json")
maximum_hr, subject_max_hr = check_data(subject_data["birth_year"])

#%% UC 2.4 Erstellen einer Zusammenfassung
## Ausgabe einer Zusammenfassung der verarbeiteten Daten

def print_summary():
    """Daten werden zusammengefasst ausgegeben und angezeigt"""

    print("Summary for Subject: " + str(subject_data["subject_id"]))
    print("Year of birth:  " + str(subject_data["birth_year"]))
    print("Test level power in W:  " + str(subject_data["test_power_w"]))
    print("\n")
    print("Maximum HR was: " + str(maximum_hr))
    print("Was test terminated because exceeding HR: " + str(termination))

print_summary()

#%% UC 2.5 Visualisierung der Daten
## Erstellung eines Plots

def load_power_data(filename):
    """Einlesen der Watt-Daten aus den power_data.txt-Dateien, Rückgabe: Watt-Daten des Patienten"""

    folder_input_data = os.path.join(os.path.dirname(__file__), 'input_data')
    file_name =  os.path.join(folder_input_data, filename)
    power_data_watts = open(file_name).read().split("\n")
    power_data_watts.pop(-1)
    len(power_data_watts)

    return power_data_watts

def plot_power_data():
    """Erstellen und Anzeigen des Plots mit Watt Daten und moving_average der Herzrate, Rückgabe: Peaks der Herzrate mit verringerter Amplitude (normalisiert)"""

    peaks_downsampled = heartrate[heartrate.index % 1000 == 0]  
    peaks_downsampled = peaks_downsampled.reset_index(drop=True)
    peaks_downsampled = peaks_downsampled.drop(["ECG_R_Peaks"],axis=1)
    peaks_downsampled["Power (Watt)"] = pd.to_numeric(power_data_watts)
    peaks_downsampled.plot()

    return peaks_downsampled

power_data_watts = load_power_data("power_data_3.txt")
peaks_downsampled = plot_power_data()

#%% UC 2.6 Manuelle Eingabe eines Abbruchkritierums
## Abfrage an Nutzer:in, ob Abgebrochen werden soll

def manual_term():
    """Manuelle Eingabemöglichkeit von Abbruchkriterien für Nutzer:in, Rückgabe: Grund des Abbruchs"""

    manual_termination = False
    manual_termination = input("Is this test invalid? (leave blank if valid): ")

    if manual_termination != False:
        termination = True

    return manual_termination

manual_termination = manual_term()

#%% UC 2.7 Speichern der Daten

# Zu schreibende Daten
data = {
    "User ID" : subject_data["subject_id"], 
    "Reason for test termation" : manual_termination, 
    "Average Heart Rate" : average_hr_test, 
    "Maximum Heart Rate" : subject_max_hr, 
    "Test Length (s)" : len(power_data_watts), 
    "Test Power (W)" : subject_data["test_power_w"], 
    "Average Power" : peaks_downsampled["Power (Watt)"].mean()
}


def write_data():
    """Schreiben der Daten des Test als JSON-Datei in result-Ordner"""

    folder_input_data = os.path.join(os.path.dirname(__file__) , 'result_data')
    results_file = os.path.join(folder_input_data, 'data.json')

    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

write_data()
