import Vintageous.ex.parser.subscanners

from .scanner_command_split import scan_command_split
from .scanner_command_vnew import scan_command_vnew

Vintageous.ex.parser.subscanners.patterns[r's(?:plit)?'] = scan_command_split
Vintageous.ex.parser.subscanners.patterns[r'vne(?:w)?'] = scan_command_vnew
