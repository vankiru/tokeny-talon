title: /.*\.rb (.*) - VIM/
-

print:
  user.vim_tokeny_insert("method_name base", "puts")

print <user.text>:
  user.vim_tokeny_insert("method_name base", "puts")
  user.vim_tokeny_insert("string double", text)

call {user.std_method}:
  user.vim_tokeny_insert("call base", std_method)

(safe | save) (call | cold) {user.std_method}:
  user.vim_tokeny_insert("call safe", std_method)

(bang | bank) {user.std_method}:
  user.vim_tokeny_insert("call bang", std_method)
