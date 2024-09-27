from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_BLOCK_TOKENS = {
    "block": {
        "input": {
            "block": "inline",
            "block do": "block",
            "block end": "block"
        },
        "search": { }
    },
}
