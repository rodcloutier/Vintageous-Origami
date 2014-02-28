import Vintageous.vi
from Vintageous.vi.utils import modes

def vio_ctrl_w_s(state, **kwargs):
    cmd = {}
    cmd['action'] = '_vio_ctrl_w_s'
    cmd['action_args'] = {'mode': state.mode, 'count': state.count}
    return cmd

def vio_ctrl_w_v(state, **kwargs):
    cmd = {}
    cmd['action'] = '_vio_ctrl_w_v'
    cmd['action_args'] = {'mode': state.mode, 'count': state.count}
    return cmd

def vio_ctrl_w_c(state, **kwargs):
    cmd = {}
    cmd['action'] = '_vio_ctrl_w_c'
    cmd['action_args'] = {'mode': state.mode, 'count': state.count}
    return cmd

def patch():
    for func in (vio_ctrl_w_c, vio_ctrl_w_s, vio_ctrl_w_v):
        setattr(Vintageous.vi.actions, func.__name__, func)


        
