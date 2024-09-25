from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_COMMENT_TOKENS = {
    "comment": {
        "input": {
            "capture": "text",
            "remark": "base",
            "multi remark": "multi",
        },
        "search": { }
    },
    "frozen_string": {
        "input": {
            "frozen string": "base"
        },
        "search": { }
    },
    "magic_encode": {
        "input": {
            "capture": "snake_name",
            "magic encode": "base"
        },
        "search": { }
    },
    "magic_warn": {
        "input": {
            "capture": "snake_name",
            "magic warn": "base"
        },
        "search": { }
    },
    "magic_share": {
        "input": {
            "capture": "snake_name",
            "magic share": "base"
        },
        "search": { }
    },
}
