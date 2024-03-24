regex_pattern = r"^[M]{0,3}(CM|D?[C]{0,3}|CD)?(XC|L?[X]{0,3}|XL)?(IX|V?[I]{0,3}|IV)?$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))