from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_MODULE_TOKENS = {
    "module": {
        "input": {
            "capture": "class_name",
            "base": ["module", "model"],
        },
        "search": {
            "captures": ["class_name"],
            "actions": ["module", "model"],
        },
    },
    "refine": {
        "input": {
            "capture": "class_name",
            "base": ["refine"],
        },
        "search": {
            "captures": ["class_name"],
            "actions": ["refine"],
        },
    },
    "include": {
        "input": {
            "capture": "class_name",
            "base": ["include"],
        },
        "search": {
            "captures": ["class_name"],
            "actions": ["include"],
        },
    },
    "extend": {
        "input": {
            "capture": "class_name",
            "base": ["extend"],
        },
        "search": {
            "captures": ["class_name"],
            "actions": ["extend"],
        },
    },
    "using": {
        "input": {
            "capture": "class_name",
            "base": ["using"],
        },
        "search": {
            "captures": ["class_name"],
            "actions": ["using"],
        },
    },
}
