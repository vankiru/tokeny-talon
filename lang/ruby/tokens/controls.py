from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_CONTROL_TOKENS = {
    "if": {
        "input": {
            "capture": "blank",
            "inline": ["if"],
            "multi": ["if do", "if end", "leaf"]
        },
        "search": {
            "captures": ["expression"],
            "actions": ["if"],
        },
    },
    "unless": {
        "input": {
            "capture": "blank",
            "inline": ["unless"],
            "multi": ["unless do", "unless end"]
        },
        "search": {
            "captures": ["expression"],
            "actions": ["unless"],
        },
    },
    "while": {
        "input": {
            "capture": "blank",
            "inline": ["while"],
            "multi": ["while do", "while end"]
        },
        "search": {
            "captures": ["expression"],
            "actions": ["while"],
        },
    },
    "until": {
        "input": {
            "capture": "blank",
            "inline": ["until"],
            "multi": ["until do", "until end"]
        },
        "search": {
            "captures": ["expression"],
            "actions": ["until"],
        },
    },
    "else": {
        "input": {
            "capture": "blank",
            "base": ["else"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["else"],
        },
    },
    "elsif": {
        "input": {
            "capture": "blank",
            "base": ["else if"],
        },
        "search": {
            "captures": ["expression"],
            "actions": ["else if"],
        },
    },
    "triple": {
        "input": {
            "capture": "blank",
            "base": ["triple"],
        },
        "search": {
            "captures": ["expression"],
            "actions": ["triple"],
        },
    },
    "case": {
        "input": {
            "capture": "blank",
            "base": ["case"],
        },
        "search": {
            "captures": ["expression"],
            "actions": ["case"],
        },
    },
    "when": {
        "input": {
            "capture": "blank",
            "base": ["when"],
        },
        "search": {
            "captures": ["expression"],
            "actions": ["when"],
        },
    },
    "then": {
        "input": {
            "capture": "blank",
            "base": ["then do"],
        },
        "search": {
            "captures": ["expression"],
            "actions": ["then do", "then"],
        },
    },
    "begin": {
        "input": {
            "capture": "blank",
            "base": ["begin do"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["begin do", "begin"],
        },
    },
    "end": {
        "input": {
            "capture": "blank",
            "base": ["do end"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["do end", "end"],
        },
    },
    "break": {
        "input": {
            "capture": "blank",
            "base": ["break"],
        },
        "search": {
            "captures": ["expression"],
            "actions": ["break"],
        },
    },
    "next": {
        "input": {
            "capture": "blank",
            "base": ["next do"],
        },
        "search": {
            "captures": ["expression"],
            "actions": ["next"],
        },
    },
}
