# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

ki = LINETCR.LINE()
ki.login(qr=True)
ki.loginResult()

kk = LINETCR.LINE()
kk.login(qr=True)
kk.loginResult()

kc = LINETCR.LINE()
kc.login(qr=True)
kc.loginResult()

kd = LINETCR.LINE()
kd.login(qr=True)
kd.loginResult()

ke = LINETCR.LINE()
ke.login(qr=True)
ke.loginResult()

kf = LINETCR.LINE()
kf.login(qr=True)
kf.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""          🐼คำสั่งบอททั่วไป🐼
 
   📝คำสั่งบอท📝        📝การทำงาน📝
  
🔰[Panda:key]      = คำสั่ง
🔰[Panda:gift]     = ส่งของขวัญ
🔰[Panda:gn]       = เปลี่ยนชื่อกลุ่ม
🔰[Panda:me]       = คำสั่ง/แท๊กชื่อ-ส่งคท
🔰[Panda:mid]      = คำสั่ง/แท๊กชื่อ-ส่งคท
🔰[Panda:ginfo]    = เช็คข้อมูลกลุ่ม
🔰[Panda:gcreator] = แสดงผู้สร้างกลุ่ม
🔰[Gcreator:inv]   = เชิญผู้สร้างกลุ่ม
🔰[Panda:blacklist]= รายชื่อบรรชีดำ
🔰[Panda:creator]  = แสดงผู้เขียนยอท
🔰[Panda:staff]    = รายชื่อสั่งการ
🔰[SetLastPoint]   = จับเวลา
🔰[Viewlastseen]   = ดูคนอ่าน
*********************************
    ****Created AoF!!bot****
   Http://line.me/ti/p/~aofbot
     **Protect Your Group**
*********************************
"""
helpMessage2 =""" 🐼การทำงานของบอท🐼

√ ระบบป้องกันสมาชิกเตะคน
√ ระบบป้องกันสมาชิกเชิญคน
√ ระบบป้องกันการ ปิด-เปิดลิ้ง
√ ระบบ แบน-บัญชีดำ
√ ระบบดูคนอ่านหน้าแชท
√ เช็คการทำงาน การตอบสนอง
√ แชร์ลิ้ง
√ เช็ครูป สเตตัส ก๊อปปี้ได้ 
√ มีฟังชั่นล้างห้างที่ไม่ไช้
√ ตรวจสอบบอทว่าอยู่ห้องไหนบ้าง 
√ เชิญบอทเข้าและออก ด้วยคำสั่ง
√ เชิญด้วยการแท๊กชื่อ หรือส่ง mid
√ ฟั่งชั่นเสริมอีกมากมายให้เลือกใช้
*********************************
    ****Created AoF!!bot****
   Http://line.me/ti/p/~aofbot
     **Protect Your Group**
*********************************
"""
helpMessage3 ="""  🐼คำสั่งสำหรับ แอดมิน/สตาร์ฟ🐼

   📝คำสั่งบอท📝        📝การทำงาน📝
   
🔰[Panda:key@]        = สำหรับแอด
🔰[Panda:view]	      = ดูการตั้งค่า
🔰[Panda:set]         = เช็คการตั้งค่า
🔰[Panda:option]      = การทำงาน
🔰[Getpict @]         = ดูรูปสมาชิก
🔰[Mid @]             = ดู mid
🔰[Me @]              = ดูคอนแทรค
🔰[Addminlist]        = แอดมิน
🔰[Stafflist]         = สตาร์ฟ
🔰[Botlist]           = บอท
🔰[Panda:listgroup]   = รายชื่อกลุ่ม
🔰[Panda:join]        = เชิญบอทเข้า
🔰[Panda:bye]         = เชิญบอทออก
🔰[Panda:@bye]        = สั่งบอทออก
🔰[Panda:ban @]       = แบน
🔰[Panda:unban @]       = ปลดแบน
🔰[Panda:addblacklist]= แบนคท
🔰[Panda:addwhitelist]= ปลดแบนคท
🔰[Nk @] Bye @        = สั่งเตะ
🔰[Panda:kickban]     = สั่งเตะแบน
🔰[Panda:fighting]    = เตะทุกคน
🔰[Panda:tagall]      = แท๊กชื่อ
🔰[Panda:spon]        = เช็คบอท
🔰[Panda:speed]       = ความเร็ว
🔰[Panda:test]        = การทำงาน
🔰[Panda:contact]     = รายชื่อบอท
🔰[Invite]Mid         = เชิญ mid
🔰[Panda:cancelinvite]= ยกเชิญ
🔰[Panda:linkon]      = เปิดลิ้ง
🔰[Panda:linkoff]     = ปิดลิ้ง
🔰[Blockinvite:on]    = เปิดเชิญ
🔰[Blockinvite:off]   = ปิดเชิญ
🔰[Panda:qron]        = เปิดอาร์โค๊ต
🔰[Panda:qroff]       = ปิดคิวอาร์โค๊ต
🔰[cancelall          = ลบห้องเชิญ
🔰[Admin add @]    = เพิ่มแอด
🔰[Remove admin @] = ลบแอด
🔰[Staff add @]       = เพิ่มสตาร์ฟ
🔰[Staff remove @]    = ลบสตาร์ฟ
🔰[Gurl]              = แชร์ลิ้ง
🔰[Cn] 
🔰[Ip Like]  
🔰[Loveyou]
*********************************
    ****Created AoF!!bot****
   Http://line.me/ti/p/~aofbot
     **Protect Your Group**
*********************************
"""
Setgroup =""" 🔘การตั้งค่าป้องกันกลุ่ม🔘
[Protect QR -- Panda:qron/qroff]
[Protect Kicker -- Panda:on/off]
[Protect Invite -- Blockinvite:on/off]
[Protect Backup -- Backup on / off]
[Mid Via Contact -- Contact On / Off]
"""
KAC=[cl,ki,kk,kc,kd,ke,kf]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Fmid = kf.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,"udee626454be8e869860bbcbbdb1139d0","u08ef801f7cdf1bb7588ace0b764be826","u083bdc9ca7257b41cd4d1de933a5ad8e","uac662b8157b8f813a3c980c600d9a257"]
staff=["udee626454be8e869860bbcbbdb1139d0","u08ef801f7cdf1bb7588ace0b764be826","u083bdc9ca7257b41cd4d1de933a5ad8e","uac662b8157b8f813a3c980c600d9a257"]
admin=["udee626454be8e869860bbcbbdb1139d0","u08ef801f7cdf1bb7588ace0b764be826","u083bdc9ca7257b41cd4d1de933a5ad8e","uac662b8157b8f813a3c980c600d9a257"]
adminMID = "udee626454be8e869860bbcbbdb1139d0","u08ef801f7cdf1bb7588ace0b764be826","u083bdc9ca7257b41cd4d1de933a5ad8e","uac662b8157b8f813a3c980c600d9a257"
wait = {
    'protect':True,
    'protectinv':True,
    'protectqr':True,
    'Backup':True,
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"====================================\nThanks for add me\nMy Creator Http://line.me/ti/p/~aofbot\n====================================",
    "lang":"JP",
    "comment":"====================================\nThanks for add me , Dont Forget For add Owner Me\nIDLine: aofbot\n====================================",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"Panda'master ",
    "cName2":"Panda'1 ",
    "cName3":"Panda'2 ",
    "cName4":"Panda'3 ",
    "cName5":"Panda'4 ",
    "cName6":"Panda'5 ",
    "cName7":"Panda'6 ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "staff":{},
    "wstaff":False,
    "dstaff":False,
    "atjointicket":True,
    "protectionOn":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = kd.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)

                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ke.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)

                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = kf.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)

                if op.param3 in Fmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kf.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 55:
                try:
                    if op.param1 in wait2['readPoint']:
                        Name = cl.getContact(op.param2).displayName
                        if Name in wait2['readMember'][op.param1]:
                            pass
                        else:
                            wait2['readMember'][op.param1] += "\n・" + Name
                            wait2['ROM'][op.param1][op.param2] = "・" + Name
                    else:
                        pass
                except:
                    pass

        if op.type == 24:
	    if op.param2 in Bots:
                return
            if op.param2 in admin:
                return
            if op.param2 in staff:
                return
            elif wait ["protect"] == True:
                ke.kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])
	    else:
                pass

        if op.type == 15:
	    if op.param3 in admin:
		pass
        	cl.inviteIntoGroup(op.param1, admin)
	    else:
		pass

        if op.type == 32:
            if op.param2 in Bots:
                return
            if op.param2 in admin:
                return
            if op.param2 in staff:
                return
		cl.kickoutFromGroup(op.param1,[op.param2])
		cl.inviteIntoGroup(op.param1,[op.param3])
	    else:
		pass

        if op.type == 11:
	    if op.param2 in Bots:
                return
            if op.param2 in admin:
                return
            if op.param2 in staff:
                return
	    elif wait ["protectqr"] == True:
		X = cl.getGroup(op.param1)
		X.preventJoinByTicket = True
		cl.updateGroup(X)
	    else:
		pass

	if op.type == 19:
            if op.param2 in Bots:
                return
            if op.param2 in admin:
                return
            if op.param2 in staff:
                return
            elif wait ["protect"] == True:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 13:
            if op.param2 in Bots:
                return
            if op.param2 in admin:
                return
            if op.param2 in staff:
                return
	    if wait ["protectinv"] == True:
                try:
                    X = cl.getGroup(op.param1)
                    gInviMids = [contact.mid for contact in X.invitee]
                    cl.cancelGroupInvitation(msg.to, gInviMids)
                    ke.kickoutFromGroup(op.param1,[op.param2])
                    print gInviMids + "INVITE CANCEL"
                except:
                    try:
                        print "RETRY CANCEL INVITATION"
                        X = cl.getGroup(op.param1)
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        print gInviMids + "INVITE CANCELED"
                    except:
                        print "BOT CAN'T CANCEL THE INVITATION"
                        pass

        if op.type == 19:
            if op.param3 in admin:
                ke.kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1, admin)
            else:
                pass
	    if op.param3 in staff:
		kd.kickoutFromGroup(op.param1,[op.param2])
		cl.inviteIntoGroup(op.param1, staff)
	    else:
		pass

        if op.type == 19:
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        cl.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kd.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kd.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            ke.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            kf.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kd.updateGroup(X)
                    Ti = kd.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kd.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kd.updateGroup(G)
                    Ticket = kd.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kf.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kf.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kf.updateGroup(G)
                    Ticket = kf.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            ke.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.inviteIntoGroup(op.param1, admin)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        cl.inviteIntoGroup(op.param1, admin)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Dihapus")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"ถูกเพิ่มในบัญชีดำ")
                        print "SUKSES -- BLACKLIST ADD"

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"][ลบรายชื่อบัญชีดำ")
                        print "SUKSES -- BLACKLIST DELETE"
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wstaff"] == True:
                   if msg.contentMetadata["mid"] in wait["staff"]:
                        cl.sendText(msg.to,"already")
                        wait["wstaff"] = False
                   else:
                        wait["staff"][msg.contentMetadata["mid"]] = True
                        wait["wstaff"] = False
                        cl.sendText(msg.to,"เพิ่มในรายชื่อสตร์าฟ")

               elif wait["dstaff"] == True:
                   if msg.contentMetadata["mid"] in wait["staff"]:
                        del wait["staff"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"ลบจากรายการสตาร์ฟ")
                        wait["dstaff"] = False

                   else:
                        wait["dstaff"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Panda:key"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    print "SUKSES -- KEYWORD"
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Panda:option"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage2)
                else:
                    pass
                    print "SUKSES -- FITUR BOT"
            elif msg.text in ["Panda:key@"]:
              if msg.from_ in staff:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage3)
                else:
                    print "SUKSES -- KEYWORD"
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Panda:view"]:
              if msg.from_ in staff:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Panda:gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                    print "SUKSES -- CHANGE NAME GROUP"
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bye " in msg.text):
              if msg.from_ in staff:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Kick " in msg.text:
              if msg.from_ in staff:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "Invite " in msg.text:
              if msg.from_ in staff:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
                contact = cl.getContact(mid)
                cl.sendText(msg.to, ""+contact.displayName+" I invited you")
                print "SUKSES -- INVITED BY MID"
            elif msg.text in ["Panda:creator"]:
                msg.contentType = 13
                cl.sendText(msg.to, "ADD MY CREATOR BOT Protect\nPROTECT GROUP")
                msg.contentMetadata = {'mid': 'udee626454be8e869860bbcbbdb1139d0'}
                cl.sendMessage(msg)
                pass
            elif msg.text in ["Panda:staff"]:
                msg.contentType = 13
                cl.sendText(msg.to, "ADD MY STAFF BOT Protect\nPROTECT GROUP")
                msg.contentMetadata = {'mid': 'udee626454be8e869860bbcbbdb1139d0'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'u08ef801f7cdf1bb7588ace0b764be826'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'u083bdc9ca7257b41cd4d1de933a5ad8e'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'uac662b8157b8f813a3c980c600d9a257'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'u15116b749f6cc532da1cea54601b207a'}
                cl.sendMessage(msg)
                print "SUKSES -- SEND CREATOR AND STAFF"
            elif msg.text in ["Panda:contact"]:
                msg.contentType = 13
                cl.sendText(msg.to, "ADD MY CONTACT BOT Protect\nBOT PROTECT GROUP")
                msg.contentMetadata = {'mid': 'u7d706713ded20b9e42ef747c73069c90'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'u15116b749f6cc532da1cea54601b207a'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'ud676f6c52c3928e73fe32b6f744b93d5'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'u8413e526c005b92f8fe9f31ee3656943'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'u6e33ebcc43f41f0f3f6082a0cd6ef18d'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'u794e26f0fcedc90bf14c92814d50ac8b'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'u9e9d7f28cb22e98ba95004cfc6d9b8da'}
                cl.sendMessage(msg)
                print "SUKSES -- SEND CONTACT BOT"
            elif msg.text in ["Panda:me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
            elif msg.text in ["Panda:gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '1066653',
                                    'PRDTYPE': 'STICKER',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
                print "SUKSES -- SEND GIFT"
            elif msg.text in ["gift1","Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8588',
                                    'PRDTYPE': 'STICKER',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
                print "SUKSES -- SEND GIFT"
            elif msg.text in ["gift2","Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '5594',
                                    'PRDTYPE': 'STICKER',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
                print "SUKSES -- SEND GIFT"
            elif msg.text in ["Panda:cancelinvite"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        print "SUKSES -- CANCEL INVITE GROUP"
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Panda:linkon"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    print "SUKSES -- OPEN URL GROUP"
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Panda:linkoff"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    print "SUKSES -- CLOSE URL GROUP"
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Panda:ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    print "SUKSES -- SEND PANDAINFO"
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        md = ("[รายชื่อกลุ่มติดตั้งระบบป้องกัน]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[ผู้สร้างกลุ่ม]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                        cl.sendText(msg.to,md)
                    else:
                        md = ("[รายชื่อกลุ่มติดตั้งระบบป้องกัน]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[ผู้สร้างกลุ่ม]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                        cl.sendText(msg.to,md)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ไม่สามารถใช้นอกกลุ่มได้")
                    else:
                        cl.sendText(msg.to,"ไม่ใช้งานน้อยกว่ากลุ่ม")
            elif msg.text in ["Panda:gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
            elif msg.text in ["Gcreator:inv","GCreator:inv","gcreator:inv"]:
              if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        cl.findAndAddContactsByMid(gCreator)
                        cl.inviteIntoGroup(msg.to,[gCreator])
                    except:
                        gCreator = "Error"
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif msg.text in ["Panda:mid"]:
                print "SUKSES -- SHOW MID USER"
                cl.sendText(msg.to, msg.from_)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif ("Cn " in msg.text):
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif ("Cn1 " in msg.text):
              if msg.from_ in admin:
                string = msg.text.replace("Cn1 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif ("Cn2 " in msg.text):
              if msg.from_ in admin:
                string = msg.text.replace("Cn2 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif ("Cn3 " in msg.text):
              if msg.from_ in admin:
                string = msg.text.replace("Cn3 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kc.getProfile()
                    profile_B.displayName = string
                    kc.updateProfile(profile_B)
                    kc.sendText(msg.to,"name " + string + " done")
            elif ("Cn4 " in msg.text):
              if msg.from_ in admin:
                string = msg.text.replace("Cn4 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kd.getProfile()
                    profile_B.displayName = string
                    kd.updateProfile(profile_B)
                    kd.sendText(msg.to,"name " + string + " done")
            elif ("Cn5 " in msg.text):
              if msg.from_ in admin:
                string = msg.text.replace("Cn5 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ke.getProfile()
                    profile_B.displayName = string
                    ke.updateProfile(profile_B)
                    ke.sendText(msg.to,"name " + string + " done")
            elif ("Cn6 " in msg.text):
              if msg.from_ in admin:
                string = msg.text.replace("Cn6 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kf.getProfile()
                    profile_B.displayName = string
                    kf.updateProfile(profile_B)
                    kf.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid": msg.from_}
                cl.sendMessage(msg)
            elif msg.text in ["Backup:on"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        print "EXECUTED -- BACKUP ON"
                        cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Panda:on"]:
              if msg.from_ in staff:
		if wait["protect"] == True:
		    if wait["lang"] == "JP":
                        print "EXECUTED -- PROTECT ON"
			cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
		    else:
			cl.sendText(msg.to,"Done")
		else:
		    wait["protect"] = True
		    if wait["lang"] == "JP":
                        print "SUKSES -- PROTECT ON"
			cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
		    else:
			cl.sendText(msg.to,"Done")
	    elif msg.text in ["Panda:off"]:
              if msg.from_ in staff:
		if wait["protect"] == False:
		    if wait["lang"] == "JP":
                        print "EXECUTED -- PROTECT OFF"
			cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
		    else:
			cl.sendText(msg.to,"Done")
		else:
		    wait["protect"] = False
		    if wait["lang"] == "JP":
                        print "SUKSES -- PROTECT OFF"
			cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
		    else:
			cl.sendText(msg.to,"Done")
	    elif msg.text in ["Blockinvite:on"]:
              if msg.from_ in staff:
		if wait["protectinv"] == True:
		    if wait["lang"] == "JP":
                        print "EXECUTED -- PROTECT INV ON"
			cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
		    else:
			cl.sendText(msg.to,"Done")
		else:
		    wait["protectinv"] = True
		    if wait["lang"] == "JP":
                        print "SUKSES -- PROTECT INV ON"
			cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
		    else:
			cl.sendText(msg.to,"Done")
	    elif msg.text in ["Blockinvite:off"]:
              if msg.from_ in staff:
		if wait["protectinv"] == False:
		    if wait["lang"] == "JP":
                        print "EXECUTED -- PROTECT INV OFF"
			cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
		    else:
			cl.sendText(msg.to,"Done")
		else:
		    wait["protectinv"] = False
		    if wait["lang"] == "JP":
                        print "SUKSES -- PROTECT INV OFF"
			cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
		    else:
			cl.sendText(msg.to,"Done")
	    elif msg.text in ["Panda:qron"]:
              if msg.from_ in staff:
		if wait["protectqr"] == True:
		    if wait["lang"] == "JP":
                        print "EXECUTED -- PROTECT QR ON"
			cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
		    else:
			cl.sendText(msg.to,"Done")
		else:
		    wait["protectqr"] = True
		    if wait["lang"] == "JP":
                        print "SUKSES -- PROTECT QR ON"
			cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
		    else:
			cl.sendText(msg.to,"Done")
	    elif msg.text in ["Panda:qroff"]:
              if msg.from_ in staff:
		if wait["protectqr"] == False:
		    if wait["lang"] == "JP":
                        print "EXECUTED -- PROTECT QR OFF"
			cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
		    else:
			cl.sendText(msg.to,"Done")
		else:
		    wait["protectqr"] = False
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
			print "SUKSES -- PROTECT QR OFF"
		    else:
			cl.sendText(msg.to,"Done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K:on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
              if msg.from_ in staff:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K:off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join:on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
              if msg.from_ in staff:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join:off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
              if msg.from_ in staff:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ⛔\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave:on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave:off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in staff:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ⛔")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share:on","Share on"]:
              if msg.from_ in staff:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share:off","Share off"]:
              if msg.from_ in staff:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Panda:set"]:
                md = ""
                if wait["Backup"] == True: md+="[🔛] Backup : on\n"
                else:md+="[⛔] Backup : off\n"
                if wait["protect"] == True: md+="[🔛] Protect : on\n"
                else: md+="[⛔] Protect : off\n"
                if wait["protectinv"] == True: md+="[🔛] Protectinv : on\n"
                else: md+="[⛔] Protectinv : off\n"
                if wait["protectqr"] == True: md+="[🔛] Protectqr : on\n"
                else: md+="[⛔] Protectqr : off\n"
                if wait["contact"] == True: md+="[🔛] Contact : on\n"
                else: md+="[⛔] Contact : off\n"
                if wait["autoJoin"] == True: md+="[🔛] Auto join : on\n"
                else: md +="[⛔] Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+="[🔛] Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "[⛔] Group cancel : off\n"
                if wait["leaveRoom"] == True: md+="[🔛] Auto leave : on\n"
                else: md+="[⛔] Auto leave : off\n"
                if wait["timeline"] == True: md+="[🔛] Share : on\n"
                else:md+="[⛔] Share : off\n"
                if wait["autoAdd"] == True: md+="[🔛] Auto add : on\n"
                else:md+="[⛔] Auto add : off\n"
                if wait["commentOn"] == True: md+="[🔛] Comment : on\n"
                else:md+="[⛔] Comment : off\n"
                cl.sendText(msg.to,md)
            elif msg.text in ["Group id","group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Panda:listgroup"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[=> %s\n" % (cl.getGroup(i).name)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in staff:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                    print "SUKSES -- SEND CANCELALL"
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add:on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add:off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "spam change: " in msg.text:
                wait["spam"] = msg.text.replace("spam change: ","")
                cl.sendText(msg.to,"spam Change")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif "spam add: " in msg.text:
                wait["spam"] = msg.text.replace("spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"LINE GROUP =" " line://ti/g/" + gurl)
                    print "SUKSES -- OPEN AND SHARE LINK GROUP"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam Update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "SetLastPoint":
                    cl.sendText(msg.to, "บันทึกเวลาดูคนอ่าน")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "SUKSES -- SEND $SET CHECK SIDERS"
            elif msg.text == "Viewlastseen":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "⬇️รายชื่อคนที่อ่านล่าสุด ⬇️%s\n⬆️⬆️⬆️\n⬇️Orang - คนที่ไม่สนใจอ่าน⬇️\n%sมันไม่ปกติ ♪\n\nสร้างเมื่อวันที่และเวลา:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "SUKSES -- SEND $READ CHECK SIDERS"
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------
            elif msg.text in ["Panda:join"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.0)
                    kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.0)
                    kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.0)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    print "SUKSES -- SUMMON BOT"
                    G.preventJoinByTicket(G)
                    ki.updateGroup(G)

            elif msg.text in ["Protect join"]:
                  X = kc.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  kc.updateGroup(X)
                  invsend = 0
                  Ti = kc.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kc.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Cv3 join"]:
                if msg.from_ in staff:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "JOIN -- SUCCESS"
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Panda:bye"]:
                  if msg.from_ in staff:
                    ginfo = cl.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        kf.leaveGroup(msg.to)
                        print "SUKSES -- BOT OUT GROUP"
                    except:
                        pass
            elif msg.text in ["Panda:@bye"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                    except:
                        pass

#-------------------------KILL USER BANNED START-------------------------#
            elif msg.text in ["Panda:kickban"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"BYE")
                        return
                    for jj in matched_list:
                        try:
                            klist=[kc,kd,ke,kf]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                            print "SUKSES -- SEND KILL"
                        except:
                            pass
#-----------------------[Cleanse Section (USE AT YOUR OWN RISK!)]------------------------
            elif "Panda:fighting" in msg.text:
                if msg.from_ in staff:
                    print "ok"
                    _name = msg.text.replace("Panda:fighting","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    ki.sendText(msg.to,"Just some casual cleansing ")
                    kk.sendText(msg.to,"Group cleansed.")
                    kk.sendText(msg.to,"Bye All")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        kk.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if target not in Bots or staff or admin:
                            try:
                                klist=[cl,ki,kk,kc,kd,ke,kf]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Group cleanse")
                                kk.sendText(msg,to,"Group cleanse")
								
			#---------------kickall started----------------#                   
            elif "Loveyou" in msg.text:
              if msg.from_ in staff:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Loveyou","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    #gs = ki4.getGroup(msg.to)
                    #gs = ki5.getGroup(msg.to)
                    ki.sendText(msg.to,"「 PANDA」\nPANDA is STARTING♪\n abort to abort♪")
                    kk.sendText(msg.to,"「 PANDA 」\nแล้วเธอจะเข้าใจสิ่งที่ฉันทำ\nฉันรักเธอ")
                    kc.sendText(msg.to,"Good Bye (*´･ω･*)")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kd.sendText(msg.to,"Not Found")
                    else:
                        for target in targets:
                            if target not in Bots and staff:
                                try:
                                   klist=[ki,kk,kc,kd,ke,kf]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki3.sendText(msg.to,"PANDA done")
#-----------------------[Ban/Unban Section]------------------------
            elif "Nk " in msg.text:
                if msg.from_ in staff:
                       print "EXECUTED -- NK TARGET"
                       msg.contentType = 13
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kf.kickoutFromGroup(msg.to,[target])
                                    msg.contentMetadata = {'mid': target}
                                    cl.sendMessage(msg)
                                    print "SUKSES -- NK TARGET"
                                except:
                                    pass
#-------------------------TAG MEMBER START-------------------------#
            elif msg.text in ["Panda:tagall"]:
                if msg.from_ in staff:
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    cb = ""
                    cb2 = ""
                    strt = int(0)
                    akh = int(0)
                    for md in nama:
                        nrik = cl.getContact(md).displayName
                        akh = akh + int(5)
                        cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                        strt = strt + int(6)
                        akh = akh + 1
                        cb2 += "@nrik\n"
                    cb = (cb[:int(len(cb)-1)])
                    msg.contentType = 0
                    msg.text = cb2
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                    
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error

            elif msg.text in ["Tag All"]:
              if msg.from_ in admin:
                 group = cl.getGroup(msg.to)
                 mem = [contact.mid for contact in group.members]
                 for mm in mem:
                  xname = cl.getContact(mm).displayName
                  xlen = str(len(xname)+1)
                  msg.contentType = 0
                  msg.text = "@"+xname+" "
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
                  try:
                     ki.sendMessage(msg)
                  except Exception as error:
                                            print error
#-------------------------TAG MEMBER FINISHED-------------------------#
            elif "Blacklist @" in msg.text:
                _name = msg.text.replace("Blacklist @","")
                _kicktarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Succes Cv")
                                except:
                                    ki.sendText(msg.to,"error")
            elif ("Panda:ban " in msg.text):
              if msg.from_ in staff:
                print "EXECUTED -- BAN TARGET"
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"แบนเรียบร้อย")
                      print "SUKSES -- BAN TARGET"
                   except:
                      pass
            elif "Panda:unban @" in msg.text:
              if msg.from_ in staff:
                if msg.toType == 2:
                    print "EXECUTED -- UNBAN TARGET"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ki.sendText(msg.to,"ปลดแบนเรียบร้อย")
                                print "SUKSES -- UNBAN TARGET"
                            except:
                                ki.sendText(msg.to,"Succes UNBANNED")
            elif "Getpict @" in msg.text:
              if msg.from_ in staff:
                if msg.toType == 2:
                    _name = msg.text.replace("getpict @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                ginfo = cl.getContact(target)
                                cl.sendText(msg.to, "[Profile Status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                                cl.sendImage("http://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                                print "SUKSES -- Getpict TARGET"
                            except:
                                pass
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Me @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("Me @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                        pass
            elif "status @" in msg.text:
                msg.contentType = 0
                _name = msg.text.replace("status @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getContact(mid)
                for g in gs.members:
                    if _nametarget == gs.displayName:
                        cl.sendText(msg.to, "[Status Message]" + gs.statusMessage)
                    else:
                        pass 
#-----------------------------------------------
            elif msg.text in ["Panda:test"]:
               if msg.from_ in staff:
                ki.sendText(msg.to,"Ok Panda 􀨁􀄻double thumbs up􏿿")
#-----------------------------------------------
            elif "Bc " in msg.text:
                if msg.from_ in staff:
                    bctxt = msg.text.replace("Bc ","")
		    ki.sendText(msg.to,(bctxt))
                    kk.sendText(msg.to,(bctxt))
                    kc.sendText(msg.to,(bctxt))
#-----------------------------------------------

            elif msg.text in ["Panda:spon"]:
              if msg.from_ in staff:
                cl.sendText(msg.to,"Panda[V1]")
                ki.sendText(msg.to,"Panda[V2]")
                kk.sendText(msg.to,"Panda[V3]")
                kc.sendText(msg.to,"Panda[V4]")
                kd.sendText(msg.to,"Panda[V5]")
                ke.sendText(msg.to,"Panda[V6]")
                kf.sendText(msg.to,"Panda[V7]")
#-----------------------------------------------

            elif msg.text in ["Panda:speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
		pass
		start = time()
                ki.sendText(msg.to, "Progress...")
                elapsed_time = time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
				
				
#------------------------------------------------------------------	
            elif "Steal home @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
#------------------------------------------------------------------
            elif "Steal dp @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
#------------------------------------------------------------------

#-----------------------------------------------
            elif "Say:" in msg.text:
				bctxt = msg.text.replace("Say:","")
				cl.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
				kd.sendText(msg.to,(bctxt))
				ke.sendText(msg.to,(bctxt))
				kf.sendText(msg.to,(bctxt))
#----------------------------------------------- 

#------------------------------------------------------------------
            elif "Staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
					
            elif "Staff remove @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("staff remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif "Add admin @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]admin add executing"
                    _name = msg.text.replace("Add admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to)
                    #gs = kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Added to the admin list")
                            except:
                                pass
                    print "[Command]admin add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Remove admin @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]admin remove executing"
                    _name = msg.text.replace("Remove admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to)
                    #gs = kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Removed to the admin list")
                            except:
                                pass
                    print "[Command]admin remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Admin list","admin list"]:
                if admin == []:
                    ki.sendText(msg.to,"The stafflist is empty")
                else:
                    ki.sendText(msg.to,"Admin list:")
                    mc = ""
                    for mi_d in admin:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Adminlist executed"		
            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list:") 
                    mc = ""
                    for mi_d in staff:
                        mc += "->" "@"+cl.getContact(mi_d).displayName+"\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
            elif msg.text in ["Botlist","botlist"]:
                if Bots == []:
                    cl.sendText(msg.to,"The Botlist is empty")
                else:
                    cl.sendText(msg.to,"BOT list:")
                    mc = ""
                    for mi_d in Bots:
                        mc += "->" "@"+cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
            elif msg.text in ["Ip Like", "Ar like"]:
                if msg.from_ in staff:
                    print "[Command]Like executed"
                    cl.sendText(msg.to,"Trying to Like post(s) from staff")
                    try:
                        likePost()
                    except:
                        pass
#-----------------------[Auto Cancel Section]------------------------
                            
            elif msg.text in ["Panda:addblacklist"]:
              if msg.from_ in staff:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"กรุณาลงคอนแทรคที่จะแบน")
            elif msg.text in ["Panda:addwhitelist"]:
              if msg.from_ in staff:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"กรุณาลงคอนแทรคที่ปลดแบน")
            elif msg.text in ["Panda:blacklist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"ไม่มีรายชื่อที่ถูกแบน")
                else:
                    cl.sendText(msg.to,"รายชื่อผู้ที่ติดดำ")
                    cb = ""
                    cb2 = ""
                    strt = int(0)
                    akh = int(0)
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        nrik = cl.getContact(mi_d).displayName
                        akh = akh + int(5)
                        cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mi_d)+"},"""

                        strt = strt + int(6)
                        akh = akh + 1
                        cb2 += "@nrik\n"
                    cb = (cb[:int(len(cb)-1)])
                    msg.contentType = 0
                    msg.text = cb2
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                    
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Panda:killban"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    print "EXCUTED -- KILL BAN"
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        print "SUKSES -- KILL BAN"
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Good Bye ")
            elif "Cp @" in msg.text:
              if msg.from_ in staff:
                if msg.toType == 2:
                    print "EXECUTED -- BAN TARGET"
                    _name = msg.text.replace("Cp @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,msg.contentMetadata["g.mid"])
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            cl.sendText(msg.to,g.mid)
                        else:
                            pass
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["g.mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["g.mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["g.mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["g.mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["g.mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[g.mid]:\n" + msg.contentMetadata["g.mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif ("Contact " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(msg.contentMetadata["mid"])
                try:
                    cu = cl.channel.getCover(msg.contentMetadata["mid"])
                except:
                       cu = ""
                md = "[displayName]:\n" + contact.displayName + "\n[mid]:\n" +key1 + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu)
                cl.sendText(msg.to,md)
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)

                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"] + nowT
                ki.updateProfile(profile)

                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"] + nowT
                kk.updateProfile(profile)

                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"] + nowT
                kc.updateProfile(profile)

                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile5 = kd.getProfile()
                profile5.displayName = wait["cName5"] + nowT
                kd.updateProfile(profile)

                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile6 = ke.getProfile()
                profile6.displayName = wait["cName6"] + nowT
                ke.updateProfile(profile)

                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile7 = kf.getProfile()
                profile7.displayName = wait["cName7"] + nowT
                kf.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
    if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try: 
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By : IP\n\nPANDA")
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By: IP\n\nPANDA")
            print "Like"
        except:
            pass
    else:
        print "Already Liked"
        time.sleep(500)

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)