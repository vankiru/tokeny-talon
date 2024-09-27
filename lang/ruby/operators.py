from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_OPERATOR_TOKENS = {
    "set_to": {
        "input": {
            "set to": "base",
            "set two": "base",
            "said to": "base",
            "said two": "base"
        },
        "search": { }
    },
    "index": {
        "input": {"index": "base"},
        "search": { }
    },
    "plus": {
        "input": {"plus": "base"},
        "search": { }
    },
    "minus": {
        "input": {"minus": "base"},
        "search": { }
    },
    "multi": {
        "input": {"multi": "base"},
        "search": { }
    },
    "divide": {
        "input": {"divide": "base"},
        "search": { }
    },
    "mod": {
        "input": {
            "mode": "base",
            "modulus": "base"
        },
        "search": { }
    },
    "power": {
        "input": {"power": "base"},
        "search": { }
    },
    "plus_equal": {
        "input": {"plus equal": "base"},
        "search": { }
    },
    "minus_equal": {
        "input": {"minus equal": "base"},
        "search": { }
    },
    "multi_equal": {
        "input": {"multi equal": "base"},
        "search": { }
    },
    "divide_equal": {
        "input": {"divide equal": "base"},
        "search": { }
    },
    "mod_equal": {
        "input": {
            "mode equal": "base",
            "modulus equal": "base"
        },
        "search": { }
    },
    "power_equal": {
        "input": {"power equal": "base"},
        "search": { }
    },
    "equal": {
        "input": {"equal": "base"},
        "search": { }
    },
    "not_equal": {
        "input": {"not equal": "base"},
        "search": { }
    },
    "great": {
        "input": {"great": "base"},
        "search": { }
    },
    "less": {
        "input": {"less": "base"},
        "search": { }
    },
    "great_equal": {
        "input": {"great equal": "base"},
        "search": { }
    },
    "less_equal": {
        "input": {"less equal": "base"},
        "search": { }
    },
    "test_equal": {
        "input": {"test equal": "base"},
        "search": { }
    },
    "compare": {
        "input": {"compare": "base"},
        "search": { }
    },
    "and": {
        "input": {"also": "base"},
        "search": { }
    },
    "or": {
        "input": {"either": "base"},
        "search": { }
    },
    "not": {
        "input": {"not": "base"},
        "search": { }
    },
    "in": {
        "input": {"inside": "base"},
        "search": { }
    },
    "match": {
        "input": {
            "match": "base",
            "much": "base"
        },
        "search": { }
    },
    "bit_and": {
        "input": {
            "bit and": "base",
            "bit add": "base",
            "bit also": "base"
        },
        "search": { }
    },
    "bit_or": {
        "input": {
            "bit or": "base",
            "bit either": "base"
        },
        "search": { }
    },
    "bit_xor": {
        "input": {"bit ex": "base"},
        "search": { }
    },
    "bit_not": {
        "input": {"bit not": "base"},
        "search": { }
    },
    "shift_left": {
        "input": {"shift left": "base"},
        "search": { }
    },
    "shift_right": {
        "input": {"shift right": "base"},
        "search": { }
    },
}
