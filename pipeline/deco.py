
def beforeafter(before, after):

    def decor(func):

        def wrapper(html):
            preprocessed_html = before(html)
            result = func(preprocessed_html)
            postprocessed_result = after(result)

            return postprocessed_result

        return wrapper

    return decor


