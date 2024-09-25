@mod.action_class
class Actions:
    def code_go_to(token: str, identifier: str = ""):
        """Go to the next token"""

    def code_back_to(token: str, identifier: str = ""):
        """Go to the next token"""

    def code_search(token: str, identifier: str = "", direction: str = "/"):
        """Search for a token"""

@ctx.action_class("user")
class CodeActions:
    def code_go_to(token: str, identifier: str = ""):
        actions.user.vim_command_mode("TokenyTo {str} {identifier}")

    def code_back_to(token: str, identifier: str = ""):
        actions.user.vim_command_mode("TokenyBack {str} {identifier}")

    def code_search(token: str, identifier: str = "", direction: str = "/"):
        actions.user.vim_command_mode("TokenySearch {str} {identifier}")
