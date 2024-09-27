from talon import Module, Context, actions
from .tokens import RUBY_TOKENS

ctx = Context()
ctx.matches = "title: /.*\.rb (.*) - VIM/"

mod = Module()
mod.list("input_no_capture", desc="Input for tokens without capture")
mod.list("input_text", desc="Input for text tokens")
mod.list("input_decimal_number", desc="Input for number tokens")
mod.list("input_snake_name", desc="Input for variable name tokens")
mod.list("input_class_name", desc="Input for class name tokens")
mod.list("input_const_name", desc="Input for const name tokens")
mod.list("input_file_path", desc="Input for file path tokens")

def register_tokens(tokens):
    lists = {}

    for name, token in tokens.items():
        input = token["input"]
        capture = input.get("capture", "no_capture")
        list = f"user.input_{capture}"

        if list not in lists:
            lists[list] = {}
        
        for command, variation in input.items():
            if command == "capture":
                continue

            lists[list][command] = f"{name} {variation}"

    return lists

lists = register_tokens(RUBY_TOKENS)
print(lists)

for name, list in lists.items():
    ctx.lists[name] = lists[name]

