import Vintageous.vi
from Vintageous.vi.utils import modes
from Vintageous.vi.cmd_defs import cmd_defs, cmds

def patch_class(cls, patch):
    for attr in (a for a in dir(patch) if not a.startswith('__')):
        setattr(cls, attr, getattr(patch, attr))


class seqs:

    CTRL_W_C        = '<C-w>c'
    CTRL_W_H        = '<C-w>h'
    CTRL_W_BIG_H    = '<C-w>H'
    CTRL_W_J        = '<C-w>j'
    CTRL_W_BIG_J    = '<C-w>J'
    CTRL_W_K        = '<C-w>k'
    CTRL_W_BIG_K    = '<C-w>K'
    CTRL_W_L        = '<C-w>l'
    CTRL_W_BIG_L    = '<C-w>L'
    CTRL_W_N        = '<C-w>n'
    CTRL_W_CTRL_N   = '<C-w><C-n>'
    CTRL_W_O        = '<C-w>o'
    CTRL_W_CTRL_O   = '<C-w><C-o>'
    CTRL_W_S        = '<C-w>s'
    CTRL_W_BIG_S    = '<C-w>S'
    CTRL_W_CTRL_S   = '<C-w><C-s>'
    CTRL_W_V        = '<C-w>v'
    CTRL_W_CTRL_V   = '<C-w><C-v>'


def patch():


    mappings = {
        modes.NORMAL: {
            getattr(seqs, attr): cmd_defs[modes.NORMAL][getattr(cmds, attr)]
            for attr in dir(seqs) if not attr.startswith('__')
        }
    }

    patch_class(Vintageous.vi.keys.seqs, seqs)

    for mode in [modes.NORMAL, modes.VISUAL, modes.VISUAL_LINE, modes.VISUAL_BLOCK]:
        Vintageous.vi.keys.mappings[mode].update(mappings[modes.NORMAL])
