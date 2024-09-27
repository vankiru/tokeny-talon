title: /\w*\.rb (.*) - VIM/
-

test <user.decimal_number>:
  user.vim_insert_mode(decimal_number)

# range

range <user.decimal_number> (to | by) <user.decimal_number>:
  user.vim_tokeny_insert("range full_by", "{decimal_number_1} {decimal_number_2}")

range <user.decimal_number> until <user.decimal_number>:
  user.vim_tokeny_insert("range full_until", "{decimal_number_1} {decimal_number_2}")

# interpolation

interpol <user.snake_name>:
  user.vim_tokeny_insert("interpolation base", snake_name)

interpol:
  user.vim_tokeny_insert("interpolation empty")

# key

key <user.key_name> [to]:
  user.vim_tokeny_insert("key symbol", key_name)

key to:
  user.vim_tokeny_insert("key symbol")

string key <user.key_name> [to]:
  user.vim_tokeny_insert("key string", key_name)

object key <user.variable_name> [to]:
  user.vim_tokeny_insert("key object", key_name)
