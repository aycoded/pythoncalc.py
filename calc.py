from tkinter import*

def icalc(source , side):
    storeObj= Frame(source,borderwidth=1,bd=4,bg="powder blue")
    storeObj.pack(side=side, expand=YES,fill=BOTH)
    return storeObj


def button(source,side,text,command=None):
    storeObj=Button(source,text=text,command=command)
    storeObj.pack(side=side,expand=YES,fill=BOTH)
    return storeObj
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font','arial 20 bold')
        self.pack(expand=YES,fill=BOTH)
        self.master.title('calculator')

        

        display = StringVar()
        Entry(self, relief= GROOVE,
                textvariable=display,justify="right", bd=35,bg='green').pack(side=TOP,expand=YES,fill=BOTH)

        
        for clearBut in ( ["CE"],["C"]):
            erase =icalc(self,TOP)
            for ichar in clearBut:
                button(erase,LEFT,ichar,
                       lambda storeObj=display ,q=ichar:storeObj.set(' '))
        for NumBut in ('123/','456+','789-','0.*'):
                FunctionNum =icalc(self,TOP)
                for char in NumBut:
                    button(FunctionNum,LEFT,char,
                           lambda storeObj =display, q=char:storeObj.set(storeObj.get()+q))
 
        EqualsButton=icalc(self,TOP)
        for iEquals in "=":
           if iEquals == "=":
               btniEquals=button(EqualsButton,LEFT,iEquals)
               btniEquals.bind('<ButtonRelease-1>',
                               lambda e ,s=self ,  storeObj=dipslay: s.calc(storeObj), '+')
        else:
              btniEquals=button(EqualsButton,LEFT,iEquals,
                                lambda storeObj=display, s='%s  '%iEquasls: storeObj.set(storeObj.get()+s)) 

                            
              
                            
        















if __name__ == '__main__':
    app().mainloop()



    
