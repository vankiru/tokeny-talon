from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_DATA_TYPE_TOKENS = {
    "true": {
        "input": {
            "capture": "blank",
            "base": ["true"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["true"],
        },
    },
    "false": {
        "input": {
            "capture": "blank",
            "base": ["false"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["false"],
        },
    },
    "nil": {
        "input": {
            "capture": "blank",
            "base": ["none", "nil"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["none", "nil"],
        },
    },
    "number": {
        "input": {
            "capture": "decimal_number",
            "positive": ["number"],
        },
        "search": {
            "captures": ["decimal_number"],
            "actions": ["number"],
        },
    },
    "string": {
        "input": {
            "capture": "text",
            "double": ["string"],
            "quote": ["quote"],
            "grave": ["grave"],
            "heredoc": ["docs"],
        },
        "search": {
            "captures": ["text"],
            "actions": ["string"],
        },
    },
    "symbol": {
        "input": {
            "capture": "snake_name",
            "base": ["sim"],
        },
        "search": {
            "captures": ["snake_name"],
            "actions": ["sim"],
        },
    },
    "regex": {
        "input": {
            "capture": "text",
            "base": ["rig"],
            "object": ["object rig"],
        },
        "search": {
            "captures": ["text"],
            "actions": ["rig"],
        },
    },
    "array": {
        "input": {
            "capture": "blank",
            "base": ["list"],
            "sim": ["sim list"],
            "string": ["string list"],
            "object": ["object list"],
        },
        "search": {
            "captures": ["expression"],
            "actions": ["list"],
        },
    },
    "hash": {
        "input": {
            "capture": "blank",
            "base": ["hash"],
            "object": ["object hash"],
        },
        "search": {
            "captures": ["expression"],
            "actions": ["hash"],
        },
    },
    "set": {
        "input": {
            "capture": "blank",
            "base": ["set list"],
        },
        "search": {
            "captures": ["expression"],
            "actions": ["set list", "set"],
        },
    },
    "lambda": {
        "input": {
            "capture": "blank",
            "lambda": ["lambda"],
            "proc": ["proc"],
        },
        "search": {
            "captures": ["expression"],
            "actions": ["lambda", "proc"],
        },
    },
    "range": {
        "input": {
            "capture": "decimal_number",
            "left_by": ["range"],
            "right_by": ["range to"],
            "right_by": ["range by"],
            "right_until": ["range until"],
        },
        "search": {
            "captures": ["digital_number"],
            "actions": ["range"],
        },
    },
    "key": {
        "search": {
            "captures": ["expression"],
            "actions": ["key"]
        },
    }
}
