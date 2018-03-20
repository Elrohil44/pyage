def load_file(file):
    values = []
    variables = 0
    clauses = 0
    with open(file, 'r') as f:
        clause = []
        for line in f:
            if line[0] == 'c':
                continue
            if line[0] == 'p':
                x = line.split(' ')
                variables = int(x[2])
                clauses = int(x[3])
                continue

            x = line.split(' ')
            for val in x:
                if not val:
                    continue
                num = int(val)
                if num != 0:
                    clause.append((1 if num > 0 else 0, abs(num) - 1))
                else:
                    values.append(clause)
                    clause = []

    return values, variables, clauses
