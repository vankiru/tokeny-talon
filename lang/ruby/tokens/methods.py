from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_METHOD_TOKENS = {
    "method": {
        "input": {
            "capture": "snake_name",
            "base": ["def", "deaf", "death", "met", "meth"],
            "short": ["short def", "short deaf", "short death", "short met", "short meth"],
        },
        "search": {
            "captures": ["snake_name"],
            "actions": ["def", "deaf", "death", "met", "meth"],
        },
    },
    "call": {
        "input": {
            "capture": "snake_name",
            "base": ["call", "cold"],
            "safe": ["safe call", "safe cold", "save call", "save cold"],
        },
        "search": {
            "captures": ["snake_name"],
            "actions": ["call", "cold"],
        },
    },
    "return": {
        "search": {
            "captures": ["expression"],
            "actions": ["return"],
        },
    },
    "super": {
        "search": {
            "captures": ["expression"],
            "actions": ["superb"],
        },
    },
    "yield": {
        "search": {
            "captures": ["expression"],
            "actions": ["yield"],
        },
    }
}
