from .tokens.arguments import RUBY_ARGUMENT_TOKENS
from .tokens.blocks import RUBY_BLOCK_TOKENS
from .tokens.classes import RUBY_CLASS_TOKENS
from .tokens.comments import RUBY_COMMENT_TOKENS
from .tokens.controls import RUBY_CONTROL_TOKENS
from .tokens.data_types import RUBY_DATA_TYPE_TOKENS
from .tokens.exceptions import RUBY_EXCEPTION_TOKENS
from .tokens.methods import RUBY_METHOD_TOKENS
from .tokens.modules import RUBY_MODULE_TOKENS
from .tokens.names import RUBY_NAME_TOKENS
from .tokens.operators import RUBY_OPERATOR_TOKENS
from .tokens.statements import RUBY_STATEMENT_TOKENS

RUBY_TOKENS = {
    **RUBY_ARGUMENT_TOKENS,
    **RUBY_BLOCK_TOKENS,
    **RUBY_CLASS_TOKENS,
    **RUBY_COMMENT_TOKENS,
    **RUBY_CONTROL_TOKENS,
    **RUBY_DATA_TYPE_TOKENS,
    **RUBY_EXCEPTION_TOKENS,
    **RUBY_METHOD_TOKENS,
    **RUBY_MODULE_TOKENS,
    **RUBY_NAME_TOKENS,
    **RUBY_OPERATOR_TOKENS,
    **RUBY_STATEMENT_TOKENS,
}

