from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_CLASS_TOKENS = {
    "class": {
        "input": {
            "capture": "class_name",
            "class": "base"
        },
        "search": { }
    },
    "super_class": {
        "input": {
            "capture": "class_name",
            "superclass": "base"
        },
        "search": { }
    },
    "self_class": {
        "input": {
            "self class": "base"
        },
        "search": { }
    },
    "initialize": {
        "input": {
            "class init": "base"
        },
        "search": { }
    },
    "new": {
        "input": {
            "capture": "class_name",
            "new": "base"
        },
        "search": { }
    },
    "private": {
        "input": {
            "private": "base"
        },
        "search": { }
    },
    "protected": {
        "input": {
            "protected": "base"
        },
        "search": { }
    },
    "public": {
        "input": {
            "public": "base"
        },
        "search": { }
    },
}
