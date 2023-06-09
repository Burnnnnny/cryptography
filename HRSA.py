from Crypto.Util.number import *

p = 102917468046616568070479080437602349605790044856847368227989900438678598347252242912474630778930183524103498634272903762436029311481137741713080659077027483465896792512517855786714336938418831349151567425537183094315541122606131460802382497841037179253750742567612375678233281962828108691356598122015035462931
q = 155409405226203238058015527018600466439894178201393804291867914008619674289107580497614221099756010997177702316412488380301911465872315087011512265127913696978059566003514595719636467623534496220114055190116473471302619324855013682151351145662146108598413909004492093001297173273875378143449965795752096407249
e = 257
n = 15994342496511457631852165745889134659106113775792815345660283109468603940964892042894072452338973417508989267182581106246598435022873385443407040336706693823717245966048048753547976289148494787906459582665400524599910456936861809339918570553400623639334162939976766980991427000240636672326892016855733342336543332550988035515870213111437557851461183289944204759548833820909869065701576126243727856888072220248575585769081790850141026448275329427960153467083111068539569641547854318739805365356286162575492346400298725777857883327406673789140613479637379861625904116837931896101781221369655018622189149174730619186819
C = 9616384404213524657863670808981125526907268432622976664325249394851244870192789713737122799469499856887739253362805246859649606786263701308805488844336941066141053596437114630658542913559798796936296332917154444568198618992503828589914317105542317632873299732945292007245940129956165369995868033142331830348424499649247621627957887323716236781832428323377989036111392368810898382355775057357502240259332598797482858241354811610086476550911065698726091155648159869780115791767209206584503973202288411298660473001567148602289414544500536763463431773097574512189310225492456529147806648758189442259263483402853811323777


phi = (p-1)*(q-1)

d = inverse(e,phi)

print(long_to_bytes(pow(C,d,p*q)))
