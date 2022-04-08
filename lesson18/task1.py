def check_format(s):
    spec_chrs = ('@','№','$','%','^','&','*','(',')')
    frmt = ('.txt', '.docx')
    result = 'OK!'

    if (s.startswith(spec_chrs)):
        result = 'error spec char'
    elif (not s.endswith(frmt)):
        result = 'error file format'

    return result

s = input('string: ')
print(check_format(s))
