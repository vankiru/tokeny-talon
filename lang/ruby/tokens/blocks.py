from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_BLOCK_TOKENS = {
    "block": {
        "input": {
            "capture": "blank",
            "inline": ["block"],
            "block": ["block do", "block end"]
        },
        "search": {
            "captures": ["blank"],
            "actions": ["block"],
        },
    },
}
