def duplicate_count(text):

    working_text = str(text.lower())

    dup = []

    for char in working_text:
        if working_text.count(char) > 1:
            dup.append(char)

        else:
            pass

    for num in dup:
        while dup.count(num) > 1:
            dup.remove(num)

    if len(dup) == 0:
        print 'No duplicate characters found!'
    elif len(dup) == 1:
        print dup[0]

    elif len(dup) == 2:
        print '%s and %s' %(dup[0], dup[1])

    else:
        print 'More than 2 duplicate characters found'

duplicate_count("indivisibility")
