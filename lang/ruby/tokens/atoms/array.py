content = "\(.\|\n\)\{-}"

prefix = "\%(\w\|[]})?!\"']\)\@<!"

array = "{prefix}\[{content}\]"
object = "Array.new(.\{-})"

delimiter = "[^[:alnum:][:space:]]"
percent_general = f"%[wWiI]\({delimiter}\){content}\1"

percent_paren = f"%[wWiI]({content})"
percent_bracket = f"%[wWiI]{{{content}}}"
percent_square = f"%[wWiI]\[{content}\]"
percent_tag = f"%[wWiI]<{content}>"

[
    [1, 2],
    [3, 4]
]


m(1, 2, Range.new(1, 2), 3)

