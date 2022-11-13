from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def dashboard():
    start_msg = '<a href="https://github.com/Elyoni003">-TGUploaderV12-</a>\n'
    start_msg += '<b>🚨𝖀𝖘𝖔: 𝕰𝖓𝖛𝖎𝖆 𝕰𝖓𝖑𝖆𝖈𝖊𝖘 𝕯𝖊 𝕯𝖊𝖘𝖈𝖆𝖗𝖌𝖆 𝖞 𝕬𝖗𝖈𝖍𝖎𝖛𝖔𝖘 𝕻𝖆𝖗𝖆 𝕻𝖗𝖔𝖈𝖊𝖘𝖆𝖗 (𝕮𝖔𝖓𝖋𝖎𝖌𝖚𝖗𝖊 𝕬𝖓𝖙𝖊𝖘 𝕯𝖊 𝕰𝖒𝖕𝖊𝖟𝖆𝖗 , 𝖁𝖊𝖆 𝕰𝖑 /tutorial)</b>\n'
    return start_msg

def text_progres(index,max,size=21,step_size=5):
    try:
        if max<1:
            max += 1
        porcent = index / max
        porcent *= 100
        porcent = round(porcent)
        make_text = ''
        index_make = 1
        make_text += '[\n'
        while(index_make<size):
            if porcent >= index_make * step_size:make_text+='●'
            else:make_text+='○'
            index_make+=1
        make_text += '\n]'
        return make_text
    except Exception as ex:
            return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = '📡 𝕯𝖊𝖘𝖈𝖆𝖗𝖌𝖆𝖓𝖉𝖔 𝕬𝖗𝖈𝖍𝖎𝖛𝖔....\n\n'
    msg += '📁 𝕬𝖗𝖈𝖍𝖎𝖛𝖔: ' + filename + '\n'
    msg += text_progres(currentBits, totalBits) + '\n'
    msg += '➤ 𝕻𝖔𝖗𝖈𝖊𝖓𝖙𝖆𝖏𝖊: ' + str(porcent(currentBits, totalBits)) + '%\n\n'
    msg += '🗂𝕿𝖔𝖙𝖆𝖑: ' + sizeof_fmt(totalBits) + '\n\n'
    msg += '⏬𝕯𝖊𝖘𝖈𝖆𝖗𝖌𝖆𝖉𝖔: ' + sizeof_fmt(currentBits) + '\n\n'
    msg += '𝕾𝖚𝖇𝖎𝖉𝖔�: ' + sizeof_fmt(speed) + '/s\n\n'
    msg += '⏱𝖙𝖎𝖊𝖒𝖕𝖔 𝖉𝖊 𝖉𝖊𝖘𝖈𝖆𝖗𝖌𝖆: ' + str(datetime.timedelta(seconds=int(time))) + 's\n\n'
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = '⏫ 𝕾𝖚𝖇𝖎𝖊𝖓𝖉𝖔 𝕬 𝕷𝖆 𝕹𝖚𝖇𝖊☁...\n\n'
    msg += '🖊 𝕹𝖔𝖒𝖇𝖗𝖊: ' + filename + '\n'
    if originalname != '':
        msg = str(msg).replace(filename, originalname)
        msg += '🖊𝕹𝖔𝖒𝖇𝖗𝖊: ' + str(filename) + '\n'
    msg += text_progres(currentBits, totalBits) + '\n'
    msg += '➤ 𝕻𝖔𝖗𝖈𝖊𝖓𝖙𝖆𝖏𝖊: ' + str(porcent(currentBits, totalBits)) + '%\n\n'
    msg += '🗂 𝕿𝖔𝖙𝖆𝖑: ' + sizeof_fmt(totalBits) + '\n\n'
    msg += '➤ 𝕾𝖚𝖇𝖎𝖉𝖔: ' + sizeof_fmt(currentBits) + '\n\n'
    msg += '📡 𝖁𝖊𝖑𝖔𝖈𝖎𝖉𝖆𝖉: ' + sizeof_fmt(speed) + '/s\n\n'
    msg += '⏱ 𝖙𝖎𝖊𝖒𝖕𝖔 𝖉𝖊 𝖉𝖊𝖘𝖈𝖆𝖗𝖌𝖆: ' + str(datetime.timedelta(seconds=int(time))) + 's\n\n'
    return msg
def createCompresing(filename,filesize,splitsize):
    msg = '📥𝕮𝖔𝖒𝖕𝖗𝖎𝖒𝖎𝖊𝖓𝖉𝖔 𝕷𝖆𝖘 𝕻𝖆𝖗𝖙𝖊𝖘... \n\n'
    msg+= '🖊𝕹𝖔𝖒𝖇𝖗𝖊: ' + str(filename)+'\n'
    msg+= '🗓𝕿𝖆𝖒𝖆ñ𝖔 𝕿𝖔𝖙𝖆𝖑: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '📦𝕿𝖆𝖒𝖆ñ𝖔 𝕻𝖆𝖗𝖙𝖊𝖘: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= '➤⏱𝖙𝖎𝖊𝖒𝖕𝖔 𝖉𝖊 𝖉𝖊𝖘𝖈𝖆𝖗𝖌𝖆: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,datacallback=None):
    msg = '✔ ' + str(filename)+ f' Subido {str(sizeof_fmt(filesize))}\n'
    if datacallback:
       msg += 'datacallback: ' + datacallback
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>🖇𝕰𝖓𝖑𝖆𝖈𝖊𝖘🖇</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">🔗' + f['𝖓𝖆𝖒𝖊'] + '🔗</a>'
            msg+= "<a href='"+url+"'>🔗"+f['𝖓𝖆𝖒𝖊']+'🔗</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = '📑𝕬𝖗𝖈𝖍𝖎𝖛𝖔𝖘 ('+str(len(evfiles))+')📑\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = '⚙️𝕮𝖔𝖓𝖋𝖎𝖌𝖚𝖗𝖆𝖈𝖎𝖔𝖓𝖊𝖘 𝕯𝖊 𝖀𝖘𝖚𝖆𝖗𝖎𝖔⚙️\n\n'
    msg+= '➤ 𝕹𝖔𝖒𝖇𝖗𝖊: @' + str(username)+'\n'
    msg+= '➤ 𝖀𝖘𝖊𝖗: ' + str(userdata['moodle_user'])+'\n'
    msg+= '➤ 𝕻𝖆𝖘𝖘𝖜𝖔𝖗𝖉: ' + str(userdata['moodle_password']) +'\n'
    msg+= '➤ 𝕳𝖔𝖘𝖙: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= '➤ 𝕽𝖊𝖕𝖔𝕴𝕯: ' + str(userdata['moodle_repo_id'])+'\n'
        msg+= '➤ 𝖀𝖕𝕿𝖞𝖕𝖊: ' + str(userdata['uploadtype'])+'\n'
    msg += '➤ 𝕮𝖑𝖔𝖚𝖉𝕿𝖞𝖕𝖊: ' + str(userdata['cloudtype']) + '\n'
    if userdata['𝖈𝖑𝖔𝖚𝖉𝖙𝖞𝖕𝖊'] == 'cloud':
        msg+= '➤ Dir: /' + str(userdata['dir'])+'\n'
    msg+= '🧰 𝕿𝖆𝖒𝖆ñ𝖔 𝖉𝖊 𝖅𝖎𝖕𝖘 : ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = '✘'

    if isadmin:
        msgAdmin = '✔'
    msg+= '➤ 𝕬𝖉𝖒𝖎𝖓 : ' + msgAdmin + '\n'
    𝖕𝖗𝖔𝖝𝖞 = '✘'
    if userdata['proxy'] !='':
       𝖕𝖗𝖔𝖝𝖞 = '✔'
    rename = '✘'
    if userdata['rename'] == 1:
       rename = '✔'
    msg+= '➤ Rename : ' + rename + '\n'
    msg+= '➤ Proxy : ' + proxy + '\n'
    shorturl = (userdata['urlshort'] == 1)
    shortener = '✘'
    if shorturl:
       shortener = '✔'
    msg += '➤ShortUrl : ' + shortener + '\n\n'
    return msg
