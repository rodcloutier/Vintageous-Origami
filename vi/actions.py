import Vintageous.vi
from Vintageous.vi.utils import modes


def vio_ctrl_w_c(state, **kwargs):
    cmd = {}
    cmd['action'] = '_vio_ctrl_w_c'
    cmd['action_args'] = {}
    return cmd

def vio_ctrl_w_n(state, **kwargs):
    cmd = {}
    cmd['action'] = '_vio_ctrl_w_n'
    cmd['action_args'] = {}
    return cmd

def vio_ctrl_w_s(state, **kwargs):
    cmd = {}
    cmd['action'] = '_vio_ctrl_w_s'
    cmd['action_args'] = {}
    return cmd

def vio_ctrl_w_v(state, **kwargs):
    cmd = {}
    cmd['action'] = '_vio_ctrl_w_v'
    cmd['action_args'] = {}
    return cmd

def vio_ctrl_w_h(state, **kwargs):
    return  {
        'action': "travel_to_pane",
        'action_args': {'direction' : 'left'}
    }

def vio_ctrl_w_j(state, **kwargs):
    return  {
        'action': "travel_to_pane",
        'action_args': {'direction' : 'down'}
    }

def vio_ctrl_w_k(state, **kwargs):
    return  {
        'action': "travel_to_pane",
        'action_args': {'direction' : 'up'}
    }

def vio_ctrl_w_l(state, **kwargs):
    return  {
        'action': "travel_to_pane",
        'action_args': {'direction' : 'right'}
    }

def vio_ctrl_w_big_h(state, **kwargs):
    return {
        'action': '_vio_exchange_files_with_pane',
        'action_args': {'direction': 'left'}
    }

def vio_ctrl_w_big_j(state, **kwargs):
    return {
        'action': '_vio_exchange_files_with_pane',
        'action_args': {'direction': 'down'}
    }

def vio_ctrl_w_big_k(state, **kwargs):
    return {
        'action': '_vio_exchange_files_with_pane',
        'action_args': {'direction': 'up'}
    }

def vio_ctrl_w_big_l(state, **kwargs):
    return {
        'action': '_vio_exchange_files_with_pane',
        'action_args': {'direction': 'right'}
    }

def vio_ctrl_w_o(state, **kwargs):
    return {
        'action': '_vio_ctrl_w_o',
        'action_args': {}
    }

def vio_ctrl_w_x(state, **kwargs):
    return {
        'action': 'close',
        'action_args': {}
    }

def vio_ctrl_w_big_x(state, **kwargs):
    return {
        'action': 'close_all',
        'action_args': {}
    }


actions = (
    vio_ctrl_w_c,
    vio_ctrl_w_h,
    vio_ctrl_w_big_h,
    vio_ctrl_w_j,
    vio_ctrl_w_big_j,
    vio_ctrl_w_k,
    vio_ctrl_w_big_k,
    vio_ctrl_w_l,
    vio_ctrl_w_big_l,
    vio_ctrl_w_n,
    vio_ctrl_w_o,
    vio_ctrl_w_s,
    vio_ctrl_w_v,
    vio_ctrl_w_x,
    vio_ctrl_w_big_x,
)

def patch():
    for func in actions:
        setattr(Vintageous.vi.actions, func.__name__, func)



