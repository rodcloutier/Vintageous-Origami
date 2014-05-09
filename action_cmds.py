
from Vintageous import plugins
from Vintageous.vi.cmd_defs import ViOperatorDef
from Vintageous.vi.utils import modes


class VintageousOrigamiBase(ViOperatorDef):
    def __init__(self, *args, **kwargs):
        ViOperatorDef.__init__(self, *args, **kwargs)

        self.repeatable = False
        self.motion_required = False


@plugins.register('<C-w>c', (modes.NORMAL,))
class VintageousOrigamiClosePane(VintageousOrigamiBase):

    def translate(self, state):
        cmd = {}
        cmd['action'] = '_vio_ctrl_w_c'
        cmd['action_args'] = {}
        return cmd

@plugins.register('<C-w>n', (modes.NORMAL,))
@plugins.register('<C-w><C-n>', (modes.NORMAL,))
class VintageousOrigamiSplitNewFile(VintageousOrigamiBase):

    def translate(self, state):
        cmd = {}
        cmd['action'] = '_vio_ctrl_w_n'
        cmd['action_args'] = {}
        return cmd

@plugins.register('<C-w>s', (modes.NORMAL,))
@plugins.register('<C-w><C-s>', (modes.NORMAL,))
class VintageousOrigamiSplitHorizontal(VintageousOrigamiBase):

    def translate(self, state):
        cmd = {}
        cmd['action'] = '_vio_ctrl_w_s'
        cmd['action_args'] = {}
        return cmd

@plugins.register('<C-w>v', (modes.NORMAL,))
@plugins.register('<C-w><C-v>', (modes.NORMAL,))
class VintageousOrigamiSplitVertical(VintageousOrigamiBase):

    def translate(self, state):
        cmd = {}
        cmd['action'] = '_vio_ctrl_w_v'
        cmd['action_args'] = {}
        return cmd

@plugins.register('<C-w>h', (modes.NORMAL,))
@plugins.register('<C-w><left>', (modes.NORMAL,))
class VintageousOrigamiTravelLeft(VintageousOrigamiBase):

    def translate(self, state):
        return  {
            'action': "travel_to_pane",
            'action_args': {'direction' : 'left'}
        }

@plugins.register('<C-w>j', (modes.NORMAL,))
@plugins.register('<C-w><down>', (modes.NORMAL,))
class VintageousOrigamiTravelDown(VintageousOrigamiBase):

    def translate(self, state):
        return  {
            'action': "travel_to_pane",
            'action_args': {'direction' : 'down'}
        }

@plugins.register('<C-w>k', (modes.NORMAL,))
@plugins.register('<C-w><up>', (modes.NORMAL,))
class VintageousOrigamiTravelUp(VintageousOrigamiBase):

    def translate(self, state):
        return  {
            'action': "travel_to_pane",
            'action_args': {'direction' : 'up'}
        }

@plugins.register('<C-w>l', (modes.NORMAL,))
@plugins.register('<C-w><right>', (modes.NORMAL,))
class VintageousOrigamiTravelRight(VintageousOrigamiBase):

    def translate(self, state):
        return  {
            'action': "travel_to_pane",
            'action_args': {'direction' : 'right'}
        }

@plugins.register('<C-w>H', (modes.NORMAL,))
class VintageousOrigamiExchangePaneLeft(VintageousOrigamiBase):

    def translate(self, state):
        return {
            'action': '_vio_exchange_files_with_pane',
            'action_args': {'direction': 'left'}
        }

@plugins.register('<C-w>J', (modes.NORMAL,))
class VintageousOrigamiExchangePaneDown(VintageousOrigamiBase):

    def translate(self, state):
        return {
            'action': '_vio_exchange_files_with_pane',
            'action_args': {'direction': 'down'}
        }

@plugins.register('<C-w>K', (modes.NORMAL,))
class VintageousOrigamiExchangePaneUp(VintageousOrigamiBase):

    def translate(self, state):
        return {
            'action': '_vio_exchange_files_with_pane',
            'action_args': {'direction': 'up'}
        }

@plugins.register('<C-w>L', (modes.NORMAL,))
class VintageousOrigamiExchangePaneRight(VintageousOrigamiBase):

    def translate(self, state):
        return {
            'action': '_vio_exchange_files_with_pane',
            'action_args': {'direction': 'right'}
        }


@plugins.register('<C-w>o', (modes.NORMAL,))
@plugins.register('<C-w><C-o>', (modes.NORMAL,))
class VintageousOrigamiMaximizePane(VintageousOrigamiBase):

    # Also command :only
    def translate(self, state):
        return {
            'action': '_vio_ctrl_w_o',
            'action_args': {}
        }

@plugins.register('<C-w>x', (modes.NORMAL,))
class VintageousOrigamiClose(VintageousOrigamiBase):
    def translate(self, state):
        return {
            'action': 'close',
            'action_args': {}
        }


@plugins.register('<C-w>X', (modes.NORMAL,))
class VintageousOrigamiCloseAll(VintageousOrigamiBase):
    def translate(self, state):
        return {
            'action': 'close_all',
            'action_args': {}
        }
