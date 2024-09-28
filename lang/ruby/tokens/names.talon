title: /\w*\.rb (.*) - VIM/
-

name <user.snake_name>:
  user.vim_tokeny_insert("variable_name base", snake_name)

instance <user.snake_name>:
  user.vim_tokeny_insert("instance_variable_name base", snake_name)

class instance <user.snake_name>:
  user.vim_tokeny_insert("class_variable_name base", snake_name)

global <user.snake_name>:
  user.vim_tokeny_insert("global_name base", snake_name)

(bang | bank) <user.snake_name>:
  user.vim_tokeny_insert("method_name bang", snake_name)

(plight | plied) <user.snake_name>:
  user.vim_tokeny_insert("method_name plight", snake_name)

self <user.snake_name>:
  user.vim_tokeny_insert("method_name self", snake_name)

const <user.const_name>:
  user.vim_tokeny_insert("const_name base", const_name)

type <user.class_name>:
  user.vim_tokeny_insert("class_name base", class_name)

pack <user.class_name>:
  user.vim_tokeny_insert("class_name pack", class_name)
