from Vintageous.ex.parser.state import EOF

from Vintageous.ex.parser.state import EOF
from Vintageous.ex.parser.tokens import TokenEof
from Vintageous.ex.parser.tokens_base import TokenOfCommand

from Vintageous.ex.ex_error import ERR_INVALID_ARGUMENT
from Vintageous.ex.ex_error import VimError
from Vintageous import ex


TOKEN_COMMAND_SPLIT = 1000



@ex.command('split', 'sp')
class TokenCommandSplit(TokenOfCommand):
    def __init__(self, params, *args, **kwargs):
        super().__init__(params,
                        TOKEN_COMMAND_SPLIT,
                        'split', *args, **kwargs)
        self.target_command = 'ex_split'


def scan_command_split(state):
    state.skip(' ')
    state.ignore()

    params = {
        'file_name': None
    }

    if state.consume() == EOF:
        return None, [TokenCommandVsplit(params), TokenEof()]

    state.backup()

    params['file_name'] = state.match(r'.+$').group(0).strip()

    return None, [TokenCommandSplit(params), TokenEof()]
