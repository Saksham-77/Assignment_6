crct, lst = ["()", "[]", "{}"], []
class validity():
    def is_valid_parenthese(self, entr):
        i = 0
        while len(entr) > i:
            x = entr[i:i+2]
            lst.append(x)
            i += 2
        for _ in lst:
            if _ not in crct:
                return False
        else:
            return True
print(validity().is_valid_parenthese("()[]{}"))
print(validity().is_valid_parenthese("[)"))
print(validity().is_valid_parenthese("({[)]"))
print(validity().is_valid_parenthese("{{{"))
