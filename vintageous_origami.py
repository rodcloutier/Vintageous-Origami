import sublime_plugin

from Origami.origami import PaneCommand as OrigamiPaneCommand

from .vi import cmd_defs
from .vi import actions
from .vi import keys

cmd_defs.patch()
actions.patch()
keys.patch()










