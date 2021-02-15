#Md Jawad
#Interview Code

import random  

class Game :

    def __init__(self,name):
        self.name = name
        self.frames =[]
        for i in range (10):
            self.frames.append([0,0])
        self.frame=0
        self.ball=0
        self.rpin=10

    def roll(self,pin):
            
            if self.ball==0 and self.rpin-pin<=0:

                self.frames[self.frame][self.ball]=10
                self.frame+=1
                self.ball=0
                self.rpin=10
                

            elif self.ball== 1 and self.rpin-pin<=0:
                self.frames[self.frame][self.ball]=self.rpin
                self.frame+=1
                self.ball=0
                self.rpin=10

            else:
                if self.ball==0:
                    self.rpin=self.rpin-pin
                    self.frames[self.frame][self.ball]=pin
                    self.ball+=1

                elif self.ball==1:
                    self.rpin=self.rpin-pin
                    self.frames[self.frame][self.ball]=pin
                    self.ball=0
                    self.frame+=1
                    self.rpin=10

                    
                

    def getframe(self):
        return self.frames
                    
    def getScore(self):
        ind=0
        score=0
        for i in self.frames:
            if i[0]==10:
                if self.frames[ind+1][0]==10:
                    score+=score+self.frames[ind+2][0]
                else:
                    score+=self.frames[ind+1][0]+self.frames[ind+1][0]
                    score+=self.frames[ind+1][0]+self.frames[ind+1][0]
                    

            elif i[self.ball] + i[self.ball+1]==10:
                score=score + self.frames[ind+1][0]
              
            else:
                score=i[self.ball] + i[self.ball+1]+ score
                score=i[self.ball] + i[self.ball+1]+ score  
                
            ind+=1
    
        return score

                
               

  
            
               

                



ame=Game("Jawad")

print(ame.roll(10))
print(ame.roll(5))
print(ame.roll(2))
print(ame.roll(10))


print(ame.getframe())
print("The score is:" + str(ame.getScore()))
