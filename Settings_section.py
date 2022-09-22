#------------------------------------------------------settings 
                    
                    def select_settings():
                        
                        set_btn_1.grid_forget()
                        lst_prf_1.place_forget()
                        set_btn_2 = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
                        set_btn_2.grid(row=2,column=5,padx=(0,30))

                    def lst_prf_slt_1(event):
                        selected_indices = lst_prf_1.curselection()
                        selected_langs = ",".join([lst_prf_1.get(i) for i in selected_indices])
                        lst_prf_1.place_forget()

                        if selected_langs == " Organization Profile":
                            
                            oacc_frame_1 = Frame(tab1)
                            oacc_frame_1.grid(row=0,column=0,sticky='nsew')

                            def oacc_responsive_widgets(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget

                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/0.32

                                dcanvas.coords("opoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("obutton1",dwidth/3.1,dheight/5)
                                dcanvas.coords("obutton2",dwidth/23,dheight/35)

                                dcanvas.coords("ohline",dwidth/21,dheight/3,dwidth/1.055,dheight/3)

                                dcanvas.coords("oimage1",dwidth/8,dheight/2.2)
                                dcanvas.coords("olabel1",dwidth/8,dheight/1.2)
                                dcanvas.coords("olabel2",dwidth/2.5,dheight/1.2)
                                dcanvas.coords("olabel3",dwidth/2.1,dheight/1.2)
                                dcanvas.coords("olabel4",dwidth/8,dheight/1.1)
                                dcanvas.coords("olabel5",dwidth/2.5,dheight/1.1)
                                dcanvas.coords("olabel6",dwidth/2.1,dheight/1.1)
                                dcanvas.coords("olabel7",dwidth/2.1,dheight/1.05)
                                dcanvas.coords("olabel8",dwidth/2.1,dheight/1)
                                dcanvas.coords("olabel9",dwidth/2.1,dheight/0.95)
                                dcanvas.coords("olabel10",dwidth/8,dheight/0.88)
                                dcanvas.coords("olabel12",dwidth/2.5,dheight/0.88)
                                dcanvas.coords("olabel11",dwidth/2.1,dheight/0.88)
                                dcanvas.coords("olabel13",dwidth/8,dheight/0.83)
                                dcanvas.coords("olabel14",dwidth/2.5,dheight/0.83)
                                dcanvas.coords("olabel15",dwidth/2.1,dheight/0.83)
                                dcanvas.coords("olabel16",dwidth/8,dheight/0.78)
                                dcanvas.coords("olabel17",dwidth/2.5,dheight/0.78)
                                dcanvas.coords("olabel18",dwidth/2.1,dheight/0.78)
                                dcanvas.coords("olabel19",dwidth/8,dheight/0.73)
                                dcanvas.coords("olabel20",dwidth/2.5,dheight/0.73)
                                dcanvas.coords("olabel21",dwidth/2.1,dheight/0.73)


                            o_sql="select * from auth_user where username=%s"
                            o_val=(nm_ent.get(),)
                            fbcursor.execute(o_sql,o_val,)
                            o_dtl=fbcursor.fetchone()

                            cmp_sql = "SELECT * FROM app1_company WHERE id_id=%s"
                            cmp_val = (o_dtl[0],)
                            fbcursor.execute(cmp_sql,cmp_val)
                            o_cmp_dtl = fbcursor.fetchone()

                            oacc_canvas=Canvas(oacc_frame_1, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,2000))

                            oacc_frame_1.grid_rowconfigure(0,weight=1)
                            oacc_frame_1.grid_columnconfigure(0,weight=1)

                            vertibar=Scrollbar(oacc_frame_1, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=oacc_canvas.yview)

                            oacc_canvas.bind("<Configure>", oacc_responsive_widgets)
                            oacc_canvas.config(yscrollcommand=vertibar.set)
                            oacc_canvas.grid(row=0,column=0,sticky='nsew')


                            oacc_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("opoly1"))

                            oacc_btn1=Label(oacc_canvas,width=28,height=1,text="ORGANIZATION PROFILE", font=('arial 20'),background="#1b3857",fg="white")
                            window_oacc_btn1 = oacc_canvas.create_window(0, 0, anchor="nw", window=oacc_btn1,tags=('obutton1'))

                            oacc_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("ohline"))

                            occ_image_1=Label(oacc_canvas,  image = prof_pics,bg="#213b52",width=170,height=170, anchor="center",font=('Calibri 14 bold'))
                            win_occ_image_1 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_image_1,tags=("oimage1"))

                            occ_label_1=Label(oacc_canvas,  text="Company Name",bg="#1b3857",width=13, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_1 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_1,tags=("olabel1"))

                            occ_label_2=Label(oacc_canvas,  text=":",bg="#1b3857",width=1, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_2 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_2,tags=("olabel2"))

                            occ_label_3=Label(oacc_canvas,  text=o_cmp_dtl[1],bg="#1b3857",width=15, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_3 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_3,tags=("olabel3"))

                            occ_label_4=Label(oacc_canvas,  text="Company Address",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_4 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_4,tags=("olabel4"))

                            occ_label_5=Label(oacc_canvas,  text=":",bg="#1b3857",width=1, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_5 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_5,tags=("olabel5"))

                            occ_label_6=Label(oacc_canvas,  text=o_cmp_dtl[2],bg="#1b3857",width=15, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_6 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_6,tags=("olabel6"))

                            occ_label_6=Label(oacc_canvas,  text=o_cmp_dtl[3],bg="#1b3857",width=15, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_6 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_6,tags=("olabel7"))

                            occ_label_6=Label(oacc_canvas,  text=o_cmp_dtl[4],bg="#1b3857",width=15, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_6 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_6,tags=("olabel8"))

                            occ_label_6=Label(oacc_canvas,  text=o_cmp_dtl[5],bg="#1b3857",width=15, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_6 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_6,tags=("olabel9"))

                            occ_label_7=Label(oacc_canvas,  text="Company E-mail ID",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_7 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_7,tags=("olabel10"))

                            occ_label_9=Label(oacc_canvas,  text=":",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_9 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_9,tags=("olabel12"))

                            occ_label_8=Label(oacc_canvas,  text=o_cmp_dtl[6],bg="#1b3857",width=15, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_8 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_8,tags=("olabel11"))

                            occ_label_10=Label(oacc_canvas,  text="Mobile No",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_10 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_10,tags=("olabel13"))

                            occ_label_11=Label(oacc_canvas,  text=":",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_11 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_11,tags=("olabel14"))

                            occ_label_12 =Label(oacc_canvas,  text=o_cmp_dtl[7],bg="#1b3857",width=15, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_12 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_12,tags=("olabel15"))

                            occ_label_13=Label(oacc_canvas,  text="Industry Type",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_13 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_13,tags=("olabel16"))

                            occ_label_14=Label(oacc_canvas,  text=":",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_14 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_14,tags=("olabel17"))

                            occ_label_15 =Label(oacc_canvas,  text=o_cmp_dtl[10],bg="#1b3857",width=20, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_15 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_15,tags=("olabel18"))

                            occ_label_16=Label(oacc_canvas,  text="Company Type",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_16 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_16,tags=("olabel19"))

                            occ_label_17 =Label(oacc_canvas,  text=":",bg="#1b3857",width=15, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_17 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_17,tags=("olabel20"))

                            occ_label_18 =Label(oacc_canvas,  text=o_cmp_dtl[11],bg="#1b3857",width=20, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_18 = oacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_18,tags=("olabel21"))


                        elif selected_langs == " User Information":
                            
                            uacc_frame_1 = Frame(tab1)
                            uacc_frame_1.grid(row=0,column=0,sticky='nsew')

                            def uacc_responsive_widgets(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget

                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/0.7

                                dcanvas.coords("upoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("ubutton1",dwidth/3.1,dheight/5)
                                dcanvas.coords("ubutton2",dwidth/23,dheight/35)

                                dcanvas.coords("uhline",dwidth/21,dheight/3,dwidth/1.055,dheight/3)

                                dcanvas.coords("ulabel1",dwidth/13,dheight/2.5)
                                dcanvas.coords("uimage1",dwidth/8,dheight/2.2)
                                dcanvas.coords("ulabel1",dwidth/8,dheight/1.2)
                                dcanvas.coords("ulabel2",dwidth/2.5,dheight/1.2)
                                dcanvas.coords("ulabel3",dwidth/2.1,dheight/1.2)
                                dcanvas.coords("ulabel4",dwidth/8,dheight/1.1)
                                dcanvas.coords("ulabel5",dwidth/2.5,dheight/1.1)
                                dcanvas.coords("ulabel6",dwidth/2.1,dheight/1.1)
                                dcanvas.coords("ulabel7",dwidth/8,dheight/1)
                                dcanvas.coords("ulabel8",dwidth/2.5,dheight/1)
                                dcanvas.coords("ulabel9",dwidth/2.1,dheight/1)
                                dcanvas.coords("ulabel10",dwidth/8,dheight/0.9)
                                dcanvas.coords("ulabel11",dwidth/2.5,dheight/0.9)
                                dcanvas.coords("ulabel12",dwidth/2.1,dheight/0.9)

                            o_sql="select * from auth_user where username=%s"
                            o_val=(nm_ent.get(),)
                            fbcursor.execute(o_sql,o_val,)
                            o_dtl=fbcursor.fetchone()

                            uacc_canvas=Canvas(uacc_frame_1, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,2000))

                            uacc_frame_1.grid_rowconfigure(0,weight=1)
                            uacc_frame_1.grid_columnconfigure(0,weight=1)

                            vertibar=Scrollbar(uacc_frame_1, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=uacc_canvas.yview)

                            uacc_canvas.bind("<Configure>", uacc_responsive_widgets)
                            uacc_canvas.config(yscrollcommand=vertibar.set)
                            uacc_canvas.grid(row=0,column=0,sticky='nsew')


                            uacc_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("upoly1"))

                            uacc_btn1=Label(uacc_canvas,width=28,height=1,text="USER INFORMATION", font=('arial 20'),background="#1b3857",fg="white")
                            window_uacc_btn1 = uacc_canvas.create_window(0, 0, anchor="nw", window=uacc_btn1,tags=('ubutton1'))

                            uacc_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("uhline"))

                            ucc_image_1=Label(uacc_canvas,  image = prof_pics,bg="#213b52",width=170,height=170, anchor="center",font=('Calibri 14 bold'))
                            win_ucc_image_1 = uacc_canvas.create_window(0, 0, anchor="nw", window=ucc_image_1,tags=("uimage1"))

                            occ_label_1=Label(uacc_canvas,  text="First Name",bg="#1b3857",width=13, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_1 = uacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_1,tags=("ulabel1"))

                            occ_label_2=Label(uacc_canvas,  text=":",bg="#1b3857",width=1, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_2 = uacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_2,tags=("ulabel2"))

                            occ_label_3=Label(uacc_canvas,  text=o_dtl[5],bg="#1b3857",width=15, anchor="w",foreground="white",font=('arial 16'))
                            win_occ_label_3 = uacc_canvas.create_window(0, 0, anchor="nw", window=occ_label_3,tags=("ulabel3"))

                            ucc_label_4=Label(uacc_canvas,  text="Last Name",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_ucc_label_4 = uacc_canvas.create_window(0, 0, anchor="nw", window=ucc_label_4,tags=("ulabel4"))

                            ucc_label_5=Label(uacc_canvas,  text=":",bg="#1b3857",width=1, anchor="w",foreground="white",font=('arial 16'))
                            win_ucc_label_5 = uacc_canvas.create_window(0, 0, anchor="nw", window=ucc_label_5,tags=("ulabel5"))

                            ucc_label_6=Label(uacc_canvas,  text=o_dtl[6],bg="#1b3857",width=15, anchor="w",foreground="white",font=('arial 16'))
                            win_ucc_label_6 = uacc_canvas.create_window(0, 0, anchor="nw", window=ucc_label_6,tags=("ulabel6"))


                            ucc_label_7=Label(uacc_canvas,  text="User E-mail ID",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_ucc_label_7 = uacc_canvas.create_window(0, 0, anchor="nw", window=ucc_label_7,tags=("ulabel7"))

                            ucc_label_9=Label(uacc_canvas,  text=":",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_ucc_label_9 = uacc_canvas.create_window(0, 0, anchor="nw", window=ucc_label_9,tags=("ulabel8"))

                            ucc_label_8=Label(uacc_canvas,  text=o_dtl[7],bg="#1b3857",width=15, anchor="w",foreground="white",font=('arial 16'))
                            win_ucc_label_8 = uacc_canvas.create_window(0, 0, anchor="nw", window=ucc_label_8,tags=("ulabel9"))

                            ucc_label_10=Label(uacc_canvas,  text="Username",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_ucc_label_10 = uacc_canvas.create_window(0, 0, anchor="nw", window=ucc_label_10,tags=("ulabel10"))

                            ucc_label_11=Label(uacc_canvas,  text=":",bg="#1b3857",width=16, anchor="w",foreground="white",font=('arial 16'))
                            win_ucc_label_11 = uacc_canvas.create_window(0, 0, anchor="nw", window=ucc_label_11,tags=("ulabel11"))

                            ucc_label_12 =Label(uacc_canvas,  text=o_dtl[4],bg="#1b3857",width=15, anchor="w",foreground="white",font=('arial 16'))
                            win_ucc_label_12 = uacc_canvas.create_window(0, 0, anchor="nw", window=ucc_label_12,tags=("ulabel12"))

                       
                        elif selected_langs == " Accounts and Settings":
                            acc_frame = Frame(tab1)
                            acc_frame.grid(row=0,column=0,sticky='nsew')

                            def acc_responsive_widgets(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget

                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/0.32

                                dcanvas.coords("aspoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("asbutton1",dwidth/3.1,dheight/5)
                                dcanvas.coords("asbutton2",dwidth/1.485,dheight/5)
                                dcanvas.coords("asbutton3",dwidth/2.5,dheight/0.4)

                                dcanvas.coords("ashline",dwidth/21,dheight/3,dwidth/1.055,dheight/3)

                                dcanvas.coords("aslabel1",dwidth/13,dheight/2.5)
                                dcanvas.coords("aslabel2",dwidth/13.85,dheight/1.85)
                                dcanvas.coords("aslabel3",dwidth/1.935,dheight/1.85)
                                dcanvas.coords("aslabel4",dwidth/13.95,dheight/1.42)
                                dcanvas.coords("aslabel5",dwidth/1.935,dheight/1.42)
                                dcanvas.coords("aslabel6",dwidth/18,dheight/1.14)
                                dcanvas.coords("aslabel7",dwidth/1.935,dheight/1.14)
                                dcanvas.coords("aslabel8",dwidth/13.6,dheight/0.95)
                                dcanvas.coords("aslabel9",dwidth/13,dheight/0.82)
                                dcanvas.coords("aslabel10",dwidth/18,dheight/0.73)
                                dcanvas.coords("aslabel11",dwidth/1.97,dheight/0.73)
                                dcanvas.coords("aslabel12",dwidth/15,dheight/0.64)
                                dcanvas.coords("aslabel13",dwidth/1.935,dheight/0.64)
                                dcanvas.coords("aslabel14",dwidth/15,dheight/0.574)
                                dcanvas.coords("aslabel15",dwidth/1.935,dheight/0.574)
                                dcanvas.coords("aslabel16",dwidth/15,dheight/0.515)
                                dcanvas.coords("aslabel17",dwidth/1.94,dheight/0.515)
                                dcanvas.coords("aslabel18",dwidth/16,dheight/0.47)
                                dcanvas.coords("aslabel19",dwidth/1.95,dheight/0.47)
                                dcanvas.coords("aslabel20",dwidth/18,dheight/0.43)

                                dcanvas.coords("asentry1",dwidth/13.8,dheight/1.665)
                                dcanvas.coords("asentry2",dwidth/1.93,dheight/1.665)
                                dcanvas.coords("asentry3",dwidth/13.8,dheight/1.3)
                                dcanvas.coords("asentry4",dwidth/1.93,dheight/1.3)
                                dcanvas.coords("asentry5",dwidth/13.8,dheight/1.06)
                                dcanvas.coords("asentry6",dwidth/1.93,dheight/1.06)
                                dcanvas.coords("asentry7",dwidth/13.8,dheight/0.9)
                                dcanvas.coords("asentry8",dwidth/13.8,dheight/0.7)
                                dcanvas.coords("asentry9",dwidth/1.93,dheight/0.7)
                                dcanvas.coords("asentry10",dwidth/13.8,dheight/0.621)
                                dcanvas.coords("asentry11",dwidth/1.93,dheight/0.621)
                                dcanvas.coords("asentry12",dwidth/13.8,dheight/0.554)
                                dcanvas.coords("asentry13",dwidth/1.93,dheight/0.554)
                                dcanvas.coords("asentry14",dwidth/13.8,dheight/0.5)
                                dcanvas.coords("asentry15",dwidth/1.93,dheight/0.5)
                                dcanvas.coords("asentry16",dwidth/13.8,dheight/0.418)

                                dcanvas.coords("ascombo1",dwidth/13.8,dheight/0.455)
                                dcanvas.coords("ascombo2",dwidth/1.93,dheight/0.455)

                            as_sql="select * from auth_user where username=%s"
                            as_val=(nm_ent.get(),)
                            fbcursor.execute(as_sql,as_val,)
                            as_dtl=fbcursor.fetchone()

                            def as_update_profile():
                                first_name=acc_entry_1.get()
                                pro_email=acc_entry_3.get()
                                last_name=acc_entry_2.get()
                                pro_username=acc_entry_4.get()
                                pro_new_pass=acc_entry_6.get()

                                sql_signup='select * from auth_user'
                                fbcursor.execute(sql_signup)
                                check_none=fbcursor.fetchone()

                                if as_dtl[4]==pro_username and as_dtl[1]==acc_entry_5.get() and pro_new_pass=="" :
                                            passw=acc_entry_5.get()
                                    
                                            prof_edit="update auth_user set first_name=%s,last_name=%s,email=%s,username=%s,password=%s where id=%s" #adding values into db
                                            prof_edit_val=(first_name,last_name,pro_email,pro_username,passw,as_dtl[0])
                                            fbcursor.execute(prof_edit,prof_edit_val)
                                            finsysdb.commit()

                                            #compnay
                                            cmp_name=acc_entry_8.get()
                                            cmp_cty=acc_entry_10.get()
                                            cmp_pin=acc_entry_12.get()
                                            cmp_phn=acc_entry_14.get()
                                            cmp_ind=as_combo_1.get()
                                            cmp_addr=acc_entry_9.get()
                                            cmp_st=acc_entry_11.get()
                                            cmp_em=acc_entry_13.get()
                                            cmp_bname=acc_entry_15.get()
                                            cmp_typ=as_combo_2.get()
                                            logo=acc_entry_16.get()

                                            cmp_edit="update app1_company set cname=%s,caddress=%s,city=%s,state=%s,pincode=%s,cemail=%s,phone=%s,cimg=%s,bname=%s,industry=%s,ctype=%s where id_id =%s" #adding values into db
                                            cmp_edit_val=(cmp_name,cmp_addr,cmp_cty,cmp_st,cmp_pin,cmp_em,cmp_phn,logo,cmp_bname,cmp_ind,cmp_typ,as_dtl[0])
                                            fbcursor.execute(cmp_edit,cmp_edit_val)
                                            finsysdb.commit()
                                            
                                        
                                else:
                                    # #username same password change
                                    if acc_entry_6.get()=="":
                                        
                                        pro_new_passd=acc_entry_5.get()
                                        
                                    else:
                                        pro_new_passd=acc_entry_6.get()
                                    if pro_new_pass==acc_entry_7.get() and acc_entry_7.get()==pro_new_pass:
                                            if acc_entry_5.get()==as_dtl[1]:
                                                print(pro_new_pass)
                                                prof_edit="update auth_user set first_name=%s,last_name=%s,email=%s,username=%s,password=%s where id=%s" #adding values into db
                                                prof_edit_val=(first_name,last_name,pro_email,pro_username,pro_new_passd,as_dtl[0])
                                                fbcursor.execute(prof_edit,prof_edit_val)
                                                finsysdb.commit()

                                                #compnay
                                                cmp_name=acc_entry_8.get()
                                                cmp_cty=acc_entry_10.get()
                                                cmp_pin=acc_entry_12.get()
                                                cmp_phn=acc_entry_14.get()
                                                cmp_ind=as_combo_1.get()
                                                cmp_addr=acc_entry_9.get()
                                                cmp_st=acc_entry_11.get()
                                                cmp_em=acc_entry_13.get()
                                                cmp_bname=acc_entry_15.get()
                                                cmp_typ=as_combo_2.get()
                                                logo=acc_entry_16.get()

                                                cmp_edit="update app1_company set cname=%s,caddress=%s,city=%s,state=%s,pincode=%s,cemail=%s,phone=%s,cimg=%s,bname=%s,industry=%s,ctype=%s where id_id =%s" #adding values into db
                                                cmp_edit_val=(cmp_name,cmp_addr,cmp_cty,cmp_st,cmp_pin,cmp_em,cmp_phn,logo,cmp_bname,cmp_ind,cmp_typ,as_dtl[0])
                                                fbcursor.execute(cmp_edit,cmp_edit_val)
                                                finsysdb.commit()
                                                
                                            else:
                                                messagebox.showerror("Updation Failed","Please check your current password")
                                    else:

                                            messagebox.showerror("Updation Failed","password and conform password does not match")
                                        
                                    
                                Sys_top_frame2.pack_forget()
                                Sys_top_frame.pack_forget()
                                acc_frame.grid_forget()
                                main_frame_signin.pack(fill=X,)

                            cmp_sql = "SELECT * FROM app1_company WHERE id_id=%s"
                            cmp_val = (as_dtl[0],)
                            fbcursor.execute(cmp_sql,cmp_val)
                            as_cmp_dtl = fbcursor.fetchone()

                            acc_canvas=Canvas(acc_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,2000))

                            acc_frame.grid_rowconfigure(0,weight=1)
                            acc_frame.grid_columnconfigure(0,weight=1)

                            vertibar=Scrollbar(acc_frame, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=acc_canvas.yview)

                            acc_canvas.bind("<Configure>", acc_responsive_widgets)
                            acc_canvas.config(yscrollcommand=vertibar.set)
                            acc_canvas.grid(row=0,column=0,sticky='nsew')


                            acc_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aspoly1"))

                            acc_btn1=Button(acc_canvas,text='ACCOUNTS AND SETTINGS', width=28,height=1,foreground="white",background="#1b3857",font='arial 20',activebackground='#24a0ed', activeforeground='white')
                            window_acc_btn1 = acc_canvas.create_window(0, 0, anchor="nw", window=acc_btn1,tags=('asbutton1'))

                            
                            
                            def a_lst_prf_slt_1(event):
                                selected_indices_1 = a_lst_prf_1.curselection()
                                selected_langs_1 = ",".join([a_lst_prf_1.get(i) for i in selected_indices_1])
                                a_lst_prf_1.place_forget()

                                

                                if selected_langs_1 == "BILLING AND SUBCRIPTION":
                                    acc_frame.grid_forget()
                                    acc_frame_1 = Frame(tab1)
                                    acc_frame_1.grid(row=0,column=0,sticky='nsew')

                                    def acc_responsive_widgets_1(event):
                                        dwidth = event.width
                                        dheight = event.height
                                        dcanvas = event.widget

                                        r1 = 25
                                        x1 = dwidth/63
                                        x2 = dwidth/1.021
                                        y1 = dheight/14 
                                        y2 = dheight/0.32

                                        dcanvas.coords("bspoly1",x1 + r1,y1,
                                        x1 + r1,y1,
                                        x2 - r1,y1,
                                        x2 - r1,y1,     
                                        x2,y1,     
                                        #--------------------
                                        x2,y1 + r1,     
                                        x2,y1 + r1,     
                                        x2,y2 - r1,     
                                        x2,y2 - r1,     
                                        x2,y2,
                                        #--------------------
                                        x2 - r1,y2,     
                                        x2 - r1,y2,     
                                        x1 + r1,y2,
                                        x1 + r1,y2,
                                        x1,y2,
                                        #--------------------
                                        x1,y2 - r1,
                                        x1,y2 - r1,
                                        x1,y1 + r1,
                                        x1,y1 + r1,
                                        x1,y1,
                                        )

                                        dcanvas.coords("bsbutton2",dwidth/23,dheight/35)

                                        r1 = 25
                                        x1 = dwidth/3.5
                                        x2 = dwidth/1.4
                                        y1 = dheight/10
                                        y2 = dheight/.95

                                        dcanvas.coords("bspoly2",x1 + r1,y1,
                                        x1 + r1,y1,
                                        x2 - r1,y1,
                                        x2 - r1,y1,     
                                        x2,y1,     
                                        #--------------------
                                        x2,y1 + r1,     
                                        x2,y1 + r1,     
                                        x2,y2 - r1,     
                                        x2,y2 - r1,     
                                        x2,y2,
                                        #--------------------
                                        x2 - r1,y2,     
                                        x2 - r1,y2,     
                                        x1 + r1,y2,
                                        x1 + r1,y2,
                                        x1,y2,
                                        #--------------------
                                        x1,y2 - r1,
                                        x1,y2 - r1,
                                        x1,y1 + r1,
                                        x1,y1 + r1,
                                        x1,y1,
                                        )

                                        dcanvas.coords("bslabel1",dwidth/2.45,dheight/8)
                                        dcanvas.coords("bslabel2",dwidth/3,dheight/3.3)
                                        dcanvas.coords("bslabel3",dwidth/2.3,dheight/2.4)
                                        dcanvas.coords("bslabel4",dwidth/3,dheight/1.4)
                                        dcanvas.coords("bsbutton3",dwidth/2.3,dheight/1.25)
                                        dcanvas.coords("bslabel5",dwidth/3,dheight/1.14)
                                        dcanvas.coords("bsimage1",dwidth/2.3,dheight/1.85)
                                    
                                    acc_canvas_1=Canvas(acc_frame_1, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,2000))

                                    acc_frame_1.grid_rowconfigure(0,weight=1)
                                    acc_frame_1.grid_columnconfigure(0,weight=1)

                                    vertibar=Scrollbar(acc_frame_1, orient=VERTICAL)
                                    vertibar.grid(row=0,column=1,sticky='ns')
                                    vertibar.config(command=acc_canvas_1.yview)

                                    acc_canvas_1.bind("<Configure>", acc_responsive_widgets_1)
                                    acc_canvas_1.config(yscrollcommand=vertibar.set)
                                    acc_canvas_1.grid(row=0,column=0,sticky='nsew')
                                    
                                    acc_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("bspoly1"))

                                    acc_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#C1BCAC",tags=("bspoly2"))

                                    label_1 = Label(acc_canvas_1,width=10,height=2,text="finsYs", font=('arial 32'),background="#C1BCAC",fg="white") 
                                    window_label_1 = acc_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=('bslabel1'))

                                    label_1 = Label(acc_canvas_1,width=50,height=3,text="We hope you're enjoying your trial.To keep using \nFinsYs after free trial.please subscribe.", font=('arial 12'),background="#C1BCAC",fg="black") 
                                    window_label_1 = acc_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=('bslabel2'))

                                    label_1 = Label(acc_canvas_1,width=18,height=2,text="Cancel your trial", font=('arial 12'),background="#C1BCAC",fg="blue") 
                                    window_label_1 = acc_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=('bslabel3'))

                                    bs_image_1 = Image.open("images/finsys.png")
                                    resize_image = bs_image_1.resize((155,90))
                                    bs_image_1 = ImageTk.PhotoImage(resize_image)
                                    bslogo = Label(acc_canvas_1, width=155, height=90, background="#C1BCAC", image = bs_image_1) 
                                    window_image = acc_canvas_1.create_window(0, 0, anchor="nw", window=bslogo,tags=('bsimage1'))
                                    bslogo.photo = bs_image_1

                                    label_1 = Label(acc_canvas_1,width=50,height=2,text="Subscribe for 1095/month +applicable taxes", font=('arial 12'),background="#C1BCAC",fg="black") 
                                    window_label_1 = acc_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=('bslabel4'))

                                    bs_btn2=Button(acc_canvas_1,text='Subscribe', bd=0, foreground="white",background="red",font='arial 10 bold',activebackground="#1b3857",height=2,width=20)
                                    window_bs_btn2 = acc_canvas_1.create_window(0, 0, anchor="nw", window=bs_btn2,tags=('bsbutton3'))

                                    label_1 = Label(acc_canvas_1,width=50,height=2,text="We won’t send you spam. Unsubscribe at any time.", font=('arial 12'),background="#C1BCAC",fg="black") 
                                    window_label_1 = acc_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=('bslabel5'))

                                    def bs_back_1_():
                                        acc_frame_1.grid_forget()
                                        acc_frame.grid(row=0,column=0,sticky='nsew')

                                    bs_btn1=Button(acc_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=bs_back_1_)
                                    window_bs_btn1 = acc_canvas_1.create_window(0, 0, anchor="nw", window=bs_btn1,tags=('bsbutton2'))
                                else:
                                    pass

                        

                            def acc_settings():

                                # create a list box
                                a_langs_1 = ("BILLING AND SUBCRIPTION","SALES","EXPENSE")

                                a_langs_var = StringVar(value=a_langs_1)
                                global a_lst_prf_1
                                a_lst_prf_1 = Listbox(acc_canvas,listvariable=a_langs_var,height=3 ,selectmode='extended',bg="black",fg="white",width=28)
                                a_lst_prf_1.bind('<<ListboxSelect>>', a_lst_prf_slt_1)
                                a_lst_prf_1.place(relx=0.68, rely=0.30)
                                


                            acc_btn2=Button(acc_canvas,text='▼', width=2,height=1,foreground="#24a0ed",background="#1b3857",font='arial 20',activebackground='#24a0ed', activeforeground='white',command=acc_settings)
                            window_acc_btn2 = acc_canvas.create_window(0, 0, anchor="nw", window=acc_btn2,tags=('asbutton2'))

                            acc_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("ashline"))

                            label_1 = Label(acc_canvas,width=10,height=2,text="Personal Info", font=('arial 18'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel1'))

                            label_1 = Label(acc_canvas,width=10,height=2,text="First Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel2'))

                            acc_entry_1=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_1 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_1, tags=('asentry1'))
                            acc_entry_1.delete(0,END)
                            acc_entry_1.insert(0,as_dtl[5])

                            label_1 = Label(acc_canvas,width=10,height=2,text="Last Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel3'))

                            acc_entry_2=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_2 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_2, tags=('asentry2'))
                            acc_entry_2.delete(0,END)
                            acc_entry_2.insert(0,as_dtl[6])

                            label_1 = Label(acc_canvas,width=7,height=2,text="E-mail", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel4'))

                            acc_entry_3=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_3 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_3, tags=('asentry3'))
                            acc_entry_3.delete(0,END)
                            acc_entry_3.insert(0,as_dtl[7])

                            label_1 = Label(acc_canvas,width=10,height=2,text="Username", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel5'))

                            acc_entry_4=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_4 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_4, tags=('asentry4'))
                            acc_entry_4.delete(0,END)
                            acc_entry_4.insert(0,as_dtl[4])

                            label_1 = Label(acc_canvas,width=28,height=2,text="Enter your Current Password", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel6'))

                            acc_entry_5=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",show="*")
                            window_acc_entry_5 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_5, tags=('asentry5'))
                            acc_entry_5.delete(0,END)
                            acc_entry_5.insert(0,as_dtl[1])

                            label_1 = Label(acc_canvas,width=18,height=2,text="Enter New Password", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel7'))

                            
                            acc_entry_6=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",show="*")
                            window_acc_entry_6 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_6, tags=('asentry6'))
                            def as_pas_val_fun1_1(value):
            
                                pattern = r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
                                if re.fullmatch(pattern, value) is None:
                                                    
                                    return False

                                acc_entry_6.config(fg="white")
                                return True

                            def as_pass_inval_fun1_1():
                                acc_entry_6.config(fg="red")

                            as_pas_val1_1 = (acc_canvas.register(as_pas_val_fun1_1), '%P')
                            as_pass_inval1_1 = (acc_canvas.register(as_pass_inval_fun1_1),)

                            acc_entry_6.config(validate='focusout', validatecommand=as_pas_val1_1, invalidcommand=as_pass_inval1_1)

                            label_1 = Label(acc_canvas,width=18,height=2,text="Re-type New Password", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel8'))


                            acc_entry_7=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",show="*")
                            window_acc_entry_7 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_7, tags=('asentry7'))

                            def as_pas_val_fun1(value):
            
                                pattern = r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
                                if re.fullmatch(pattern, value) is None:
                                                    
                                    return False

                                acc_entry_7.config(fg="white")
                                return True

                            def as_pass_inval_fun1():
                                acc_entry_7.config(fg="red")

                            as_pas_val1 = (acc_canvas.register(as_pas_val_fun1), '%P')
                            as_pass_inval1 = (acc_canvas.register(as_pass_inval_fun1),)

                            acc_entry_7.config(validate='focusout', validatecommand=as_pas_val1, invalidcommand=as_pass_inval1)

                            label_1 = Label(acc_canvas,width=11,height=2,text="Company Info", font=('arial 18'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel9'))

                            label_1 = Label(acc_canvas,width=18,height=2,text="Company Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel10'))

                            acc_entry_8=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_8 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_8, tags=('asentry8'))
                            acc_entry_8.delete(0,END)
                            acc_entry_8.insert(0,as_cmp_dtl[1])

                            label_1 = Label(acc_canvas,width=18,height=2,text="Company Address", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel11'))

                            acc_entry_9=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_9 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_9, tags=('asentry9'))
                            acc_entry_9.delete(0,END)
                            acc_entry_9.insert(0,as_cmp_dtl[2])

                            label_1 = Label(acc_canvas,width=5,height=2,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel12'))

                            acc_entry_10=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_10 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_10, tags=('asentry10'))
                            acc_entry_10.delete(0,END)
                            acc_entry_10.insert(0,as_cmp_dtl[3])

                            label_1 = Label(acc_canvas,width=6,height=2,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel13'))

                            acc_entry_11=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_11 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_11, tags=('asentry11'))
                            acc_entry_11.delete(0,END)
                            acc_entry_11.insert(0,as_cmp_dtl[4])

                            label_1 = Label(acc_canvas,width=8,height=2,text="Pincode", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel14'))

                            acc_entry_12=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_12 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_12, tags=('asentry12'))
                            acc_entry_12.delete(0,END)
                            acc_entry_12.insert(0,as_cmp_dtl[5])

                            label_1 = Label(acc_canvas,width=6,height=2,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel15'))

                            acc_entry_13=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_13 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_13, tags=('asentry13'))
                            acc_entry_13.delete(0,END)
                            acc_entry_13.insert(0,as_cmp_dtl[6])

                            label_1 = Label(acc_canvas,width=13,height=2,text="Phone Number", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel16'))

                            acc_entry_14=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_14 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_14, tags=('asentry14'))
                            acc_entry_14.delete(0,END)
                            acc_entry_14.insert(0,as_cmp_dtl[7])

                            label_1 = Label(acc_canvas,width=20,height=2,text="Legal Business Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel17'))

                            acc_entry_15=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_15 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_15, tags=('asentry15'))
                            acc_entry_15.delete(0,END)
                            acc_entry_15.insert(0,as_cmp_dtl[9])

                            label_1 = Label(acc_canvas,width=14,height=2,text="Your Industry", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel18'))

                            as_combo_1 = ttk.Combobox(acc_canvas, font=('arial 10'))
                            as_combo_1['values'] = ("Accounting Services","Consultants, Doctors, Lawyers and similar","Information Technology","Manufacturing","Professional, Scientific and Technical Services","Resturant/Bar and similar","Retail and similar","Other Financial Services",)
                            as_combo_1.current(0)
                            window_as_combo_1 = acc_canvas.create_window(0, 0, anchor="nw", width=540, height=30,window=as_combo_1,tags=('ascombo1'))  
                            as_combo_1.delete(0,'end')
                            as_combo_1.insert(0,as_cmp_dtl[10])

                            label_1 = Label(acc_canvas,width=13,height=2,text="Company Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel19'))

                            as_combo_2 = ttk.Combobox(acc_canvas, font=('arial 10'))
                            as_combo_2['values'] = ("Private Limited Company","Public Limited Company","Joint-Venture Company","Partnership Firm Company","One Person Company","Branch Office Company","Non Government Organization",)
                            as_combo_2.current(0)
                            window_as_combo_2 = acc_canvas.create_window(0, 0, anchor="nw", width=540, height=30,window=as_combo_2,tags=('ascombo2'))  
                            as_combo_2.delete(0,'end')
                            as_combo_2.insert(0,as_cmp_dtl[11])

                            label_1 = Label(acc_canvas,width=50,height=2,text="Do you want to change Company Image ? Browse here ⤓", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = acc_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=('aslabel20'))  

                            def as_fil_ents(event):
                                sql_log_sql_1='select * from auth_user where username=%s'
                                val_1=(nm_ent.get(),)
                                fbcursor.execute(sql_log_sql_1,val_1)
                                check_logins=fbcursor.fetchone()
                                cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                                logo_crp_1=cmp_logo.split('/',-1)
                                
                                im1 = Image.open(r""+cmp_logo) 
                                im1 = im1.save("profilepic/propic"+str(check_logins[0])+".png")

                                acc_entry_16.delete("0",END)
                                acc_entry_16.insert(0,logo_crp_1[-1])  

                            acc_entry_16=Entry(acc_canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_acc_entry_16 = acc_canvas.create_window(0, 0, anchor="nw", height=30,window=acc_entry_16, tags=('asentry16'))
                            acc_entry_16.delete(0,END)
                            acc_entry_16.insert(0,as_cmp_dtl[8])
                            acc_entry_16.bind("<Button-1>",as_fil_ents)

                            as_btn1=Button(acc_canvas,text='UPDATE PROFILE', bd=0, foreground="white",background="#2f516f",font='arial 14 bold',activebackground="#1b3857",activeforeground="white",width=25,height=2,command=as_update_profile)
                            window_as_btn1 = acc_canvas.create_window(0, 0, anchor="nw", window=as_btn1,tags=('asbutton3'))   

                        elif selected_langs == " Customize Form Style":    
                            cs_frame = Frame(tab1)
                            cs_frame.grid(row=0,column=0,sticky='nsew')

                            def cs_responsive_widgets(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget

                                dcanvas.coords("cstree1",dwidth/12,dheight/1.8)
                                

                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("cspoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("cshline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                                dcanvas.coords("cslabel1",dwidth/2.5,dheight/8.00)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.8


                                dcanvas.coords("cspoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("csbutton1",dwidth/2.1,dheight/2.4)
                                dcanvas.coords("csbutton2",dwidth/1.59,dheight/2.4)
                                dcanvas.coords("csbutton3",dwidth/1.28,dheight/2.26)
                                dcanvas.coords("cscombo1",dwidth/1.179,dheight/1.52)

                            cs_canvas=Canvas(cs_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,2000))

                            cs_frame.grid_rowconfigure(0,weight=1)
                            cs_frame.grid_columnconfigure(0,weight=1)

                            vertibar=Scrollbar(cs_frame, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=cs_canvas.yview)

                            cs_canvas.bind("<Configure>", cs_responsive_widgets)
                            cs_canvas.config(yscrollcommand=vertibar.set)
                            cs_canvas.grid(row=0,column=0,sticky='nsew')


                            cs_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("cspoly1"))

                            label_1 = Label(cs_canvas,width=20,height=1,text="CUSTOM FORM STYLES", font=('arial 25'),background="#1b3857",fg="white") 
                            window_label_1 = cs_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("cslabel1"))

                            cs_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("cshline"))

                            
                            cs_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("cspoly2"))


                            fgthi = ttk.Style()
                            fgthi.theme_use("default")
                            fgthi.configure('mystyle103.Treeview', background='#2f516f',State='DISABLE',foreground='white',fieldbackground='#2f516f',font=(None,11))
                            fgthi.configure('mystyle103.Treeview.Heading', background='#2f516f',State='DISABLE')

                            cs_scrollbar = Scrollbar(cs_frame,orient="vertical")

                            cs_tree = ttk.Treeview(cs_canvas, columns = (1,2,3,4), height = 10, show = "headings",style='mystyle103.Treeview',yscrollcommand=cs_scrollbar.set)
                            cs_tree.heading(1)
                            cs_tree.heading(2, text="NAME")
                            # cs_tree.heading(3, text="FORM-TYPE")
                            cs_tree.heading(3, text="LAST EDITED")
                            cs_tree.heading(4, text="APPLIED")
                            
                            cs_tree.column(1, width = 50)
                            cs_tree.column(2, width = 570)
                            # cs_tree.column(3, width = 270)
                            cs_tree.column(3, width = 300)
                            cs_tree.column(4, width = 200)
                            window_label_4 = cs_canvas.create_window(0, 0, anchor="nw", window=cs_tree,tags=('cstree1'))

                            cs_scrollbar.config(command=cs_tree.yview)
                            cs_scrollbar.grid(row=0,column=2,sticky='ns')

                            sql_pr="select * from auth_user where username=%s"
                            sql_pr_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pr,sql_pr_val,)
                            pr_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pr_dtl[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dtl=fbcursor.fetchone()

                            c_sql_1 = "SELECT * FROM app1_customize where selected=1 and cid_id=%s"
                            c_val_1 = (cmp_dtl[0],)
                            fbcursor.execute(c_sql_1,c_val_1,)
                            cs_data_1 = fbcursor.fetchall()

                            count0 = 0
                            for i in cs_data_1:
                                
                                if True:
                                    cs_tree.insert(parent='',index='end',iid=i,text='',values=('',i[1],i[6],"APPLIED"))
                                
                            count0 += 1

                            c_sql_1 = "SELECT * FROM app1_customize where selected=0 and cid_id=%s"
                            c_val_1 = (cmp_dtl[0],)
                            fbcursor.execute(c_sql_1,c_val_1,)
                            cs_data_2 = fbcursor.fetchall()

                            count0 = 0
                            for i in cs_data_2:
                                
                                if True:
                                    cs_tree.insert(parent='',index='end',iid=i,text='',values=('',i[1],i[6],"NOT APPLIED"))
                                
                            count0 += 1

                            def add_newstyle():
                                cs_frame.grid_forget()
                                cs_frame_1 = Frame(tab1)
                                cs_frame_1.grid(row=0,column=0,sticky='nsew')

                                def cs_responsive_widgets_1(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                    
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("nspoly1",x1 + r1,y1,
                                    x1 + r1,y1,
                                    x2 - r1,y1,
                                    x2 - r1,y1,     
                                    x2,y1,     
                                    #--------------------
                                    x2,y1 + r1,     
                                    x2,y1 + r1,     
                                    x2,y2 - r1,     
                                    x2,y2 - r1,     
                                    x2,y2,
                                    #--------------------
                                    x2 - r1,y2,     
                                    x2 - r1,y2,     
                                    x1 + r1,y2,
                                    x1 + r1,y2,
                                    x1,y2,
                                    #--------------------
                                    x1,y2 - r1,
                                    x1,y2 - r1,
                                    x1,y1 + r1,
                                    x1,y1 + r1,
                                    x1,y1,
                                    )

                                    dcanvas.coords("nslabel1",dwidth/2.5,dheight/8.24)
                                    dcanvas.coords("nshline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.32


                                    dcanvas.coords("nspoly2",x11 + r2,y11,
                                    x11 + r2,y11,
                                    x21 - r2,y11,
                                    x21 - r2,y11,     
                                    x21,y11,     
                                    #--------------------
                                    x21,y11 + r2,     
                                    x21,y11 + r2,     
                                    x21,y21 - r2,     
                                    x21,y21 - r2,     
                                    x21,y21,
                                    #--------------------
                                    x21 - r2,y21,     
                                    x21 - r2,y21,     
                                    x11 + r2,y21,
                                    x11 + r2,y21,
                                    x11,y21,
                                    #--------------------
                                    x11,y21 - r2,
                                    x11,y21 - r2,
                                    x11,y11 + r2,
                                    x11,y11 + r2,
                                    x11,y11,
                                    )
                                    dcanvas.coords("nsbutton3",dwidth/23,dheight/3.415)
                                    dcanvas.coords("nslabel2",dwidth/21,dheight/2.3)
                                    dcanvas.coords("nsentry1",dwidth/20,dheight/2.05)

                                    dcanvas.coords("nslabel3",dwidth/22.2,dheight/1.75)
                                    dcanvas.coords("nsentry6",dwidth/20,dheight/1.57)
                                    dcanvas.coords("nsentry7",dwidth/20,dheight/1.45)
                                    dcanvas.coords("nsentry8",dwidth/20,dheight/1.34)
                                    dcanvas.coords("nsentry9",dwidth/20,dheight/1.25)
                                    dcanvas.coords("nsentry10",dwidth/20,dheight/1.17)
                                    dcanvas.coords("nsbutton7",dwidth/9,dheight/1)

                                    dcanvas.coords("nslabel7",dwidth/21,dheight/1)
                                    dcanvas.coords("nsentry2",dwidth/20,dheight/0.95)
                                    dcanvas.coords("nsbutton4",dwidth/20,dheight/0.88)
                                    dcanvas.coords("nsbutton5",dwidth/5.8,dheight/0.88)
                                    
                                    dcanvas.coords("nslabel4",dwidth/22.8,dheight/0.83)
                                    dcanvas.coords("nsentry3",dwidth/20,dheight/0.798)
                                    dcanvas.coords("nsbutton8",dwidth/20,dheight/0.75)
                                    dcanvas.coords("nsbutton9",dwidth/9,dheight/0.75)
                                    dcanvas.coords("nsbutton10",dwidth/5.72,dheight/0.75)
                                    dcanvas.coords("nsbutton11",dwidth/4.2,dheight/0.75)
                                    dcanvas.coords("nsbutton12",dwidth/20,dheight/0.695)
                                    dcanvas.coords("nsbutton13",dwidth/9,dheight/0.695)
                                    dcanvas.coords("nsbutton14",dwidth/5.72,dheight/0.695)
                                    dcanvas.coords("nsbutton15",dwidth/4.2,dheight/0.695)
                                    dcanvas.coords("nsbutton16",dwidth/20,dheight/0.65)
                                    dcanvas.coords("nsbutton17",dwidth/9,dheight/0.65)
                                    dcanvas.coords("nsbutton18",dwidth/5.72,dheight/0.65)
                                    dcanvas.coords("nsbutton19",dwidth/4.2,dheight/0.65)
                                    dcanvas.coords("nslabel5",dwidth/22.8,dheight/0.595)
                                    dcanvas.coords("nsentry4",dwidth/20,dheight/0.58)
                                    dcanvas.coords("nsbutton20",dwidth/20,dheight/0.55)
                                    dcanvas.coords("nsbutton21",dwidth/9,dheight/0.55)
                                    dcanvas.coords("nsbutton22",dwidth/5.72,dheight/0.55)
                                    dcanvas.coords("nsbutton23",dwidth/4.2,dheight/0.55)
                                    dcanvas.coords("nsbutton24",dwidth/20,dheight/0.52)
                                    dcanvas.coords("nsbutton25",dwidth/9,dheight/0.52)
                                    dcanvas.coords("nsbutton26",dwidth/5.72,dheight/0.52)
                                    dcanvas.coords("nsbutton27",dwidth/4.2,dheight/0.52)
                                    dcanvas.coords("nsbutton28",dwidth/20,dheight/0.493)
                                    dcanvas.coords("nsbutton29",dwidth/9,dheight/0.493)
                                    dcanvas.coords("nsbutton30",dwidth/5.72,dheight/0.493)
                                    dcanvas.coords("nsbutton31",dwidth/4.2,dheight/0.493) 
                                    dcanvas.coords("nslabel6",dwidth/22.5,dheight/0.464)
                                    dcanvas.coords("nsentry5",dwidth/20,dheight/0.45)
                                    dcanvas.coords("nsbutton32",dwidth/20,dheight/0.43)
                                    dcanvas.coords("nsbutton33",dwidth/5.8,dheight/0.43)
                                    dcanvas.coords("nsbutton34",dwidth/20,dheight/0.4)
                                    dcanvas.coords("nsbutton35",dwidth/5.8,dheight/0.4)
                                    dcanvas.coords("nscheck1",dwidth/8.5,dheight/0.37)
                                    dcanvas.coords("nsbutton1",dwidth/8.5,dheight/0.355)

                                    #--------------------------Classic------------------------------

                                    r2 = 25
                                    x11 = dwidth/3
                                    x21 = dwidth/1.05
                                    y11 = dheight/2.3
                                    y21 = dheight/0.38


                                    dcanvas.coords("nspoly3",x11 + r2,y11,
                                    x11 + r2,y11,
                                    x21 - r2,y11,
                                    x21 - r2,y11,     
                                    x21,y11,     
                                    #--------------------
                                    x21,y11 + r2,     
                                    x21,y11 + r2,     
                                    x21,y21 - r2,     
                                    x21,y21 - r2,     
                                    x21,y21,
                                    #--------------------
                                    x21 - r2,y21,     
                                    x21 - r2,y21,     
                                    x11 + r2,y21,
                                    x11 + r2,y21,
                                    x11,y21,
                                    #--------------------
                                    x11,y21 - r2,
                                    x11,y21 - r2,
                                    x11,y11 + r2,
                                    x11,y11 + r2,
                                    x11,y11,
                                    )

                                    r2 = 0
                                    x11 = dwidth/2.955
                                    x21 = dwidth/1.057
                                    y11 = dheight/2.2
                                    y21 = dheight/0.382


                                    dcanvas.coords("nspoly3_1",x11 + r2,y11,
                                    x11 + r2,y11,
                                    x21 - r2,y11,
                                    x21 - r2,y11,     
                                    x21,y11,     
                                    #--------------------
                                    x21,y11 + r2,     
                                    x21,y11 + r2,     
                                    x21,y21 - r2,     
                                    x21,y21 - r2,     
                                    x21,y21,
                                    #--------------------
                                    x21 - r2,y21,     
                                    x21 - r2,y21,     
                                    x11 + r2,y21,
                                    x11 + r2,y21,
                                    x11,y21,
                                    #--------------------
                                    x11,y21 - r2,
                                    x11,y21 - r2,
                                    x11,y11 + r2,
                                    x11,y11 + r2,
                                    x11,y11,
                                    )

                                    dcanvas.coords("naivlabel1",dwidth/1.33,dheight/1.72)
                                    dcanvas.coords("naivlabel2",dwidth/1.33,dheight/1.59)
                                    dcanvas.coords("naivlabel3",dwidth/1.33,dheight/1.48)
                                    dcanvas.coords("naivlabel4",dwidth/1.33,dheight/1.38)
                                    dcanvas.coords("naivlabel5",dwidth/1.33,dheight/1.29)
                                    dcanvas.coords("naivlabel6",dwidth/1.33,dheight/1.2)
                                    dcanvas.coords("naivlabel7",dwidth/1.8,dheight/2.11)
                                    dcanvas.coords("nline1",dwidth/2.95,dheight/0.875,dwidth/1.057,dheight/0.875)

                                    dcanvas.coords("nimage1",dwidth/2.65,dheight/1.72)

                                    dcanvas.coords("naivlabel8",dwidth/2.87,dheight/1.16)
                                    dcanvas.coords("naivlabel17",dwidth/2.60,dheight/1.11)
                                   
                                    dcanvas.coords("naivlabel9",dwidth/1.35,dheight/0.865)
                                    dcanvas.coords("naivlabel10",dwidth/1.35,dheight/0.835)
                                    dcanvas.coords("naivlabel11",dwidth/1.35,dheight/0.805)
                                    dcanvas.coords("naivlabel12",dwidth/1.35,dheight/0.785)

                                    dcanvas.coords("naivlabel18",dwidth/1.16,dheight/0.865)
                                    dcanvas.coords("naivlabel19",dwidth/1.16,dheight/0.835)
                                    dcanvas.coords("naivlabel20",dwidth/1.16,dheight/0.805)
                                    dcanvas.coords("naivlabel21",dwidth/1.16,dheight/0.785)

                                    dcanvas.coords("nline2",dwidth/2.95,dheight/0.759,dwidth/1.057,dheight/0.759)

                                    dcanvas.coords("naivtree1",dwidth/2.9,dheight/0.75)
                                    
                                    dcanvas.coords("nline3",dwidth/2.9,dheight/0.7,dwidth/1.062,dheight/0.7)
                                    dcanvas.coords("nline4",dwidth/2.9,dheight/0.67,dwidth/1.062,dheight/0.67)
                                    dcanvas.coords("nline5",dwidth/2.9,dheight/0.64,dwidth/1.062,dheight/0.64)
                                    dcanvas.coords("nline6",dwidth/2.9,dheight/0.61,dwidth/1.062,dheight/0.61)

                                    dcanvas.coords("naivtlabel1",dwidth/2.88,dheight/0.729)
                                    dcanvas.coords("naivtlabel2",dwidth/2.88,dheight/0.69)
                                    dcanvas.coords("naivtlabel3",dwidth/2.88,dheight/0.66)
                                    dcanvas.coords("naivtlabel4",dwidth/2.88,dheight/0.63)

                                    dcanvas.coords("naivtlabel5",dwidth/2.67,dheight/0.729)
                                    dcanvas.coords("naivtlabel6",dwidth/2.67,dheight/0.69)
                                    dcanvas.coords("naivtlabel7",dwidth/2.67,dheight/0.66)
                                    dcanvas.coords("naivtlabel8",dwidth/2.67,dheight/0.63)

                                    dcanvas.coords("naivtlabel9",dwidth/1.9,dheight/0.729)
                                    dcanvas.coords("naivtlabel10",dwidth/1.9,dheight/0.69)
                                    dcanvas.coords("naivtlabel11",dwidth/1.9,dheight/0.66)
                                    dcanvas.coords("naivtlabel12",dwidth/1.9,dheight/0.63)

                                    dcanvas.coords("naivtlabel13",dwidth/1.65,dheight/0.729)
                                    dcanvas.coords("naivtlabel14",dwidth/1.65,dheight/0.69)
                                    dcanvas.coords("naivtlabel15",dwidth/1.65,dheight/0.66)
                                    dcanvas.coords("naivtlabel16",dwidth/1.65,dheight/0.63)

                                    dcanvas.coords("naivtlabel17",dwidth/1.48,dheight/0.729)
                                    dcanvas.coords("naivtlabel18",dwidth/1.48,dheight/0.69)
                                    dcanvas.coords("naivtlabel19",dwidth/1.48,dheight/0.66)
                                    dcanvas.coords("naivtlabel20",dwidth/1.48,dheight/0.63)

                                    dcanvas.coords("naivtlabel21",dwidth/1.195,dheight/0.729)
                                    dcanvas.coords("naivtlabel22",dwidth/1.195,dheight/0.69)
                                    dcanvas.coords("naivtlabel23",dwidth/1.195,dheight/0.66)
                                    dcanvas.coords("naivtlabel24",dwidth/1.195,dheight/0.63)

                                    dcanvas.coords("naivtlabel25",dwidth/1.33,dheight/0.729)
                                    dcanvas.coords("naivtlabel26",dwidth/1.33,dheight/0.69)
                                    dcanvas.coords("naivtlabel27",dwidth/1.33,dheight/0.66)
                                    dcanvas.coords("naivtlabel28",dwidth/1.33,dheight/0.63)

                                    
                                    dcanvas.coords("naivlabel13",dwidth/1.47,dheight/0.59)
                                    dcanvas.coords("naivlabels13",dwidth/1.21,dheight/0.59)
                                    dcanvas.coords("naivlabel14",dwidth/1.47,dheight/0.565)
                                    dcanvas.coords("naivlabels14",dwidth/1.21,dheight/0.565)
                                    dcanvas.coords("naivlabel15",dwidth/1.47,dheight/0.54)
                                    dcanvas.coords("naivlabels15",dwidth/1.21,dheight/0.54)

                                    dcanvas.coords("naivlabels16",dwidth/2.5,dheight/0.50)
                                    dcanvas.coords("naivlabels17",dwidth/2.5,dheight/0.49)
                                    dcanvas.coords("naivlabels18",dwidth/2.5,dheight/0.48)
                                    dcanvas.coords("naivlabels19",dwidth/2.5,dheight/0.47)

                                    dcanvas.coords("naivline23",dwidth/2.6,dheight/0.4,dwidth/1.11,dheight/0.4)

                                    dcanvas.coords("naivlabel16",dwidth/2.52,dheight/0.395)

                                    dcanvas.coords("naivbutton3",dwidth/23,dheight/3.415)

                                    
                                cs_canvas_1=Canvas(cs_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2000))

                                cs_frame_1.grid_columnconfigure(0,weight=1)
                                cs_frame_1.grid_rowconfigure(0,weight=1)

                                
                                vertibar=Scrollbar(cs_frame_1, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=cs_canvas_1.yview)

                                cs_canvas_1.bind("<Configure>", cs_responsive_widgets_1)
                                cs_canvas_1.config(yscrollcommand=vertibar.set)
                                cs_canvas_1.grid(row=0,column=0,sticky='nsew')

                                def insert_data():
                                    name = ns_entry_1.get()
                                    # template = ns_entry_2.get()
                                    pcolour = ns_entry_3.get()
                                    scolour = ns_entry_4.get()
                                    fonts = ns_entry_5.get()
                                    lastedited = datetime.date.today()
                                    selected = ns_chk_str_1.get()

                                    usr_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usr_val = (nm_ent.get(),)
                                    fbcursor.execute(usr_sql,usr_val)
                                    usr_data = fbcursor.fetchone()

                                    cmp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmp_val = (usr_data[0],)
                                    fbcursor.execute(cmp_sql,cmp_val)
                                    cmp_data = fbcursor.fetchone()
                                    cid = cmp_data[0]

                                    cs_sql_1 = "INSERT INTO app1_customize (name,pcolour,scolour,fonts,lastedited,selected,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                                    cs_val_1=(name,pcolour,scolour,fonts,lastedited,selected,cid)
                                    fbcursor.execute(cs_sql_1,cs_val_1)
                                    finsysdb.commit()

                                    #----------Refresh Insert Tree--------#

                                    for record in cs_tree.get_children():
                                            cs_tree.delete(record)

                                    sql_pr="select * from auth_user where username=%s"
                                    sql_pr_val=(nm_ent.get(),)
                                    fbcursor.execute(sql_pr,sql_pr_val,)
                                    pr_dtl=fbcursor.fetchone()

                                    sql = "select * from app1_company where id_id=%s"
                                    val = (pr_dtl[0],)
                                    fbcursor.execute(sql, val,)
                                    cmp_dtl=fbcursor.fetchone()

                                    c_sql_1 = "SELECT * FROM app1_customize where selected=1 and cid_id=%s"
                                    c_val_1 = (cmp_dtl[0],)
                                    fbcursor.execute(c_sql_1,c_val_1,)
                                    cs_data_1 = fbcursor.fetchall()

                                    count0 = 0
                                    for i in cs_data_1:
                                        
                                        if True:
                                            cs_tree.insert(parent='',index='end',iid=i,text='',values=('',i[1],i[6],"APPLIED"))
                                        
                                    count0 += 1

                                    c_sql_1 = "SELECT * FROM app1_customize where selected=0 and cid_id=%s"
                                    c_val_1 = (cmp_dtl[0],)
                                    fbcursor.execute(c_sql_1,c_val_1,)
                                    cs_data_2 = fbcursor.fetchall()

                                    count0 = 0
                                    for i in cs_data_2:
                                        
                                        if True:
                                            cs_tree.insert(parent='',index='end',iid=i,text='',values=('',i[1],i[6],"NOT APPLIED"))
                                        
                                    count0 += 1

                                    cs_frame_1.destroy()
                                    cs_frame.grid(row=0,column=0,sticky='nsew')

                                    


                                cs_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("nspoly1"))

                                label_1 = Label(cs_canvas_1,width=20,height=1,text="CREATE FORM STYLES", font=('arial 20'),background="#1b3857",fg="white") 
                                window_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("nslabel1"))

                                cs_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("nshline"))

                                cs_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("nspoly2"))

                                label_1 = Label(cs_canvas_1,width=10,height=1,text="Form Name", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("nslabel2"))

                                ns_entry_1=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white")
                                window_ns_entry_1 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_1, tags=('nsentry1'))


                                ns_str = StringVar()
                                ns_str.set("TAX INVOICE")
                                ns_entry_6=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white",textvariable=ns_str)
                                window_ns_entry_6 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_6, tags=('nsentry6'))

                                ns_str_1 = StringVar()
                                ns_str_1.set("Invoice No")
                                ns_entry_7=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white",textvariable=ns_str_1)
                                window_ns_entry_7 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_7, tags=('nsentry7'))

                                ns_str_2 = StringVar()
                                ns_str_2.set("Invoice Date")
                                ns_entry_8=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white",textvariable=ns_str_2)
                                window_ns_entry_8 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_8, tags=('nsentry8'))

                                ns_str_3 = StringVar()
                                ns_str_3.set("Due Date")
                                ns_entry_9=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white",textvariable=ns_str_3)
                                window_ns_entry_9 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_9, tags=('nsentry9'))

                                ns_str_4 = StringVar()
                                ns_str_4.set("Terms")
                                ns_entry_10=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white",textvariable=ns_str_4)
                                window_ns_entry_10 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_10, tags=('nsentry10'))

                                label_1 = Label(cs_canvas_1,width=30,height=1,text="Customize Invoice text labels", font=('arial 12'),background="#1b3857",fg="white", anchor="w") 
                                window_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("nslabel3"))



                                label_1 = Label(cs_canvas_1,width=16,height=1,text="Primary Colours", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("nslabel4"))

                                def color_1_1():
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, "#E9967A")

                                    c_label_1.config(fg="#E9967A")
                                    c_label_7.config(fg="#E9967A")
                                    
      
                                
                                def color_1_2():
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, "#8FBC8F")
                                    
                                    c_label_1.config(fg="#8FBC8F")
                                    c_label_7.config(fg="#8FBC8F")
                                    
                                    
                                
                                def color_1_3():
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, "#B0C4DE")
                                    
                                    c_label_1.config(fg="#B0C4DE")
                                    c_label_7.config(fg="#B0C4DE")
                                    

                                def color_1_4():
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, "#87CEFA")
                                    
                                    c_label_1.config(fg="#87CEFA")
                                    c_label_7.config(fg="#87CEFA")
                                    
                                def color_1_5():
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, "#F0E68C")
                                    
                                    c_label_1.config(fg="#F0E68C")
                                    c_label_7.config(fg="#F0E68C")
                                    
                                
                                def color_1_6():
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, "#DDA0DD")
                                    
                                    c_label_1.config(fg="#DDA0DD")
                                    c_label_7.config(fg="#DDA0DD")
                                    

                                def color_1_7():
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, "#2F4F4F")
                                    
                                    c_label_1.config(fg="#2F4F4F")
                                    c_label_7.config(fg="#2F4F4F")
                                    

                                def color_1_8():
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, "#98FB98")
                                    
                                    c_label_1.config(fg="#98FB98")
                                    c_label_7.config(fg="#98FB98")
                                    
                                    
                                def color_1_9():
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, "#DB7093")
                                    
                                    c_label_1.config(fg="#DB7093")
                                    c_label_7.config(fg="#DB7093")
                                    

                                def color_1_10():
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, "#D2B48C")
                                    
                                    c_label_1.config(fg="#D2B48C")
                                    c_label_7.config(fg="#D2B48C")
                                    
                                
                                def color_1_11():
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, "#D3D3D3")
                                    
                                    c_label_1.config(fg="#D3D3D3")
                                    c_label_7.config(fg="#D3D3D3")        
                                    
                                
                                def color_1_12():
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, "#F5F5F5")
                                    
                                    c_label_1.config(fg="#F5F5F5")
                                    c_label_7.config(fg="#F5F5F5")
                                    

                                ns_entry_3=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white")
                                window_ns_entry_3 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_3, tags=('nsentry3'))

                                ns_btn5=Button(cs_canvas_1, width=5,height=2, activebackground="#E9967A",background="#E9967A",font='arial 12',command=color_1_1)
                                window_ns_btn5 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn5, tags=("nsbutton8"))

                                ns_btn6=Button(cs_canvas_1, width=5,height=2, activebackground="#8FBC8F",background="#8FBC8F",font='arial 12',command=color_1_2)
                                window_ns_btn6 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn6, tags=("nsbutton9"))

                                ns_btn7=Button(cs_canvas_1, width=5,height=2, activebackground="#B0C4DE",background="#B0C4DE",font='arial 12',command=color_1_3)
                                window_ns_btn7 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn7, tags=("nsbutton10"))

                                ns_btn8=Button(cs_canvas_1, width=5,height=2, activebackground="#87CEFA",background="#87CEFA",font='arial 12',command=color_1_4)
                                window_ns_btn8 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn8, tags=("nsbutton11"))

                                ns_btn9=Button(cs_canvas_1, width=5,height=2, activebackground="#F0E68C",background="#F0E68C",font='arial 12',command=color_1_5)
                                window_ns_btn9 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn9, tags=("nsbutton12"))

                                ns_btn10=Button(cs_canvas_1, width=5,height=2, activebackground="#DDA0DD",background="#DDA0DD",font='arial 12',command=color_1_6)
                                window_ns_btn10 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn10, tags=("nsbutton13"))

                                ns_btn11=Button(cs_canvas_1, width=5,height=2, activebackground="#2F4F4F",background="#2F4F4F",font='arial 12',command=color_1_7)
                                window_ns_btn11 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn11, tags=("nsbutton14"))

                                ns_btn12=Button(cs_canvas_1, width=5,height=2, activebackground="#98FB98",background="#98FB98",font='arial 12',command=color_1_8)
                                window_ns_btn12 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn12, tags=("nsbutton15"))

                                ns_btn13=Button(cs_canvas_1, width=5,height=2, activebackground="#DB7093",background="#DB7093",font='arial 12',command=color_1_9)
                                window_ns_btn13 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn13, tags=("nsbutton16"))

                                ns_btn14=Button(cs_canvas_1, width=5,height=2, activebackground="#D2B48C",background="#D2B48C",font='arial 12',command=color_1_10)
                                window_ns_btn14 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn14, tags=("nsbutton17"))

                                ns_btn15=Button(cs_canvas_1, width=5,height=2, activebackground="#D3D3D3",background="#D3D3D3",font='arial 12',command=color_1_11)
                                window_ns_btn15 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn15, tags=("nsbutton18"))

                                ns_btn16=Button(cs_canvas_1, width=5,height=2, activebackground="#F5F5F5",background="#F5F5F5",font='arial 12',command=color_1_12)
                                window_ns_btn16 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn16, tags=("nsbutton19"))

                                label_1 = Label(cs_canvas_1,width=18,height=1,text="Secondary Colours", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("nslabel5"))

                                def color_2_1():
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, "#E9967A")
                                
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='#E9967A',State='DISABLE',foreground='black')
                                
                                
                                def color_2_2():
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, "#8FBC8F")
                                    
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='#8FBC8F',State='DISABLE',foreground='black')
       

                                def color_2_3():
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, "#B0C4DE")
                                    
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='#B0C4DE',State='DISABLE',foreground='black')
                                    

                                def color_2_4():
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, "#87CEFA")
                                    
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='#87CEFA',State='DISABLE',foreground='black')
                                    
                                def color_2_5():
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, "#F0E68C")
                                    
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='#F0E68C',State='DISABLE',foreground='black')
                                
                                
                                def color_2_6():
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, "#DDA0DD")
                                    
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='#DDA0DD',State='DISABLE',foreground='black')
                                    
                                def color_2_7():
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, "#2F4F4F")
                                    
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='#2F4F4F',State='DISABLE',foreground='black')
                                    

                                def color_2_8():
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, "#98FB98")
                                    
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='#98FB98',State='DISABLE',foreground='black')
                                    
                                def color_2_9():
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, "#DB7093")
                                    
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='#DB7093',State='DISABLE',foreground='black')
                                    

                                def color_2_10():
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, "#D2B48C")
                                    
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='#D2B48C',State='DISABLE',foreground='black')
                                    
                                
                                def color_2_11():
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, "#D3D3D3")
                                    
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='#D3D3D3',State='DISABLE',foreground='black')
                                    
                                
                                def color_2_12():
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, "#F5F5F5")
                                    
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='#F5F5F5',State='DISABLE',foreground='black')
                                    

                                ns_entry_4=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white")
                                window_ns_entry_4 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_4, tags=('nsentry4'))

                                ns_btn17=Button(cs_canvas_1, width=5,height=2, activebackground="#E9967A",background="#E9967A",font='arial 12',command=color_2_1)
                                window_ns_btn17 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn17, tags=("nsbutton20"))

                                ns_btn18=Button(cs_canvas_1, width=5,height=2, activebackground="#8FBC8F",background="#8FBC8F",font='arial 12',command=color_2_2)
                                window_ns_btn18 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn18, tags=("nsbutton21"))

                                ns_btn19=Button(cs_canvas_1, width=5,height=2, activebackground="#B0C4DE",background="#B0C4DE",font='arial 12',command=color_2_3)
                                window_ns_btn19 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn19, tags=("nsbutton22"))

                                ns_btn20=Button(cs_canvas_1, width=5,height=2, activebackground="#87CEFA",background="#87CEFA",font='arial 12',command=color_2_4)
                                window_ns_btn20 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn20, tags=("nsbutton23"))

                                ns_btn21=Button(cs_canvas_1, width=5,height=2, activebackground="#F0E68C",background="#F0E68C",font='arial 12',command=color_2_5)
                                window_ns_btn21 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn21, tags=("nsbutton24"))

                                ns_btn22=Button(cs_canvas_1, width=5,height=2, activebackground="#DDA0DD",background="#DDA0DD",font='arial 12',command=color_2_6)
                                window_ns_btn22 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn22, tags=("nsbutton25"))

                                ns_btn23=Button(cs_canvas_1, width=5,height=2, activebackground="#2F4F4F",background="#2F4F4F",font='arial 12',command=color_2_7)
                                window_ns_btn23 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn23, tags=("nsbutton26"))

                                ns_btn24=Button(cs_canvas_1, width=5,height=2, activebackground="#98FB98",background="#98FB98",font='arial 12',command=color_2_8)
                                window_ns_btn24 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn24, tags=("nsbutton27"))

                                ns_btn25=Button(cs_canvas_1, width=5,height=2, activebackground="#DB7093",background="#DB7093",font='arial 12',command=color_2_9)
                                window_ns_btn25 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn25, tags=("nsbutton28"))

                                ns_btn26=Button(cs_canvas_1, width=5,height=2, activebackground="#D2B48C",background="#D2B48C",font='arial 12',command=color_2_10)
                                window_ns_btn26 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn26, tags=("nsbutton29"))

                                ns_btn27=Button(cs_canvas_1, width=5,height=2, activebackground="#D3D3D3",background="#D3D3D3",font='arial 12',command=color_2_11)
                                window_ns_btn27 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn27, tags=("nsbutton30"))

                                ns_btn28=Button(cs_canvas_1, width=5,height=2, activebackground="#F5F5F5",background="#F5F5F5",font='arial 12',command=color_2_12)
                                window_ns_btn28 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn28, tags=("nsbutton31"))

                                label_1 = Label(cs_canvas_1,width=14,height=1,text="Try New Fonts", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("nslabel6"))

                                def Serif():
                                    ns_entry_5.delete(0,"end")
                                    ns_entry_5.insert(0, "Serif Serif font")

                                    c_label_1.config(font=('Garamond bold',12))
                                    c_label_2.config(font=('Garamond',12))
                                    c_label_3.config(font=('Garamond',12))
                                    c_label_4.config(font=('Garamond',12))
                                    c_label_5.config(font=('Garamond',12))
                                    c_label_6.config(font=('Garamond',12))
                                    c_label_7.config(font=('Garamond bold',20))
                                    c_label_8.config(font=('Garamond bold',14))
                                    c_label_9.config(font=('Garamond',12))
                                    c_label_10.config(font=('Garamond bold',12))
                                    c_label_11.config(font=('Garamond',12))
                                    c_label_12.config(font=('Garamond bold',12))
                                    c_label_13.config(font=('Garamond',12))
                                    c_label_14.config(font=('Garamond bold',12))
                                    c_label_15.config(font=('Garamond',12))
                                    c_label_16.config(font=('Garamond bold',12))
                                    c_label_17.config(font=('Garamond',12))
                                    c_label_18.config(font=('Garamond bold',12))
                                    c_label_19.config(font=('Garamond bold',12))
                                    c_label_20.config(font=('Garamond bold',12))
                                    c_label_21.config(font=('Garamond bold',12))
                                    c_label_22.config(font=('Garamond bold',12))
                                    c_label_23.config(font=('Garamond bold',12))
                                    c_label_24.config(font=('Garamond',12))
                                    c_label_25.config(font=('Garamond',12))
                                    c_label_26.config(font=('Garamond',12))
                                    c_label_27.config(font=('Garamond',12))
                                    c_label_28.config(font=('Garamond',12))
                                    c_label_29.config(font=('Garamond',12))
                                    c_label_30.config(font=('Garamond',12))
                                    c_label_31.config(font=('Garamond',12))
                                    c_label_32.config(font=('Garamond',12))
                                    c_label_33.config(font=('Garamond',12))
                                    c_label_34.config(font=('Garamond',12))
                                    c_label_35.config(font=('Garamond',12))
                                    c_label_36.config(font=('Garamond',12))
                                    c_label_37.config(font=('Garamond',12))
                                    c_label_38.config(font=('Garamond',12))
                                    c_label_39.config(font=('Garamond',12))
                                    c_label_40.config(font=('Garamond',12))
                                    c_label_41.config(font=('Garamond',12))
                                    c_label_42.config(font=('Garamond',12))
                                    c_label_43.config(font=('Garamond',12))
                                    c_label_44.config(font=('Garamond',12))
                                    c_label_45.config(font=('Garamond',12))
                                    c_label_46.config(font=('Garamond',12))
                                    c_label_47.config(font=('Garamond',12))
                                    c_label_48.config(font=('Garamond',12))
                                    c_label_49.config(font=('Garamond',12))
                                    c_label_50.config(font=('Garamond',12))
                                    c_label_51.config(font=('Garamond',12))
                                    c_label_52.config(font=('Garamond',12))
                                    c_label_53.config(font=('Garamond bold',12))
                                    c_label_54.config(font=('Garamond',12))
                                    c_label_55.config(font=('Garamond',12))
                                    c_label_56.config(font=('Garamond',12))
                                    
                                def Sans():
                                    ns_entry_5.delete(0,"end")
                                    ns_entry_5.insert(0, "Sans-serif Sans-serif font")

                                    
                                    c_label_1.config(font=('Arial bold',12))
                                    c_label_2.config(font=('Arial',12))
                                    c_label_3.config(font=('Arial',12))
                                    c_label_4.config(font=('Arial',12))
                                    c_label_5.config(font=('Arial',12))
                                    c_label_6.config(font=('Arial',12))
                                    c_label_7.config(font=('Arial bold',20))
                                    c_label_8.config(font=('Arial bold',14))
                                    c_label_9.config(font=('Arial',12))
                                    c_label_10.config(font=('Arial bold',12))
                                    c_label_11.config(font=('Arial',12))
                                    c_label_12.config(font=('Arial bold',12))
                                    c_label_13.config(font=('Arial',12))
                                    c_label_14.config(font=('Arial bold',12))
                                    c_label_15.config(font=('Arial',12))
                                    c_label_16.config(font=('Arial bold',12))
                                    c_label_17.config(font=('Arial',12))
                                    c_label_18.config(font=('Arial bold',12))
                                    c_label_19.config(font=('Arial bold',12))
                                    c_label_20.config(font=('Arial bold',12))
                                    c_label_21.config(font=('Arial bold',12))
                                    c_label_22.config(font=('Arial bold',12))
                                    c_label_23.config(font=('Arial bold',12))
                                    c_label_24.config(font=('Arial',12))
                                    c_label_25.config(font=('Arial',12))
                                    c_label_26.config(font=('Arial',12))
                                    c_label_27.config(font=('Arial',12))
                                    c_label_28.config(font=('Arial',12))
                                    c_label_29.config(font=('Arial',12))
                                    c_label_30.config(font=('Arial',12))
                                    c_label_31.config(font=('Arial',12))
                                    c_label_32.config(font=('Arial',12))
                                    c_label_33.config(font=('Arial',12))
                                    c_label_34.config(font=('Arial',12))
                                    c_label_35.config(font=('Arial',12))
                                    c_label_36.config(font=('Arial',12))
                                    c_label_37.config(font=('Arial',12))
                                    c_label_38.config(font=('Arial',12))
                                    c_label_39.config(font=('Arial',12))
                                    c_label_40.config(font=('Arial',12))
                                    c_label_41.config(font=('Arial',12))
                                    c_label_42.config(font=('Arial',12))
                                    c_label_43.config(font=('Arial',12))
                                    c_label_44.config(font=('Arial',12))
                                    c_label_45.config(font=('Arial',12))
                                    c_label_46.config(font=('Arial',12))
                                    c_label_47.config(font=('Arial',12))
                                    c_label_48.config(font=('Arial',12))
                                    c_label_49.config(font=('Arial',12))
                                    c_label_50.config(font=('Arial',12))
                                    c_label_51.config(font=('Arial',12))
                                    c_label_52.config(font=('Arial',12))
                                    c_label_53.config(font=('Arial bold',12))
                                    c_label_54.config(font=('Arial',12))
                                    c_label_55.config(font=('Arial',12))
                                    c_label_56.config(font=('Arial',12))
                                    
                                def Monospace():
                                    ns_entry_5.delete(0,"end")
                                    ns_entry_5.insert(0, "Monospace Monospace font")

                                    
                                    c_label_1.config(font=('Helvetica bold',12))
                                    c_label_2.config(font=('Helvetica',12))
                                    c_label_3.config(font=('Helvetica',12))
                                    c_label_4.config(font=('Helvetica',12))
                                    c_label_5.config(font=('Helvetica',12))
                                    c_label_6.config(font=('Helvetica',12))
                                    c_label_7.config(font=('Helvetica bold',20))
                                    c_label_8.config(font=('Helvetica bold',14))
                                    c_label_9.config(font=('Helvetica',12))
                                    c_label_10.config(font=('Helvetica bold',12))
                                    c_label_11.config(font=('Helvetica',12))
                                    c_label_12.config(font=('Helvetica bold',12))
                                    c_label_13.config(font=('Helvetica',12))
                                    c_label_14.config(font=('Helvetica bold',12))
                                    c_label_15.config(font=('Helvetica',12))
                                    c_label_16.config(font=('Helvetica bold',12))
                                    c_label_17.config(font=('Helvetica',12))
                                    c_label_18.config(font=('Helvetica bold',12))
                                    c_label_19.config(font=('Helvetica bold',12))
                                    c_label_20.config(font=('Helvetica bold',12))
                                    c_label_21.config(font=('Helvetica bold',12))
                                    c_label_22.config(font=('Helvetica bold',12))
                                    c_label_23.config(font=('Helvetica bold',12))
                                    c_label_24.config(font=('Helvetica',12))
                                    c_label_25.config(font=('Helvetica',12))
                                    c_label_26.config(font=('Helvetica',12))
                                    c_label_27.config(font=('Helvetica',12))
                                    c_label_28.config(font=('Helvetica',12))
                                    c_label_29.config(font=('Helvetica',12))
                                    c_label_30.config(font=('Helvetica',12))
                                    c_label_31.config(font=('Helvetica',12))
                                    c_label_32.config(font=('Helvetica',12))
                                    c_label_33.config(font=('Helvetica',12))
                                    c_label_34.config(font=('Helvetica',12))
                                    c_label_35.config(font=('Helvetica',12))
                                    c_label_36.config(font=('Helvetica',12))
                                    c_label_37.config(font=('Helvetica',12))
                                    c_label_38.config(font=('Helvetica',12))
                                    c_label_39.config(font=('Helvetica',12))
                                    c_label_40.config(font=('Helvetica',12))
                                    c_label_41.config(font=('Helvetica',12))
                                    c_label_42.config(font=('Helvetica',12))
                                    c_label_43.config(font=('Helvetica',12))
                                    c_label_44.config(font=('Helvetica',12))
                                    c_label_45.config(font=('Helvetica',12))
                                    c_label_46.config(font=('Helvetica',12))
                                    c_label_47.config(font=('Helvetica',12))
                                    c_label_48.config(font=('Helvetica',12))
                                    c_label_49.config(font=('Helvetica',12))
                                    c_label_50.config(font=('Helvetica',12))
                                    c_label_51.config(font=('Helvetica',12))
                                    c_label_52.config(font=('Helvetica',12))
                                    c_label_53.config(font=('Helvetica bold',12))
                                    c_label_54.config(font=('Helvetica',12))
                                    c_label_55.config(font=('Helvetica',12))
                                    c_label_56.config(font=('Helvetica',12))
                                    

                                def System():
                                    ns_entry_5.delete(0,"end")
                                    ns_entry_5.insert(0, "System-ui System-ui font")

                                    
                                    c_label_1.config(font=('Roboto bold',12))
                                    c_label_2.config(font=('Roboto',12))
                                    c_label_3.config(font=('Roboto',12))
                                    c_label_4.config(font=('Roboto',12))
                                    c_label_5.config(font=('Roboto',12))
                                    c_label_6.config(font=('Roboto',12))
                                    c_label_7.config(font=('Roboto bold',20))
                                    c_label_8.config(font=('Roboto bold',14))
                                    c_label_9.config(font=('Roboto',12))
                                    c_label_10.config(font=('Roboto bold',12))
                                    c_label_11.config(font=('Roboto',12))
                                    c_label_12.config(font=('Roboto bold',12))
                                    c_label_13.config(font=('Roboto',12))
                                    c_label_14.config(font=('Roboto bold',12))
                                    c_label_15.config(font=('Roboto',12))
                                    c_label_16.config(font=('Roboto bold',12))
                                    c_label_17.config(font=('Roboto',12))
                                    c_label_18.config(font=('Roboto bold',12))
                                    c_label_19.config(font=('Roboto bold',12))
                                    c_label_20.config(font=('Roboto bold',12))
                                    c_label_21.config(font=('Roboto bold',12))
                                    c_label_22.config(font=('Roboto bold',12))
                                    c_label_23.config(font=('Roboto bold',12))
                                    c_label_24.config(font=('Roboto',12))
                                    c_label_25.config(font=('Roboto',12))
                                    c_label_26.config(font=('Roboto',12))
                                    c_label_27.config(font=('Roboto',12))
                                    c_label_28.config(font=('Roboto',12))
                                    c_label_29.config(font=('Roboto',12))
                                    c_label_30.config(font=('Roboto',12))
                                    c_label_31.config(font=('Roboto',12))
                                    c_label_32.config(font=('Roboto',12))
                                    c_label_33.config(font=('Roboto',12))
                                    c_label_34.config(font=('Roboto',12))
                                    c_label_35.config(font=('Roboto',12))
                                    c_label_36.config(font=('Roboto',12))
                                    c_label_37.config(font=('Roboto',12))
                                    c_label_38.config(font=('Roboto',12))
                                    c_label_39.config(font=('Roboto',12))
                                    c_label_40.config(font=('Roboto',12))
                                    c_label_41.config(font=('Roboto',12))
                                    c_label_42.config(font=('Roboto',12))
                                    c_label_43.config(font=('Roboto',12))
                                    c_label_44.config(font=('Roboto',12))
                                    c_label_45.config(font=('Roboto',12))
                                    c_label_46.config(font=('Roboto',12))
                                    c_label_47.config(font=('Roboto',12))
                                    c_label_48.config(font=('Roboto',12))
                                    c_label_49.config(font=('Roboto',12))
                                    c_label_50.config(font=('Roboto',12))
                                    c_label_51.config(font=('Roboto',12))
                                    c_label_52.config(font=('Roboto',12))
                                    c_label_53.config(font=('Roboto bold',12))
                                    c_label_54.config(font=('Roboto',12))
                                    c_label_55.config(font=('Roboto',12))
                                    c_label_56.config(font=('Roboto',12))
                                    

                                ns_entry_5=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white")
                                window_ns_entry_5 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_5, tags=('nsentry5'))
                                
                                ns_btn29=Button(cs_canvas_1,text='Serif\nSerif font', width=15,height=4,foreground="white",background="#1b3857",font='arial 12',command=Serif)
                                window_ns_btn29 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn29, tags=("nsbutton32"))

                                ns_btn30=Button(cs_canvas_1,text='Sans-serif\nSans-serif font', width=15,height=4,foreground="white",background="#1b3857",font='arial 12',command=Sans)
                                window_ns_btn30 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn30, tags=("nsbutton33"))

                                ns_btn31=Button(cs_canvas_1,text='Monospace\nMonospace font', width=15,height=4,foreground="white",background="#1b3857",font='arial 12',command=Monospace)
                                window_ns_btn31 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn31, tags=("nsbutton34"))

                                ns_btn32=Button(cs_canvas_1,text='System-ui\nSystem-ui font', width=15,height=4,foreground="white",background="#1b3857",font='arial 12',command=System)
                                window_ns_btn32 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn32, tags=("nsbutton35"))

                                ns_chk_str_1 = BooleanVar()
                                ns_chkbtn2 = Checkbutton(cs_canvas_1, text = "Apply this theme", variable = ns_chk_str_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                                window_ns_chkbtn2 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_chkbtn2,tags=("nscheck1"))

                                #----------------------------------------Template 1-----------------------------------------

                                sql_u = 'select * from auth_user where username=%s'
                                val_u = (nm_ent.get(),)
                                fbcursor.execute(sql_u,val_u)
                                u_dtl = fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (u_dtl[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dtl=fbcursor.fetchone()
                                

                                sql = 'select * from app1_invoice where cid_id=%s'
                                val =  (cmp_dtl[0],)
                                fbcursor.execute(sql,val,)
                                cl_view = fbcursor.fetchone()

                                cs_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="white",tags=("nspoly3"))


                                c_label_1 = Label(cs_canvas_1,width=12,height=1,text=cmp_dtl[1], font=('arial 14 bold'),background="white",fg="skyblue",anchor="w") 
                                window_c_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_1, tags=("naivlabel1"))

                                c_label_2 = Label(cs_canvas_1,width=15,height=1,text=cmp_dtl[2], font=('arial 12 '),background="white",fg="black",anchor="w") 
                                window_c_label_2 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_2, tags=("naivlabel2"))

                                c_label_3 = Label(cs_canvas_1,width=15,height=1,text=cmp_dtl[3]+","+cmp_dtl[4], font=('arial 12 '),background="white",fg="black",anchor="w") 
                                window_c_label_3 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_3, tags=("naivlabel3"))

                                c_label_4 = Label(cs_canvas_1,width=15,height=1,text=cmp_dtl[5], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_4 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_4, tags=("naivlabel4"))

                                c_label_5 = Label(cs_canvas_1,width=15,height=1,text=cmp_dtl[6], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_5 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_5, tags=("naivlabel5"))

                                c_label_6 = Label(cs_canvas_1,width=10,height=1,text=cmp_dtl[7], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_6 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_6, tags=("naivlabel6"))

                                c_label_7 = Label(cs_canvas_1,width=20,height=1,text=""+ns_entry_6.get(), font=('arial 20 bold'),background="white",fg="skyblue",anchor="w") 
                                window_c_label_7 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_7, tags=("naivlabel7"))


                                cs_image_1=Label(cs_canvas_1,  image = prof_pics,bg="#213b52",width=200,height=150,  anchor="center",font=('Calibri 14 bold'))
                                win_cs_image_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=cs_image_1,tags=("nimage1"))

                                c_label_8 = Label(cs_canvas_1,width=15,height=1,text="Bill To", font=('arial 14 bold'),background="white",fg="black") 
                                window_c_label_8 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_8, tags=("naivlabel8"))

                                c_label_9 = Label(cs_canvas_1,width=20,height=8,text=cl_view[7], font=('arial 12'),background="white",fg="black",anchor="w") 
                                window_c_label_9 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_9, tags=("naivlabel17"))

                                cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('nline1'))


                                c_label_10 = Label(cs_canvas_1,width=11,height=1,text=""+ns_entry_7.get(), font=('arial 12 bold'),background="white",fg="black",anchor="w") 
                                window_c_label_10 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_10, tags=("naivlabel9"))

                                c_label_11 = Label(cs_canvas_1,width=11,height=1,text=cl_view[3], font=('arial 12'),background="white",fg="black",anchor="w") 
                                window_c_label_11 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_11, tags=("naivlabel18"))

                                c_label_12 = Label(cs_canvas_1,width=11,height=1,text=""+ns_entry_8.get(), font=('arial 12 bold'),background="white",fg="black",anchor="w") 
                                window_c_label_12 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_12, tags=("naivlabel10"))

                                c_label_13 = Label(cs_canvas_1,width=10,height=1,text=cl_view[5], font=('arial 12'),background="white",fg="black",anchor="w") 
                                window_c_label_13 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_13, tags=("naivlabel19"))

                                c_label_14 = Label(cs_canvas_1,width=11,height=1,text=""+ns_entry_9.get(), font=('arial 12 bold'),background="white",fg="black",anchor="w") 
                                window_c_label_14 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_14, tags=("naivlabel11"))

                                c_label_15 = Label(cs_canvas_1,width=10,height=1,text=cl_view[6], font=('arial 12'),background="white",fg="black",anchor="w") 
                                window_c_label_15 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_15, tags=("naivlabel20"))

                                c_label_16 = Label(cs_canvas_1,width=11,height=1,text=""+ns_entry_10.get(), font=('arial 12 bold'),background="white",fg="black",anchor="w") 
                                window_c_label_16 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_16, tags=("naivlabel12"))

                                cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('nline2'))
                                

                                c_label_17 = Label(cs_canvas_1,width=10,height=1,text=cl_view[4], font=('arial 12'),background="white",fg="black",anchor="w") 
                                window_c_label_17 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_17, tags=("naivlabel21"))

                                fgthvi_1 = ttk.Style()
                                fgthvi_1.theme_use("default")
                                fgthvi_1.configure('mystyle10.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                                fgthvi_1.configure('mystyle10.Treeview.Heading', background='skyblue',State='DISABLE',foreground='black')

                                nsview_tree = ttk.Treeview(cs_canvas_1, columns = (1,2,3,4,5,6,7), height = 0, show = "headings",style='mystyle10.Treeview')
                                nsview_tree.pack(side = 'top')
                                nsview_tree.heading(1)
                                nsview_tree.heading(2, text="PRODUCT/SERVICES")
                                nsview_tree.heading(3, text="HSN")
                                nsview_tree.heading(4, text="QTY")
                                nsview_tree.heading(5, text="PRICE")
                                nsview_tree.heading(6, text="TOTAL")
                                nsview_tree.heading(7, text="TAX(%)")
                                
                                nsview_tree.column(1, width = 30)
                                nsview_tree.column(2, width = 200)
                                nsview_tree.column(3, width = 110)
                                nsview_tree.column(4, width = 90)
                                nsview_tree.column(5, width = 105)
                                nsview_tree.column(6, width = 105)
                                nsview_tree.column(7, width = 155)

                                window = cs_canvas_1.create_window(0, 0, anchor="nw", height=0, window=nsview_tree,tags=('naivtree1'))

                                cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('nline3'))
                                cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('nline4'))
                                cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('nline5'))
                                cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('nline6'))
                                

                                c_label_25 = Label(cs_canvas_1,width=1,height=1,text="1", font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_25 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_25, tags=("naivtlabel1"))

                                c_label_26 = Label(cs_canvas_1,width=1,height=1,text="2", font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_26 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_26, tags=("naivtlabel2"))

                                c_label_27 = Label(cs_canvas_1,width=1,height=1,text="3", font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_27 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_27, tags=("naivtlabel3"))

                                c_label_28 = Label(cs_canvas_1,width=1,height=1,text="4", font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_28 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_28, tags=("naivtlabel4"))

                                c_label_29 = Label(cs_canvas_1,width=8,height=1,text=cl_view[9], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_29 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_29, tags=("naivtlabel5"))

                                c_label_30 = Label(cs_canvas_1,width=8,height=1,text=cl_view[18], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_30 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_30, tags=("naivtlabel6"))

                                c_label_31 = Label(cs_canvas_1,width=8,height=1,text=cl_view[25], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_31 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_31, tags=("naivtlabel7"))

                                c_label_32 = Label(cs_canvas_1,width=8,height=1,text=cl_view[32], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_32 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_32, tags=("naivtlabel8"))

                                c_label_33 = Label(cs_canvas_1,width=8,height=1,text=cl_view[10], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_33 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_33, tags=("naivtlabel9"))

                                c_label_34 = Label(cs_canvas_1,width=8,height=1,text=cl_view[19], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_34 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_34, tags=("naivtlabel10"))

                                c_label_35 = Label(cs_canvas_1,width=8,height=1,text=cl_view[26], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_35 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_35, tags=("naivtlabel11"))

                                c_label_36 = Label(cs_canvas_1,width=8,height=1,text=cl_view[33], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_36 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_36, tags=("naivtlabel12"))

                                c_label_37 = Label(cs_canvas_1,width=2,height=1,text=cl_view[12], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_37 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_37, tags=("naivtlabel13"))

                                c_label_38 = Label(cs_canvas_1,width=2,height=1,text=cl_view[21], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_38 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_38, tags=("naivtlabel14"))

                                c_label_39 = Label(cs_canvas_1,width=2,height=1,text=cl_view[28], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_39 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_39, tags=("naivtlabel15"))

                                c_label_40 = Label(cs_canvas_1,width=2,height=1,text=cl_view[35], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_40 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_40, tags=("naivtlabel16"))

                                c_label_41 = Label(cs_canvas_1,width=7,height=1,text=cl_view[13], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_41 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_41, tags=("naivtlabel25"))

                                c_label_42 = Label(cs_canvas_1,width=7,height=1,text=cl_view[22], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_42 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_42, tags=("naivtlabel26"))

                                c_label_43 = Label(cs_canvas_1,width=7,height=1,text=cl_view[29], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_43 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_43, tags=("naivtlabel27"))

                                c_label_44 = Label(cs_canvas_1,width=7,height=1,text=cl_view[36], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_44 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_44, tags=("naivtlabel28"))


                                c_label_45 = Label(cs_canvas_1,width=7,height=1,text=cl_view[14], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_45 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_45, tags=("naivtlabel17"))

                                c_label_46 = Label(cs_canvas_1,width=7,height=1,text=cl_view[23], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_46 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_46, tags=("naivtlabel18"))

                                c_label_47 = Label(cs_canvas_1,width=7,height=1,text=cl_view[30], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_47 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_47, tags=("naivtlabel19"))

                                c_label_48 = Label(cs_canvas_1,width=7,height=1,text=cl_view[37], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_48 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_48, tags=("naivtlabel20"))

                                c_label_49 = Label(cs_canvas_1,width=14,height=1,text=cl_view[15], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_49 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_49, tags=("naivtlabel21"))

                                c_label_50 = Label(cs_canvas_1,width=14,height=1,text=cl_view[24], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_50 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_50, tags=("naivtlabel22"))

                                c_label_51 = Label(cs_canvas_1,width=14,height=1,text=cl_view[31], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_51 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_51, tags=("naivtlabel23"))

                                c_label_52 = Label(cs_canvas_1,width=14,height=1,text=cl_view[38], font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_52 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_52, tags=("naivtlabel24"))


                                c_label_18 = Label(cs_canvas_1,width=11,height=1,text="Subtotal", font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                window_c_label_18 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_18, tags=("naivlabel13"))

                                c_label_19 = Label(cs_canvas_1,width=10,height=1,text=cl_view[16], font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                window_c_label_19 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_19, tags=("naivlabels13"))

                                c_label_20 = Label(cs_canvas_1,width=11,height=1,text="Tax Amount", font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                window_c_label_20 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_20, tags=("naivlabel14"))

                                c_label_21 = Label(cs_canvas_1,width=10,height=1,text=cl_view[40], font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                window_c_label_21 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_21, tags=("naivlabels14"))


                                c_label_22 = Label(cs_canvas_1,width=5,height=1,text="Total", font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                window_c_label_22 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_22, tags=("naivlabel15"))

                                c_label_23 = Label(cs_canvas_1,width=10,height=1,text=cl_view[17], font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                window_c_label_23 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_23, tags=("naivlabels15"))

                                c_label_53 = Label(cs_canvas_1,width=22,height=1,text="Terms and Conditions", font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                window_c_label_53 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_53, tags=("naivlabels16"))

                                c_label_54 = Label(cs_canvas_1,width=40,height=1,text="1. Goods once sold will not be taken back.", font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_54 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_54, tags=("naivlabels17"))

                                c_label_55 = Label(cs_canvas_1,width=50,height=1,text="2. If cheque bounced, Rs 500/- will be taken as Charges.", font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_55 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_55, tags=("naivlabels18"))

                                c_label_56 = Label(cs_canvas_1,width=55,height=1,text="3. Rs 100/- per day will charged for delayed payment after due date.", font=('arial 12'),background="white",fg="black", anchor="w") 
                                window_c_label_56 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_56, tags=("naivlabels19"))

                                cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('naivline23'))

                                c_label_24 = Label(cs_canvas_1,width=75,height=0,text="Invoice was created on a computer and is valid without the signature and seal.", font=('arial 12'),background="white",fg="black") 
                                window_c_label_24 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_24, tags=("naivlabel16"))

                                
                                def cs_refresh():
                                        c_label_7.config(text=""+ns_entry_6.get())
                                        c_label_10.config(text=""+ns_entry_7.get())
                                        c_label_12.config(text=""+ns_entry_8.get())
                                        c_label_14.config(text=""+ns_entry_9.get())
                                        c_label_16.config(text=""+ns_entry_10.get())

                                refreshbtn = Button(cs_canvas_1,text="Refresh",width=15,height=1,foreground="white",background="#1b3857",font='arial 12',command=cs_refresh)
                                window_refreshbtn = cs_canvas_1.create_window(0, 0, anchor="nw", window=refreshbtn, tags=("nsbutton7"))
                                
                                ns_sub_btn1=Button(cs_canvas_1,text='Submit', width=15,height=2,bd=0, foreground="white",background="#2f516f",font='arial 12',activebackground="#2f516f",command=insert_data)
                                window_ns_sub_btn1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_sub_btn1,tags=('nsbutton1'))

                                def ns_back_1_():
                                    cs_frame_1.grid_forget()
                                    cs_frame.grid(row=0,column=0,sticky='nsew')


                                ns_bck_btn1=Button(cs_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=ns_back_1_)
                                window_ns_bck_btn1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_bck_btn1,tags=('nsbutton3'))
                                

                            cs_btn1=Button(cs_canvas,text='New Style', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_newstyle)
                            window_cs_btn1 = cs_canvas.create_window(0, 0, anchor="nw", window=cs_btn1, tags=("csbutton2"))

                            # #-------------------------------Edit Section-----------------------------------#
                            def edit_newstyle(event):
                                if cs_comb_1.get()=="Edit":
                                    cs_id_1 = cs_tree.item(cs_tree.focus())["values"][1]
                                        
                                        
                                    sql_u = 'select * from auth_user where username=%s'
                                    val_u = (nm_ent.get(),)
                                    fbcursor.execute(sql_u,val_u)
                                    u_dtl = fbcursor.fetchone()

                                    sql_c = 'select * from app1_company where id_id=%s'
                                    val_c = (u_dtl[0],)
                                    fbcursor.execute(sql_c,val_c)
                                    c_dtl = fbcursor.fetchone()

                                    sql = 'select * from app1_customize where name=%s and cid_id=%s'
                                    val = (cs_id_1,c_dtl[0],)
                                    fbcursor.execute(sql,val)
                                    e_dtl = fbcursor.fetchone()

                                    cs_frame.grid_forget()
                                    cs_frame_1 = Frame(tab1)
                                    cs_frame_1.grid(row=0,column=0,sticky='nsew')

                                    def cs_responsive_widgets_1(event):
                                        dwidth = event.width
                                        dheight = event.height
                                        dcanvas = event.widget
                                        
                                        r1 = 25
                                        x1 = dwidth/63
                                        x2 = dwidth/1.021
                                        y1 = dheight/14 
                                        y2 = dheight/3.505

                                        dcanvas.coords("nspoly1",x1 + r1,y1,
                                        x1 + r1,y1,
                                        x2 - r1,y1,
                                        x2 - r1,y1,     
                                        x2,y1,     
                                        #--------------------
                                        x2,y1 + r1,     
                                        x2,y1 + r1,     
                                        x2,y2 - r1,     
                                        x2,y2 - r1,     
                                        x2,y2,
                                        #--------------------
                                        x2 - r1,y2,     
                                        x2 - r1,y2,     
                                        x1 + r1,y2,
                                        x1 + r1,y2,
                                        x1,y2,
                                        #--------------------
                                        x1,y2 - r1,
                                        x1,y2 - r1,
                                        x1,y1 + r1,
                                        x1,y1 + r1,
                                        x1,y1,
                                        )

                                        dcanvas.coords("nslabel1",dwidth/2.5,dheight/8.24)
                                        dcanvas.coords("nshline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                        r2 = 25
                                        x11 = dwidth/63
                                        x21 = dwidth/1.021
                                        y11 = dheight/2.8
                                        y21 = dheight/0.32


                                        dcanvas.coords("nspoly2",x11 + r2,y11,
                                        x11 + r2,y11,
                                        x21 - r2,y11,
                                        x21 - r2,y11,     
                                        x21,y11,     
                                        #--------------------
                                        x21,y11 + r2,     
                                        x21,y11 + r2,     
                                        x21,y21 - r2,     
                                        x21,y21 - r2,     
                                        x21,y21,
                                        #--------------------
                                        x21 - r2,y21,     
                                        x21 - r2,y21,     
                                        x11 + r2,y21,
                                        x11 + r2,y21,
                                        x11,y21,
                                        #--------------------
                                        x11,y21 - r2,
                                        x11,y21 - r2,
                                        x11,y11 + r2,
                                        x11,y11 + r2,
                                        x11,y11,
                                        )
                                        dcanvas.coords("nsbutton3",dwidth/23,dheight/3.415)
                                        dcanvas.coords("nslabel2",dwidth/21,dheight/2.3)
                                        dcanvas.coords("nsentry1",dwidth/20,dheight/2.05)

                                        dcanvas.coords("nslabel3",dwidth/22.2,dheight/1.75)
                                        dcanvas.coords("nsentry6",dwidth/20,dheight/1.57)
                                        dcanvas.coords("nsentry7",dwidth/20,dheight/1.45)
                                        dcanvas.coords("nsentry8",dwidth/20,dheight/1.34)
                                        dcanvas.coords("nsentry9",dwidth/20,dheight/1.25)
                                        dcanvas.coords("nsentry10",dwidth/20,dheight/1.17)
                                        dcanvas.coords("nsbutton7",dwidth/9,dheight/1)

                                        # dcanvas.coords("nslabel3",dwidth/22.2,dheight/1.64)
                                        # dcanvas.coords("nsentry2",dwidth/20,dheight/1.5)
                                        # dcanvas.coords("nsbutton4",dwidth/20,dheight/1.25)
                                        # dcanvas.coords("nsbutton5",dwidth/5.8,dheight/1.25)
                                        # dcanvas.coords("nsbutton6",dwidth/20,dheight/1)
                                        # dcanvas.coords("nsbutton7",dwidth/5.8,dheight/1)
                                        dcanvas.coords("nslabel4",dwidth/22.8,dheight/0.83)
                                        dcanvas.coords("nsentry3",dwidth/20,dheight/0.798)
                                        dcanvas.coords("nsbutton8",dwidth/20,dheight/0.75)
                                        dcanvas.coords("nsbutton9",dwidth/9,dheight/0.75)
                                        dcanvas.coords("nsbutton10",dwidth/5.72,dheight/0.75)
                                        dcanvas.coords("nsbutton11",dwidth/4.2,dheight/0.75)
                                        dcanvas.coords("nsbutton12",dwidth/20,dheight/0.695)
                                        dcanvas.coords("nsbutton13",dwidth/9,dheight/0.695)
                                        dcanvas.coords("nsbutton14",dwidth/5.72,dheight/0.695)
                                        dcanvas.coords("nsbutton15",dwidth/4.2,dheight/0.695)
                                        dcanvas.coords("nsbutton16",dwidth/20,dheight/0.65)
                                        dcanvas.coords("nsbutton17",dwidth/9,dheight/0.65)
                                        dcanvas.coords("nsbutton18",dwidth/5.72,dheight/0.65)
                                        dcanvas.coords("nsbutton19",dwidth/4.2,dheight/0.65)
                                        dcanvas.coords("nslabel5",dwidth/22.8,dheight/0.595)
                                        dcanvas.coords("nsentry4",dwidth/20,dheight/0.58)
                                        dcanvas.coords("nsbutton20",dwidth/20,dheight/0.55)
                                        dcanvas.coords("nsbutton21",dwidth/9,dheight/0.55)
                                        dcanvas.coords("nsbutton22",dwidth/5.72,dheight/0.55)
                                        dcanvas.coords("nsbutton23",dwidth/4.2,dheight/0.55)
                                        dcanvas.coords("nsbutton24",dwidth/20,dheight/0.52)
                                        dcanvas.coords("nsbutton25",dwidth/9,dheight/0.52)
                                        dcanvas.coords("nsbutton26",dwidth/5.72,dheight/0.52)
                                        dcanvas.coords("nsbutton27",dwidth/4.2,dheight/0.52)
                                        dcanvas.coords("nsbutton28",dwidth/20,dheight/0.493)
                                        dcanvas.coords("nsbutton29",dwidth/9,dheight/0.493)
                                        dcanvas.coords("nsbutton30",dwidth/5.72,dheight/0.493)
                                        dcanvas.coords("nsbutton31",dwidth/4.2,dheight/0.493) 
                                        dcanvas.coords("nslabel6",dwidth/22.5,dheight/0.464)
                                        dcanvas.coords("nsentry5",dwidth/20,dheight/0.45)
                                        dcanvas.coords("nsbutton32",dwidth/20,dheight/0.43)
                                        dcanvas.coords("nsbutton33",dwidth/5.8,dheight/0.43)
                                        dcanvas.coords("nsbutton34",dwidth/20,dheight/0.4)
                                        dcanvas.coords("nsbutton35",dwidth/5.8,dheight/0.4)
                                        dcanvas.coords("nscheck1",dwidth/8.5,dheight/0.37)
                                        dcanvas.coords("nsbutton1",dwidth/8.5,dheight/0.355)

                                        #--------------------------Classic------------------------------

                                        r2 = 25
                                        x11 = dwidth/3
                                        x21 = dwidth/1.05
                                        y11 = dheight/2.3
                                        y21 = dheight/0.38


                                        dcanvas.coords("nspoly3",x11 + r2,y11,
                                        x11 + r2,y11,
                                        x21 - r2,y11,
                                        x21 - r2,y11,     
                                        x21,y11,     
                                        #--------------------
                                        x21,y11 + r2,     
                                        x21,y11 + r2,     
                                        x21,y21 - r2,     
                                        x21,y21 - r2,     
                                        x21,y21,
                                        #--------------------
                                        x21 - r2,y21,     
                                        x21 - r2,y21,     
                                        x11 + r2,y21,
                                        x11 + r2,y21,
                                        x11,y21,
                                        #--------------------
                                        x11,y21 - r2,
                                        x11,y21 - r2,
                                        x11,y11 + r2,
                                        x11,y11 + r2,
                                        x11,y11,
                                        )

                                        r2 = 0
                                        x11 = dwidth/2.955
                                        x21 = dwidth/1.057
                                        y11 = dheight/2.2
                                        y21 = dheight/0.382


                                        dcanvas.coords("nspoly3_1",x11 + r2,y11,
                                        x11 + r2,y11,
                                        x21 - r2,y11,
                                        x21 - r2,y11,     
                                        x21,y11,     
                                        #--------------------
                                        x21,y11 + r2,     
                                        x21,y11 + r2,     
                                        x21,y21 - r2,     
                                        x21,y21 - r2,     
                                        x21,y21,
                                        #--------------------
                                        x21 - r2,y21,     
                                        x21 - r2,y21,     
                                        x11 + r2,y21,
                                        x11 + r2,y21,
                                        x11,y21,
                                        #--------------------
                                        x11,y21 - r2,
                                        x11,y21 - r2,
                                        x11,y11 + r2,
                                        x11,y11 + r2,
                                        x11,y11,
                                        )

                                        dcanvas.coords("naivlabel1",dwidth/1.33,dheight/1.72)
                                        dcanvas.coords("naivlabel2",dwidth/1.33,dheight/1.59)
                                        dcanvas.coords("naivlabel3",dwidth/1.33,dheight/1.48)
                                        dcanvas.coords("naivlabel4",dwidth/1.33,dheight/1.38)
                                        dcanvas.coords("naivlabel5",dwidth/1.33,dheight/1.29)
                                        dcanvas.coords("naivlabel6",dwidth/1.33,dheight/1.2)
                                        dcanvas.coords("naivlabel7",dwidth/1.8,dheight/2.11)
                                        dcanvas.coords("nline1",dwidth/2.95,dheight/0.875,dwidth/1.057,dheight/0.875)

                                        dcanvas.coords("nimage1",dwidth/2.65,dheight/1.72)

                                        dcanvas.coords("naivlabel8",dwidth/2.87,dheight/1.16)
                                        dcanvas.coords("naivlabel17",dwidth/2.60,dheight/1.11)
                                    
                                        dcanvas.coords("naivlabel9",dwidth/1.35,dheight/0.865)
                                        dcanvas.coords("naivlabel10",dwidth/1.35,dheight/0.835)
                                        dcanvas.coords("naivlabel11",dwidth/1.35,dheight/0.805)
                                        dcanvas.coords("naivlabel12",dwidth/1.35,dheight/0.785)

                                        dcanvas.coords("naivlabel18",dwidth/1.16,dheight/0.865)
                                        dcanvas.coords("naivlabel19",dwidth/1.16,dheight/0.835)
                                        dcanvas.coords("naivlabel20",dwidth/1.16,dheight/0.805)
                                        dcanvas.coords("naivlabel21",dwidth/1.16,dheight/0.785)

                                        dcanvas.coords("nline2",dwidth/2.95,dheight/0.759,dwidth/1.057,dheight/0.759)

                                        dcanvas.coords("naivtree1",dwidth/2.9,dheight/0.75)
                                        
                                        dcanvas.coords("nline3",dwidth/2.9,dheight/0.7,dwidth/1.062,dheight/0.7)
                                        dcanvas.coords("nline4",dwidth/2.9,dheight/0.67,dwidth/1.062,dheight/0.67)
                                        dcanvas.coords("nline5",dwidth/2.9,dheight/0.64,dwidth/1.062,dheight/0.64)
                                        dcanvas.coords("nline6",dwidth/2.9,dheight/0.61,dwidth/1.062,dheight/0.61)

                                        dcanvas.coords("naivtlabel1",dwidth/2.88,dheight/0.729)
                                        dcanvas.coords("naivtlabel2",dwidth/2.88,dheight/0.69)
                                        dcanvas.coords("naivtlabel3",dwidth/2.88,dheight/0.66)
                                        dcanvas.coords("naivtlabel4",dwidth/2.88,dheight/0.63)

                                        dcanvas.coords("naivtlabel5",dwidth/2.67,dheight/0.729)
                                        dcanvas.coords("naivtlabel6",dwidth/2.67,dheight/0.69)
                                        dcanvas.coords("naivtlabel7",dwidth/2.67,dheight/0.66)
                                        dcanvas.coords("naivtlabel8",dwidth/2.67,dheight/0.63)

                                        dcanvas.coords("naivtlabel9",dwidth/1.9,dheight/0.729)
                                        dcanvas.coords("naivtlabel10",dwidth/1.9,dheight/0.69)
                                        dcanvas.coords("naivtlabel11",dwidth/1.9,dheight/0.66)
                                        dcanvas.coords("naivtlabel12",dwidth/1.9,dheight/0.63)

                                        dcanvas.coords("naivtlabel13",dwidth/1.65,dheight/0.729)
                                        dcanvas.coords("naivtlabel14",dwidth/1.65,dheight/0.69)
                                        dcanvas.coords("naivtlabel15",dwidth/1.65,dheight/0.66)
                                        dcanvas.coords("naivtlabel16",dwidth/1.65,dheight/0.63)

                                        dcanvas.coords("naivtlabel17",dwidth/1.48,dheight/0.729)
                                        dcanvas.coords("naivtlabel18",dwidth/1.48,dheight/0.69)
                                        dcanvas.coords("naivtlabel19",dwidth/1.48,dheight/0.66)
                                        dcanvas.coords("naivtlabel20",dwidth/1.48,dheight/0.63)

                                        dcanvas.coords("naivtlabel21",dwidth/1.195,dheight/0.729)
                                        dcanvas.coords("naivtlabel22",dwidth/1.195,dheight/0.69)
                                        dcanvas.coords("naivtlabel23",dwidth/1.195,dheight/0.66)
                                        dcanvas.coords("naivtlabel24",dwidth/1.195,dheight/0.63)

                                        dcanvas.coords("naivtlabel25",dwidth/1.33,dheight/0.729)
                                        dcanvas.coords("naivtlabel26",dwidth/1.33,dheight/0.69)
                                        dcanvas.coords("naivtlabel27",dwidth/1.33,dheight/0.66)
                                        dcanvas.coords("naivtlabel28",dwidth/1.33,dheight/0.63)

                                        
                                        dcanvas.coords("naivlabel13",dwidth/1.47,dheight/0.59)
                                        dcanvas.coords("naivlabels13",dwidth/1.21,dheight/0.59)
                                        dcanvas.coords("naivlabel14",dwidth/1.47,dheight/0.565)
                                        dcanvas.coords("naivlabels14",dwidth/1.21,dheight/0.565)
                                        dcanvas.coords("naivlabel15",dwidth/1.47,dheight/0.54)
                                        dcanvas.coords("naivlabels15",dwidth/1.21,dheight/0.54)

                                        dcanvas.coords("naivlabels16",dwidth/2.5,dheight/0.50)
                                        dcanvas.coords("naivlabels17",dwidth/2.5,dheight/0.49)
                                        dcanvas.coords("naivlabels18",dwidth/2.5,dheight/0.48)
                                        dcanvas.coords("naivlabels19",dwidth/2.5,dheight/0.47)

                                        dcanvas.coords("naivline23",dwidth/2.6,dheight/0.4,dwidth/1.11,dheight/0.4)

                                        dcanvas.coords("naivlabel16",dwidth/2.52,dheight/0.395)

                                        dcanvas.coords("naivbutton3",dwidth/23,dheight/3.415)

                                    cs_canvas_1=Canvas(cs_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2000))

                                    cs_frame_1.grid_columnconfigure(0,weight=1)
                                    cs_frame_1.grid_rowconfigure(0,weight=1)

                                    
                                    vertibar=Scrollbar(cs_frame_1, orient=VERTICAL)
                                    vertibar.grid(row=0,column=1,sticky='ns')
                                    vertibar.config(command=cs_canvas_1.yview)

                                    cs_canvas_1.bind("<Configure>", cs_responsive_widgets_1)
                                    cs_canvas_1.config(yscrollcommand=vertibar.set)
                                    cs_canvas_1.grid(row=0,column=0,sticky='nsew')

                                    def einsert_data():
                                        name = ns_entry_1.get()
                                        # template = ns_entry_2.get()
                                        pcolour = ns_entry_3.get()
                                        scolour = ns_entry_4.get()
                                        fonts = ns_entry_5.get()
                                        lastedited = datetime.date.today()
                                        selected = ns_chk_str_1.get()

                                        usr_sql = "SELECT id FROM auth_user WHERE username=%s"
                                        usr_val = (nm_ent.get(),)
                                        fbcursor.execute(usr_sql,usr_val)
                                        usr_data = fbcursor.fetchone()

                                        cmp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                        cmp_val = (usr_data[0],)
                                        fbcursor.execute(cmp_sql,cmp_val)
                                        cmp_data = fbcursor.fetchone()
                                        cid = cmp_data[0]

                                        cs_sql_1 = "UPDATE  app1_customize set name=%s,pcolour=%s,scolour=%s,fonts=%s,lastedited=%s,selected=%s,cid_id=%s where name=%s"
                                        cs_val_1=(name,pcolour,scolour,fonts,lastedited,selected,cid,cs_id_1)
                                        fbcursor.execute(cs_sql_1,cs_val_1)
                                        finsysdb.commit()

                                        #----------Refresh Insert Tree--------#

                                        for record in cs_tree.get_children():
                                                cs_tree.delete(record)

                                        sql_pr="select * from auth_user where username=%s"
                                        sql_pr_val=(nm_ent.get(),)
                                        fbcursor.execute(sql_pr,sql_pr_val,)
                                        pr_dtl=fbcursor.fetchone()

                                        sql = "select * from app1_company where id_id=%s"
                                        val = (pr_dtl[0],)
                                        fbcursor.execute(sql, val,)
                                        cmp_dtl=fbcursor.fetchone()

                                        c_sql_1 = "SELECT * FROM app1_customize where selected=1 and cid_id=%s"
                                        c_val_1 = (cmp_dtl[0],)
                                        fbcursor.execute(c_sql_1,c_val_1,)
                                        cs_data_1 = fbcursor.fetchall()

                                        count0 = 0
                                        for i in cs_data_1:
                                            
                                            if True:
                                                cs_tree.insert(parent='',index='end',iid=i,text='',values=('',i[1],i[6],"APPLIED"))
                                            
                                        count0 += 1

                                        c_sql_1 = "SELECT * FROM app1_customize where selected=0 and cid_id=%s"
                                        c_val_1 = (cmp_dtl[0],)
                                        fbcursor.execute(c_sql_1,c_val_1,)
                                        cs_data_2 = fbcursor.fetchall()

                                        count0 = 0
                                        for i in cs_data_2:
                                            
                                            if True:
                                                cs_tree.insert(parent='',index='end',iid=i,text='',values=('',i[1],i[6],"NOT APPLIED"))
                                            
                                        count0 += 1

                                        cs_frame_1.destroy()
                                        cs_frame.grid(row=0,column=0,sticky='nsew')

                                        


                                    cs_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("nspoly1"))

                                    label_1 = Label(cs_canvas_1,width=20,height=1,text="CREATE FORM STYLES", font=('arial 20'),background="#1b3857",fg="white") 
                                    window_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("nslabel1"))

                                    cs_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("nshline"))

                                    cs_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("nspoly2"))

                                    label_1 = Label(cs_canvas_1,width=10,height=1,text="Form Name", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("nslabel2"))

                                    ns_entry_1=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white")
                                    window_ns_entry_1 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_1, tags=('nsentry1'))
                                    ns_entry_1.delete(0,"end")
                                    ns_entry_1.insert(0, e_dtl[1])


                                    ns_str = StringVar()
                                    ns_str.set("TAX INVOICE")
                                    ns_entry_6=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white",textvariable=ns_str)
                                    window_ns_entry_6 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_6, tags=('nsentry6'))

                                    ns_str_1 = StringVar()
                                    ns_str_1.set("Invoice No")
                                    ns_entry_7=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white",textvariable=ns_str_1)
                                    window_ns_entry_7 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_7, tags=('nsentry7'))

                                    ns_str_2 = StringVar()
                                    ns_str_2.set("Invoice Date")
                                    ns_entry_8=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white",textvariable=ns_str_2)
                                    window_ns_entry_8 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_8, tags=('nsentry8'))

                                    ns_str_3 = StringVar()
                                    ns_str_3.set("Due Date")
                                    ns_entry_9=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white",textvariable=ns_str_3)
                                    window_ns_entry_9 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_9, tags=('nsentry9'))

                                    ns_str_4 = StringVar()
                                    ns_str_4.set("Terms")
                                    ns_entry_10=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white",textvariable=ns_str_4)
                                    window_ns_entry_10 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_10, tags=('nsentry10'))

                                    label_1 = Label(cs_canvas_1,width=30,height=1,text="Customize Invoice text labels", font=('arial 12'),background="#1b3857",fg="white", anchor="w") 
                                    window_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("nslabel3"))


                                    

                                    label_1 = Label(cs_canvas_1,width=16,height=1,text="Primary Colours", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("nslabel4"))

                                    def color_1_1():
                                        ns_entry_3.delete(0,"end")
                                        ns_entry_3.insert(0, "#E9967A")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        c_label_7.config(fg="#E9967A")
                                        # else:
                                        #     pass

                                    
                                    def color_1_2():
                                        ns_entry_3.delete(0,"end")
                                        ns_entry_3.insert(0, "#8FBC8F")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        c_label_7.config(fg="#8FBC8F")
                                        # else:
                                        #     pass
                                    
                                    def color_1_3():
                                        ns_entry_3.delete(0,"end")
                                        ns_entry_3.insert(0, "#B0C4DE")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        c_label_7.config(fg="#B0C4DE")
                                        # else:
                                        #     pass

                                    def color_1_4():
                                        ns_entry_3.delete(0,"end")
                                        ns_entry_3.insert(0, "#87CEFA")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        c_label_7.config(fg="#87CEFA")
                                        # else:
                                        #     pass

                                    def color_1_5():
                                        ns_entry_3.delete(0,"end")
                                        ns_entry_3.insert(0, "#F0E68C")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        c_label_7.config(fg="#F0E68C")
                                        # else:
                                        #     pass
                                    
                                    def color_1_6():
                                        ns_entry_3.delete(0,"end")
                                        ns_entry_3.insert(0, "#DDA0DD")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        c_label_7.config(fg="#DDA0DD")
                                        # else:
                                        #     pass

                                    def color_1_7():
                                        ns_entry_3.delete(0,"end")
                                        ns_entry_3.insert(0, "#2F4F4F")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        c_label_7.config(fg="#2F4F4F")
                                        # else:
                                        #     pass

                                    def color_1_8():
                                        ns_entry_3.delete(0,"end")
                                        ns_entry_3.insert(0, "#98FB98")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        c_label_7.config(fg="#98FB98")
                                        # else:
                                        #     pass
                                    
                                    def color_1_9():
                                        ns_entry_3.delete(0,"end")
                                        ns_entry_3.insert(0, "#DB7093")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        c_label_7.config(fg="#DB7093")
                                        # else:
                                        #     pass

                                    def color_1_10():
                                        ns_entry_3.delete(0,"end")
                                        ns_entry_3.insert(0, "#D2B48C")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        c_label_7.config(fg="#D2B48C")
                                        # else:
                                        #     pass
                                    
                                    def color_1_11():
                                        ns_entry_3.delete(0,"end")
                                        ns_entry_3.insert(0, "#D3D3D3")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        c_label_7.config(fg="#D3D3D3")
                                        # else:
                                        #     pass
                                    
                                    def color_1_12():
                                        ns_entry_3.delete(0,"end")
                                        ns_entry_3.insert(0, "#F5F5F5")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        c_label_7.config(fg="#F5F5F5")
                                        # else:
                                        #     pass


                                    ns_entry_3=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white")
                                    window_ns_entry_3 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_3, tags=('nsentry3'))
                                    ns_entry_3.delete(0,"end")
                                    ns_entry_3.insert(0, e_dtl[3])

                                    ns_btn5=Button(cs_canvas_1, width=5,height=2, activebackground="#E9967A",background="#E9967A",font='arial 12',command=color_1_1)
                                    window_ns_btn5 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn5, tags=("nsbutton8"))

                                    ns_btn6=Button(cs_canvas_1, width=5,height=2, activebackground="#8FBC8F",background="#8FBC8F",font='arial 12',command=color_1_2)
                                    window_ns_btn6 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn6, tags=("nsbutton9"))

                                    ns_btn7=Button(cs_canvas_1, width=5,height=2, activebackground="#B0C4DE",background="#B0C4DE",font='arial 12',command=color_1_3)
                                    window_ns_btn7 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn7, tags=("nsbutton10"))

                                    ns_btn8=Button(cs_canvas_1, width=5,height=2, activebackground="#87CEFA",background="#87CEFA",font='arial 12',command=color_1_4)
                                    window_ns_btn8 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn8, tags=("nsbutton11"))

                                    ns_btn9=Button(cs_canvas_1, width=5,height=2, activebackground="#F0E68C",background="#F0E68C",font='arial 12',command=color_1_5)
                                    window_ns_btn9 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn9, tags=("nsbutton12"))

                                    ns_btn10=Button(cs_canvas_1, width=5,height=2, activebackground="#DDA0DD",background="#DDA0DD",font='arial 12',command=color_1_6)
                                    window_ns_btn10 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn10, tags=("nsbutton13"))

                                    ns_btn11=Button(cs_canvas_1, width=5,height=2, activebackground="#2F4F4F",background="#2F4F4F",font='arial 12',command=color_1_7)
                                    window_ns_btn11 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn11, tags=("nsbutton14"))

                                    ns_btn12=Button(cs_canvas_1, width=5,height=2, activebackground="#98FB98",background="#98FB98",font='arial 12',command=color_1_8)
                                    window_ns_btn12 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn12, tags=("nsbutton15"))

                                    ns_btn13=Button(cs_canvas_1, width=5,height=2, activebackground="#DB7093",background="#DB7093",font='arial 12',command=color_1_9)
                                    window_ns_btn13 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn13, tags=("nsbutton16"))

                                    ns_btn14=Button(cs_canvas_1, width=5,height=2, activebackground="#D2B48C",background="#D2B48C",font='arial 12',command=color_1_10)
                                    window_ns_btn14 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn14, tags=("nsbutton17"))

                                    ns_btn15=Button(cs_canvas_1, width=5,height=2, activebackground="#D3D3D3",background="#D3D3D3",font='arial 12',command=color_1_11)
                                    window_ns_btn15 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn15, tags=("nsbutton18"))

                                    ns_btn16=Button(cs_canvas_1, width=5,height=2, activebackground="#F5F5F5",background="#F5F5F5",font='arial 12',command=color_1_12)
                                    window_ns_btn16 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn16, tags=("nsbutton19"))

                                    label_1 = Label(cs_canvas_1,width=18,height=1,text="Secondary Colours", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("nslabel5"))

                                    def color_2_1():
                                        ns_entry_4.delete(0,"end")
                                        ns_entry_4.insert(0, "#E9967A")
                                    
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        fgthvi_1.configure('mystyle10.Treeview.Heading', background='#E9967A',State='DISABLE',foreground='black')
                                        # else:
                                        #     pass

                                        
                                    
                                    def color_2_2():
                                        ns_entry_4.delete(0,"end")
                                        ns_entry_4.insert(0, "#8FBC8F")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        fgthvi_1.configure('mystyle10.Treeview.Heading', background='#8FBC8F',State='DISABLE',foreground='black')
                                        # else:
                                        #     pass

                                       
                                    def color_2_3():
                                        ns_entry_4.delete(0,"end")
                                        ns_entry_4.insert(0, "#B0C4DE")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        fgthvi_1.configure('mystyle10.Treeview.Heading', background='#B0C4DE',State='DISABLE',foreground='black')
                                        # else:
                                        #     pass

                                        

                                    def color_2_4():
                                        ns_entry_4.delete(0,"end")
                                        ns_entry_4.insert(0, "#87CEFA")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        fgthvi_1.configure('mystyle10.Treeview.Heading', background='#87CEFA',State='DISABLE',foreground='black')
                                        # else:
                                        #     pass

                                        

                                    def color_2_5():
                                        ns_entry_4.delete(0,"end")
                                        ns_entry_4.insert(0, "#F0E68C")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        fgthvi_1.configure('mystyle10.Treeview.Heading', background='#F0E68C',State='DISABLE',foreground='black')
                                        # else:
                                        #     pass

                                        
                                    
                                    def color_2_6():
                                        ns_entry_4.delete(0,"end")
                                        ns_entry_4.insert(0, "#DDA0DD")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        fgthvi_1.configure('mystyle10.Treeview.Heading', background='#DDA0DD',State='DISABLE',foreground='black')
                                        # else:
                                        #     pass

                                        

                                    def color_2_7():
                                        ns_entry_4.delete(0,"end")
                                        ns_entry_4.insert(0, "#2F4F4F")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        fgthvi_1.configure('mystyle10.Treeview.Heading', background='#2F4F4F',State='DISABLE',foreground='black')
                                        # else:
                                        #     pass

                                        

                                    def color_2_8():
                                        ns_entry_4.delete(0,"end")
                                        ns_entry_4.insert(0, "#98FB98")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        fgthvi_1.configure('mystyle10.Treeview.Heading', background='#98FB98',State='DISABLE',foreground='black')
                                        # else:
                                        #     pass

                                        
                                    
                                    def color_2_9():
                                        ns_entry_4.delete(0,"end")
                                        ns_entry_4.insert(0, "#DB7093")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        fgthvi_1.configure('mystyle10.Treeview.Heading', background='#DB7093',State='DISABLE',foreground='black')
                                        # else:
                                        #     pass

                                        

                                    def color_2_10():
                                        ns_entry_4.delete(0,"end")
                                        ns_entry_4.insert(0, "#D2B48C")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        fgthvi_1.configure('mystyle10.Treeview.Heading', background='#D2B48C',State='DISABLE',foreground='black')
                                        # else:
                                        #     pass

                                        
                                    
                                    def color_2_11():
                                        ns_entry_4.delete(0,"end")
                                        ns_entry_4.insert(0, "#D3D3D3")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        fgthvi_1.configure('mystyle10.Treeview.Heading', background='#D3D3D3',State='DISABLE',foreground='black')
                                        # else:
                                        #     pass

                                        
                                    def color_2_12():
                                        ns_entry_4.delete(0,"end")
                                        ns_entry_4.insert(0, "#F5F5F5")
                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        fgthvi_1.configure('mystyle10.Treeview.Heading', background='#F5F5F5',State='DISABLE',foreground='black')
                                        # else:
                                        #     pass

                                        
                                    ns_entry_4=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white")
                                    window_ns_entry_4 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_4, tags=('nsentry4'))
                                    ns_entry_4.delete(0,"end")
                                    ns_entry_4.insert(0, e_dtl[4])

                                    ns_btn17=Button(cs_canvas_1, width=5,height=2, activebackground="#E9967A",background="#E9967A",font='arial 12',command=color_2_1)
                                    window_ns_btn17 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn17, tags=("nsbutton20"))

                                    ns_btn18=Button(cs_canvas_1, width=5,height=2, activebackground="#8FBC8F",background="#8FBC8F",font='arial 12',command=color_2_2)
                                    window_ns_btn18 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn18, tags=("nsbutton21"))

                                    ns_btn19=Button(cs_canvas_1, width=5,height=2, activebackground="#B0C4DE",background="#B0C4DE",font='arial 12',command=color_2_3)
                                    window_ns_btn19 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn19, tags=("nsbutton22"))

                                    ns_btn20=Button(cs_canvas_1, width=5,height=2, activebackground="#87CEFA",background="#87CEFA",font='arial 12',command=color_2_4)
                                    window_ns_btn20 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn20, tags=("nsbutton23"))

                                    ns_btn21=Button(cs_canvas_1, width=5,height=2, activebackground="#F0E68C",background="#F0E68C",font='arial 12',command=color_2_5)
                                    window_ns_btn21 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn21, tags=("nsbutton24"))

                                    ns_btn22=Button(cs_canvas_1, width=5,height=2, activebackground="#DDA0DD",background="#DDA0DD",font='arial 12',command=color_2_6)
                                    window_ns_btn22 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn22, tags=("nsbutton25"))

                                    ns_btn23=Button(cs_canvas_1, width=5,height=2, activebackground="#2F4F4F",background="#2F4F4F",font='arial 12',command=color_2_7)
                                    window_ns_btn23 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn23, tags=("nsbutton26"))

                                    ns_btn24=Button(cs_canvas_1, width=5,height=2, activebackground="#98FB98",background="#98FB98",font='arial 12',command=color_2_8)
                                    window_ns_btn24 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn24, tags=("nsbutton27"))

                                    ns_btn25=Button(cs_canvas_1, width=5,height=2, activebackground="#DB7093",background="#DB7093",font='arial 12',command=color_2_9)
                                    window_ns_btn25 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn25, tags=("nsbutton28"))

                                    ns_btn26=Button(cs_canvas_1, width=5,height=2, activebackground="#D2B48C",background="#D2B48C",font='arial 12',command=color_2_10)
                                    window_ns_btn26 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn26, tags=("nsbutton29"))

                                    ns_btn27=Button(cs_canvas_1, width=5,height=2, activebackground="#D3D3D3",background="#D3D3D3",font='arial 12',command=color_2_11)
                                    window_ns_btn27 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn27, tags=("nsbutton30"))

                                    ns_btn28=Button(cs_canvas_1, width=5,height=2, activebackground="#F5F5F5",background="#F5F5F5",font='arial 12',command=color_2_12)
                                    window_ns_btn28 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn28, tags=("nsbutton31"))

                                    label_1 = Label(cs_canvas_1,width=14,height=1,text="Try New Fonts", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("nslabel6"))

                                    def Serif():
                                        ns_entry_5.delete(0,"end")
                                        ns_entry_5.insert(0, "Serif Serif font")

                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        #     print('wow')
                                        c_label_1.config(font=('Garamond bold',12))
                                        c_label_2.config(font=('Garamond',12))
                                        c_label_3.config(font=('Garamond',12))
                                        c_label_4.config(font=('Garamond',12))
                                        c_label_5.config(font=('Garamond',12))
                                        c_label_6.config(font=('Garamond',12))
                                        c_label_7.config(font=('Garamond bold',20))
                                        c_label_8.config(font=('Garamond bold',14))
                                        c_label_9.config(font=('Garamond',12))
                                        c_label_10.config(font=('Garamond bold',12))
                                        c_label_11.config(font=('Garamond',12))
                                        c_label_12.config(font=('Garamond bold',12))
                                        c_label_13.config(font=('Garamond',12))
                                        c_label_14.config(font=('Garamond bold',12))
                                        c_label_15.config(font=('Garamond',12))
                                        c_label_16.config(font=('Garamond bold',12))
                                        c_label_17.config(font=('Garamond',12))
                                        c_label_18.config(font=('Garamond bold',12))
                                        c_label_19.config(font=('Garamond bold',12))
                                        c_label_20.config(font=('Garamond bold',12))
                                        c_label_21.config(font=('Garamond bold',12))
                                        c_label_22.config(font=('Garamond bold',12))
                                        c_label_23.config(font=('Garamond bold',12))
                                        c_label_24.config(font=('Garamond',12))
                                        c_label_25.config(font=('Garamond',12))
                                        c_label_26.config(font=('Garamond',12))
                                        c_label_27.config(font=('Garamond',12))
                                        c_label_28.config(font=('Garamond',12))
                                        c_label_29.config(font=('Garamond',12))
                                        c_label_30.config(font=('Garamond',12))
                                        c_label_31.config(font=('Garamond',12))
                                        c_label_32.config(font=('Garamond',12))
                                        c_label_33.config(font=('Garamond',12))
                                        c_label_34.config(font=('Garamond',12))
                                        c_label_35.config(font=('Garamond',12))
                                        c_label_36.config(font=('Garamond',12))
                                        c_label_37.config(font=('Garamond',12))
                                        c_label_38.config(font=('Garamond',12))
                                        c_label_39.config(font=('Garamond',12))
                                        c_label_40.config(font=('Garamond',12))
                                        c_label_41.config(font=('Garamond',12))
                                        c_label_42.config(font=('Garamond',12))
                                        c_label_43.config(font=('Garamond',12))
                                        c_label_44.config(font=('Garamond',12))
                                        c_label_45.config(font=('Garamond',12))
                                        c_label_46.config(font=('Garamond',12))
                                        c_label_47.config(font=('Garamond',12))
                                        c_label_48.config(font=('Garamond',12))
                                        c_label_49.config(font=('Garamond',12))
                                        c_label_50.config(font=('Garamond',12))
                                        c_label_51.config(font=('Garamond',12))
                                        c_label_52.config(font=('Garamond',12))
                                        c_label_53.config(font=('Garamond bold',12))
                                        c_label_54.config(font=('Garamond',12))
                                        c_label_55.config(font=('Garamond',12))
                                        c_label_56.config(font=('Garamond',12))
                                        
                                    

                                    def Sans():
                                        ns_entry_5.delete(0,"end")
                                        ns_entry_5.insert(0, "Sans-serif Sans-serif font")

                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        #     print('wow')
                                        c_label_1.config(font=('Arial bold',12))
                                        c_label_2.config(font=('Arial',12))
                                        c_label_3.config(font=('Arial',12))
                                        c_label_4.config(font=('Arial',12))
                                        c_label_5.config(font=('Arial',12))
                                        c_label_6.config(font=('Arial',12))
                                        c_label_7.config(font=('Arial bold',20))
                                        c_label_8.config(font=('Arial bold',14))
                                        c_label_9.config(font=('Arial',12))
                                        c_label_10.config(font=('Arial bold',12))
                                        c_label_11.config(font=('Arial',12))
                                        c_label_12.config(font=('Arial bold',12))
                                        c_label_13.config(font=('Arial',12))
                                        c_label_14.config(font=('Arial bold',12))
                                        c_label_15.config(font=('Arial',12))
                                        c_label_16.config(font=('Arial bold',12))
                                        c_label_17.config(font=('Arial',12))
                                        c_label_18.config(font=('Arial bold',12))
                                        c_label_19.config(font=('Arial bold',12))
                                        c_label_20.config(font=('Arial bold',12))
                                        c_label_21.config(font=('Arial bold',12))
                                        c_label_22.config(font=('Arial bold',12))
                                        c_label_23.config(font=('Arial bold',12))
                                        c_label_24.config(font=('Arial',12))
                                        c_label_25.config(font=('Arial',12))
                                        c_label_26.config(font=('Arial',12))
                                        c_label_27.config(font=('Arial',12))
                                        c_label_28.config(font=('Arial',12))
                                        c_label_29.config(font=('Arial',12))
                                        c_label_30.config(font=('Arial',12))
                                        c_label_31.config(font=('Arial',12))
                                        c_label_32.config(font=('Arial',12))
                                        c_label_33.config(font=('Arial',12))
                                        c_label_34.config(font=('Arial',12))
                                        c_label_35.config(font=('Arial',12))
                                        c_label_36.config(font=('Arial',12))
                                        c_label_37.config(font=('Arial',12))
                                        c_label_38.config(font=('Arial',12))
                                        c_label_39.config(font=('Arial',12))
                                        c_label_40.config(font=('Arial',12))
                                        c_label_41.config(font=('Arial',12))
                                        c_label_42.config(font=('Arial',12))
                                        c_label_43.config(font=('Arial',12))
                                        c_label_44.config(font=('Arial',12))
                                        c_label_45.config(font=('Arial',12))
                                        c_label_46.config(font=('Arial',12))
                                        c_label_47.config(font=('Arial',12))
                                        c_label_48.config(font=('Arial',12))
                                        c_label_49.config(font=('Arial',12))
                                        c_label_50.config(font=('Arial',12))
                                        c_label_51.config(font=('Arial',12))
                                        c_label_52.config(font=('Arial',12))
                                        c_label_53.config(font=('Arial bold',12))
                                        c_label_54.config(font=('Arial',12))
                                        c_label_55.config(font=('Arial',12))
                                        c_label_56.config(font=('Arial',12))

                                        
                                    

                                    def Monospace():
                                        ns_entry_5.delete(0,"end")
                                        ns_entry_5.insert(0, "Monospace Monospace font")

                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        #     print('wow')
                                        c_label_1.config(font=('Helvetica bold',12))
                                        c_label_2.config(font=('Helvetica',12))
                                        c_label_3.config(font=('Helvetica',12))
                                        c_label_4.config(font=('Helvetica',12))
                                        c_label_5.config(font=('Helvetica',12))
                                        c_label_6.config(font=('Helvetica',12))
                                        c_label_7.config(font=('Helvetica bold',20))
                                        c_label_8.config(font=('Helvetica bold',14))
                                        c_label_9.config(font=('Helvetica',12))
                                        c_label_10.config(font=('Helvetica bold',12))
                                        c_label_11.config(font=('Helvetica',12))
                                        c_label_12.config(font=('Helvetica bold',12))
                                        c_label_13.config(font=('Helvetica',12))
                                        c_label_14.config(font=('Helvetica bold',12))
                                        c_label_15.config(font=('Helvetica',12))
                                        c_label_16.config(font=('Helvetica bold',12))
                                        c_label_17.config(font=('Helvetica',12))
                                        c_label_18.config(font=('Helvetica bold',12))
                                        c_label_19.config(font=('Helvetica bold',12))
                                        c_label_20.config(font=('Helvetica bold',12))
                                        c_label_21.config(font=('Helvetica bold',12))
                                        c_label_22.config(font=('Helvetica bold',12))
                                        c_label_23.config(font=('Helvetica bold',12))
                                        c_label_24.config(font=('Helvetica',12))
                                        c_label_25.config(font=('Helvetica',12))
                                        c_label_26.config(font=('Helvetica',12))
                                        c_label_27.config(font=('Helvetica',12))
                                        c_label_28.config(font=('Helvetica',12))
                                        c_label_29.config(font=('Helvetica',12))
                                        c_label_30.config(font=('Helvetica',12))
                                        c_label_31.config(font=('Helvetica',12))
                                        c_label_32.config(font=('Helvetica',12))
                                        c_label_33.config(font=('Helvetica',12))
                                        c_label_34.config(font=('Helvetica',12))
                                        c_label_35.config(font=('Helvetica',12))
                                        c_label_36.config(font=('Helvetica',12))
                                        c_label_37.config(font=('Helvetica',12))
                                        c_label_38.config(font=('Helvetica',12))
                                        c_label_39.config(font=('Helvetica',12))
                                        c_label_40.config(font=('Helvetica',12))
                                        c_label_41.config(font=('Helvetica',12))
                                        c_label_42.config(font=('Helvetica',12))
                                        c_label_43.config(font=('Helvetica',12))
                                        c_label_44.config(font=('Helvetica',12))
                                        c_label_45.config(font=('Helvetica',12))
                                        c_label_46.config(font=('Helvetica',12))
                                        c_label_47.config(font=('Helvetica',12))
                                        c_label_48.config(font=('Helvetica',12))
                                        c_label_49.config(font=('Helvetica',12))
                                        c_label_50.config(font=('Helvetica',12))
                                        c_label_51.config(font=('Helvetica',12))
                                        c_label_52.config(font=('Helvetica',12))
                                        c_label_53.config(font=('Helvetica bold',12))
                                        c_label_54.config(font=('Helvetica',12))
                                        c_label_55.config(font=('Helvetica',12))
                                        c_label_56.config(font=('Helvetica',12))

                                        
                                    

                                    def System():
                                        ns_entry_5.delete(0,"end")
                                        ns_entry_5.insert(0, "System-ui System-ui font")

                                        # #----------------------------------------Classic-----------------------------------------

                                        # if ns_entry_2.get()=="Classic":
                                        #     print('wow')
                                        c_label_1.config(font=('Roboto bold',12))
                                        c_label_2.config(font=('Roboto',12))
                                        c_label_3.config(font=('Roboto',12))
                                        c_label_4.config(font=('Roboto',12))
                                        c_label_5.config(font=('Roboto',12))
                                        c_label_6.config(font=('Roboto',12))
                                        c_label_7.config(font=('Roboto bold',20))
                                        c_label_8.config(font=('Roboto bold',14))
                                        c_label_9.config(font=('Roboto',12))
                                        c_label_10.config(font=('Roboto bold',12))
                                        c_label_11.config(font=('Roboto',12))
                                        c_label_12.config(font=('Roboto bold',12))
                                        c_label_13.config(font=('Roboto',12))
                                        c_label_14.config(font=('Roboto bold',12))
                                        c_label_15.config(font=('Roboto',12))
                                        c_label_16.config(font=('Roboto bold',12))
                                        c_label_17.config(font=('Roboto',12))
                                        c_label_18.config(font=('Roboto bold',12))
                                        c_label_19.config(font=('Roboto bold',12))
                                        c_label_20.config(font=('Roboto bold',12))
                                        c_label_21.config(font=('Roboto bold',12))
                                        c_label_22.config(font=('Roboto bold',12))
                                        c_label_23.config(font=('Roboto bold',12))
                                        c_label_24.config(font=('Roboto',12))
                                        c_label_25.config(font=('Roboto',12))
                                        c_label_26.config(font=('Roboto',12))
                                        c_label_27.config(font=('Roboto',12))
                                        c_label_28.config(font=('Roboto',12))
                                        c_label_29.config(font=('Roboto',12))
                                        c_label_30.config(font=('Roboto',12))
                                        c_label_31.config(font=('Roboto',12))
                                        c_label_32.config(font=('Roboto',12))
                                        c_label_33.config(font=('Roboto',12))
                                        c_label_34.config(font=('Roboto',12))
                                        c_label_35.config(font=('Roboto',12))
                                        c_label_36.config(font=('Roboto',12))
                                        c_label_37.config(font=('Roboto',12))
                                        c_label_38.config(font=('Roboto',12))
                                        c_label_39.config(font=('Roboto',12))
                                        c_label_40.config(font=('Roboto',12))
                                        c_label_41.config(font=('Roboto',12))
                                        c_label_42.config(font=('Roboto',12))
                                        c_label_43.config(font=('Roboto',12))
                                        c_label_44.config(font=('Roboto',12))
                                        c_label_45.config(font=('Roboto',12))
                                        c_label_46.config(font=('Roboto',12))
                                        c_label_47.config(font=('Roboto',12))
                                        c_label_48.config(font=('Roboto',12))
                                        c_label_49.config(font=('Roboto',12))
                                        c_label_50.config(font=('Roboto',12))
                                        c_label_51.config(font=('Roboto',12))
                                        c_label_52.config(font=('Roboto',12))
                                        c_label_53.config(font=('Roboto bold',12))
                                        c_label_54.config(font=('Roboto',12))
                                        c_label_55.config(font=('Roboto',12))
                                        c_label_56.config(font=('Roboto',12))

                                    

                                    ns_entry_5=Entry(cs_canvas_1,width=52,justify=LEFT,background='#2f516f',foreground="white")
                                    window_ns_entry_5 = cs_canvas_1.create_window(0, 0, anchor="nw", height=30,window=ns_entry_5, tags=('nsentry5'))
                                    ns_entry_5.delete(0,"end")
                                    ns_entry_5.insert(0, e_dtl[5])
                                    
                                    ns_btn29=Button(cs_canvas_1,text='Serif\nSerif font', width=15,height=4,foreground="white",background="#1b3857",font='arial 12',command=Serif)
                                    window_ns_btn29 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn29, tags=("nsbutton32"))

                                    ns_btn30=Button(cs_canvas_1,text='Sans-serif\nSans-serif font', width=15,height=4,foreground="white",background="#1b3857",font='arial 12',command=Sans)
                                    window_ns_btn30 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn30, tags=("nsbutton33"))

                                    ns_btn31=Button(cs_canvas_1,text='Monospace\nMonospace font', width=15,height=4,foreground="white",background="#1b3857",font='arial 12',command=Monospace)
                                    window_ns_btn31 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn31, tags=("nsbutton34"))

                                    ns_btn32=Button(cs_canvas_1,text='System-ui\nSystem-ui font', width=15,height=4,foreground="white",background="#1b3857",font='arial 12',command=System)
                                    window_ns_btn32 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_btn32, tags=("nsbutton35"))

                                    ns_chk_str_1 = BooleanVar()
                                    ns_chkbtn2 = Checkbutton(cs_canvas_1, text = "Apply this theme", variable = ns_chk_str_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                                    window_ns_chkbtn2 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_chkbtn2,tags=("nscheck1"))

                                    #----------------------------------------Template 1-----------------------------------------

                                    sql_u = 'select * from auth_user where username=%s'
                                    val_u = (nm_ent.get(),)
                                    fbcursor.execute(sql_u,val_u)
                                    u_dtl = fbcursor.fetchone()

                                    sql = "select * from app1_company where id_id=%s"
                                    val = (u_dtl[0],)
                                    fbcursor.execute(sql, val,)
                                    cmp_dtl=fbcursor.fetchone()
                                    

                                    sql = 'select * from app1_invoice where cid_id=%s'
                                    val =  (cmp_dtl[0],)
                                    fbcursor.execute(sql,val,)
                                    cl_view = fbcursor.fetchone()

                                    cs_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="white",tags=("nspoly3"))


                                    c_label_1 = Label(cs_canvas_1,width=12,height=1,text=cmp_dtl[1], font=('arial 14 bold'),background="white",fg="skyblue",anchor="w") 
                                    window_c_label_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_1, tags=("naivlabel1"))

                                    c_label_2 = Label(cs_canvas_1,width=15,height=1,text=cmp_dtl[2], font=('arial 12 '),background="white",fg="black",anchor="w") 
                                    window_c_label_2 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_2, tags=("naivlabel2"))

                                    c_label_3 = Label(cs_canvas_1,width=15,height=1,text=cmp_dtl[3]+","+cmp_dtl[4], font=('arial 12 '),background="white",fg="black",anchor="w") 
                                    window_c_label_3 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_3, tags=("naivlabel3"))

                                    c_label_4 = Label(cs_canvas_1,width=15,height=1,text=cmp_dtl[5], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_4 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_4, tags=("naivlabel4"))

                                    c_label_5 = Label(cs_canvas_1,width=15,height=1,text=cmp_dtl[6], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_5 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_5, tags=("naivlabel5"))

                                    c_label_6 = Label(cs_canvas_1,width=10,height=1,text=cmp_dtl[7], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_6 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_6, tags=("naivlabel6"))

                                    c_label_7 = Label(cs_canvas_1,width=20,height=1,text=""+ns_entry_6.get(), font=('arial 20 bold'),background="white",fg="skyblue",anchor="w") 
                                    window_c_label_7 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_7, tags=("naivlabel7"))


                                    cs_image_1=Label(cs_canvas_1,  image = prof_pics,bg="#213b52",width=200,height=150,  anchor="center",font=('Calibri 14 bold'))
                                    win_cs_image_1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=cs_image_1,tags=("nimage1"))

                                    c_label_8 = Label(cs_canvas_1,width=15,height=1,text="Bill To", font=('arial 14 bold'),background="white",fg="black") 
                                    window_c_label_8 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_8, tags=("naivlabel8"))

                                    c_label_9 = Label(cs_canvas_1,width=20,height=8,text=cl_view[7], font=('arial 12'),background="white",fg="black",anchor="w") 
                                    window_c_label_9 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_9, tags=("naivlabel17"))

                                    cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('nline1'))


                                    c_label_10 = Label(cs_canvas_1,width=11,height=1,text=""+ns_entry_7.get(), font=('arial 12 bold'),background="white",fg="black",anchor="w") 
                                    window_c_label_10 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_10, tags=("naivlabel9"))

                                    c_label_11 = Label(cs_canvas_1,width=11,height=1,text=cl_view[3], font=('arial 12'),background="white",fg="black",anchor="w") 
                                    window_c_label_11 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_11, tags=("naivlabel18"))

                                    c_label_12 = Label(cs_canvas_1,width=11,height=1,text=""+ns_entry_8.get(), font=('arial 12 bold'),background="white",fg="black",anchor="w") 
                                    window_c_label_12 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_12, tags=("naivlabel10"))

                                    c_label_13 = Label(cs_canvas_1,width=10,height=1,text=cl_view[5], font=('arial 12'),background="white",fg="black",anchor="w") 
                                    window_c_label_13 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_13, tags=("naivlabel19"))

                                    c_label_14 = Label(cs_canvas_1,width=11,height=1,text=""+ns_entry_9.get(), font=('arial 12 bold'),background="white",fg="black",anchor="w") 
                                    window_c_label_14 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_14, tags=("naivlabel11"))

                                    c_label_15 = Label(cs_canvas_1,width=10,height=1,text=cl_view[6], font=('arial 12'),background="white",fg="black",anchor="w") 
                                    window_c_label_15 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_15, tags=("naivlabel20"))

                                    c_label_16 = Label(cs_canvas_1,width=11,height=1,text=""+ns_entry_10.get(), font=('arial 12 bold'),background="white",fg="black",anchor="w") 
                                    window_c_label_16 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_16, tags=("naivlabel12"))

                                    cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('nline2'))
                                    

                                    c_label_17 = Label(cs_canvas_1,width=10,height=1,text=cl_view[4], font=('arial 12'),background="white",fg="black",anchor="w") 
                                    window_c_label_17 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_17, tags=("naivlabel21"))

                                    fgthvi_1 = ttk.Style()
                                    fgthvi_1.theme_use("default")
                                    fgthvi_1.configure('mystyle10.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                                    fgthvi_1.configure('mystyle10.Treeview.Heading', background='skyblue',State='DISABLE',foreground='black')

                                    nsview_tree = ttk.Treeview(cs_canvas_1, columns = (1,2,3,4,5,6,7), height = 0, show = "headings",style='mystyle10.Treeview')
                                    nsview_tree.pack(side = 'top')
                                    nsview_tree.heading(1)
                                    nsview_tree.heading(2, text="PRODUCT/SERVICES")
                                    nsview_tree.heading(3, text="HSN")
                                    nsview_tree.heading(4, text="QTY")
                                    nsview_tree.heading(5, text="PRICE")
                                    nsview_tree.heading(6, text="TOTAL")
                                    nsview_tree.heading(7, text="TAX(%)")
                                    
                                    nsview_tree.column(1, width = 30)
                                    nsview_tree.column(2, width = 200)
                                    nsview_tree.column(3, width = 110)
                                    nsview_tree.column(4, width = 90)
                                    nsview_tree.column(5, width = 105)
                                    nsview_tree.column(6, width = 105)
                                    nsview_tree.column(7, width = 155)

                                    window = cs_canvas_1.create_window(0, 0, anchor="nw", height=0, window=nsview_tree,tags=('naivtree1'))

                                    cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('nline3'))
                                    cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('nline4'))
                                    cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('nline5'))
                                    cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('nline6'))
                                    

                                    c_label_25 = Label(cs_canvas_1,width=1,height=1,text="1", font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_25 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_25, tags=("naivtlabel1"))

                                    c_label_26 = Label(cs_canvas_1,width=1,height=1,text="2", font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_26 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_26, tags=("naivtlabel2"))

                                    c_label_27 = Label(cs_canvas_1,width=1,height=1,text="3", font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_27 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_27, tags=("naivtlabel3"))

                                    c_label_28 = Label(cs_canvas_1,width=1,height=1,text="4", font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_28 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_28, tags=("naivtlabel4"))

                                    c_label_29 = Label(cs_canvas_1,width=8,height=1,text=cl_view[9], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_29 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_29, tags=("naivtlabel5"))

                                    c_label_30 = Label(cs_canvas_1,width=8,height=1,text=cl_view[18], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_30 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_30, tags=("naivtlabel6"))

                                    c_label_31 = Label(cs_canvas_1,width=8,height=1,text=cl_view[25], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_31 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_31, tags=("naivtlabel7"))

                                    c_label_32 = Label(cs_canvas_1,width=8,height=1,text=cl_view[32], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_32 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_32, tags=("naivtlabel8"))

                                    c_label_33 = Label(cs_canvas_1,width=8,height=1,text=cl_view[10], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_33 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_33, tags=("naivtlabel9"))

                                    c_label_34 = Label(cs_canvas_1,width=8,height=1,text=cl_view[19], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_34 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_34, tags=("naivtlabel10"))

                                    c_label_35 = Label(cs_canvas_1,width=8,height=1,text=cl_view[26], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_35 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_35, tags=("naivtlabel11"))

                                    c_label_36 = Label(cs_canvas_1,width=8,height=1,text=cl_view[33], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_36 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_36, tags=("naivtlabel12"))

                                    c_label_37 = Label(cs_canvas_1,width=2,height=1,text=cl_view[12], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_37 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_37, tags=("naivtlabel13"))

                                    c_label_38 = Label(cs_canvas_1,width=2,height=1,text=cl_view[21], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_38 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_38, tags=("naivtlabel14"))

                                    c_label_39 = Label(cs_canvas_1,width=2,height=1,text=cl_view[28], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_39 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_39, tags=("naivtlabel15"))

                                    c_label_40 = Label(cs_canvas_1,width=2,height=1,text=cl_view[35], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_40 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_40, tags=("naivtlabel16"))

                                    c_label_41 = Label(cs_canvas_1,width=7,height=1,text=cl_view[13], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_41 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_41, tags=("naivtlabel25"))

                                    c_label_42 = Label(cs_canvas_1,width=7,height=1,text=cl_view[22], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_42 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_42, tags=("naivtlabel26"))

                                    c_label_43 = Label(cs_canvas_1,width=7,height=1,text=cl_view[29], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_43 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_43, tags=("naivtlabel27"))

                                    c_label_44 = Label(cs_canvas_1,width=7,height=1,text=cl_view[36], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_44 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_44, tags=("naivtlabel28"))


                                    c_label_45 = Label(cs_canvas_1,width=7,height=1,text=cl_view[14], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_45 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_45, tags=("naivtlabel17"))

                                    c_label_46 = Label(cs_canvas_1,width=7,height=1,text=cl_view[23], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_46 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_46, tags=("naivtlabel18"))

                                    c_label_47 = Label(cs_canvas_1,width=7,height=1,text=cl_view[30], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_47 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_47, tags=("naivtlabel19"))

                                    c_label_48 = Label(cs_canvas_1,width=7,height=1,text=cl_view[37], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_48 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_48, tags=("naivtlabel20"))

                                    c_label_49 = Label(cs_canvas_1,width=14,height=1,text=cl_view[15], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_49 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_49, tags=("naivtlabel21"))

                                    c_label_50 = Label(cs_canvas_1,width=14,height=1,text=cl_view[24], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_50 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_50, tags=("naivtlabel22"))

                                    c_label_51 = Label(cs_canvas_1,width=14,height=1,text=cl_view[31], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_51 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_51, tags=("naivtlabel23"))

                                    c_label_52 = Label(cs_canvas_1,width=14,height=1,text=cl_view[38], font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_52 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_52, tags=("naivtlabel24"))


                                    c_label_18 = Label(cs_canvas_1,width=11,height=1,text="Subtotal", font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                    window_c_label_18 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_18, tags=("naivlabel13"))

                                    c_label_19 = Label(cs_canvas_1,width=10,height=1,text=cl_view[16], font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                    window_c_label_19 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_19, tags=("naivlabels13"))

                                    c_label_20 = Label(cs_canvas_1,width=11,height=1,text="Tax Amount", font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                    window_c_label_20 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_20, tags=("naivlabel14"))

                                    c_label_21 = Label(cs_canvas_1,width=10,height=1,text=cl_view[40], font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                    window_c_label_21 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_21, tags=("naivlabels14"))


                                    c_label_22 = Label(cs_canvas_1,width=5,height=1,text="Total", font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                    window_c_label_22 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_22, tags=("naivlabel15"))

                                    c_label_23 = Label(cs_canvas_1,width=10,height=1,text=cl_view[17], font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                    window_c_label_23 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_23, tags=("naivlabels15"))

                                    c_label_53 = Label(cs_canvas_1,width=22,height=1,text="Terms and Conditions", font=('arial 12 bold'),background="white",fg="black", anchor="w") 
                                    window_c_label_53 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_53, tags=("naivlabels16"))

                                    c_label_54 = Label(cs_canvas_1,width=40,height=1,text="1. Goods once sold will not be taken back.", font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_54 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_54, tags=("naivlabels17"))

                                    c_label_55 = Label(cs_canvas_1,width=50,height=1,text="2. If cheque bounced, Rs 500/- will be taken as Charges.", font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_55 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_55, tags=("naivlabels18"))

                                    c_label_56 = Label(cs_canvas_1,width=55,height=1,text="3. Rs 100/- per day will charged for delayed payment after due date.", font=('arial 12'),background="white",fg="black", anchor="w") 
                                    window_c_label_56 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_56, tags=("naivlabels19"))

                                    cs_canvas_1.create_line(0, 0, 0, 0, fill='skyblue',width=2, tags=('naivline23'))

                                    c_label_24 = Label(cs_canvas_1,width=75,height=0,text="Invoice was created on a computer and is valid without the signature and seal.", font=('arial 12'),background="white",fg="black") 
                                    window_c_label_24 = cs_canvas_1.create_window(0, 0, anchor="nw", window=c_label_24, tags=("naivlabel16"))


                                    def cs_refresh():
                                        c_label_7.config(text=""+ns_entry_6.get())
                                        c_label_10.config(text=""+ns_entry_7.get())
                                        c_label_12.config(text=""+ns_entry_8.get())
                                        c_label_14.config(text=""+ns_entry_9.get())
                                        c_label_16.config(text=""+ns_entry_10.get())

                                    refreshbtn = Button(cs_canvas_1,text="Refresh",width=15,height=1,foreground="white",background="#1b3857",font='arial 12',command=cs_refresh)
                                    window_refreshbtn = cs_canvas_1.create_window(0, 0, anchor="nw", window=refreshbtn, tags=("nsbutton7"))

                                    ns_sub_btn1=Button(cs_canvas_1,text='Submit', width=15,height=2,bd=0, foreground="white",background="#2f516f",font='arial 12',activebackground="#2f516f",command=einsert_data)
                                    window_ns_sub_btn1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_sub_btn1,tags=('nsbutton1'))

                                    def ns_back_1_():
                                        cs_frame_1.grid_forget()
                                        cs_frame.grid(row=0,column=0,sticky='nsew')

                                    ns_bck_btn1=Button(cs_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=ns_back_1_)
                                    window_ns_bck_btn1 = cs_canvas_1.create_window(0, 0, anchor="nw", window=ns_bck_btn1,tags=('nsbutton3'))


                                elif cs_comb_1.get() == "Delete":
                                    cs_del = messagebox.askyesno("Delete Invoice","Are you sure to delete this invoice?")

                                    if cs_del == True:
                                        cs_id_1 = cs_tree.item(cs_tree.focus())["values"][1]
                                        
                                        
                                        sql_u = 'select * from auth_user where username=%s'
                                        val_u = (nm_ent.get(),)
                                        fbcursor.execute(sql_u,val_u)
                                        u_dtl = fbcursor.fetchone()

                                        sql_c = 'select * from app1_company where id_id=%s'
                                        val_c = (u_dtl[0],)
                                        fbcursor.execute(sql_c,val_c)
                                        c_dtl = fbcursor.fetchone()

                                        sql = 'delete from app1_customize where name=%s and cid_id=%s'
                                        val = (cs_id_1,c_dtl[0],)
                                        fbcursor.execute(sql,val)
                                        finsysdb.commit()

                                    #----------Refresh Insert Tree--------#

                                    for record in cs_tree.get_children():
                                            cs_tree.delete(record)

                                    sql_pr="select * from auth_user where username=%s"
                                    sql_pr_val=(nm_ent.get(),)
                                    fbcursor.execute(sql_pr,sql_pr_val,)
                                    pr_dtl=fbcursor.fetchone()

                                    sql = "select * from app1_company where id_id=%s"
                                    val = (pr_dtl[0],)
                                    fbcursor.execute(sql, val,)
                                    cmp_dtl=fbcursor.fetchone()

                                    c_sql_1 = "SELECT * FROM app1_customize where selected=1 and cid_id=%s"
                                    c_val_1 = (cmp_dtl[0],)
                                    fbcursor.execute(c_sql_1,c_val_1,)
                                    cs_data_1 = fbcursor.fetchall()

                                    count0 = 0
                                    for i in cs_data_1:
                                        
                                        if True:
                                            cs_tree.insert(parent='',index='end',iid=i,text='',values=('',i[1],i[6],"APPLIED"))
                                        
                                    count0 += 1

                                    c_sql_1 = "SELECT * FROM app1_customize where selected=0 and cid_id=%s"
                                    c_val_1 = (cmp_dtl[0],)
                                    fbcursor.execute(c_sql_1,c_val_1,)
                                    cs_data_2 = fbcursor.fetchall()

                                    count0 = 0
                                    for i in cs_data_2:
                                        
                                        if True:
                                            cs_tree.insert(parent='',index='end',iid=i,text='',values=('',i[1],i[6],"NOT APPLIED"))
                                        
                                    count0 += 1
                        

                            cs_comb_1 = ttk.Combobox(cs_canvas,font=('arial 10'))
                            cs_comb_1['values'] = ("Actions","Edit","Delete")
                            cs_comb_1.current(0)
                            window_cs_comb_1 = cs_canvas.create_window(0, 0, anchor="nw", width=110,height=30,window=cs_comb_1,tags=('csbutton3'))
                            cs_comb_1.bind("<<ComboboxSelected>>",edit_newstyle)



                    def settings():
                        set_btn.grid_forget()

                        # create a list box
                        langs_1 = (" Organization Profile"," User Information"," Accounts and Settings"," Customize Form Style")

                        langs_var = StringVar(value=langs_1)
                        global lst_prf_1
                        lst_prf_1 = Listbox(root,listvariable=langs_var,height=7 ,selectmode='extended',bg="black",fg="white",width=30)
                        lst_prf_1.bind('<<ListboxSelect>>', lst_prf_slt_1)
                        lst_prf_1.place(relx=0.70, rely=0.10)
                        

                        global set_btn_1
                        set_btn_1 = Button(tp_lb_srh, image=stn_img,command=select_settings, bg="#213b52", fg="black",border=0)
                        set_btn_1.grid(row=2,column=5,padx=(0,30))

                    set_btn = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
                    set_btn.grid(row=2,column=5,padx=(0,30))