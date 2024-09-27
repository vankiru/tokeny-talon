from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_MODULE_TOKENS = {
    "module": {
        "input": {
            "capture": "class_name",
            "module": "base",
            "model": "base",
        },
        "search": { }
    },
    "refine": {
        "input": {
            "capture": "class_name",
            "refine": "base",
        },
        "search": { }
    },
    "include": {
        "input": {
            "capture": "class_name",
            "include": "base",
        },
        "search": { }
    },
    "extend": {
        "input": {
            "capture": "class_name",
            "extend": "base",
        },
        "search": { }
    },
    "using": {
        "input": {
            "capture": "class_name",
            "using": "base",
        },
        "search": { }
    },
}
