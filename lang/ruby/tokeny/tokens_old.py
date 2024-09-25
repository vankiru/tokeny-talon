from talon import Module, Context, actions

mod = Module()
# mod.list("nameless_token_regex", desc="Regex for nameless tokens")
# mod.list("number_token_regex", desc="Regex for number tokens")
# mod.list("text_token_regex", desc="Regex for text tokens")
# mod.list("snake_name_token_regex", desc="Regex for snake name tokens")
# mod.list("class_name_token_regex", desc="Regex for class name tokens")
# mod.list("const_name_token_regex", desc="Regex for const name tokens")
# mod.list("file_name_token_regex", desc="Regex for file name tokens")


tokens = {
    # arguments
    "comma": {"name": "comma"},
    "art": {
        "name": "art",
        "id": "snake_name,class_name,number"
    },
    "arts": {
        "name": "arts",
        "id": "snake_name,class_name,number"
    },
    "barbs": {
        "name": "barbs",
        "id": "snake_name,class_name,number"
    },

    # blocks
    "block": {"name": "block"},

    # classes
    "class": {
        "name": "class",
        "id": "class_name"
    },
    "superclass": {
        "name": "super_class",
        "id": "class_name"
    },
    "self class": {"name": "self_class"},
    "class init": {"name": "initialize"},
    "private": {
        "name": "private",
        "id": "snake_name"
    },
    "protected": {
        "name": "protected",
        "id": "snake_name"
    },
    "public": {
        "name": "public",
        "id": "snake_name"
    },
    "new": {
        "name": "new",
        "id": ["class_name"]
    },

    # comments
    "comment": {
        "name": "remark",
        "id": "text"
    },
    "frozen string": {"name": "frozen_string"},
    "magic encode": {
        "name": "magic_encode",
        "id": "snake_name"
    },
    "magic warn": {
        "name": "magic_warn",
        "id": "snake_name"
    },

    # controls
    "if": {
        "name": "if",
        "id": "snake_name,class_name,number"
    },
    "else": {
        "name": "else",
        "id": "snake_name,class_name,number"
    },
    "else if": {
        "name": "elsif",
        "id": "snake_name,class_name,number"
    },
    "unless": {
        "name": "unless",
        "id": "snake_name,class_name,number"
    },
    "triple": {
        "name": "tripple",
        "id": "snake_name,class_name,number"
    },
    "case": {
        "name": "case",
        "id": "snake_name,class_name,number"
    },
    "when": {
        "name": "when",
        "id": "snake_name,class_name,number"
    },
    "then": {
        "name": "then",
        "id": "snake_name,class_name,number"
    },
    "while": {
        "name": "while",
        "id": "snake_name,class_name,number"
    },
    "until": {
        "name": "until",
        "id": "snake_name,class_name,number"
    },
    "break": {
        "name": "break",
        "id": "snake_name,class_name,number"
    },
    "next": {
        "name": "next",
        "id": "snake_name,class_name,number"
    },
}

noname_tokens = [
    "comma",
    "block",
    "superclass": "super_class",
    "self class": "self_class",
    "class init": "initialize",
    "forzen string": "frozen_string"
    "else"
    "ensure"
    "retry"
    # operators
    "set_to"
    "plus"
    "minus"
    "multi"
    "divide"
    "mod"
    "power"
    "plus_equal"
    "minus_equal"
    "multi_equal"
    "divide_equal"
    "mod_equal"
    "power_equal"
    "equal"
    "not_equal"
    "great"
    "less"
    "great_equal"
    "less_equal"
    "compare"
    "test_equal"
    "and"
    "or"
    "not"
    "in"
    "match"
    "bit_and"
    "bit_or"
    "bit_xor"
    "bit_not"
    "shift_left"
    "shift_right"
]


ctx.lists["user.simple_tokens"] = {
    # data types
    "true": "true",
    "false": "false",
    "none": "nil",
    "nun": "nil",
    "list": "array",
    "hash": "hash",
    "set": "set",
    "lambda": "lambda",
    # exceptions
    "begin": "begin",
    "ensure": "ensure",
    "retry": "retry",
    # methods
    "return": "return",
    "parent": "super",
    "yeild": "yield",
    "yeild self": "yeild self",
    # operators
    "set to": "set_to",
    "plus": "plus",
    "minus": "minus",
    "multi": "multi",
    "divide": "divide",
    "modulus": "modulus",
    "power": "power",
    "plus equal": "plus_equal",
    "minus equal": "minus_equal",
    "multi equal": "multi_equal",
    "divide equal": "divide_equal",
    "mod equal": "mod_equal",
    "power equal": "power_equal",
    "equal": "equal",
    "not equal": "not_equal",
    "great": "great",
    "less": "less",
    "great equal": "great_equal",
    "less equal": "less_equal",
    "compare": "compare",
    "test equal": "test_equal",
    "also": "also",
    "either": "either",
    "not": "not",
    "index": "index",
    "inside": "inside",
    "match": "match",
    "bit and": "bit_and",
    "bit or": "bit_or",
    "bit ex": "bit_ex",
    "bit not": "bit_not",
    "shift left": "shift_left",
    "shift right": "shift_right",
    # library
    "print": "puts",
}

ctx.lists["user.number_tokens"] = {
    # data types
    "number": "number",
    "range": "range",
    "range to": "(\.\.{identifier}\d*)",
    "range by": "(\.\.{identifier}\d*)",
    "range until": "(\.\.\.{identifier}\d*)",
}

ctx.lists["user.text_tokens"] = {
    # data types
    "string": "string",
    "rig": "regex"
}

ctx.lists["user.snake_name_tokens"] = {
    # data types
    "interpol": "interpolation",
    "sim": "symbol",
    "key": "key",
    # exceptions
    "rescue as": "rescue",
    # methods
    "def": "method",
    "deaf": "method",
    "met": "method",
    "call": "call",
    # names
    "name": "snake_name",
    "instance": "instance_variable_name",
    "type instance": "class_variable_name",
    "self": "self",
    "global": "global",
    # statements
    "unbind": "undef",
    "defined": "defined"
    "art read": "attr_reader",
    "art write": "attr_writer",
    "art access": "attr_accessor",
}

ctx.lists["user.class_name_tokens"] = {
    # exceptions
    "raise": "raise",
    "rescue": "rescue",
    # modules
    "module": "module",
    "model": "module",
    "refine": "refine",
    "include": "include",
    "extend": "extend",
    "using": "using",
    # names
    "type": "class_name"
}

ctx.lists["user.const_name_tokens"] = {
    "const": "const",
}

ctx.lists["user.file_name_tokens"] = {
    "require": "require",
}
snake_name_tokens = [
    "private"
    "protected"
    "public"
    "comment"
    "magic encode": "magic_encode"
    "magic warn": "magic_warn"
    "if"
    "unless"
    "while"
    "until"
    "else if": "elsif"
    "tripple"
    "case"
    "when"
    "then"
    "begin"
    "break"
    "next"
    "return"
    "yield"
    "super"

    "attr_reader"
    "attr_writer"
    "attr_accessor"
]
