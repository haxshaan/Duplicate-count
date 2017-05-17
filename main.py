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

    elif len(dup) == 3:
        print '%s, %s and %s' %(dup[0], dup[1], dup[2])

    elif len(dup) == 4:
        print '%s, %s, %s and %s' %(dup[0], dup[1], dup[2], dup[3])

    elif len(dup) == 5:
        print '%s, %s, %s, %s and %s' %(dup[0], dup[1], dup[2], dup[3], dup[4])

    elif len(dup) == 6:
        print '%s, %s, %s, %s, %s and %s' %(dup[0], dup[1], dup[2], dup[3], dup[4], dup[5])

    elif len(dup) == 7:
        print '%s, %s, %s, %s, %s, %s and %s' %(dup[0], dup[1], dup[2], dup[3], dup[4], dup[5], dup[6])
    else:
        print 'More than 8 duplicate characters found'
