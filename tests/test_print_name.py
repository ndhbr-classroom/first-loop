import random
import string
import os.path

from loop import print_name

# Check if files exist
def test_exists():

    err = "Die Datei loop.py existiert nicht"
    assert os.path.exists('loop.py'), err

    err = "Die Datei main.py existiert nicht"
    assert os.path.exists('main.py'), err

# Check for functionality
def test_print_name(capfd):
    name = ''.join(random.choices(string.ascii_letters, k=10))
    print_name(name, 3)
    out, err = capfd.readouterr()

    err = """Deine Funktion wurde auf einen zufälligen Namen getestet.
    Überprüfe deine Ausgabe, ob wirklich jedes Zeichen stimmt (mit Groß-
    und Kleinschreibung)"""

    assert out == f'{name} 0\n{name} 1\n{name} 2\n', err