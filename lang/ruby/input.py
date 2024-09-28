from talon import Module, Context, actions
from .token import RUBY_TOKENS

ctx = Context()
ctx.matches = "title: /.*\.rb (.*) - VIM/"

mod = Module()
mod.list("tokeny_input_blank", desc="Input for tokens without capture")
mod.list("tokeny_input_text", desc="Input for text tokens")
mod.list("tokeny_input_decimal_number", desc="Input for number tokens")
mod.list("tokeny_input_snake_name", desc="Input for variable name tokens")
mod.list("tokeny_input_class_name", desc="Input for class name tokens")
mod.list("tokeny_input_const_name", desc="Input for const name tokens")
mod.list("tokeny_input_file_path", desc="Input for file path tokens")

TOKENY_LISTS = {}

def register_tokens(tokens):
    for name, token in tokens.items():
        register_input(name, token)
        register_search(name, token)
        register_select(name, token)

    return TOKENY_LISTS

def register_input(name, token):
    input = token.get("input", {})

    if not input:
        return

    list = f"user.tokeny_input_{input['capture']}"

    if list not in TOKENY_LISTS:
        TOKENY_LISTS[list] = {}

    for variation, actions in input.items():
        if variation == "capture":
            continue

        for action in actions:
            TOKENY_LISTS[list][action] = f"{name} {variation}"

def register_search(name, token):
    search = token["search"]

    for capture in search["captures"]:
        list = f"user.tokeny_search_{capture}"

        if list not in TOKENY_LISTS:
            TOKENY_LISTS[list] = {}

        for action in search["actions"]:
            TOKENY_LISTS[list][action] = f"{name}"

def register_select(name, token):
    pass

lists = register_tokens(RUBY_TOKENS)
print(lists)

for name, list in lists.items():
    ctx.lists[name] = lists[name]

