import tkinter
import tkinter.messagebox
import pickle

def createbtn(root,API_ent,Auth_ent,DBurl_ent,Sbuc_ent):
    config = {"apiKey": API_ent.get(),"authDomain": Auth_ent.get(),"databaseURL": DBurl_ent.get(),"storageBucket": Sbuc_ent.get()}
    with open("Configuration.pyrebaseConfig","wb") as file:
        pickle.dump(config,file)
    tkinter.messagebox.showinfo('Done','Configuration file Successfully created..')
    root.destroy()



def createconfig():
    PyrebaseConfigWin = tkinter.Tk()
    PyrebaseConfigWin.title("Create a new Configuration File")
    frame = tkinter.LabelFrame(PyrebaseConfigWin, text = "Create a new Pyrebase Configuration File")

    API_lbl = tkinter.Label(frame,text = "API KEY:")
    API_lbl.grid(row = 1,column = 1, padx = 10 , pady = 10)
    API_ent = tkinter.Entry(frame, bd = 2)
    API_ent.grid(row = 1,column = 2 , padx = 10 , pady = 10)

    Auth_lbl = tkinter.Label(frame,text = "AuthDomain:")
    Auth_lbl.grid(row = 2,column = 1, padx = 10 , pady = 10)
    Auth_ent = tkinter.Entry(frame, bd = 2)
    Auth_ent.grid(row = 2,column = 2 , padx = 10 , pady = 10)

    DBurl_lbl = tkinter.Label(frame,text = "Database URL:")
    DBurl_lbl.grid(row = 3,column = 1, padx = 10 , pady = 10)
    DBurl_ent = tkinter.Entry(frame, bd = 2)
    DBurl_ent.grid(row = 3,column = 2 , padx = 10 , pady = 10)

    Sbuc_lbl = tkinter.Label(frame,text = "Storage Bucket:")
    Sbuc_lbl.grid(row = 4,column = 1, padx = 10 , pady = 10)
    Sbuc_ent = tkinter.Entry(frame, bd = 2)
    Sbuc_ent.grid(row = 4,column = 2 , padx = 10 , pady = 10)

    cre_btn = tkinter.Button(frame , text = "Create", command = lambda:createbtn(PyrebaseConfigWin,API_ent,Auth_ent,DBurl_ent,Sbuc_ent))
    cre_btn.grid(row = 5,column = 2, padx = 10, pady = 10)

    frame.pack(fill = "both", expand = 'yes')
    PyrebaseConfigWin.mainloop()

def Loadconfig():
    PyrebaseConfigWin = tkinter.Tk()
    PyrebaseConfigWin.title("Information in Configuration File")
    frame = tkinter.LabelFrame(PyrebaseConfigWin, text = "Configuration File Info")

    with open("Configuration.pyrebaseConfig",'rb') as file:
        config = {}
        config = pickle.load(file)
    
    API_lbl = tkinter.Label(frame,text = "API KEY:")
    API_lbl.grid(row = 1,column = 1, padx = 10 , pady = 10)
    APIinfo_lbl = tkinter.Label(frame,text = config['apiKey'])
    APIinfo_lbl.grid(row = 1,column = 2 , padx = 10 , pady = 10)

    Auth_lbl = tkinter.Label(frame,text = "AuthDomain:")
    Auth_lbl.grid(row = 2,column = 1, padx = 10 , pady = 10)
    Authinfo_lbl = tkinter.Label(frame,text = config['authDomain'])
    Authinfo_lbl.grid(row = 2,column = 2 , padx = 10 , pady = 10)
    
    DBurl_lbl = tkinter.Label(frame,text = "Database URL:")
    DBurl_lbl.grid(row = 3,column = 1, padx = 10 , pady = 10)
    DBurlinfo_lbl = tkinter.Label(frame,text = config['databaseURL'])
    DBurlinfo_lbl.grid(row = 3,column = 2 , padx = 10 , pady = 10)

    Sbuc_lbl = tkinter.Label(frame,text = "Storage Bucket:")
    Sbuc_lbl.grid(row = 4,column = 1, padx = 10 , pady = 10)
    Sbucinfo_lbl = tkinter.Label(frame,text = config['storageBucket'])
    Sbucinfo_lbl.grid(row = 4,column = 2 , padx = 10 , pady = 10)

    cre_btn = tkinter.Button(frame , text = "Ok", command = PyrebaseConfigWin.destroy)
    cre_btn.grid(row = 5,column = 2, padx = 10, pady = 10)

    frame.pack(fill = "both", expand = 'yes')
    PyrebaseConfigWin.mainloop()

