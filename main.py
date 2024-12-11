
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from gui.interface import Interface
from gui.entry_window import EntryWindow
from gui.show_results import ShowResults

# Cria e executa a interface
interface = Interface()
interface.run()
