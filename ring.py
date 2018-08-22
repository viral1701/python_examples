from ring_doorbell import Ring
myring = Ring('viralpatel1@gmail.com',"fTqeD|b#pzY3fS@@*QMl")
for doorbell in myring.doorbells:

    # listing the last 15 events of any kind
    for event in doorbell.history(limit=1):
        print('ID:       %s' % event['id'])
        print('Kind:     %s' % event['kind'])
        print('Answered: %s' % event['answered'])
        print('When:     %s' % event['created_at'])
        print('--' * 50)

    # get a event list only the triggered by motion
    events = doorbell.history(kind='motion')