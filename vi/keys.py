import Vintageous.vi
from Vintageous.vi.utils import modes
from Vintageous.vi.cmd_defs import cmd_defs, cmds

def patch_class(cls, patch):
    for attr in (a for a in dir(patch) if not a.startswith('__')):
        setattr(cls, attr, getattr(patch, attr))


class seqs:

    CTRL_W_C = '<C-w>c'
    CTRL_W_S = '<C-w>s'
    CTRL_W_V = '<C-w>v'


def patch():



    mappings = {
        modes.NORMAL: {
            seqs.CTRL_W_C: cmd_defs[modes.NORMAL][cmds.CTRL_W_C],
            seqs.CTRL_W_S: cmd_defs[modes.NORMAL][cmds.CTRL_W_S],
            seqs.CTRL_W_V: cmd_defs[modes.NORMAL][cmds.CTRL_W_V],
        },
    }

    patch_class(Vintageous.vi.keys.seqs, seqs)

    for mode in [modes.NORMAL, modes.VISUAL, modes.VISUAL_LINE, modes.VISUAL_BLOCK]:
        Vintageous.vi.keys.mappings[mode].update(mappings[modes.NORMAL])
