from tkinter import*
from tkinter import ttk

   
def Accept():
        x=lista_desplegable.get()
        y=lista_desplegable2.get()
        print(x)
        print(y)
#------------------------------------------------------diodo        
        if((x=="DIODO") and (y=="100Hz")):
            imageIT.config(image=imagenDIODO100)
            imageIT2.config(image=imagenDIODO100Esq)#---------------------
            textod.config(text="""
            Diode
            Among all the static switching devices used un power electronics (PE), the power diode is perhaps
            the simples. It is a two terminal device, and terminal A is known as the anode whereas terminal K is
            known as a cathode. If terminal A experiences a higher potential compared to terminal K, the
            device is said to be forward biased and a current called forward current. This causes a small voltage
            drop across the device (<1V), wich in ideal condition is usually ignored. On the hand other, when a 
            diode is reverse biased, it does not conduct and a practical diode do experience a small current 
            flowing in the reverse direction called the leakage current. Both the forward voltage drop and the 
            leakage current are ignores in an ideal diode. Usually in PE applications a diode is considered to be 
            an ideal static switch.
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 
            
        elif((x=="DIODO") and (y=="1KHz")):
            imageIT.config(image=imagenDIODO1k)
            imageIT2.config(image=imagenDIODO1KEsq)#---------------------
            textod.config(text="""
            Diode
            Among all the static switching devices used un power electronics (PE), the power diode is perhaps
            the simples. It is a two terminal device, and terminal A is known as the anode whereas terminal K is
            known as a cathode. If terminal A experiences a higher potential compared to terminal K, the
            device is said to be forward biased and a current called forward current. This causes a small voltage
            drop across the device (<1V), wich in ideal condition is usually ignored. On the hand other, when a 
            diode is reverse biased, it does not conduct and a practical diode do experience a small current 
            flowing in the reverse direction called the leakage current. Both the forward voltage drop and the 
            leakage current are ignores in an ideal diode. Usually in PE applications a diode is considered to be 
            an ideal static switch.
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black")
        elif((x=="DIODO") and (y=="10KHz")):
            imageIT.config(image=imagenDIODO10k)
            imageIT2.config(image=imagenDIODO10KEsq)#---------------------
            textod.config(text="""
            Diode
            Among all the static switching devices used un power electronics (PE), the power diode is perhaps
            the simples. It is a two terminal device, and terminal A is known as the anode whereas terminal K is
            known as a cathode. If terminal A experiences a higher potential compared to terminal K, the
            device is said to be forward biased and a current called forward current. This causes a small voltage
            drop across the device (<1V), wich in ideal condition is usually ignored. On the hand other, when a 
            diode is reverse biased, it does not conduct and a practical diode do experience a small current 
            flowing in the reverse direction called the leakage current. Both the forward voltage drop and the 
            leakage current are ignores in an ideal diode. Usually in PE applications a diode is considered to be 
            an ideal static switch.
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black")             
        elif((x=="DIODO") and (y=="100KHz")):
            imageIT.config(image=imagenDIODO100k)
            imageIT2.config(image=imagenDIODO100KEsq)#---------------------
            textod.config(text="""
            Diode
            Among all the static switching devices used un power electronics (PE), the power diode is perhaps
            the simples. It is a two terminal device, and terminal A is known as the anode whereas terminal K is
            known as a cathode. If terminal A experiences a higher potential compared to terminal K, the
            device is said to be forward biased and a current called forward current. This causes a small voltage
            drop across the device (<1V), wich in ideal condition is usually ignored. On the hand other, when a 
            diode is reverse biased, it does not conduct and a practical diode do experience a small current 
            flowing in the reverse direction called the leakage current. Both the forward voltage drop and the 
            leakage current are ignores in an ideal diode. Usually in PE applications a diode is considered to be 
            an ideal static switch.
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 
#-------------------------------------------------------mosfet
        elif((x=="MOSFET") and (y=="100Hz")):
            imageIT.config(image=imagenMOSFET100)
            imageIT2.config(image=imagenMOSFET100Esq)#---------------------
            textod.config(text="""
            MOSFET
            Unlike the bipolar junction transistor (BJT), the MOSFET device belongs to the Unipolar Device 
            family, since it uses only the majority carriers in conduction. The development of the metal oxide 
            semiconductor technology for microelectronic circuits opened the way for developing the power 
            metal oxide semiconductor field effect transistor (MOSFET) device in 1975. It is the fastest power        
            switching device whit switching frequency more tan 1 MHz, whit voltage power ratings up to             
            1000V and current rating as high as 300 A. the P-N junction between p-base (also referred to as 
            body or bulk region) and the n-drift region provide the forward voltage blocking capabilities. The             
            source metal contact is connected directly to the p-base region through a break in the n+ source 
            region in order to allow for a fixed potential to p-base region during the normal device operation.
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black")             
        elif((x=="MOSFET") and (y=="1KHz")):
            imageIT.config(image=imagenMOSFET1K)
            imageIT2.config(image=imagenMOSFET1KEsq)#---------------------
            textod.config(text="""
            MOSFET
            Unlike the bipolar junction transistor (BJT), the MOSFET device belongs to the Unipolar Device 
            family, since it uses only the majority carriers in conduction. The development of the metal oxide 
            semiconductor technology for microelectronic circuits opened the way for developing the power 
            metal oxide semiconductor field effect transistor (MOSFET) device in 1975. It is the fastest power        
            switching device whit switching frequency more tan 1 MHz, whit voltage power ratings up to             
            1000V and current rating as high as 300 A. the P-N junction between p-base (also referred to as 
            body or bulk region) and the n-drift region provide the forward voltage blocking capabilities. The             
            source metal contact is connected directly to the p-base region through a break in the n+ source 
            region in order to allow for a fixed potential to p-base region during the normal device operation.
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 
        elif((x=="MOSFET") and (y=="10KHz")):
            imageIT.config(image=imagenMOSFET10K)
            imageIT2.config(image=imagenMOSFET10KEsq)#---------------------
            textod.config(text="""
            MOSFET
            Unlike the bipolar junction transistor (BJT), the MOSFET device belongs to the Unipolar Device 
            family, since it uses only the majority carriers in conduction. The development of the metal oxide 
            semiconductor technology for microelectronic circuits opened the way for developing the power 
            metal oxide semiconductor field effect transistor (MOSFET) device in 1975. It is the fastest power        
            switching device whit switching frequency more tan 1 MHz, whit voltage power ratings up to             
            1000V and current rating as high as 300 A. the P-N junction between p-base (also referred to as 
            body or bulk region) and the n-drift region provide the forward voltage blocking capabilities. The             
            source metal contact is connected directly to the p-base region through a break in the n+ source 
            region in order to allow for a fixed potential to p-base region during the normal device operation.
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 
        elif((x=="MOSFET") and (y=="100KHz")):
            imageIT.config(image=imagenMOSFET100K)
            imageIT2.config(image=imagenMOSFET100KEsq)#---------------------
            textod.config(text="""
            MOSFET
            Unlike the bipolar junction transistor (BJT), the MOSFET device belongs to the Unipolar Device 
            family, since it uses only the majority carriers in conduction. The development of the metal oxide 
            semiconductor technology for microelectronic circuits opened the way for developing the power 
            metal oxide semiconductor field effect transistor (MOSFET) device in 1975. It is the fastest power        
            switching device whit switching frequency more tan 1 MHz, whit voltage power ratings up to             
            1000V and current rating as high as 300 A. the P-N junction between p-base (also referred to as 
            body or bulk region) and the n-drift region provide the forward voltage blocking capabilities. The             
            source metal contact is connected directly to the p-base region through a break in the n+ source 
            region in order to allow for a fixed potential to p-base region during the normal device operation.
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 
#-------------------------------------------------------bjt
        elif((x=="BJT") and (y=="100Hz")):
            imageIT.config(image=imagenBJT100)
            imageIT2.config(image=imagenBJT100Esq)#---------------------
            textod.config(text="""
            BJT
            The bipolar junction transistor (BJT) consists of a three-region structure of n-type semiconductor
            materials, it can be constructed as npn as well as pnp. The operation is closely related to that of a
            junction diode where in normal conditions the pn junction between the base and collector is
            forward-biased (VBE>0) causing electrons to be injected from the emitter into the base. Since the
            base region is thin, the electrons travel across arriving at the reverse-biased base-collector
            junction (VBC<0) where there is an electric field (depletion region). Even though the forward
            biased Base-emitter junction injects holes from base to emitter they do not contribute to the
            collector current but result in a net current Flow component into a base from the external base
            terminal.            
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 
        elif((x=="BJT") and (y=="1KHz")):
            imageIT.config(image=imagenBJT1K)
            imageIT2.config(image=imagenBJT1KEsq)#---------------------
            textod.config(text="""
            BJT
            The bipolar junction transistor (BJT) consists of a three-region structure of n-type semiconductor
            materials, it can be constructed as npn as well as pnp. The operation is closely related to that of a
            junction diode where in normal conditions the pn junction between the base and collector is
            forward-biased (VBE>0) causing electrons to be injected from the emitter into the base. Since the
            base region is thin, the electrons travel across arriving at the reverse-biased base-collector
            junction (VBC<0) where there is an electric field (depletion region). Even though the forward
            biased Base-emitter junction injects holes from base to emitter they do not contribute to the
            collector current but result in a net current Flow component into a base from the external base
            terminal.            
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 
        elif((x=="BJT") and (y=="10KHz")):
            imageIT.config(image=imagenBJT10K)
            imageIT2.config(image=imagenBJT10KEsq)#---------------------
            textod.config(text="""
            BJT
            The bipolar junction transistor (BJT) consists of a three-region structure of n-type semiconductor
            materials, it can be constructed as npn as well as pnp. The operation is closely related to that of a
            junction diode where in normal conditions the pn junction between the base and collector is
            forward-biased (VBE>0) causing electrons to be injected from the emitter into the base. Since the
            base region is thin, the electrons travel across arriving at the reverse-biased base-collector
            junction (VBC<0) where there is an electric field (depletion region). Even though the forward
            biased Base-emitter junction injects holes from base to emitter they do not contribute to the
            collector current but result in a net current Flow component into a base from the external base
            terminal.            
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 
        elif((x=="BJT") and (y=="100KHz")):
            imageIT.config(image=imagenBJT100K)
            imageIT2.config(image=imagenBJT100KEsq)#---------------------
            textod.config(text="""
            BJT
            The bipolar junction transistor (BJT) consists of a three-region structure of n-type semiconductor
            materials, it can be constructed as npn as well as pnp. The operation is closely related to that of a
            junction diode where in normal conditions the pn junction between the base and collector is
            forward-biased (VBE>0) causing electrons to be injected from the emitter into the base. Since the
            base region is thin, the electrons travel across arriving at the reverse-biased base-collector
            junction (VBC<0) where there is an electric field (depletion region). Even though the forward
            biased Base-emitter junction injects holes from base to emitter they do not contribute to the
            collector current but result in a net current Flow component into a base from the external base
            terminal.            
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 
#-------------------------------------------------------igbt
        elif((x=="IGBT") and (y=="100Hz")):
            imageIT.config(image=imagenIGBT100)
            imageIT2.config(image=imagenIGBT100Esq)#---------------------
            textod.config(text="""
            IGBT
            IGBT is a three-terminal power semiconductor switch used to control the electrical energy. Prior 
            to the advent of IGBT, power bipolar junction transistors (BJT) and power metal oxide field effect 
            transistors (MOSFET) were widely used in low to medium power and high-frequency applications, 
            where the speed of gate turn-off thyristors was not adequate. Power BJTs have Good on-state 
            characteristics but have long switching times especially at turn-off. They are current-controlled 
            devices whit small current gain because of high-level injection effects and wide base width 
            required to prevent reach-through breakdown for hig blocking voltage capability. Therefore, they 
            require complex base drive circuits to provide the base current during  on-state, wich increases 
            the power lost in the control electrode
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 
        elif((x=="IGBT") and (y=="1KHz")):
            imageIT.config(image=imagenIGBT1K)
            imageIT2.config(image=imagenIGBT1KEsq)#---------------------
            textod.config(text="""
            IGBT
            IGBT is a three-terminal power semiconductor switch used to control the electrical energy. Prior 
            to the advent of IGBT, power bipolar junction transistors (BJT) and power metal oxide field effect 
            transistors (MOSFET) were widely used in low to medium power and high-frequency applications, 
            where the speed of gate turn-off thyristors was not adequate. Power BJTs have Good on-state 
            characteristics but have long switching times especially at turn-off. They are current-controlled 
            devices whit small current gain because of high-level injection effects and wide base width 
            required to prevent reach-through breakdown for hig blocking voltage capability. Therefore, they 
            require complex base drive circuits to provide the base current during  on-state, wich increases 
            the power lost in the control electrode
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 
        elif((x=="IGBT") and (y=="10KHz")):
            imageIT.config(image=imagenIGBT10K)
            imageIT2.config(image=imagenIGBT10KEsq)#---------------------
            textod.config(text="""
            IGBT
            IGBT is a three-terminal power semiconductor switch used to control the electrical energy. Prior 
            to the advent of IGBT, power bipolar junction transistors (BJT) and power metal oxide field effect 
            transistors (MOSFET) were widely used in low to medium power and high-frequency applications, 
            where the speed of gate turn-off thyristors was not adequate. Power BJTs have Good on-state 
            characteristics but have long switching times especially at turn-off. They are current-controlled 
            devices whit small current gain because of high-level injection effects and wide base width 
            required to prevent reach-through breakdown for hig blocking voltage capability. Therefore, they 
            require complex base drive circuits to provide the base current during  on-state, wich increases 
            the power lost in the control electrode
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 
        elif((x=="IGBT") and (y=="100KHz")):
            imageIT.config(image=imagenIGBT100K)
            imageIT2.config(image=imagenIGBT100KEsq)#---------------------
            textod.config(text="""
            IGBT
            IGBT is a three-terminal power semiconductor switch used to control the electrical energy. Prior 
            to the advent of IGBT, power bipolar junction transistors (BJT) and power metal oxide field effect 
            transistors (MOSFET) were widely used in low to medium power and high-frequency applications, 
            where the speed of gate turn-off thyristors was not adequate. Power BJTs have Good on-state 
            characteristics but have long switching times especially at turn-off. They are current-controlled 
            devices whit small current gain because of high-level injection effects and wide base width 
            required to prevent reach-through breakdown for hig blocking voltage capability. Therefore, they 
            require complex base drive circuits to provide the base current during  on-state, wich increases 
            the power lost in the control electrode
            """,justify=LEFT,font=("Times new roman",14),bg="white",fg="black") 

VP=Tk()
#Condiguración de ventana principal
VP.geometry("1300x780+100+10")
VP.title("Power electronics ")
VP.config(bg="white")
VP.iconbitmap("itc.ico")

textoI= Label(VP,text="Instructions ",font=("Times new roman",24,"bold"),bg="white",fg="black")
textoI.place(x=10,y=10)
textoIC= Label(VP,text="Select the corresponding boxes you want to know",font=("Times new roman",12),bg="white",fg="black")
textoIC.place(x=10,y=55)



#------IGBT---------------------------------------------------------------ya
imagenIGBT100=PhotoImage(file="IGBT-100Hz.png")
imagenIGBT100Esq=PhotoImage(file="EsquematicoIGBT.png")#-------------------------


imagenIGBT1K=PhotoImage(file="IGBT-1KHz.png")
imagenIGBT1KEsq=PhotoImage(file="EsquematicoIGBT.png")#-------------------------

imagenIGBT10K=PhotoImage(file="IGBT-10KHz.png")
imagenIGBT10KEsq=PhotoImage(file="EsquematicoIGBT.png")#-------------------------

imagenIGBT100K=PhotoImage(file="IGBT-100KHz.png")
imagenIGBT100KEsq=PhotoImage(file="EsquematicoIGBT.png")#-------------------------

#DIODO---------------------------------------------------------------------ya
imagenDIODO100=PhotoImage(file="Diode at 100Hz.png")
imagenDIODO100Esq=PhotoImage(file="EsquematicoDIODO.png")#-------------------------

imagenDIODO1k=PhotoImage(file="Diode at 1KHz.png")
imagenDIODO1KEsq=PhotoImage(file="EsquematicoDIODO.png")#-------------------------

imagenDIODO10k=PhotoImage(file="Diode at 10KHz.png")
imagenDIODO10KEsq=PhotoImage(file="EsquematicoDIODO.png")#-------------------------

imagenDIODO100k=PhotoImage(file="Diode at 100KHz.png")
imagenDIODO100KEsq=PhotoImage(file="EsquematicoDIODO.png")#-------------------------

#MOSFET----------------------------------------------------------------------ya
imagenMOSFET100=PhotoImage(file="MOSFET-100Hz.png")
imagenMOSFET100Esq=PhotoImage(file="EsquematicoMOSFET.png")#-------------------------

imagenMOSFET1K=PhotoImage(file="MOSFET-1KHz.png")
imagenMOSFET1KEsq=PhotoImage(file="EsquematicoMOSFET.png")#-------------------------

imagenMOSFET10K=PhotoImage(file="MOSFET-10KHz.png")
imagenMOSFET10KEsq=PhotoImage(file="EsquematicoMOSFET.png")#-------------------------

imagenMOSFET100K=PhotoImage(file="MOSFET-100KHz.png")
imagenMOSFET100KEsq=PhotoImage(file="EsquematicoMOSFET.png")#-------------------------

#BJT-------------------------------------------------------------------------ya
imagenBJT100=PhotoImage(file="BJT-100Hz.png")
imagenBJT100Esq=PhotoImage(file="EsquematicoBJT.png")#-------------------------

imagenBJT1K=PhotoImage(file="BJT-1KHz.png")
imagenBJT1KEsq=PhotoImage(file="EsquematicoBJT.png")#-------------------------

imagenBJT10K=PhotoImage(file="BJT-10KHz.png")
imagenBJT10KEsq=PhotoImage(file="EsquematicoBJT.png")#-------------------------

imagenBJT100K=PhotoImage(file="BJT-100KHz.png")
imagenBJT100KEsq=PhotoImage(file="EsquematicoBJT.png")#-------------------------


#Lista desplegable
lista_desplegable=ttk.Combobox(VP,width=17)
lista_desplegable.place(x=30,y=100)
#lista de opciones
opciones=["DIODO","IGBT","BJT","MOSFET"]
lista_desplegable['values']=opciones

#Lista desplegable frecuencias
lista_desplegable2=ttk.Combobox(VP,width=17)
lista_desplegable2.place(x=200,y=100)
#lista de opciones
opciones2=["100Hz","1KHz","10KHz","100KHz"]
lista_desplegable2['values']=opciones2


botonOK=Button(VP,text="Accept",command=Accept,font=("Times new roman",12,"bold"),width=14,bg="hot pink")
botonOK.place(x=400,y=100)

imagenT=PhotoImage(file="Transparente.png")
imageIT=Label(VP,image=imagenT,bg="white")
imageIT.place(x=850,y=150)
imageIT2=Label(VP,image=imagenT,bg="white")
imageIT2.place(x=350,y=400)
textod= Label(VP,text=" ",bg="white",fg="black")
textod.place(x=0,y=150)

VP.mainloop()

