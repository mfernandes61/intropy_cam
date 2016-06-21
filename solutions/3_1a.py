def simple_mean(x, y):
    try:
        mean = (x + y) / 2.0
        return mean
    except TypeError, e:
        print "Arguments must be numeric", e
        return None


def better_mean(values):
    total = 0
    for v in values:
        total += v
    mean = total / float(len(values))
    return mean

print "Mean of 30 & 60:", simple_mean(30, 60)
print "Mean of 30 & '60':", simple_mean(30, '60')
print "Mean of values even numbers under 20:", better_mean(range(0, 20, 2))

