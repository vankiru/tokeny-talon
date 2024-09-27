from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

RUBY_METHOD_TOKENS = {
    "method": {
        "input": {
            "capture": "snake_name",
            "def": "base",
            "deaf": "base",
            "death": "base",
            "met": "base",
            "meth": "base",
            "short def": "short",
            "short deaf": "short",
            "short death": "short",
            "short met": "short",
            "short meth": "short"
        },
        "search": { }
    },
    "call": {
        "input": {
            "capture": "snake_name",
            "call": "base",
            "cold": "base",
            "safe call": "safe",
            "safe cold": "safe",
        },
        "search": { }
    },
}
