from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_NAME_TOKENS = {
    "variable_name": {
        "search": {
            "captures": ["snake_name"],
            "actions": ["name"],
        },
    },
    "instance_variable_name": {
        "search": {
            "captures": ["snake_name"],
            "actions": ["instance"],
        },
    },
    "class_variable_name": {
        "search": {
            "captures": ["snake_name"],
            "actions": ["class instance"],
        },
    },
    "global_name": {
        "search": {
            "captures": ["snake_name"],
            "actions": ["global"],
        },
    },
    "method_name": {
        "search": {
            "captures": ["snake_name"],
            "actions": ["met name"],
        },
    },
    "const_name": {
        "search": {
            "captures": ["const_name"],
            "actions": ["const"],
        },
    },
    "class_name": {
        "search": {
            "captures": ["class_name"],
            "actions": ["type"],
        },
    },
}
