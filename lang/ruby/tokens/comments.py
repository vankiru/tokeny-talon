from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_COMMENT_TOKENS = {
    "comment": {
        "input": {
            "capture": "text",
            "base": ["remark"],
            "multi": ["multi remark"],
        },
        "search": {
            "captures": ["text"],
            "actions": ["remark"],
        },
    },
    "frozen_string": {
        "input": {
            "capture": "blank",
            "base": ["frozen string"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["frozen string"],
        },
    },
    "magic_encode": {
        "input": {
            "capture": "snake_name",
            "base": ["magic encode"],
        },
        "search": {
            "captures": ["snake_name"],
            "actions": ["magic encode"],
        },
    },
    "magic_warn": {
        "input": {
            "capture": "snake_name",
            "base": ["magic warn"],
        },
        "search": {
            "captures": ["snake_name"],
            "actions": ["magic warn"],
        },
    },
    "magic_share": {
        "input": {
            "capture": "snake_name",
            "base": ["magic share"],
        },
        "search": {
            "captures": ["snake_name"],
            "actions": ["magic share"],
        },
    },
}
