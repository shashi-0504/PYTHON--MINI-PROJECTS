from tkinter import *
import speedtest
def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+" Mbps"
    up= str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
    l1.config(text=down)
    l2.config(text=up)
sp=Tk()
sp.title(" INTERNET SPEED TEST")
sp.geometry("500x650")
sp.config(bg='lightblue')
l=Label(sp,text="INTERNET SPEED TEST",font=("Time New Roman",20,"bold"),bg='lightblue',fg="blue")
l.place(x=65,y=40,height=50,width=380)
l=Label(sp,text="DOWNLOAD SPEED",font=("Time New Roman",20,"bold"))
l.place(x=65,y=130,height=50,width=380)
l1=Label(sp,text="00",font=("Time New Roman",20,"bold"))
l1.place(x=65,y=200,height=50,width=380)
l=Label(sp,text="UPLOAD SPEED",font=("Time New Roman",20,"bold"))
l.place(x=65,y=290,height=50,width=380)
l2=Label(sp,text="00",font=("Time New Roman",20,"bold"))
l2.place(x=65,y=360,height=50,width=380)

but=Button(sp,text="CHECK SPEED",font=("Time New Roman",20,"bold"),relief=RAISED,bg="red",fg="white",command=speedcheck)
but.place(x=65,y=460,height=50,width=380)
sp.mainloop()
