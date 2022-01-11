import os.path

from loop import print_name

# Check if files exist
def test_exists():

    err = "Die Datei loop.py existiert nicht"
    assert os.path.exists('loop.py'), err

    err = "Die Datei main.py existiert nicht"
    assert os.path.exists('main.py'), err
