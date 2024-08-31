from MagicVadTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from MagicVadLogic.Base.LogicBase import LogicBase
from MagicVadTitan.Logic.Math.LogicLong import LogicLong
class LogicClientAvatar:
 def encode(self, encoder: ChecksumEncoder):
        
        encoder.writeInt(0) #unk
        encoder.writeInt(0) #HighID
        encoder.writeInt(1) #LowID
        encoder.writeInt(0)
        encoder.writeInt(1) #AllianceId
        encoder.writeBoolean(0) #Player is in clan
        
        encoder.writeInt(16) #League
        
        encoder.writeInt(0)
        encoder.writeInt(10)
        encoder.writeInt(0)
        encoder.writeInt(1)
        
        encoder.writeString("vadim_not_dev") #Name
        encoder.writeString(None)
        
        encoder.writeInt(99) #ExpLevel
        encoder.writeInt(999) #ExpPoints
        encoder.writeInt(9999) #FreeDiamonds
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(9999) #Trophies
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
        
        encoder.writeByte(0) #unk boolean
        
        encoder.writeByte(0) #unk boolean
        
        encoder.writeInt(0)
        
        encoder.writeInt(0) #array
        
        encoder.writeInt(0) #array 2, resource data slot
        
        encoder.writeInt(0) #array 3, unit slot data
        
        encoder.writeInt(0) #array 4, spell slot data
        
        encoder.writeInt(0) #array 5, unit upgrade slot
        
        encoder.writeInt(0) #array 6, spell upgrade slot
        
        encoder.writeInt(0) #array 7, hero upgrade slot
        
        encoder.writeInt(0) #array 8, hero health slot
        
        encoder.writeInt(0) #array 9, hero state slot
        
        encoder.writeInt(0) #array 10, alliance unit data
        
        encoder.writeInt(0) #array 11
        
        encoder.writeInt(0) #array 12
        
        encoder.writeInt(0) #array 13, achievement progress data
        
        encoder.writeInt(0) #array 14, npc map progress data
        
        encoder.writeInt(0) #array 15, npc looted gold data
        
        encoder.writeInt(0) #array 16, npc looted elixir data