#-------------------------------Customers-----------------------------#
                    tab3_3.grid_columnconfigure(0,weight=1)
                    tab3_3.grid_rowconfigure(0,weight=1)

                    cus_frame = Frame(tab3_3)
                    cus_frame.grid(row=0,column=0,sticky='nsew')

                    def cus_responsive_widgets(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget

                        dcanvas.coords("ctree1",dwidth/12,dheight/1.8)
                        

                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/14 
                        y2 = dheight/3.505

                        dcanvas.coords("cpoly1",x1 + r1,y1,
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

                        dcanvas.coords("chline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                        dcanvas.coords("clabel1",dwidth/2.5,dheight/8.00)

                        r2 = 25
                        x11 = dwidth/63
                        x21 = dwidth/1.021
                        y11 = dheight/2.8
                        y21 = dheight/0.8


                        dcanvas.coords("cpoly2",x11 + r2,y11,
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

                        dcanvas.coords("cbutton1",dwidth/2.1,dheight/2.4)
                        dcanvas.coords("cbutton2",dwidth/1.59,dheight/2.4)
                        dcanvas.coords("cbutton3",dwidth/1.28,dheight/2.26)
                        dcanvas.coords("ccombo1",dwidth/1.179,dheight/1.52)


                    cus_canvas=Canvas(cus_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

                    cus_frame.grid_rowconfigure(0,weight=1)
                    cus_frame.grid_columnconfigure(0,weight=1)

                    vertibar=Scrollbar(cus_frame, orient=VERTICAL)
                    vertibar.grid(row=0,column=1,sticky='ns')
                    vertibar.config(command=cus_canvas.yview)
                    cus_canvas.bind("<Configure>", cus_responsive_widgets)
                    cus_canvas.config(yscrollcommand=vertibar.set)
                    cus_canvas.grid(row=0,column=0,sticky='nsew')

                    cus_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("cpoly1"))

                    label_1 = Label(cus_canvas,width=12,height=1,text="CUSTOMERS", font=('arial 25'),background="#1b3857",fg="white") 
                    window_label_1 = cus_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("clabel1"))

                    cus_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("chline"))

                    
                    cus_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("cpoly2"))



                    fgthi = ttk.Style()
                    fgthi.theme_use("default")
                    fgthi.configure('mystyle105.Treeview', background='#2f516f',State='DISABLE',foreground='white',fieldbackground='#2f516f',font=(None,11))
                    fgthi.configure('mystyle105.Treeview.Heading', background='#2f516f',State='DISABLE')

                    cus_scrollbar = Scrollbar(cus_frame,orient="vertical")

                    cus_tree = ttk.Treeview(cus_canvas, columns = (1,2,3,4,5,6,7), height = 10, show = "headings",style='mystyle105.Treeview',yscrollcommand=cus_scrollbar.set)
                    cus_tree.heading(1)
                    cus_tree.heading(2, text="CUSTOMER")
                    cus_tree.heading(3, text="GST TYPE")
                    cus_tree.heading(4, text="GSTIN")
                    cus_tree.heading(5, text="PAN NO")
                    cus_tree.heading(6, text="EMAIL ID")
                    cus_tree.heading(7, text="MOBILE NO")
                    
                    cus_tree.column(1, width = 50)
                    cus_tree.column(2, width = 200)
                    cus_tree.column(3, width = 220)
                    cus_tree.column(4, width = 150)
                    cus_tree.column(5, width = 150)
                    cus_tree.column(6, width = 200)
                    cus_tree.column(7, width = 150)
                    window_label_4 = cus_canvas.create_window(0, 0, anchor="nw", window=cus_tree,tags=('ctree1'))

                    cus_scrollbar.config(command=cus_tree.yview)
                    cus_scrollbar.grid(row=0,column=2,sticky='ns')

                    sql_pr="select * from auth_user where username=%s"
                    sql_pr_val=(nm_ent.get(),)
                    fbcursor.execute(sql_pr,sql_pr_val,)
                    pr_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (pr_dtl[0],)
                    fbcursor.execute(sql, val,)
                    cmp_dtl=fbcursor.fetchone()

                    c_sql_1 = "SELECT * FROM app1_customer where cid_id=%s"
                    c_val_1 = (cmp_dtl[0],)
                    fbcursor.execute(c_sql_1,c_val_1,)
                    c_data_1 = fbcursor.fetchall()

                    count0 = 0
                    for i in c_data_1:
                        if True:
                            cus_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                        else:
                            pass
                    count0 += 1


                    def add_customer():
                        cus_frame.grid_forget()
                        cus_frame_1 = Frame(tab3_3)
                        cus_frame_1.grid(row=0,column=0,sticky='nsew')

                        def cus_responsive_widgets2(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                            
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("acpoly1",x1 + r1,y1,
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

                            dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
                            dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/2.8
                            y21 = dheight/0.45


                            dcanvas.coords("acpoly2",x11 + r2,y11,
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

                            dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
                            dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
                            dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
                            dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
                            dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
                            dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
                            dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
                            dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
                            dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
                            dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
                            dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
                            dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
                            dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
                            dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
                            dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
                            dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
                            dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
                            dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
                            dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
                            dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
                            dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
                            dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
                            dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
                            dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
                            dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

                            dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
                            dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

                            dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
                            dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
                            dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
                            dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
                            dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
                            dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
                            dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
                            dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
                            dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
                            dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
                            dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
                            dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
                            dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
                            dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
                            dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
                            dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
                            dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
                            dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
                            dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

                            dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
                            dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

                            dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
                            dcanvas.coords("acbutton3",dwidth/23,dheight/3.415)


                        cus_canvas_1=Canvas(cus_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

                        cus_frame_1.grid_columnconfigure(0,weight=1)
                        cus_frame_1.grid_rowconfigure(0,weight=1)

                        
                        vertibar=Scrollbar(cus_frame_1, orient=VERTICAL)
                        vertibar.grid(row=0,column=1,sticky='ns')
                        vertibar.config(command=cus_canvas_1.yview)

                        cus_canvas_1.bind("<Configure>", cus_responsive_widgets2)
                        cus_canvas_1.config(yscrollcommand=vertibar.set)
                        cus_canvas_1.grid(row=0,column=0,sticky='nsew')
                        
                        def sales_add_new_cus():
                            title = comb_cus_1.get()
                            firstname = entry_cus_f1.get()
                            lastname = entry_cus_l2.get()
                            company = entry_cus_com3.get()
                            location = cus_loc4.get()
                            gsttype = comb_cus_g2.get()
                            gstin = entry_cus_gin5.get()
                            panno = entry_cus_pan6.get()
                            email = entry_cus_em7.get()
                            website = entry_cus_web8.get()
                            mobile = entry_cus_mob9.get()
                            street = entry_cus_10.get()
                            city = entry_cus_12.get()
                            state = entry_cus_13.get()
                            pincode = entry_cus_p12.get()
                            country = entry_cus_c13.get()
                            shipstreet = entry_cus_11.get()
                            shipcity = entry_cus_14.get()
                            shipstate = entry_cus_15.get()
                            shippincode = entry_cus_pin.get()
                            shipcountry = entry_cus_c15.get()

                            usr_sql = "SELECT id FROM auth_user WHERE username=%s"
                            usr_val = (nm_ent.get(),)
                            fbcursor.execute(usr_sql,usr_val)
                            usr_data = fbcursor.fetchone()

                            cmp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                            cmp_val = (usr_data[0],)
                            fbcursor.execute(cmp_sql,cmp_val)
                            cmp_data = fbcursor.fetchone()
                            cid = cmp_data[0]

                            if chk_str_1.get() == True:

                                cus_sql = "INSERT INTO app1_customer (title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                cus_val=(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid)
                                fbcursor.execute(cus_sql,cus_val)
                                finsysdb.commit()

                                #----------Refresh Insert Tree--------#

                                for record in cus_tree.get_children():
                                        cus_tree.delete(record)

                                sql_pr="select * from auth_user where username=%s"
                                sql_pr_val=(nm_ent.get(),)
                                fbcursor.execute(sql_pr,sql_pr_val,)
                                pr_dtl=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dtl[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dtl=fbcursor.fetchone()

                                c_sql_1 = "SELECT * FROM app1_customer where cid_id=%s"
                                c_val_1 = (cmp_dtl[0],)
                                fbcursor.execute(c_sql_1,c_val_1,)
                                c_data_1 = fbcursor.fetchall()

                                count0 = 0
                                for i in c_data_1:
                                    if True:
                                        cus_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                                    else:
                                        pass
                                count0 += 1

                                
                                cus_frame_1.destroy()
                                cus_frame.grid(row=0,column=0,sticky='nsew')

                            else:
                                pass
                        

                        cus_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

                        label_1 = Label(cus_canvas_1,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
                        window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

                        cus_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

                        cus_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

                        label_1 = Label(cus_canvas_1,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
                        window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

                        cus_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

                        label_2 = Label(cus_canvas_1,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

                        comb_cus_1 = ttk.Combobox(cus_canvas_1, font=('arial 10'))
                        comb_cus_1['values'] = ("Mr","Mrs","Miss","Ms",)
                        comb_cus_1.current(0)
                        window_comb_cus_1 = cus_canvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_cus_1, tags=("accombo1"))

                        label_2 = Label(cus_canvas_1,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

                        entry_cus_f1=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_f1 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_f1, tags=("acentry1"))

                        label_2 = Label(cus_canvas_1,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

                        entry_cus_l2=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_l2 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_l2, tags=("acentry2"))

                        label_2 = Label(cus_canvas_1,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

                        entry_cus_com3=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_com3 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_com3, tags=("acentry3"))

                        label_2 = Label(cus_canvas_1,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

                        cus_loc4=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_cus_loc4 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=cus_loc4, tags=("acentry4"))

                        label_2 = Label(cus_canvas_1,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

                        comb_cus_g2 = ttk.Combobox(cus_canvas_1, font=('arial 10'))
                        comb_cus_g2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
                        comb_cus_g2.current(0)
                        window_comb_cus_g2 = cus_canvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_cus_g2, tags=("accombo2"))

                        label_2 = Label(cus_canvas_1,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))

                        def gst_validate(value):
            
                            """
                            Validat the email entry
                            :param value:
                            :return:
                            """
                            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                            if re.fullmatch(pattern, value) is None:
                                
                                return False

                            entry_cus_gin5.config(fg="white")
                            return True

                        def gst_invalidate():
                            entry_cus_gin5.config(fg="red")

                        def ac_gst_in(event):
                            if entry_cus_gin5.get()=="29APPCK7465F1Z1":
                                entry_cus_gin5.delete(0,END)
                            else:
                                pass
                        
                        entry_cus_gin5=Entry(cus_canvas_1,width=34,justify=LEFT,background='#2f516f',font=('arial 10'))
                        val_gst = (cus_canvas_1.register(gst_validate), '%P')
                        ival_gst = (cus_canvas_1.register(gst_invalidate),)
                        entry_cus_gin5.config(validate='focusout', validatecommand=val_gst, invalidcommand=ival_gst)
                        window_entry_cus_gin5 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_gin5, tags=("acentry5"))
                        entry_cus_gin5.insert(0,"29APPCK7465F1Z1")
                        entry_cus_gin5.bind("<Button-1>",ac_gst_in)


                        label_2 = Label(cus_canvas_1,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

                        def ac_pan_no(event):
                            if entry_cus_pan6.get()=="APPCK7465F":
                                entry_cus_pan6.delete(0,END)
                            else:
                                pass

                        def pan_validate(value):
            
                            """
                            Validat the email entry
                            :param value:
                            :return:
                            """
                            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                            if re.fullmatch(pattern, value) is None:
                                
                                return False

                            entry_cus_pan6.config(fg="white")
                            return True

                        def pan_invalidate():
                            entry_cus_pan6.config(fg="red")

                        entry_cus_pan6=Entry(cus_canvas_1,width=34,justify=LEFT,background='#2f516f',font=('arial 10'))
                        val_pan = (cus_canvas_1.register(pan_validate), '%P')
                        ival_pan = (cus_canvas_1.register(pan_invalidate),)
                        entry_cus_pan6.config(validate='focusout', validatecommand=val_pan, invalidcommand=ival_pan)
                        window_entry_cus_pan6 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_pan6, tags=("acentry6"))
                        entry_cus_pan6.insert(0,"APPCK7465F")
                        entry_cus_pan6.bind("<Button-1>",ac_pan_no)

                        label_2 = Label(cus_canvas_1,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

                        def email_validate(value):
            
                            """
                            Validat the email entry
                            :param value:
                            :return:
                            """
                            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                            if re.fullmatch(pattern, value) is None:
                                
                                return False

                            entry_cus_em7.config(fg="white")
                            return True

                        def email_invalidate():
                            entry_cus_em7.config(fg="red")

                        entry_cus_em7=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f')
                        val_email = (cus_canvas_1.register(email_validate), '%P')
                        ival_email = (cus_canvas_1.register(email_invalidate),)
                        entry_cus_em7.config(validate='focusout', validatecommand=val_email, invalidcommand=ival_email)
                        window_entry_cus_em7 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_em7, tags=("acentry7"))

                        label_2 = Label(cus_canvas_1,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

                        entry_cus_web8=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_web8 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_web8, tags=("acentry8"))

                        label_2 = Label(cus_canvas_1,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))

                        entry_cus_mob9=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_mob9 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_mob9, tags=("acentry9"))

                        def copy_cus_details():
                            entry_cus_11.delete(0, END)
                            entry_cus_11.insert(0,entry_cus_10.get())
                            entry_cus_14.delete(0, END)
                            entry_cus_14.insert(0,entry_cus_12.get())
                            entry_cus_15.delete(0, END)
                            entry_cus_15.insert(0,entry_cus_13.get())
                            entry_cus_pin.delete(0, END)
                            entry_cus_pin.insert(0,entry_cus_p12.get())
                            entry_cus_c15.delete(0, END)
                            entry_cus_c15.insert(0,entry_cus_c13.get())

                        label_1 = Label(cus_canvas_1,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
                        window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

                        label_2 = Label(cus_canvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

                        entry_cus_10=Entry(cus_canvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_10 = cus_canvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_cus_10, tags=("acentry10"))

                        label_1 = Label(cus_canvas_1,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
                        window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

                        label_2 = Label(cus_canvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

                        entry_cus_11=Entry(cus_canvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_11 = cus_canvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_cus_11, tags=("acentry11"))

                        label_2 = Label(cus_canvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

                        entry_cus_12=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_12 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_12, tags=("acentry12"))
                        
                        label_2 = Label(cus_canvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

                        entry_cus_13=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_13 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_13, tags=("acentry13"))

                        label_2 = Label(cus_canvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

                        entry_cus_14=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_14 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_14, tags=("acentry14"))

                        label_2 = Label(cus_canvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

                        entry_cus_15=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_15 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_15, tags=("acentry15"))

                        label_2 = Label(cus_canvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

                        entry_cus_p12=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_p12 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_p12, tags=("acentry16"))
                        
                        label_2 = Label(cus_canvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

                        entry_cus_c13=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_c13 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_c13, tags=("acentry17"))

                        label_2 = Label(cus_canvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

                        entry_cus_pin=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_pin = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_pin, tags=("acentry18"))

                        label_2 = Label(cus_canvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

                        entry_cus_c15=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_cus_c15 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_c15, tags=("acentry19"))

                        chk_str = StringVar()
                        chkbtn1 = Checkbutton(cus_canvas_1, text = "Same As Billing Address", variable = chk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f",command=copy_cus_details)
                        chkbtn1.select()
                        window_chkbtn_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=chkbtn1, tags=("accheck1"))

                        chk_str_1 = BooleanVar()
                        chkbtn2 = Checkbutton(cus_canvas_1, text = "Agree to terms and conditions", variable = chk_str_1, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
                        window_chkbtn_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=chkbtn2,tags=("accheck2"))

                        def ac_back_1_():
                            cus_frame_1.grid_forget()
                            cus_frame.grid(row=0,column=0,sticky='nsew')

                        ac_bck_btn1=Button(cus_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=ac_back_1_)
                        window_ac_bck_btn1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=ac_bck_btn1,tags=('acbutton3'))

                        cus_btn2=Button(cus_canvas_1,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12',command=sales_add_new_cus)
                        window_cus_btn2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=cus_btn2,tags=("acbutton1"))

                    btn1=Button(cus_canvas,text='Add Customer', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_customer)
                    window_btn1 = cus_canvas.create_window(0, 0, anchor="nw", window=btn1, tags=("cbutton2"))

                    def edit_delete_customer(event):
                        if cus_comb_1.get() == 'Edit':
                            cus_frame.grid_forget()
                            cus_eframe_1 = Frame(tab3_3)
                            cus_eframe_1.grid(row=0,column=0,sticky='nsew')

                            def ecus_responsive_widgets2(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                                
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("acpoly1",x1 + r1,y1,
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

                                dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
                                dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.45


                                dcanvas.coords("acpoly2",x11 + r2,y11,
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

                                dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
                                dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
                                dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
                                dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
                                dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
                                dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
                                dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
                                dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
                                dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
                                dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
                                dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
                                dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
                                dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
                                dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
                                dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
                                dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
                                dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
                                dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
                                dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
                                dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
                                dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
                                dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
                                dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
                                dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
                                dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

                                dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
                                dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

                                dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
                                dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
                                dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
                                dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
                                dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
                                dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
                                dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
                                dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
                                dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
                                dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
                                dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
                                dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
                                dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
                                dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
                                dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
                                dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
                                dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
                                dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
                                dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

                                dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
                                dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

                                dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
                                dcanvas.coords("acbutton3",dwidth/23,dheight/3.415)


                            cus_ecanvas_1=Canvas(cus_eframe_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

                            cus_eframe_1.grid_columnconfigure(0,weight=1)
                            cus_eframe_1.grid_rowconfigure(0,weight=1)

                            
                            vertibar=Scrollbar(cus_eframe_1, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=cus_ecanvas_1.yview)

                            cus_ecanvas_1.bind("<Configure>", ecus_responsive_widgets2)
                            cus_ecanvas_1.config(yscrollcommand=vertibar.set)
                            cus_ecanvas_1.grid(row=0,column=0,sticky='nsew')

                            c_editid = cus_tree.item(cus_tree.focus())["values"][4]
                            print(c_editid)
                            c_editid_1 = cus_tree.item(cus_tree.focus())["values"][5]
                            print(c_editid_1)

                            sql_u = 'select * from auth_user where username=%s'
                            val_u = (nm_ent.get(),)
                            fbcursor.execute(sql_u,val_u)
                            pr_dtl = fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pr_dtl[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dtl=fbcursor.fetchone()
                            print(cmp_dtl)

                            sql = 'select * from app1_customer where panno = %s and email = %s and cid_id = %s'
                            val =  (c_editid,c_editid_1,cmp_dtl[0],)
                            fbcursor.execute(sql,val)
                            edit_cus = fbcursor.fetchone()
        

                            def sales_edit_new_cus():
                                title = comb_ecus_1.get()
                                firstname = entry_ecus_1.get()
                                lastname = entry_ecus_2.get()
                                company = entry_ecus_3.get()
                                location = ecus_4.get()
                                gsttype = comb_ecus_2.get()
                                gstin = entry_ecus_5.get()
                                panno = entry_ecus_6.get()
                                email = entry_ecus_7.get()
                                website = entry_ecus_8.get()
                                mobile = entry_ecus_9.get()
                                street = entry_ecus_10.get()
                                city = entry_ecus_12.get()
                                state = entry_ecus_13.get()
                                pincode = entry_ecus_p12.get()
                                country = entry_ecus_c13.get()
                                shipstreet = entry_ecus_11.get()
                                shipcity = entry_ecus_14.get()
                                shipstate = entry_ecus_15.get()
                                shippincode = entry_ecus_pin14.get()
                                shipcountry = entry_ecus_co15.get()

                                usre_sql = "SELECT id FROM auth_user WHERE username=%s"
                                usre_val = (nm_ent.get(),)
                                fbcursor.execute(usre_sql,usre_val)
                                usre_data = fbcursor.fetchone()

                                cmpne_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                cmpne_val = (usre_data[0],)
                                fbcursor.execute(cmpne_sql,cmpne_val)
                                cmpne_data = fbcursor.fetchone()
                                cid = cmpne_data[0]

                                if echk_str_1.get() == True:

                                    cus_sql = "UPDATE app1_customer set title=%s,firstname=%s,lastname=%s,company=%s,location=%s,gsttype=%s,gstin=%s,panno=%s,email=%s,website=%s,mobile=%s,street=%s,city=%s,state=%s,pincode=%s,country=%s,shipstreet=%s,shipcity=%s,shipstate=%s,shippincode=%s,shipcountry=%s,cid_id=%s where panno=%s and email = %s"
                                    cus_val=(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid,c_editid,c_editid_1)
                                    fbcursor.execute(cus_sql,cus_val)
                                    finsysdb.commit()

                                    #----------Refresh Insert Tree--------#

                                    for record in cus_tree.get_children():
                                            cus_tree.delete(record)

                                    sql_pr_1="select * from auth_user where username=%s"
                                    sql_pr1_val=(nm_ent.get(),)
                                    fbcursor.execute(sql_pr_1,sql_pr1_val,)
                                    pr_dtl_1=fbcursor.fetchone()

                                    sql_2 = "select * from app1_company where id_id=%s"
                                    val_2 = (pr_dtl_1[0],)
                                    fbcursor.execute(sql_2, val_2,)
                                    cmp_dtl_2=fbcursor.fetchone()

                                    c_sql_2 = "SELECT * FROM app1_customer where cid_id=%s"
                                    c_val_2 = (cmp_dtl_2[0],)
                                    fbcursor.execute(c_sql_2,c_val_2,)
                                    c_data_2 = fbcursor.fetchall()

                                    count1 = 0
                                    for i in c_data_2:
                                        if True:
                                            cus_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                                        else:
                                            pass
                                    count1 += 1

                                    cus_eframe_1.destroy()
                                    cus_frame.grid(row=0,column=0,sticky='nsew')

                                else:
                                    pass


                            cus_ecanvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

                            label_1 = Label(cus_ecanvas_1,width=15,height=1,text="EDIT CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

                            cus_ecanvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

                            cus_ecanvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

                            label_1 = Label(cus_ecanvas_1,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

                            cus_ecanvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

                            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

                            comb_ecus_1 = ttk.Combobox(cus_ecanvas_1, font=('arial 10'))
                            comb_ecus_1['values'] = ("Mr","Mrs","Miss","Ms",)
                            comb_ecus_1.current(0)
                            window_comb_ecus_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_ecus_1, tags=("accombo1"))
                            comb_ecus_1.delete(0,'end')
                            comb_ecus_1.insert(0, edit_cus[1])

                            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

                            entry_ecus_1=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_1, tags=("acentry1"))
                            entry_ecus_1.delete(0,'end')
                            entry_ecus_1.insert(0, edit_cus[2])

                            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

                            entry_ecus_2=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_2, tags=("acentry2"))
                            entry_ecus_2.delete(0,'end')
                            entry_ecus_2.insert(0, edit_cus[3])

                            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

                            entry_ecus_3=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_3 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_3, tags=("acentry3"))
                            entry_ecus_3.delete(0,'end')
                            entry_ecus_3.insert(0, edit_cus[4])


                            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

                            ecus_4=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_ecus_4 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=ecus_4, tags=("acentry4"))
                            ecus_4.delete(0,'end')
                            ecus_4.insert(0, edit_cus[5])


                            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

                            comb_ecus_2 = ttk.Combobox(cus_ecanvas_1, font=('arial 10'))
                            comb_ecus_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
                            comb_ecus_2.current(0)
                            window_comb_ecus_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_ecus_2, tags=("accombo2"))
                            comb_ecus_2.delete(0,'end')
                            comb_ecus_2.insert(0, edit_cus[6])

                            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))

                            def gst_validate(value):
            
                                """
                                Validat the email entry
                                :param value:
                                :return:
                                """
                                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                                if re.fullmatch(pattern, value) is None:
                                    
                                    return False

                                entry_ecus_5.config(fg="white")
                                return True

                            def gst_invalidate():
                                entry_ecus_5.config(fg="red")

                            

                            entry_ecus_5=Entry(cus_ecanvas_1,width=34,justify=LEFT,background='#2f516f',font=('arial 10'))
                            eval_gst = (cus_ecanvas_1.register(gst_validate), '%P')
                            eival_gst = (cus_ecanvas_1.register(gst_invalidate),)
                            entry_ecus_5.config(validate='focusout', validatecommand=eval_gst, invalidcommand=eival_gst)
                            window_entry_ecus_5 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_5, tags=("acentry5"))
                            entry_ecus_5.delete(0,'end')
                            entry_ecus_5.insert(0, edit_cus[7])

                            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

                            def pan_validate(value):
            
                                """
                                Validat the email entry
                                :param value:
                                :return:
                                """
                                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                                if re.fullmatch(pattern, value) is None:
                                    
                                    return False

                                entry_ecus_6.config(fg="white")
                                return True

                            def pan_invalidate():
                                entry_ecus_6.config(fg="red")


                            entry_ecus_6=Entry(cus_ecanvas_1,width=34,justify=LEFT,background='#2f516f',font=('arial 10'))
                            eval_pan = (cus_ecanvas_1.register(pan_validate), '%P')
                            eival_pan = (cus_ecanvas_1.register(pan_invalidate),)
                            entry_ecus_6.config(validate='focusout', validatecommand=eval_pan, invalidcommand=eival_pan)
                            window_entry_ecus_6 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_6, tags=("acentry6"))
                            entry_ecus_6.delete(0,'end')
                            entry_ecus_6.insert(0, edit_cus[8])

                            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

                            def email_validate(value):
            
                                """
                                Validat the email entry
                                :param value:
                                :return:
                                """
                                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                                if re.fullmatch(pattern, value) is None:
                                    
                                    return False

                                entry_ecus_7.config(fg="white")
                                return True

                            def email_invalidate():
                                entry_ecus_7.config(fg="red")

                            entry_ecus_7=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f')
                            eval_email = (cus_ecanvas_1.register(email_validate), '%P')
                            eival_email = (cus_ecanvas_1.register(email_invalidate),)
                            entry_ecus_7.config(validate='focusout', validatecommand=eval_email, invalidcommand=eival_email)
                            window_entry_ecus_7 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_7, tags=("acentry7"))
                            entry_ecus_7.delete(0,'end')
                            entry_ecus_7.insert(0, edit_cus[9])


                            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

                            entry_ecus_8=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_8 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_8, tags=("acentry8"))
                            entry_ecus_8.delete(0,'end')
                            entry_ecus_8.insert(0, edit_cus[10])

                            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))
                            

                            entry_ecus_9=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_9 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_9, tags=("acentry9"))
                            entry_ecus_9.delete(0,'end')
                            entry_ecus_9.insert(0, edit_cus[11])

                            label_1 = Label(cus_ecanvas_1,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
                            window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

                            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

                            entry_ecus_10=Entry(cus_ecanvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_10 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_ecus_10, tags=("acentry10"))
                            entry_ecus_10.delete(0,'end')
                            entry_ecus_10.insert(0, edit_cus[12])


                            label_1 = Label(cus_ecanvas_1,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
                            window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

                            echk_str = StringVar()
                            echkbtn1 = Checkbutton(cus_ecanvas_1, text = "Same As Billing Address", variable = echk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            echkbtn1.select()
                            window_echkbtn_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=echkbtn1, tags=("accheck1"))

                            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

                            entry_ecus_11=Entry(cus_ecanvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_11 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_ecus_11, tags=("acentry11"))
                            entry_ecus_11.delete(0,'end')
                            entry_ecus_11.insert(0, edit_cus[17])

                            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

                            entry_ecus_12=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_12 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_12, tags=("acentry12"))
                            entry_ecus_12.delete(0,'end')
                            entry_ecus_12.insert(0, edit_cus[13])
                            
                            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

                            entry_ecus_13=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_13 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_13, tags=("acentry13"))
                            entry_ecus_13.delete(0,'end')
                            entry_ecus_13.insert(0, edit_cus[14])

                            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

                            entry_ecus_14=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_14 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_14, tags=("acentry14"))
                            entry_ecus_14.delete(0,'end')
                            entry_ecus_14.insert(0, edit_cus[18])

                            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

                            entry_ecus_15=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_15 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_15, tags=("acentry15"))
                            entry_ecus_15.delete(0,'end')
                            entry_ecus_15.insert(0, edit_cus[19])

                            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

                            entry_ecus_p12=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_p12 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_p12, tags=("acentry16"))
                            entry_ecus_p12.delete(0,'end')
                            entry_ecus_p12.insert(0, edit_cus[15])
                            
                            label_2 = Label(cus_ecanvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

                            entry_ecus_c13=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_c13 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_c13, tags=("acentry17"))
                            entry_ecus_c13.delete(0,'end')
                            entry_ecus_c13.insert(0, edit_cus[16])

                            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

                            entry_ecus_pin14=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_pin14 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_pin14, tags=("acentry18"))
                            entry_ecus_pin14.delete(0,'end')
                            entry_ecus_pin14.insert(0, edit_cus[20])

                            label_2 = Label(cus_ecanvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

                            entry_ecus_co15=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ecus_co15 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_co15, tags=("acentry19"))
                            entry_ecus_co15.delete(0,'end')
                            entry_ecus_co15.insert(0, edit_cus[21])

                            echk_str_1 = BooleanVar()
                            echkbtn2 = Checkbutton(cus_ecanvas_1, text = "Agree to terms and conditions", variable = echk_str_1, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            window_echkbtn_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=echkbtn2,tags=("accheck2"))

                            def ec_back_1_():
                                cus_eframe_1.grid_forget()
                                cus_frame.grid(row=0,column=0,sticky='nsew')

                            ec_bck_btn1=Button(cus_ecanvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=ec_back_1_)
                            window_ec_bck_btn1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=ec_bck_btn1,tags=('acbutton3'))

                            ecus_btn2=Button(cus_ecanvas_1,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12',command=sales_edit_new_cus)
                            window_ecus_btn2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=ecus_btn2,tags=("acbutton1"))

                        elif cus_comb_1.get() == 'Delete':
                            cus_del = messagebox.askyesno("Delete Customer","Are you sure to delete this customer?")

                            if cus_del == True:
                                cus_id_1 = cus_tree.item(cus_tree.focus())["values"][4]
                                cus_id_2 = cus_tree.item(cus_tree.focus())["values"][5]

                                sql_u = 'select * from auth_user where username=%s'
                                val_u = (nm_ent.get(),)
                                fbcursor.execute(sql_u,val_u)
                                u_dtl = fbcursor.fetchone()

                                sql_c = 'select * from app1_company where id_id=%s'
                                val_c = (u_dtl[0],)
                                fbcursor.execute(sql_c,val_c)
                                c_dtl = fbcursor.fetchone()

                                sql = 'delete from app1_customer where panno=%s and email=%s and cid_id=%s'
                                val = (cus_id_1,cus_id_2,c_dtl[0],)
                                fbcursor.execute(sql,val)
                                finsysdb.commit()

                                #----------Refresh Insert Tree--------#

                                for record in cus_tree.get_children():
                                        cus_tree.delete(record)

                                sql_pr="select * from auth_user where username=%s"
                                sql_pr_val=(nm_ent.get(),)
                                fbcursor.execute(sql_pr,sql_pr_val,)
                                pr_dtl=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dtl[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dtl=fbcursor.fetchone()

                                c_sql_1 = "SELECT * FROM app1_customer where cid_id=%s"
                                c_val_1 = (cmp_dtl[0],)
                                fbcursor.execute(c_sql_1,c_val_1,)
                                c_data_1 = fbcursor.fetchall()

                                count0 = 0
                                for i in c_data_1:
                                    if True:
                                        cus_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                                    else:
                                        pass
                                count0 += 1

                            else:
                                pass
                        else:  
                            pass

                    

                    cus_comb_1 = ttk.Combobox(cus_canvas,font=('arial 10'))
                    cus_comb_1['values'] = ("Actions","Edit","Delete")
                    cus_comb_1.current(0)
                    window_cus_comb_1 = cus_canvas.create_window(0, 0, anchor="nw", width=110,height=30,window=cus_comb_1,tags=('cbutton3'))
                    cus_comb_1.bind("<<ComboboxSelected>>",edit_delete_customer)