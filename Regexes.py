emails = r"col-lg-4\s*hidden-md\s*hidden-sm\s*hidden-xs\s*marbt40(?:[^\u003c]*\u003c){12,25}div\s*class=\u0022roboto-medium\u0022\u003e\s*([^\u003c]*)(?:[^\u003c]*\u003c){2,7}a\s*class=\u0022redemail\u0022\s*(?:[^\u003e]*\u003e)([^\u003c]*)"
extra_email = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
joining_message = r"Joining\s*Message(?:[^\u003c]*\u003c){1,100}[^\u003e]*id=\u0022headingTwo\u0022"
name = r"\u003ctitle\u003e\s*([^\u003c]*)"
address_part = r"(text-md-left\s*address(?:[^\u003e]*\u003e){2,26}(?:POSTAL\s*ADDRESS|\u003ca\s*class=\u0022button btn btn-white\u0022))"
address = r"\u003cbr\u003e([^\u003c]*)"
non_existing = r"(ECB\s*Error\s*Page)"
mobile_phone = r"Telephone:\s*[^\u003e]*\u003e\s*([^\u003c]*)\s*\u003c"
