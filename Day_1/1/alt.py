f = sorted(eval(open('input.txt').read().
    replace('\n\n', ',').replace('\n', '+')))

print(f[-1], sum(f[-3:]))