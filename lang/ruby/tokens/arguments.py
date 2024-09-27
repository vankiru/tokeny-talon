from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_ARGUMENT_TOKENS = {
    "comma": {
        "input": {
            "comma": "base",
            "coma": "base" 
        }
    },
    "art": {
        "input": {
            "capture": "snake_name",
            "list art": "list",
            "hash art": "hash",
            "block art": "block",
            "default to": "default"
        },
        "search": { }
    },
    "arts": {
        "input": {
            "arts": "base",
            "left art": "left",
            "right art": "right"
        },
        "search": { }
    },
    "barbs": {
        "input": {
            "barbs": "base",
            "barb": "single"
        }
    }
}
