title: /\w*\.rb (.*) - VIM/
-

return:
  user.vim_tokeny_insert("return empty")

return <user.snake_name>:
  user.vim_tokeny_insert("return base", snake_name)

superb:
  user.vim_tokeny_insert("super empty")

superb <user.snake_name>:
  user.vim_tokeny_insert("super base", snake_name)

yield:
  user.vim_tokeny_insert("yield empty")

yield <user.snake_name>:
  user.vim_tokeny_insert("yield base", snake_name)
