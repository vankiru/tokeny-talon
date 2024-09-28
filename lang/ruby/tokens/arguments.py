from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_ARGUMENT_TOKENS = {
    "comma": {
        "input": {
            "capture": "blank",
            "base": ["comma", "coma"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["comma", "coma"]
        },
    },
    "art": {
        "input": {
            "capture": "snake_name",
            "list": ["list art"],
            "hash": ["hash art"],
            "block": ["block art"],
            "default": ["default to"],
        },
        "search": {
            "captures": [],
            "actions": []
        },
    },
    "arts": {
        "input": {
            "capture": "blank",
            "base": ["arts"],
            "left": ["left art"],
            "right": ["right art"],
        },
        "search": {
            "captures": ["snake_name"],
            "actions": ["arts", "art"],
        },
    },
    "barbs": {
        "input": {
            "capture": "blank",
            "base": ["barbs"],
            "single": ["barb"],
        },
        "search": {
            "captures": ["snake_name"],
            "actions": ["barbs", "barb"],
        },
    }
}
