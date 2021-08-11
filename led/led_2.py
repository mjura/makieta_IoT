"""
Plik do sterowania diodą podłączoną do wybranego GPIO
"""
import sys
#Pobranie biblioteki do sterowania GPIO
import RPi.GPIO as GPIO
#Używamy numeracji GPIO, a nie fizycznych pinów
GPIO.setmode(GPIO.BCM)
#Wyłączenie ostrzeżeń, które mogłby pojawić się przy ponownym otwieraniu pliku bez czyszczenia GPIO
GPIO.setwarnings(False)

#Definiujemy pod, który pin GPIO podłączona jest dioda
pin = int(input("Podaj port GPIO pod który podłączona jest dioda (domyślnie: 5)"))

#Podajemy zgodnie z preferencją użytkownika na wcześniej zdefiniowany pin
print("""
Wybierz czynność:
- Y - Włącz diodę
- N - Wyłącz diodę
- Q - Wyjdź z programu
""")
while True:
    operacja = input("Czynność:")
    if operacja == "Y":
        GPIO.output(pin, GPIO.HIGH)
    elif operacja == "N":
        GPIO.output(pin, GPIO.LOW)
    elif operacja == "Q":
        GPIO.cleanup()
        break
    else:
        input("Błędna komenda! Wybierz jeszcze raz! (Naciśnij, aby kontynuować)")
        #Czekaj na reakcję użytkownika
        continue

sys.exit(0)