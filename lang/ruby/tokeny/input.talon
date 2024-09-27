title: /.*\.rb (.*) - VIM/
-

{user.input_no_capture}:
  user.vim_tokeny_insert(input_no_capture)

{user.input_decimal_number} <user.decimal_number>:
  user.vim_tokeny_insert(input_decimal_number, decimal_number)

{user.input_text} <user.text>:
  user.vim_tokeny_insert(input_text, text)

{user.input_snake_name} <user.snake_name>:
  user.vim_tokeny_insert(input_snake_name, snake_name)

{user.input_class_name} <user.class_name>:
  user.vim_tokeny_insert(input_class_name, class_name)

{user.input_const_name} <user.const_name>:
  user.vim_tokeny_insert(input_const_name, const_name)

{user.input_file_path} <user.file_path>:
  user.vim_tokeny_insert(input_file_path, file_path)
