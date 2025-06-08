secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here. 아니 클래스 뭐 어케 쓰는거냐

class Mission:
    def __init__( self, secret_code, meeting_point, time ):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time
    def printcheck(self):
        print('secret code : ' + self.secret_code)
        print('meeting point : ' + self.meeting_point)
        print('time : ' + str(self.time))

mission = Mission( secret_code, meeting_point, time )
mission.printcheck()