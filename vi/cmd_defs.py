import Vintageous.vi
from Vintageous.vi.utils import modes
from Vintageous.vi.cmd_defs import cmd_types


def patch_class(cls, patch):
    for attr in (a for a in dir(patch) if not a.startswith('__')):
        setattr(cls, attr, getattr(patch, attr))

class cmds:

    CTRL_W_C        = 'vio_ctrl_w_c'
    CTRL_W_H        = 'vio_ctrl_w_h'
    CTRL_W_BIG_H    = 'vio_ctrl_w_big_h'
    CTRL_W_J        = 'vio_ctrl_w_j'
    CTRL_W_BIG_J    = 'vio_ctrl_w_big_j'
    CTRL_W_K        = 'vio_ctrl_w_k'
    CTRL_W_BIG_K    = 'vio_ctrl_w_big_k'
    CTRL_W_L        = 'vio_ctrl_w_l'
    CTRL_W_BIG_L    = 'vio_ctrl_w_big_l'
    CTRL_W_N        = 'vio_ctrl_w_n'
    CTRL_W_CTRL_N   = 'vio_ctrl_w_n'
    CTRL_W_O        = 'vio_ctrl_w_o'
    CTRL_W_CTRL_O   = 'vio_ctrl_w_o'
    CTRL_W_S        = 'vio_ctrl_w_s'
    CTRL_W_BIG_S    = 'vio_ctrl_w_s'
    CTRL_W_CTRL_S   = 'vio_ctrl_w_s'
    CTRL_W_V        = 'vio_ctrl_w_v'
    CTRL_W_CTRL_V   = 'vio_ctrl_w_v'

    CTRL_W_X        = 'vio_ctrl_w_x'
    CTRL_W_BIG_X    = 'vio_ctrl_w_big_x'

    CTRL_W_UP       = 'vio_ctrl_w_k'
    CTRL_W_RIGHT    = 'vio_ctrl_w_l'
    CTRL_W_DOWN     = 'vio_ctrl_w_j'
    CTRL_W_LEFT     = 'vio_ctrl_w_h'

    CTRL_W_SHIFT_UP = 'vio_ctrl_w_big_h'


# Patch the command definitions
cmd_defs = {
    modes.NORMAL: {
        name:dict(name=name, input=None, type=cmd_types.ACTION, motion_required=False, multi_step=False, repeatable=False)
        for name in (getattr(cmds,attr) for attr in dir(cmds) if not attr.startswith('__'))
    }
}
cmd_defs[modes.VISUAL] = cmd_defs[modes.NORMAL].copy()
cmd_defs[modes.VISUAL_LINE] = cmd_defs[modes.NORMAL].copy()
cmd_defs[modes.VISUAL_BLOCK] = cmd_defs[modes.NORMAL].copy()
cmd_defs[modes.OPERATOR_PENDING] = cmd_defs[modes.NORMAL].copy()

def patch():
    patch_class(Vintageous.vi.cmd_defs.cmds, cmds)
    for mode in [modes.NORMAL, modes.OPERATOR_PENDING, modes.VISUAL, modes.VISUAL_LINE, modes.VISUAL_BLOCK]:
        Vintageous.vi.cmd_defs.cmd_defs[mode].update(cmd_defs[mode])
