
frm = "Congo ... {}, you passed with  {} !!!"


def wish(student):

    if student['marks'] < 33:
        # exit()
        return

    print(frm.format(student['name'], student['marks']))


sList = {
    '101': {
        'name': 'gk',
        'marks': 19
    },
    '102': {
        'name': 'user 1',
        'marks': 53
    },
    '103': {
        'name': 'user2',
        'marks': 99
    },
    '104': {
        'name': 'user3',
        'marks': 19
    },
    '105': {
        'name': 'user4',
        'marks': 12
    },

}

for i in sList:
    wish(sList[i])
