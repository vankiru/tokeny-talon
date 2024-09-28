from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

@ctx.capture('user.class_name', rule="<user.camel_name> ((pack | back) <user.camel_name>)*")
def class_name(m) -> str:
    names = list(
        filter(
            lambda n: n not in ["pack", "back"],
            list(m)
        )
    )

    return "::".join(names)
