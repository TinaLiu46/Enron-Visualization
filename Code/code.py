import os
import pandas as pd
from pyarrow import feather
import sys

def filter_email(list_emails):
    #filter out email outside enron organization
    remove_list = []
    for email in list_emails:    
        if "@enron.com" not in email:
            remove_list.append(email)
    filtered_list = [a for a in list_emails if a not in remove_list]
    #filter out email with strange format
    remove_list = []
    for email in filtered_list:
        if '/o' in email  or "#" in email or "<" in email:
            remove_list.append(email)
    filtered_list = [a for a in filtered_list if a not in remove_list]
    filtered_list = [a for a in filtered_list if a != ""]
    return filtered_list

def normalize_email(list_emails):
    #normalize email addresses
    for i in range(len(list_emails)):
        if  "'" in list_emails[i]:
            list_emails[i] = list_emails[i].replace("'","")
        if list_emails[i].startswith("."):
            list_emails[i] = list_emails[i][1:]         
    return list_emails


def openfile(file):
    #open each file and extract the information we need
    with open(file,"r",encoding='latin1') as f:
        contents = f.readlines()
    Date = contents[1].split()
    Date = Date[1:]
    #sender
    From = contents[2].split()[1:]
    #receipients
    To = []
    for i in range(3,len(contents)):
        line = contents[i].split()
        if line[0] != 'Subject:':
            To += line
        else: 
            break
    To = To[1:]
    #Sunject
    Subject = contents[i].strip('\n')
    if len(Subject) > 0:
        Subject = Subject[9:]
    else:
        Subject = np.nan
    List = [Date,From,To,Subject]
    return List



def getDate(list_d):
    #Create a dict for date
    Dict_Month = {'Jan':"01",'Feb':"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09",
                 "Oct":"10","Nov":"11","Dec":"12"}
    Dict_Day = {'1':"01","2":"02","3":"03","4":"04","5":"05","6":"06","7":"07","8":"08","9":"09"}
    Year = list_d[3]
    Month = Dict_Month[list_d[2]]
    if Year == '0001':
        Year = '2001'
    elif Year == '0002':
        Year = '2002'
    Day = list_d[1]
    if Day in Dict_Day.keys():
        Day = Dict_Day[Day]
    return Year+"-"+Month+"-"+Day


def getFrom(list_f):
    if list_f == []:
        return None
    List = [list_f[0]]
    Filtered_Email = filter_email(List)
    Final = normalize_email(Filtered_Email)
    if Final == []:
        return None
    else:
        From = Final[0].split("@")
        return From[0]


def getTo(list_t):
    if list_t == []:
        return None
    Filtered_Email = filter_email(list_t)
    Final = normalize_email(Filtered_Email)
    List_To = []
    if Final ==[]:
        return None
    else:
        for receipients in Final:
            receipients = receipients.split("@")
            List_To.append(receipients[0])
        Final1 = [a for a in List_To if a!=""]
        if Final1 == []:
            return None
        else:
            return Final1




def getSubject(list_s):
    if len(list_s)>0:
        subject = list_s[0]
        for string in list_s[1:]:
            subject = subject +" "+string
        return subject
    else:
        return ""



def getfilename(string):
    string = string.split("maildir/")
    filename = string[1]
    return filename





fileList = []
rootdir = sys.argv[1]
for root, dirs, files in sorted(os.walk(rootdir)):
    for f in sorted(files):
        if f != '.DS_Store':
            fileList.append(os.path.join(root,f))


MailID = []
Date = []
From = []
To = []
Recipients = []
Subject = []
filename = []
count = 0    
for i in range(len(fileList)):
    textList = openfile(fileList[i])
    if getFrom(textList[1]) and getTo(textList[2]) is not None:
        count = count + 1
        MailID.append(count)
        Date.append(getDate(textList[0]))
        From.append(getFrom(textList[1]))
        To.append(getTo(textList[2]))
        Recipients.append(len(getTo(textList[2])))
        Subject.append(getSubject(textList[3]))
        filename.append(getfilename(fileList[i]))


#convert to a DataFrame
df = pd.DataFrame({'MailID':MailID,'Date':Date,'From':From,'To':To,"Recipients":Recipients,"Subject":Subject,
                  "filename":filename})
df = df.explode('To',ignore_index=True)

#Export to feather
df.to_feather('enron.feather')





