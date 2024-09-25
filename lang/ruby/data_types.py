from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_DATA_TYPE_TOKENS = {
    "true": {
        "input": {
            "true": "base",
        },
        "search": { }
    },
    "false": {
        "input": {
            "false": "base",
        },
        "search": { }
    },
    "nil": {
        "input": {
            "none": "base",
            "nun": "base"
        },
        "search": { }
    },
    "number": {
        "input": {
            "capture": "decimal_number",
            "number": "positive"
        },
        "search": { }
    },
    "string": {
        "input": {
            "capture": "text",
            "string": "double",
            "quote": "quote",
            "grave": "grave",
            "docs": "heredoc"
        },
        "search": { }
    },
    "symbol": {
        "input": {
            "capture": "snake_name",
            "sim": "base"
        },
        "search": { }
    },
    "regex": {
        "input": {
            "capture": "text",
            "rig": "base",
            "object rig": "object"
        },
        "search": { }
    },
    "array": {
        "input": {
            "list": "base",
            "sim list": "sim",
            "string list": "string",
            "object list": "object"
        },
        "search": { }
    },
    "hash": {
        "input": {
            "hash": "base",
            "object hash": "object"
        },
        "search": { }
    },
    "set": {
        "input": {
            "set list": "base"
        },
        "search": { }
    },
    "lambda": {
        "input": {
            "lambda": "lambda",
            "proc": "proc"
        },
        "search": { }
    },
    "range": {
        "input": {
            "capture": "decimal_number",
            "range": "left_by",
            "range to": "right_by",
            "range by": "right_by",
            "range until": "right_until",
        },
        "search": { }
    }
}
