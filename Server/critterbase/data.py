import json
with open('AC.json','r',encoding='utf-8-sig') as f:
	data = json.loads(f.read())
    
from crit.models import NorthMonth, SouthMonth, Fish, Insect
north = NorthMonth.objects.all()
south = SouthMonth.objects.all()
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']

for fish in data['ACNH Fish']:
    mon = fish['Northern Hemisphere']
    mon = mon.split(", ")
    for i in mon:
        i = i.split("-")
        if len(i) > 1:
            sx = months.index(i[0]) if i[0] in months else -1
            ex = months.index(i[1]) if i[1] in months else -1
            print(sx, ex)
            if sx == -1:
                for d in range(0,12):
                    print(months[d],end=" ")
            if ex < sx:
                for d in range(sx,12):
                    print(months[d],end=" ")
                for d in range(0,ex):
                    print(months[d],end=" ")
            else:
                for d in range(sx,ex):
                    print(months[d],end=" ")
            print()
    print(fish['Fish'])

        
    
    