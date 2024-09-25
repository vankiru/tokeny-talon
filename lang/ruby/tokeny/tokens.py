from ..arguments import RUBY_ARGUMENT_TOKENS
from ..blocks import RUBY_BLOCK_TOKENS
from ..classes import RUBY_CLASS_TOKENS
from ..comments import RUBY_COMMENT_TOKENS
from ..controls import RUBY_CONTROL_TOKENS
from ..data_types import RUBY_DATA_TYPE_TOKENS

RUBY_TOKENS = {
    **RUBY_ARGUMENT_TOKENS,
    **RUBY_BLOCK_TOKENS,
    **RUBY_CLASS_TOKENS,
    **RUBY_COMMENT_TOKENS,
    **RUBY_CONTROL_TOKENS,
    **RUBY_DATA_TYPE_TOKENS,
}

