from talon import Context, Module, actions

mod = Module()
mod.tag("code_names", desc="Names commands")

# Number captures

@mod.capture(rule="<user.number_string> [point <user.number_string>]")
def decimal_number(m) -> str:
    return ".".join(m.number_string_list)

# Case captures

@mod.capture(rule="<user.text>")
def snake_name(m) -> str:
    return actions.user.code_snake_case(m.text)

@mod.capture(rule="<user.text>")
def screaming_name(m) -> str:
    return actions.user.code_screaming_case(m.text)

@mod.capture(rule="<user.text>")
def camel_name(m) -> str:
    return actions.user.code_camel_case(m.text)

# Names captures

@mod.capture(rule="<user.snake_name>")
def key_name(m) -> str:
    return m.snake_name

@mod.capture(rule="<user.snake_name>")
def variable_name(m) -> str:
    return m.snake_name

@mod.capture(rule="<user.snake_name>")
def method_name(m) -> str:
    return m.snake_name

@mod.capture(rule="<user.screaming_name>")
def const_name(m) -> str:
    return m.screaming_name

@mod.capture(rule="<user.camel_name>")
def class_name(m) -> str:
    return m.camel_name

@mod.capture(rule="<user.snake_name>")
def file_name(m) -> str:
    return m.snake_name

@mod.capture(rule="<user.file_name> (slash <user.file_name>)")
def file_path(m) -> str:
    names = list(
        filter(
            lambda n: n != "slash",
            list(m)
        )
    )

    return "/".join(names)

