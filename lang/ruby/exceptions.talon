title: /.*\.rb (.*) - VIM/
-

error ({user.exception_name} | <user.class_name>):
  user.vim_tokeny_insert("name base", exception_name or class_name)

(raise | rise):
  user.vim_tokeny_insert("raise empty")

(raise | rise) ({user.exception_name} | <user.class_name>):
  user.vim_tokeny_insert("raise base", exception_name or class_name)

rescue:
  user.vim_tokeny_insert("rescue empty")

rescue <user.class_name>:
  user.vim_tokeny_insert("rescue class", class_name)

rescue as <user.variable_name>:
  user.vim_tokeny_insert("rescue variable", variable_name)

rescue <user.class_name> as <user.variable_name>:
  user.vim_tokeny_insert("rescue class_variable", "{class_name} {variable_name}")

(ensure | insure):
  user.vim_insert_mode("ensure", "o")
