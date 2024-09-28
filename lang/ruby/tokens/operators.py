from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_OPERATOR_TOKENS = {
    "set_to": {
        "input": {
            "capture": "blank",
            "base": ["set to", "set two", "said to", "said two"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["set to", "set two", "said to", "said two"],
        },
    },
    "index": {
        "input": {
            "capture": "blank",
            "base": ["index"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["index"],
        },
    },
    "plus": {
        "input": {
            "capture": "blank",
            "base": ["plus"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["plus"],
        },
    },
    "minus": {
        "input": {
            "capture": "blank",
            "base": ["minus"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["minus"],
        },
    },
    "multi": {
        "input": {
            "capture": "blank",
            "base": ["multi"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["multi"],
        },
    },
    "divide": {
        "input": {
            "capture": "blank",
            "base": ["divide"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["divide"],
        },
    },
    "mod": {
        "input": {
            "capture": "blank",
            "base": ["mode", "modulus"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["mode", "modulus"],
        },
    },
    "power": {
        "input": {
            "capture": "blank",
            "base": ["power"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["power"],
        },
    },
    "plus_equal": {
        "input": {
            "capture": "blank",
            "base": ["plus equal"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["plus equal"],
        },
    },
    "minus_equal": {
        "input": {
            "capture": "blank",
            "base": ["minus equal"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["minus equal"],
        },
    },
    "multi_equal": {
        "input": {
            "capture": "blank",
            "base": ["multi equal"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["multi equal"],
        },
    },
    "divide_equal": {
        "input": {
            "capture": "blank",
            "base": ["divide equal"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["divide equal"],
        },
    },
    "mod_equal": {
        "input": {
            "capture": "blank",
            "base": ["mode equal", "modulus equal"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["mode equal", "modulus equal"],
        },
    },
    "power_equal": {
        "input": {
            "capture": "blank",
            "base": ["power equal"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["power equal"],
        },
    },
    "equal": {
        "input": {
            "capture": "blank",
            "base": ["equal"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["equal"],
        },
    },
    "not_equal": {
        "input": {
            "capture": "blank",
            "base": ["not equal"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["not equal"],
        },
    },
    "great": {
        "input": {
            "capture": "blank",
            "base": ["great"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["great"],
        },
    },
    "less": {
        "input": {
            "capture": "blank",
            "base": ["less"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["less"],
        },
    },
    "great_equal": {
        "input": {
            "capture": "blank",
            "base": ["great equal"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["great equal"],
        },
    },
    "less_equal": {
        "input": {
            "capture": "blank",
            "base": ["less equal"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["less equal"],
        },
    },
    "test_equal": {
        "input": {
            "capture": "blank",
            "base": ["test equal"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["test equal"],
        },
    },
    "compare": {
        "input": {
            "capture": "blank",
            "base": ["compare"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["compare"],
        },
    },
    "and": {
        "input": {
            "capture": "blank",
            "base": ["also"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["also"],
        },
    },
    "or": {
        "input": {
            "capture": "blank",
            "base": ["either"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["either"],
        },
    },
    "not": {
        "input": {
            "capture": "blank",
            "base": ["not"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["not"],
        },
    },
    "in": {
        "input": {
            "capture": "blank",
            "base": ["inside"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["inside"],
        },
    },
    "match": {
        "input": {
            "capture": "blank",
            "base": ["match", "much"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["match", "much"],
        },
    },
    "bit_and": {
        "input": {
            "capture": "blank",
            "base": ["bit and", "bit add", "bit also"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["bit and", "bit add", "bit also"],
        },
    },
    "bit_or": {
        "input": {
            "capture": "blank",
            "base": ["bit or", "bit either"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["bit or", "bit either"],
        },
    },
    "bit_xor": {
        "input": {
            "capture": "blank",
            "base": ["bit ex"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["bit ex"],
        },
    },
    "bit_not": {
        "input": {
            "capture": "blank",
            "base": ["bit not"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["bit not"],
        },
    },
    "shift_left": {
        "input": {
            "capture": "blank",
            "base": ["shift left"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["shift left"],
        },
    },
    "shift_right": {
        "input": {
            "capture": "blank",
            "base": ["shift right"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["shift right"],
        },
    },
}
