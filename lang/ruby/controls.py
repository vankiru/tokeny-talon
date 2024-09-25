from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_CONTROL_TOKENS = {
    "if": {
        "input": {
            "if": "inline",
            "if do": "multi",
            "if end": "multi",
            "leaf": "multi"
        },
        "search": { }
    },
    "unless": {
        "input": {
            "unless": "inline",
            "unless do": "multi",
            "unless end": "multi"
        },
        "search": { }
    },
    "while": {
        "input": {
            "while": "inline",
            "while do": "multi",
            "while end": "multi"
        },
        "search": { }
    },
    "until": {
        "input": {
            "until": "inline",
            "until do": "multi",
            "until end": "multi"
        },
        "search": { }
    },
    "else": {
        "input": {
            "else": "base"
        },
        "search": { }
    },
    "elsif": {
        "input": {
            "else if": "base"
        },
        "search": { }
    },
    "triple": {
        "input": {
            "triple": "base"
        },
        "search": { }
    },
    "case": {
        "input": {
            "case": "base"
        },
        "search": { }
    },
    "when": {
        "input": {
            "when": "base"
        },
        "search": { }
    },
    "then": {
        "input": {
            "then do": "base"
        },
        "search": { }
    },
    "begin": {
        "input": {
            "begin do": "base"
        },
        "search": { }
    },
    "end": {
        "input": {
            "do end": "base"
        },
        "search": { }
    },
    "break": {
        "input": {
            "break": "base"
        },
        "search": { }
    },
    "next": {
        "input": {
            "next do": "base"
        },
        "search": { }
    },
}
