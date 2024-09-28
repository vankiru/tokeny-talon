title: /.*\.rb (.*) - VIM/
-

# Go to

(go | next) [to] {user.tokeny_search_blank}:
  user.vim_tokeny_to(tokeny_search_blank)


(go | next) [to] {user.tokeny_search_text}:
  user.vim_tokeny_to(tokeny_search_text)

(go | next) [to] {user.tokeny_search_text} <user.text>:
  user.vim_tokeny_to(tokeny_search_text, text)


(go | next) [to] {user.tokeny_search_decimal_number}:
  user.vim_tokeny_to(tokeny_search_decimal_number)

(go | next) [to] {user.tokeny_search_decimal_number} <user.decimal_number>:
  user.vim_tokeny_to(tokeny_search_decimal_number, decimal_number)


(go | next) [to] {user.tokeny_search_snake_name}:
  user.vim_tokeny_to(tokeny_search_snake_name)

(go | next) [to] {user.tokeny_search_snake_name} <user.snake_name>:
  user.vim_tokeny_to(tokeny_search_snake_name, snake_name)


(go | next) [to] {user.tokeny_search_class_name}:
  user.vim_tokeny_to(tokeny_search_class_name)

(go | next) [to] {user.tokeny_search_class_name} <user.class_name>:
  user.vim_tokeny_to(tokeny_search_class_name, class_name)


(go | next) [to] {user.tokeny_search_const_name}:
  user.vim_tokeny_to(tokeny_search_const_name)

(go | next) [to] {user.tokeny_search_const_name} <user.const_name>:
  user.vim_tokeny_to(tokeny_search_const_name, const_name)


(go | next) [to] {user.tokeny_search_file_path}:
  user.vim_tokeny_to(tokeny_search_file_path)

(go | next) [to] {user.tokeny_search_file_path} <user.file_path>:
  user.vim_tokeny_to(tokeny_search_file_path, file_path)


(go | next) [to] {user.tokeny_search_expression}:
  user.vim_tokeny_to(tokeny_search_expression)

(go | next) [to] {user.tokeny_search_expression} <user.expression>:
  user.vim_tokeny_to(tokeny_search_expression, expression)











go next:
  user.vim_normal_mode("n")
  user.vim_command_mode("noh")

go (last | back):
  user.vim_normal_mode("N")
  user.vim_command_mode("noh")

# Go to

# Search

search {user.nameless_token_regex}:
  user.code_search_token(nameless_token_regex)

search {user.number_token_regex} <user.number_string>:
  user.code_search_token(number_token_regex, number_string)

search {user.text_token_regex} <user.text>:
  user.code_search_token(text_token_regex, text)

search {user.snake_name_token_regex} <user.snake_name>:
  user.code_search_token(snake_name_token_regex, snake_name)

search {user.class_name_token_regex} <user.class_name>:
  user.code_search_token(class_name_token_regex, class_name)

search {user.const_name_token_regex} <user.const_name>:
  user.code_search_token(const_name_token_regex, const_name)

search {user.file_name_token_regex} <user.file_name>:
  user.code_search_token(file_name_token_regex, file_name)

search <user.number_string>:
  user.code_search_token(number_string)

search (<user.snake_name> | <user.class_name> | <user.const_name>):
  identifier = snake_name or class_name
  identifier = identifier or const_name
  user.code_search_token(identifier)

