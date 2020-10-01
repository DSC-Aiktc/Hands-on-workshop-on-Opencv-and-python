#PREDEFINED CLASS IMPORTED

import datetime

d = datetime.datetime.now()
print(d)

#USER-DEFINED CLASS IS IMPORTED

from cardata import car

honda = car("CITY","RED")
jeep = car("WRANGLER","BLACK")

honda.printdetails()
jeep.printdetails()