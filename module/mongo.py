from conf.db_conf import client
import datetime

class PosData:
    def __init__(self):
        db = client['BackendServer']
        self.col = db['posData']

    def update(self,car,x,y,vector):
        raw = {
                "car":int(car),
                "X":x,
                "Y":y,
                "V":vector,
                "time":datetime.datetime.now()
                }
        self.col.insert_one(raw)
        client.close()
        return True

    def getlastcar(self,car):
        raw = {
                "car":int(car)
                }
        return self.col.find(raw).sort('_id',-1)

    def gettrangecar(self,intCar,intTime):
        raw = {
                "car":int(car),
                "time":
                {
                    "$gte":calcTime,"$lte":nowTime
                }
            }
        return self.col.find(raw).sort('_id',-1)


    def getsixcar(self,time):
        nowTime = datetime.datetime.now()
        deltaTime = datetime.timedelta(seconds=int(time))
        calcTime = nowTime - deltaTime
        dictCars = {}
        for car in range(0,7):
            carObj = self.col.find({"car" : car , "time" : { "$gte":calcTime,"$lte":nowTime }}).sort('_id',-1)
            if carObj.count() == 0 :
                dictCars[car] = None
            else:
                dictCars[car] = [carObj[0].get('X'),carObj[0].get('Y'),carObj[0].get('X')]
        return dictCars


class LedData:
    def __init__(self):
        self.col = db['ledData']
