
import sublime

import Vintageous.ex_commands
from Vintageous.vi.core import ViWindowCommandBase


from .xactions import (
    _vio_ctrl_w_v,
    _vio_ctrl_w_s,
    _vio_ctrl_w_n,
    _vio_ctrl_w_o,
)


class ExVsplit(ViWindowCommandBase):

    def run(self, command_line=''):
        prefs = sublime.load_settings('Preferences.sublime-settings')
        if prefs.get('vintageous_origami_override_command_vsplit', True):
            _vio_ctrl_w_v.run(self)
        else:
            if self._view.file_name():
                overrides = Vintageous.ex_commands.ExVsplit_overrides
                self.open_file = lambda file_name: overrides['open_file'](self, file_name)
                overrides['run'](self, command_line)


class ExSplit(ViWindowCommandBase):
    def run(self, command_line=''):
        _vio_ctrl_w_s.run(self)


class ExNew(Vintageous.ex_commands.ExNew):
    def run(self, command_line=''):
        prefs = sublime.load_settings('Preferences.sublime-settings')
        if prefs.get('vintageous_origami_override_command_new', True):
            _vio_ctrl_w_n.run(self)
        else:
            Vintageous.ex_commands.ExNew_run(self, command_line)


class ExVnew(ViWindowCommandBase):
    def run(self, command_line=''):
        self.window.run_command("create_pane", {"direction": "right"})
        self.window.run_command("travel_to_pane", {"direction": "right"})
        self.window.run_command("new_file")


class ExOnly(ViWindowCommandBase):
    def run(self, command_line=''):
        prefs = sublime.load_settings('Preferences.sublime-settings')
        if prefs.get('vintageous_origami_override_command_only', True):
            _vio_ctrl_w_o.run(self)
        else:
            Vintageous.ex_commands.ExOnly_run(self, command_line)


if not hasattr(Vintageous.ex_commands, 'ExVsplit_overrides'):
    Vintageous.ex_commands.ExVsplit_overrides = {
        'run': Vintageous.ex_commands.ExVsplit.run,
        'open_file': Vintageous.ex_commands.ExVsplit.open_file,
    }
    ExVsplit.MAX_SPLITS = Vintageous.ex_commands.ExVsplit.MAX_SPLITS
    ExVsplit.LAYOUT_DATA = Vintageous.ex_commands.ExVsplit.LAYOUT_DATA
    Vintageous.ex_commands.ExVsplit = ExVsplit

if not hasattr(Vintageous.ex_commands, 'ExNew_run'):
    Vintageous.ex_commands.ExNew_run = Vintageous.ex_commands.ExNew.run
    Vintageous.ex_commands.ExNew = ExNew

if not hasattr(Vintageous.ex_commands, 'ExOnly_run'):
    Vintageous.ex_commands.ExOnly_run = Vintageous.ex_commands.ExOnly.run
    Vintageous.ex_commands.ExOnly = ExOnly
