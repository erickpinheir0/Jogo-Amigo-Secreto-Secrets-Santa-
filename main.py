
import sys
import os
from gui.interface import Interface

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Cria e executa a interface
interface = Interface()
interface.run()
