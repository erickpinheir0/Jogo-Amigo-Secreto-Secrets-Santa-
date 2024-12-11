
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from interface import Interface


# Cria e executa a interface
interface = Interface()
interface.run()
