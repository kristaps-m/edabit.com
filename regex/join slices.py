import re

def split_and_delimit(txt, num, delimiter):
    pattern = '.{1,' + str(num) + '}'
    slices = re.findall(pattern, txt)
    return delimiter.join(slices)
    
    
print(split_and_delimit("bellow", 2, '&'))# "be&ll&ow")
print(split_and_delimit("magnify", 3, ':'))# "mag:nif:y")
print(split_and_delimit("poisonous", 2, '~'))# "po~is~on~ou~s")
print(split_and_delimit("shape-shifting", 5, '^'))# "shape^-shif^ting")
print(split_and_delimit("nebulous", 1, '#'))# "n#e#b#u#l#o#u#s")
