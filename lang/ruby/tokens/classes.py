from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_CLASS_TOKENS = {
    "class": {
        "input": {
            "capture": "class_name",
            "base": ["class"],
        },
        "search": {
            "captures": ["class_name"],
            "actions": ["class"],
        },
    },
    "super_class": {
        "input": {
            "capture": "class_name",
            "base": ["superclass"],
        },
        "search": {
            "captures": ["class_name"],
            "actions": ["superclass"],
        },
    },
    "self_class": {
        "input": {
            "capture": "blank",
            "base": ["self class"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["self class"],
        },
    },
    "initialize": {
        "input": {
            "capture": "blank",
            "base": ["class init"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["class init"],
        },
    },
    "new": {
        "input": {
            "capture": "class_name",
            "base": ["new"],
        },
        "search": {
            "captures": ["class_name"],
            "actions": ["new"],
        },
    },
    "private": {
        "input": {
            "capture": "blank",
            "base": ["private"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["private"],
        },
    },
    "protected": {
        "input": {
            "capture": "blank",
            "base": ["protected"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["protected"],
        },
    },
    "public": {
        "input": {
            "capture": "blank",
            "base": ["public"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["public"],
        },
    },
}
