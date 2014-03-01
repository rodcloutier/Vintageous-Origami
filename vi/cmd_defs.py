import Vintageous.vi
from Vintageous.vi.utils import modes
from Vintageous.vi.cmd_defs import cmd_types


def patch_class(cls, patch):
    for attr in (a for a in dir(patch) if not a.startswith('__')):
        setattr(cls, attr, getattr(patch, attr))

class cmds:

    CTRL_W_C = 'vio_ctrl_w_c'
    CTRL_W_H = 'vio_ctrl_w_h'
    CTRL_W_J = 'vio_ctrl_w_j'
    CTRL_W_K = 'vio_ctrl_w_k'
    CTRL_W_L = 'vio_ctrl_w_l'
    CTRL_W_N = 'vio_ctrl_w_n'
    CTRL_W_S = 'vio_ctrl_w_s'
    CTRL_W_V = 'vio_ctrl_w_v'


# Patch the command definitions
cmd_defs = {
    modes.NORMAL: {
        name:dict(name=name, input=None, type=cmd_types.ACTION, motion_required=False, multi_step=False, repeatable=False)
        for name in (getattr(cmds,attr) for attr in dir(cmds) if not attr.startswith('__'))
    }
        # cmds.CTRL_W_C: dict(name=cmds.CTRL_W_C, input=None, type=cmd_types.ACTION, motion_required=False, multi_step=False, repeatable=False),
        # cmds.CTRL_W_N: dict(name=cmds.CTRL_W_N, input=None, type=cmd_types.ACTION, motion_required=False, multi_step=False, repeatable=False),
        # cmds.CTRL_W_S: dict(name=cmds.CTRL_W_S, input=None, type=cmd_types.ACTION, motion_required=False, multi_step=False, repeatable=False),
        # cmds.CTRL_W_V: dict(name=cmds.CTRL_W_V, input=None, type=cmd_types.ACTION, motion_required=False, multi_step=False, repeatable=False),
    # }
}
cmd_defs[modes.VISUAL] = cmd_defs[modes.NORMAL].copy()
cmd_defs[modes.VISUAL_LINE] = cmd_defs[modes.NORMAL].copy()
cmd_defs[modes.VISUAL_BLOCK] = cmd_defs[modes.NORMAL].copy()
cmd_defs[modes.OPERATOR_PENDING] = cmd_defs[modes.NORMAL].copy()

def patch():
    patch_class(Vintageous.vi.cmd_defs.cmds, cmds)
    for mode in [modes.NORMAL, modes.OPERATOR_PENDING, modes.VISUAL, modes.VISUAL_LINE, modes.VISUAL_BLOCK]:
        Vintageous.vi.cmd_defs.cmd_defs[mode].update(cmd_defs[mode])
