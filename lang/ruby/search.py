from talon import Module, Context, actions
from .token import RUBY_TOKENS

ctx = Context()
ctx.matches = "title: /.*\.rb (.*) - VIM/"

mod = Module()
mod.list("tokeny_search_blank", desc="Search for tokens without capture")
mod.list("tokeny_search_text", desc="Search for text tokens")
mod.list("tokeny_search_decimal_number", desc="Search for number tokens")
mod.list("tokeny_search_snake_name", desc="Search for variable name tokens")
mod.list("tokeny_search_class_name", desc="Search for class name tokens")
mod.list("tokeny_search_const_name", desc="Search for const name tokens")
mod.list("tokeny_search_file_path", desc="Search for file path tokens")
mod.list("tokeny_search_expression", desc="Search for expression tokens")
