from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_NAME_TOKENS = {
    "variable_name": {
        "input": {
            "capture": "snake_name",
            "name": "base"
        },
        "search": { }
    },
    "instance_variable_name": {
        "input": {
            "capture": "snake_name",
            "instance": "base"
        },
        "search": { }
    },
    "class_variable_name": {
        "input": {
            "capture": "snake_name",
            "class instance": "base"
        },
        "search": { }
    },
    "global_name": {
        "input": {
            "capture": "snake_name",
            "global": "base"
        },
        "search": { }
    },
    "method_name": {
        "input": {
            "capture": "snake_name",
            "bang": "bang",
            "bank": "bang",
            "plight": "plight",
            "self": "self"
        },
        "search": { }
    },
    "const_name": {
        "input": {
            "capture": "const_name",
            "const": "base"
        },
        "search": { }
    },
    "class_name": {
        "input": {
            "capture": "class_name",
            "type": "base",
            "pack": "pack",
        },
        "search": { }
    },
}
