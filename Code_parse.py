from io import StringIO
import sys
import re
from Std import Std

def parse_text(text):
    #Поработать над Рег. выражением
    match = re.findall(r"^#python[\n\s]+([\w\s\d\n\W]+)", text)

    if match:
        with Std() as std:
            try:
                exec(
                    match[0]
                )
            except Exception as Err:
                return f'<b>{Err}</b>'
    
        output = "<b>input:</b>\n<code>%s</code>\n<b>output:</b>\n%s"%(match[0], std.read)
        return output
    else:
        return False