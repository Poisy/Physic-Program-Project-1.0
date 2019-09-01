def ohm_law(U, I, R):
    if ',' in list(U): U = U.replace(',', '.')
    if ',' in list(I): I = I.replace(',', '.')
    if ',' in list(R): R = R.replace(',', '.')
    if U is '' and I is '' or R is '' and U is '' or I is '' and R is '':
        return "Can't use the formula, need two parameters!"
    else:
        if U != '' and I != '' and R != '':
            return "There is nothing to calculate :c"
        else:
            if R is '':
                try:
                    return round(float(U)/float(I), 3), "Ω"
                except:
                    return "Can't calculate with letters or others"
            elif I is '':
                try:
                    return round(float(U)/float(R), 3), "A"
                except:
                    return "Can't calculate with letters or others"
            elif U is '':
                try:
                    return round(float(I)*float(R), 3), "V"
                except:
                    return "Can't calculate with letters or others"
            else:
                return "Something went wrong"



