from talon import Context, Module, actions
import pyperclip

mod = Module()
ctx = Context()
ctx.matches = "title: /VIM/"

@mod.action_class
class Actions:
    def pyperclip_insert(text: str):
        """Insert via copying to clipboard"""

    def vim_tokeny_insert(variation: str, values: str = ''):
        """Execute TokenyInsert"""

    def vim_tokeny_to(token: str, id: str = ''):
        """Execute TokenyTo"""

    def vim_tokeny_back(token: str, id: str = ''):
        """Execute TokenyBack"""

    def vim_tokeny_search(token: str, id: str = ''):
        """Execute TokenySearch"""

@ctx.action_class("user")
class TokenyActions:
    def pyperclip_insert(text: str):
        print("!!!!!!!!!")
        print(text)
        pyperclip.copy(text)
        actions.key('super-v')

    def vim_tokeny_insert(variation: str, values: str = ''):
        actions.user.vim_command_mode(f"TokenyInsert {variation} {values}")

    def vim_tokeny_to(token: str, id: str = ''):
        actions.user.vim_command_mode(f"TokenyTo {token} {id}")

    def vim_tokeny_back(token: str, id: str = ''):
        actions.user.vim_command_mode(f"TokenyBack {token} {id}")

    def vim_tokeny_search(token: str, id: str = ''):
        actions.user.vim_command_mode(f"TokenySearch {token} {id}")
