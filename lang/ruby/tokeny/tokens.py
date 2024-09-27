from ..arguments import RUBY_ARGUMENT_TOKENS
from ..blocks import RUBY_BLOCK_TOKENS
from ..classes import RUBY_CLASS_TOKENS
from ..comments import RUBY_COMMENT_TOKENS
from ..controls import RUBY_CONTROL_TOKENS
from ..data_types import RUBY_DATA_TYPE_TOKENS
from ..exceptions import RUBY_EXCEPTION_TOKENS
from ..methods import RUBY_METHOD_TOKENS
from ..modules import RUBY_MODULE_TOKENS
from ..names import RUBY_NAME_TOKENS
from ..operators import RUBY_OPERATOR_TOKENS
from ..statements import RUBY_STATEMENT_TOKENS

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

