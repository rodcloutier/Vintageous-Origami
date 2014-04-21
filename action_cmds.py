import sublime
import sublime_plugin

from Vintageous import plugins
from Vintageous.vi import inputs
from Vintageous.vi import utils
from Vintageous.vi.cmd_defs import ViOperatorDef
from Vintageous.vi.core import ViTextCommandBase
from Vintageous.vi.inputs import input_types
from Vintageous.vi.inputs import parser_def
from Vintageous.vi.search import reverse_search
from Vintageous.vi.utils import modes
from Vintageous.vi.utils import regions_transformer


class VintageousOrigamiBase(ViOperatorDef):
    def __init__(self, *args, **kwargs):
        ViOperatorDef.__init__(self, *args, **kwargs)

        self.repeatable = False
        self.motion_required = False


@plugins.register(keys=[('<C-w>c', (modes.NORMAL,))])
class VintageousOrigamiClosePane(VintageousOrigamiBase):

    def translate(self, state):
        cmd = {}
        cmd['action'] = '_vio_ctrl_w_c'
        cmd['action_args'] = {}
        return cmd

@plugins.register(keys=[('<C-w>n', (modes.NORMAL,))])
class VintageousOrigamiSplitNewFile(VintageousOrigamiBase):

    def translate(self, state):
        cmd = {}
        cmd['action'] = '_vio_ctrl_w_n'
        cmd['action_args'] = {}
        return cmd

@plugins.register(keys=[('<C-w>s', (modes.NORMAL,))])
class VintageousOrigamiSplitHorizontal(VintageousOrigamiBase):

    def translate(self, state):
        cmd = {}
        cmd['action'] = '_vio_ctrl_w_s'
        cmd['action_args'] = {}
        return cmd

@plugins.register(keys=[('<C-w>v', (modes.NORMAL,))])
class VintageousOrigamiSplitVertical(VintageousOrigamiBase):

    def translate(self, state):
        cmd = {}
        cmd['action'] = '_vio_ctrl_w_v'
        cmd['action_args'] = {}
        return cmd

@plugins.register(keys=[('<C-w>h', (modes.NORMAL,))])
class VintageousOrigamiTravelLeft(VintageousOrigamiBase):

    def translate(self, state):
        return  {
            'action': "travel_to_pane",
            'action_args': {'direction' : 'left'}
        }

@plugins.register(keys=[('<C-w>j', (modes.NORMAL,))])
class VintageousOrigamiTravelDown(VintageousOrigamiBase):

    def translate(self, state):
        return  {
            'action': "travel_to_pane",
            'action_args': {'direction' : 'down'}
        }

@plugins.register(keys=[('<C-w>k', (modes.NORMAL,))])
class VintageousOrigamiTravelUp(VintageousOrigamiBase):

    def translate(self, state):
        return  {
            'action': "travel_to_pane",
            'action_args': {'direction' : 'up'}
        }

@plugins.register(keys=[('<C-w>l', (modes.NORMAL,))])
class VintageousOrigamiTravelRight(VintageousOrigamiBase):

    def translate(self, state):
        return  {
            'action': "travel_to_pane",
            'action_args': {'direction' : 'right'}
        }

@plugins.register(keys=[('<C-w>H', (modes.NORMAL,))])
class VintageousOrigamiExchangePaneLeft(VintageousOrigamiBase):

    def translate(self, state):
        return {
            'action': '_vio_exchange_files_with_pane',
            'action_args': {'direction': 'left'}
        }

@plugins.register(keys=[('<C-w>J', (modes.NORMAL,))])
class VintageousOrigamiExchangePaneDown(VintageousOrigamiBase):

    def translate(self, state):
        return {
            'action': '_vio_exchange_files_with_pane',
            'action_args': {'direction': 'down'}
        }

@plugins.register(keys=[('<C-w>K', (modes.NORMAL,))])
class VintageousOrigamiExchangePaneUp(VintageousOrigamiBase):

    def translate(self, state):
        return {
            'action': '_vio_exchange_files_with_pane',
            'action_args': {'direction': 'up'}
        }

@plugins.register(keys=[('<C-w>L', (modes.NORMAL,))])
class VintageousOrigamiExchangePaneRight(VintageousOrigamiBase):

    def translate(self, state):
        return {
            'action': '_vio_exchange_files_with_pane',
            'action_args': {'direction': 'right'}
        }


@plugins.register(keys=[('<C-w>o', (modes.NORMAL,))])
class VintageousOrigamiMaximizePane(VintageousOrigamiBase):

    # Also command :only
    def translate(self, state):
        return {
            'action': '_vio_ctrl_w_o',
            'action_args': {}
        }

@plugins.register(keys=[('<C-w>x', (modes.NORMAL,))])
class VintageousOrigamiClose(VintageousOrigamiBase):
    def translate(self, state):
        return {
            'action': 'close',
            'action_args': {}
        }


@plugins.register(keys=[('<C-w>X', (modes.NORMAL,))])
class VintageousOrigamiCloseAll(VintageousOrigamiBase):
    def translate(self, state):
        return {
            'action': 'close_all',
            'action_args': {}
        }
