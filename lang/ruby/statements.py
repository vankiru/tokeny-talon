from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_STATEMENT_TOKENS = {
    "require": {
        "input": {
            "capture": "file_path",
            "require": "base",
        },
        "search": { }
    },
    "undef": {
        "input": {
            "capture": "snake_name",
            "un death": "base",
            "undead": "base",
        },
        "search": { }
    },
    "defined": {
        "input": {
            "capture": "snake_name",
            "defined": "base"
        },
        "search": { }
    },
    "attr_reader": {
        "input": {
            "art read": "base"
        },
        "search": { }
    },
    "attr_writer": {
        "input": {
            "art write": "base",
            "art right": "base"
        },
        "search": { }
    },
    "attr_accessor": {
        "input": {
            "art access": "base",
            "art axis": "base",
        },
        "search": { }
    },
}
