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
        # TODO handle the different options
        _vio_ctrl_w_v.run(self)


class ExSplit(ViWindowCommandBase):
    def run(self, command_line=''):
        _vio_ctrl_w_s.run(self)


class ExNew(ViWindowCommandBase):
    def run(self, command_line=''):
        _vio_ctrl_w_n.run(self)


class ExVnew(ViWindowCommandBase):
    def run(self, command_line=''):
        self.window.run_command("create_pane", {"direction": "right"})
        self.window.run_command("travel_to_pane", {"direction": "right"})
        self.window.run_command("new_file")


class ExOnly(ViWindowCommandBase):
    def run(self, command_line=''):
        _vio_ctrl_w_o.run(self)


# Patching
Vintageous.ex_commands.ExVsplit = ExVsplit
Vintageous.ex_commands.ExNew = ExNew
Vintageous.ex_commands.ExOnly = ExOnly
