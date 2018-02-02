HELP = "HELP TEXT GOES HERE"


def mentors_attachments(questionId):
    return [{'text': '',
            'attachment_type': 'default',
            'callback_id': 'mentorResponse_{0:d}'.format(questionId),
            'actions': [{'name': 'answer',
                         'text': 'Yes',
                         'type': 'button',
                         'value': 'yes'},
                        {'name': 'answer',
                         'text': 'No',
                         'type': 'button',
                         'value': 'no'}]}]


def mentors_text(userid, question):
    textFmt = ("*A HACKER NEEDS YOUR HELP!!!*\n"
            "<@{0}> has requested to be assisted by a mentor.\n"
            "They provided the following statement:\n"
            ">_\"{1}\"_\nCan you help this hacker?\n")

    return textFmt.format(userid, question)