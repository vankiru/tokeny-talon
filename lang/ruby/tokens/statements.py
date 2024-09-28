from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_STATEMENT_TOKENS = {
    "require": {
        "input": {
            "capture": "file_path",
            "base": ["require"],
        },
        "search": {
            "captures": ["file_path"],
            "actions": ["require"],
        },
    },
    "undef": {
        "input": {
            "capture": "snake_name",
            "base": ["un death", "undead", "unbind"],
        },
        "search": {
            "captures": ["snake_name"],
            "actions": ["un death", "undead", "unbind"],
        },
    },
    "defined": {
        "input": {
            "capture": "snake_name",
            "base": ["defined"],
        },
        "search": {
            "captures": ["snake_name"],
            "actions": ["defined"],
        },
    },
    "attr_reader": {
        "input": {
            "capture": "blank",
            "base": ["art read"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["art read"],
        },
    },
    "attr_writer": {
        "input": {
            "capture": "blank",
            "base": ["art write", "art right"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["art write", "art right"],
        },
    },
    "attr_accessor": {
        "input": {
            "capture": "blank",
            "base": ["art access", "art axis"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["art access", "art axis"],
        },
    },
}
