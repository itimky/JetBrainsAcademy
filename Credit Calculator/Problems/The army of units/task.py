army = int(input())
if army >= 1000:
    print('legion')
elif army >= 500:
    print('swarm')
elif army >= 50:
    print('horde')
elif army >= 10:
    print('pack')
elif army >= 1:
    print('few')
else:
    print('no army')
