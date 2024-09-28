from talon import Context, actions

ctx = Context()
ctx.matches = "title: /.*\.rb (.*) - VIM/"

ctx.lists["user.exception_name"] = {
    "exception": "Exception",
    "no memory": "NoMemoryError",
    "script": "ScriptError",
    "load": "LoadError",
    "not implemented": "NotImplementedError",
    "syntax": "SyntaxError",
    "security": "SecurityError",
    "signal": "SignalException",
    "interrupt": "Interrupt",
    "standard": "StandardError",
    "argument": "ArgumentError",
    "uncaught throw": "UncaughtThrowError",
    "encoding": "EncodingError",
    "fiber": "FiberError",
    "input": "IOError",
    "end file": "EOFError",
    "index": "IndexError",
    "key": "KeyError",
    "stop iteration": "StopIteration",
    "closed queue": "ClosedQueueError",
    "local jump": "LocalJumpError",
    "name": "NameError",
    "no method": "NoMethodError",
    "range": "RangeError",
    "float domain": "FloatDomainError",
    "rig": "RegexpError",
    "runtime": "RuntimeError",
    "frozen": "FrozenError",
    "system call": "SystemCallError",
    "system error": "Errno",
    "thread": "ThreadError",
    "type": "TypeError",
    "zero division": "ZeroDivisionError",
    "system exit": "SystemExit",
    "system stack": "SystemStackError"
}

RUBY_EXCEPTION_TOKENS = {
    "raise": {
        "search": {
            "captures": ["text", "expression"],
            "actions": ["raise", "rise"]
        },
    },
    "rescue": {
        "search": {
            "captures": ["expression"],
            "actions": ["rescue"]
        },
    },
    "ensure": {
        "input": {
            "capture": "blank",
            "base": ["ensure", "insure"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["ensure", "insure"],
        },
    },
    "retry": {
        "input": {
            "capture": "blank",
            "base": ["retry"],
        },
        "search": {
            "captures": ["blank"],
            "actions": ["retry"],
        },
    },
}
