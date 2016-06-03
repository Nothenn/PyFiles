info = {}
with open('names.txt') as input:
    for line in input:
        player, stats, outcome, date = (x.strip() for x in line.split('-', 3))
        stats = dict(zip(('kills', 'deaths', 'assists'), map(int, stats.split('/'))))
        date = tuple(map(int, date.split('-')))
        info[player] = dict(zip(('stats', 'outcome', 'date'), (stats, outcome, date)))

#print ('info:')
#for player, record in info.items():
#    print ('  player %r:' % player)
#    for field, value in record.items():
#        print ('    %s: %s' % (field, value))

# x resembles the items between the dashes. x.
