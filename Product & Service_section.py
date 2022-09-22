#---------------------------Product & Services------------------------#
                    tab3_4.grid_columnconfigure(0,weight=1)
                    tab3_4.grid_rowconfigure(0,weight=1)

                    pro_frame = Frame(tab3_4)
                    pro_frame.grid(row=0,column=0,sticky='nsew')

                    def pro_responsive_widgets(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget

                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/14 
                        y2 = dheight/3.505

                        dcanvas.coords("ppoly1",x1 + r1,y1,
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

                        dcanvas.coords("phline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                        dcanvas.coords("plabel1",dwidth/2.75,dheight/8.00)

                        r2 = 25
                        x11 = dwidth/63
                        x21 = dwidth/1.021
                        y11 = dheight/2.8
                        y21 = dheight/0.750


                        dcanvas.coords("ppoly2",x11 + r2,y11,
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



                        dcanvas.coords("pimage1",dwidth/5.29,dheight/2.15)
                        dcanvas.coords("pimage2",dwidth/2.05,dheight/2.15)

                        dcanvas.coords("plabel2",dwidth/5.60,dheight/1.60)
                        dcanvas.coords("plabel3",dwidth/2.09,dheight/1.60)
                        
                        dcanvas.coords("pcombo1",dwidth/1.18,dheight/1.10)

                        dcanvas.coords("pbutton1",dwidth/2.2,dheight/1.4)
                        dcanvas.coords("pbutton2",dwidth/1.645,dheight/1.4)
                        dcanvas.coords("pbutton3",dwidth/1.315,dheight/1.35)

                        dcanvas.coords("ptree1",dwidth/12,dheight/1.21)

                    pro_canvas=Canvas(pro_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

                    pro_frame.grid_rowconfigure(0,weight=1)
                    pro_frame.grid_columnconfigure(0,weight=1)

                    vertibar=Scrollbar(pro_frame, orient=VERTICAL)
                    vertibar.grid(row=0,column=1,sticky='ns')
                    vertibar.config(command=pro_canvas.yview)
                    
                    pro_canvas.bind("<Configure>", pro_responsive_widgets)
                    pro_canvas.config(yscrollcommand=vertibar.set)
                    pro_canvas.grid(row=0,column=0,sticky='nsew')

                    
                    pro_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ppoly1"))
                    
                    label_1 = Label(pro_canvas,width=23,height=1,text="PRODUCT AND SERVICES", font=('arial 25'),background="#1b3857",fg="white") 
                    window_label_1 = pro_canvas.create_window(480, 85, anchor="nw", window=label_1, tags=("plabel1"))

                    pro_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("phline"))

                    pro_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ppoly2"))


                    image_1 = Image.open("images/lowstock.png")
                    resize_image = image_1.resize((90,90))
                    image_1 = ImageTk.PhotoImage(resize_image)
                    btlogo = Label(pro_canvas, width=90, height=90, background="#1b3857", image = image_1) 
                    window_image = pro_canvas.create_window(0, 0, anchor="nw", window=btlogo,tags=('pimage1'))
                    btlogo.photo = image_1

                    label_2 = Label(pro_canvas,width=14,height=1,text="LOW STOCK : ", font=('arial 18'),background="#1b3857",fg="white") 
                    window_label_2 = pro_canvas.create_window(0, 0, anchor="nw", window=label_2,tags=('plabel2'))

                    image_2 = Image.open("images/outofstock.png")
                    resize_image_1 = image_2.resize((90,90))
                    image_2 = ImageTk.PhotoImage(resize_image_1)
                    btlogo_1 = Label(pro_canvas, width=90, height=90, background="#1b3857", image = image_2) 
                    window_image_1 = pro_canvas.create_window(0, 0, anchor="nw", window=btlogo_1,tags=('pimage2'))
                    btlogo_1.photo = image_2

                    label_2 = Label(pro_canvas,width=15,height=1,text="OUT OF STOCK : ", font=('arial 18'),background="#1b3857",fg="white") 
                    window_label_2 = pro_canvas.create_window(0, 0, anchor="nw", window=label_2,tags=('plabel3'))


                    def add_product():
                        pro_frame.grid_forget()
                        pro_frame_1 = Frame(tab3_4)
                        pro_frame_1.grid(row=0,column=0,sticky='nsew')

                        def pro_responsive_widgets_1(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                            
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("appoly1",x1 + r1,y1,
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

                            dcanvas.coords("aplabel1",dwidth/3,dheight/8.24)
                            dcanvas.coords("aphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/2.8
                            y21 = dheight/0.60


                            dcanvas.coords("appoly2",x11 + r2,y11,
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

                            r2 = 25
                            x11 = dwidth/7
                            x21 = dwidth/2.07
                            y11 = dheight/2.0
                            y21 = dheight/1.1


                            dcanvas.coords("appoly3",x11 + r2,y11,
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

                            dcanvas.coords("apimage1",dwidth/4.2,dheight/1.73)
                            
                            dcanvas.coords("aplabel2",dwidth/3.9,dheight/1.75)
                            dcanvas.coords("aplabel3",dwidth/6.30,dheight/1.54)
                            dcanvas.coords("apbutton1",dwidth/4.1,dheight/1.30)

                            r2 = 25
                            x11 = dwidth/1.93
                            x21 = dwidth/1.15
                            y11 = dheight/2.0
                            y21 = dheight/1.1


                            dcanvas.coords("appoly4",x11 + r2,y11,
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

                            dcanvas.coords("apimage2",dwidth/1.61,dheight/1.73)
                            
                            dcanvas.coords("aplabel4",dwidth/1.58,dheight/1.75)
                            dcanvas.coords("aplabel5",dwidth/1.85,dheight/1.54)
                            dcanvas.coords("apbutton2",dwidth/1.6,dheight/1.30)

                            r2 = 25
                            x11 = dwidth/7
                            x21 = dwidth/2.07
                            y11 = dheight/1.0
                            y21 = dheight/0.719


                            dcanvas.coords("appoly5",x11 + r2,y11,
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

                            
                            dcanvas.coords("apimage3",dwidth/4.2,dheight/0.93)
                            
                            dcanvas.coords("aplabel6",dwidth/3.9,dheight/0.95)
                            dcanvas.coords("aplabel7",dwidth/6.30,dheight/0.88)
                            dcanvas.coords("apbutton3",dwidth/4.1,dheight/0.80)

                            r2 = 25
                            x11 = dwidth/1.93
                            x21 = dwidth/1.15
                            y11 = dheight/1.0
                            y21 = dheight/0.719


                            dcanvas.coords("appoly6",x11 + r2,y11,
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

                            dcanvas.coords("apimage4",dwidth/1.61,dheight/0.93)

                            dcanvas.coords("aplabel8",dwidth/1.58,dheight/0.95)
                            dcanvas.coords("aplabel9",dwidth/1.85,dheight/0.88)
                            dcanvas.coords("apbutton4",dwidth/1.6,dheight/0.80)
                            dcanvas.coords("apbutton5",dwidth/23,dheight/3.415)


                        p_canvas_1=Canvas(pro_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1000))

                        pro_frame_1.grid_columnconfigure(0,weight=1)
                        pro_frame_1.grid_rowconfigure(0,weight=1)
                        
                        vertibar=Scrollbar(pro_frame_1, orient=VERTICAL)
                        vertibar.grid(row=0,column=1,sticky='ns')
                        vertibar.config(command=p_canvas_1.yview)

                        p_canvas_1.bind("<Configure>", pro_responsive_widgets_1)
                        p_canvas_1.config(yscrollcommand=vertibar.set)
                        p_canvas_1.grid(row=0,column=0,sticky='nsew')
                        
                        
                        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("appoly1"))

                        label_1 = Label(p_canvas_1,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aplabel1"))

                        p_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("aphline"))

                        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("appoly2"))

                        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly3"))

                        def invcall(event):
                            p_canvas_1.itemconfig('apimage1',state='hidden')
                            p_canvas_1.itemconfig('aplabel2',state='normal')
                            p_canvas_1.itemconfig('aplabel3',state='normal')
                            p_canvas_1.itemconfig('apbutton1',state='normal')

                        image_i1 = Image.open("images/inventory.png")
                        resize_image = image_i1.resize((200,150))
                        image_i1 = ImageTk.PhotoImage(resize_image)
                        btlogoi = Label(p_canvas_1, width=200, height=150, background="#1b3857", image = image_i1) 
                        window_image = p_canvas_1.create_window(0, 0, anchor="nw", window=btlogoi,tags=('apimage1'))
                        btlogoi.photo = image_i1
                        btlogoi.bind("<Button-1>",invcall)

                        label_1 = Label(p_canvas_1,width=10,height=1,text="Inventory", font=('arial 20'),background="#2f516f",fg="white") 
                        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel2'),state=HIDDEN)

                        label_1 = Label(p_canvas_1,width=45,height=2,text="Inventory is the goods available for sale and raw materials \nused to produce goods available for sale.", font=('arial 12'),background="#2f516f",fg="white") 
                        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel3'),state=HIDDEN)

                        def inv_add_item():
                            pro_frame_1.grid_forget()
                            pro_frame_2 = Frame(tab3_4)
                            pro_frame_2.grid(row=0,column=0,sticky='nsew')

                            def pro_responsive_widgets_2(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("ippoly1",x1 + r1,y1,
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

                                dcanvas.coords("iplabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("iphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.29


                                dcanvas.coords("ippoly2",x11 + r2,y11,
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

                                r2 = 25
                                x11 = dwidth/24
                                x21 = dwidth/1.050
                                y11 = dheight/2.1
                                y21 = dheight/1.35


                                dcanvas.coords("ippoly3",x11 + r2,y11,
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

                                dcanvas.coords("iplabel2",dwidth/2.5,dheight/1.77)
                                dcanvas.coords("ipbutton1",dwidth/1.8,dheight/1.77)

                                dcanvas.coords("iplabel3",dwidth/23.2,dheight/1.23)
                                dcanvas.coords("iplabel4",dwidth/23.3,dheight/1.02)
                                dcanvas.coords("iplabel5",dwidth/1.9,dheight/1.02)
                                dcanvas.coords("iplabel6",dwidth/1.9,dheight/0.92)
                                dcanvas.coords("iplabel7",dwidth/27,dheight/0.865)
                                dcanvas.coords("iplabel8",dwidth/1.915,dheight/0.865)
                                dcanvas.coords("iplabel9",dwidth/50,dheight/0.76)
                                dcanvas.coords("iplabel10",dwidth/2.95,dheight/0.76)
                                dcanvas.coords("iplabel11",dwidth/1.54,dheight/0.76)
                                dcanvas.coords("iplabel12",dwidth/38,dheight/0.675)
                                dcanvas.coords("iplabel13",dwidth/26.8,dheight/0.606)
                                dcanvas.coords("iplabel14",dwidth/28.3,dheight/0.538)
                                dcanvas.coords("iplabel15",dwidth/1.9,dheight/0.538)
                                dcanvas.coords("iplabel16",dwidth/28.4,dheight/0.485)
                                dcanvas.coords("iplabel17",dwidth/29.3,dheight/0.438)
                                dcanvas.coords("iplabel18",dwidth/28,dheight/0.401)
                                dcanvas.coords("iplabel19",dwidth/1.91,dheight/0.401)
                                dcanvas.coords("iplabel20",dwidth/28,dheight/0.37)
                                dcanvas.coords("iplabel21",dwidth/26,dheight/0.35)
                                dcanvas.coords("iplabel22",dwidth/1.9,dheight/0.35)

                                dcanvas.coords("ipentry1",dwidth/23.2,dheight/1.165)
                                dcanvas.coords("ipentry2",dwidth/23.2,dheight/0.975)
                                dcanvas.coords("ipentry3",dwidth/1.9,dheight/0.975)
                                dcanvas.coords("ipentry4",dwidth/1.9,dheight/0.83)
                                dcanvas.coords("ipentry5",dwidth/23.2,dheight/0.73)
                                dcanvas.coords("ipentry6",dwidth/1.52,dheight/0.73)
                                dcanvas.coords("ipentry7",dwidth/23.2,dheight/0.59)
                                dcanvas.coords("ipentry8",dwidth/23.2,dheight/0.525)
                                dcanvas.coords("ipentry9",dwidth/23.2,dheight/0.43)
                                dcanvas.coords("ipentry10",dwidth/23.2,dheight/0.394)
                                dcanvas.coords("ipentry11",dwidth/23.2,dheight/0.344)

                                dcanvas.coords("ipcombo1",dwidth/23.2,dheight/0.83)
                                dcanvas.coords("ipcombo2",dwidth/23.2,dheight/0.654)
                                dcanvas.coords("ipcombo3",dwidth/1.9,dheight/0.525)
                                dcanvas.coords("ipcombo4",dwidth/23.2,dheight/0.474)
                                dcanvas.coords("ipcombo5",dwidth/1.89,dheight/0.394)
                                dcanvas.coords("ipcombo6",dwidth/23.2,dheight/0.364)
                                dcanvas.coords("ipcombo7",dwidth/1.89,dheight/0.344)

                                dcanvas.coords("ipcbutton1",dwidth/23.2,dheight/0.51)
                                dcanvas.coords("ipcbutton2",dwidth/23.2,dheight/0.385)

                                dcanvas.coords("ipbutton2",dwidth/2.45,dheight/0.654)
                                dcanvas.coords("ipbutton3",dwidth/2.45,dheight/0.474)
                                dcanvas.coords("ipbutton4",dwidth/2.45,dheight/0.364)
                                dcanvas.coords("ipbutton5",dwidth/2.38,dheight/0.325)

                                dcanvas.coords("iphline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)

                                try:
                                    dcanvas.coords("ipdate1",dwidth/2.9,dheight/0.73)
                                except:
                                    pass


                            p_canvas_2=Canvas(pro_frame_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_2.grid_columnconfigure(0,weight=1)
                            pro_frame_2.grid_rowconfigure(0,weight=1)
                        
                            vertibar=Scrollbar(pro_frame_2, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_2.yview)

                            p_canvas_2.bind("<Configure>", pro_responsive_widgets_2)
                            p_canvas_2.config(yscrollcommand=vertibar.set)
                            p_canvas_2.grid(row=0,column=0,sticky='nsew')

                            def add_new_pro_inv():
                                name = entry_inv_item_1.get()
                                sku = entry_inv_item_2.get()
                                hsn = entry_inv_item_h2.get()
                                unit = comb_inv_item_u1.get()
                                category = entry_inv_item_3.get()
                                initialqty = entry_inv_item_4.get()
                                date = entry_inv_item_aod5.get_date()
                                stockalrt = entry_inv_item_6.get()
                                invacnt = comb_inv_item_i2.get()
                                description = entry_inv_item_7.get('1.0', 'end-1c')
                                salesprice = entry_inv_item_8.get()
                                incomeacnt = comb_inv_item_in4.get()
                                tax = comb_inv_item_t3.get()
                                purchaseinfo = entry_inv_item_9.get('1.0', 'end-1c')
                                cost = entry_inv_item_10.get()
                                expacnt = comb_inv_item_ex6.get()
                                purtax = comb_inv_item_pu5.get()
                                revcharge = entry_inv_item_11.get()
                                presupplier = comb_inv_item_pr7.get()

                                usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                                usrp_val = (nm_ent.get(),)
                                fbcursor.execute(usrp_sql,usrp_val)
                                usrp_data = fbcursor.fetchone()

                                cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                cmpp_val = (usrp_data[0],)
                                fbcursor.execute(cmpp_sql,cmpp_val)
                                cmpp_data = fbcursor.fetchone()
                                cid = cmpp_data[0]
                                
                                i_p_sql = "INSERT INTO app1_inventory(name,sku,hsn,unit,category,initialqty,date,stockalrt,invacnt,description,salesprice,incomeacnt,tax,purchaseinfo,cost,expacnt,purtax,revcharge,presupplier,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                i_p_val = (name,sku,hsn,unit,category,initialqty,date,stockalrt,invacnt,description,salesprice,incomeacnt,tax,purchaseinfo,cost,expacnt,purtax,revcharge,presupplier,cid)
                                fbcursor.execute(i_p_sql,i_p_val)
                                finsysdb.commit()

                                #_________Refresh insert tree________#
        
                                for record in pro_tree.get_children():
                                    pro_tree.delete(record)


                                sql_p="select * from auth_user where username=%s"
                                sql_p_val=(nm_ent.get(),)
                                fbcursor.execute(sql_p,sql_p_val,)
                                pr_dt=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dt[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dt=fbcursor.fetchone()

                                p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                p_val_1 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_1,p_val_1,)
                                p_data_1 = fbcursor.fetchall()
                                
                                count0 = 0
                                for i in p_data_1:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                    else:
                                        pass
                                count0 += 1

                                p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                p_val_2 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_2,p_val_2,)
                                p_data_2 = fbcursor.fetchall()

                                count1 = 0
                                for i in p_data_2:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count1 += 1

                                p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                p_val_3 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_3,p_val_3,)
                                p_data_3 = fbcursor.fetchall()
                                

                                count2 = 0
                                for i in p_data_3:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count2 += 1

                                p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                p_val_4 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_4,p_val_4,)
                                p_data_4 = fbcursor.fetchall()
                                

                                count3 = 0
                                for i in p_data_4:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                    else:
                                        pass
                                count3 += 1

                                pro_frame_2.destroy()
                                pro_frame.grid(row=0,column=0,sticky='nsew')



                            p_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('ippoly1'))

                            label_1 = Label(p_canvas_2,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel1'))

                            p_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iphline'))

                            p_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('ippoly2'))

                            p_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('ippoly3'))

                            label_1 = Label(p_canvas_2,width=10,height=2,text="INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel2'))

                            btn_item_1=Button(p_canvas_2,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
                            window_btn_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=btn_item_1, tags=('ipbutton1'))

                            label_1 = Label(p_canvas_2,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel3'))

                            entry_inv_item_1=Entry(p_canvas_2,width=200,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_entry_inv_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_1, tags=('ipentry1'))

                            label_1 = Label(p_canvas_2,width=4,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel4'))

                            def p_sku_1(event):
                                if entry_inv_item_2.get()=="N41554":
                                    entry_inv_item_2.delete(0,END)
                                else:
                                    pass
                            
                            entry_inv_item_2=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_entry_inv_item_2 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_2, tags=('ipentry2'))
                            entry_inv_item_2.insert(0,"N41554")
                            entry_inv_item_2.bind("<Button-1>",p_sku_1)


                            label_1 = Label(p_canvas_2,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel5'))

                            entry_inv_item_h2=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_entry_inv_item_h2 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_h2, tags=('ipentry3'))

                            #Define a callback function
                            def callback(url):
                                webbrowser.open_new_tab(url)

                            link_1 = Label(p_canvas_2,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
                            window_link_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=link_1, tags=('iplabel6'))
                            link_1.bind("<Button-1>", lambda e:
                            callback("https://gstcouncil.gov.in/sites/default/files/goods-rates-booklet-03July2017.pdf"))

                            label_1 = Label(p_canvas_2,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel7'))

                            comb_inv_item_u1 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                            comb_inv_item_u1['values'] = ("Choose...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards",)
                            comb_inv_item_u1.current(0)
                            window_comb_inv_item_u1 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_u1, tags=('ipcombo1'))

                            label_1 = Label(p_canvas_2,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel8'))

                            entry_inv_item_3=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_entry_inv_item_3 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_3,tags=('ipentry4'))

                            label_1 = Label(p_canvas_2,width=24,height=1,text="Initial quantity on hand", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel9'))

                            entry_inv_item_4=Entry(p_canvas_2,width=60,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_entry_inv_item_4 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_4,tags=('ipentry5'))

                            label_1 = Label(p_canvas_2,width=10,height=1,text="As of date", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel10'))
                
                            label_1 = Label(p_canvas_2,width=14,height=1,text="Low stock alert", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel11'))

                            entry_inv_item_6=Entry(p_canvas_2,width=60,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_entry_inv_item_6 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_6,tags=('ipentry6'))

                            label_1 = Label(p_canvas_2,width=22,height=1,text="Inventory asset account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(35, 910, anchor="nw", window=label_1,tags=('iplabel12'))

                            sql = "select * from auth_user where username=%s"
                            val = (nm_ent.get(),)
                            fbcursor.execute(sql,val,)
                            udtl = fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (udtl[0],)
                            fbcursor.execute(sql,val,)
                            cdtl = fbcursor.fetchone()

                            sql = "select name from app1_accounts where acctype=%s and detype=%s and cid_id=%s"
                            val = (2,'Inventory',cdtl[0],)
                            fbcursor.execute(sql,val,)
                            is_ac_data = fbcursor.fetchall()
                            ac_data_1 = ["Inventory Asset"]
                            for i in is_ac_data:
                                ac_data_1.insert(-1,i[0])

                            comb_inv_item_i2 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                            comb_inv_item_i2['values'] =(ac_data_1)
                            comb_inv_item_i2.current(0)
                            window_comb_inv_item_i2 = p_canvas_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_item_i2,tags=('ipcombo2'))

                            def inv_acc_create_1():
                                pro_frame_2.grid_forget()
                                pro_frame_2_1 = Frame(tab3_4)
                                pro_frame_2_1.grid(row=0,column=0,sticky='nsew')
                                def pro_responsive_widgets_2_1(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("iapoly1",x1 + r1,y1,
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

                                    dcanvas.coords("ialabel1",dwidth/3,dheight/8.24)
                                    dcanvas.coords("iahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.52


                                    dcanvas.coords("iapoly2",x11 + r2,y11,
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

                                    dcanvas.coords("iabutton3",dwidth/23,dheight/3.415)

                                    dcanvas.coords("ialabel2",dwidth/23,dheight/1.91)
                                    dcanvas.coords("ialabel3",dwidth/1.9,dheight/1.91)
                                    dcanvas.coords("ialabel4",dwidth/23.3,dheight/1.41)
                                    dcanvas.coords("ialabel5",dwidth/1.9,dheight/1.41)
                                    dcanvas.coords("ialabel6",dwidth/1.9,dheight/0.95)

                                    dcanvas.coords("iaentry1",dwidth/1.9,dheight/1.74)
                                    dcanvas.coords("iaentry2",dwidth/1.9,dheight/1.32)

                                    dcanvas.coords("iacombo1",dwidth/23,dheight/1.74)
                                    dcanvas.coords("iacombo2",dwidth/23,dheight/1.32)
                                    dcanvas.coords("iacombo3",dwidth/1.9,dheight/1.09)
                                    dcanvas.coords("iacombo4",dwidth/1.9,dheight/0.91)

                                    dcanvas.coords("iatext1",dwidth/23,dheight/1.15)
                                    dcanvas.coords("iacheck1",dwidth/1.9,dheight/1.155)

                                    dcanvas.coords("iabutton1",dwidth/2.3,dheight/0.73)

                                p_canvas_2_1=Canvas(pro_frame_2_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                                pro_frame_2_1.grid_columnconfigure(0,weight=1)
                                pro_frame_2_1.grid_rowconfigure(0,weight=1)
                                
                                vertibar=Scrollbar(pro_frame_2_1, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=p_canvas_2_1.yview)

                                p_canvas_2_1.bind("<Configure>", pro_responsive_widgets_2_1)
                                p_canvas_2_1.config(yscrollcommand=vertibar.set)
                                p_canvas_2_1.grid(row=0,column=0,sticky='nsew')

                                def inv_ass_acc_create_1():
                                    acctype = comb_inv_1_1.get()
                                    detype = comb_inv_1_2.get()
                                    name = entry_inv_1_2.get()
                                    description = entry_inv_1_4.get()
                                    gst = comb_inv_1_3.get()
                                    deftaxcode = comb_inv_1_4.get()
                                    balance = 0
                                    today = datetime.date.today()
                                    asof = today.strftime("%Y-%m-%d")
                                    balfordisp = 0

                                    #----------------------
                                    usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usrp_val = (nm_ent.get(),)
                                    fbcursor.execute(usrp_sql,usrp_val)
                                    usrp_data = fbcursor.fetchone()

                                    cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmpp_val = (usrp_data[0],)
                                    fbcursor.execute(cmpp_sql,cmpp_val)
                                    cmpp_data = fbcursor.fetchone()
                                    cid = cmpp_data[0]

                                    #product id --------------
                                    if acctype == "Current Assets":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (2,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data = fbcursor.fetchone()
                                    else:
                                        pass
                                    
                                    productid = product_data[0]

                                    #-------------------------
                                    acctype_sql = "SELECT accountname FROM app1_accountype WHERE accountname=%s"
                                    acctype_val = (comb_inv_1_2.get(),)
                                    fbcursor.execute(acctype_sql,acctype_val)
                                    acctype_data = fbcursor.fetchone()

                                    acct_sql = "SELECT name,cid_id FROM app1_accounts WHERE name=%s AND cid_id=%s"
                                    acct_val = (entry_inv_1_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct_sql,acct_val)
                                    acct_data = fbcursor.fetchone()

                                    acct1_sql = "SELECT name,cid_id FROM app1_accounts1 WHERE name=%s AND cid_id=%s"
                                    acct1_val = (entry_inv_1_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct1_sql,acct1_val)
                                    acct1_data = fbcursor.fetchone()
                                    print(acct1_data)

                                    if not acctype_data and not acct_data or not acct1_data:
                                        ins_acctype_sql = "INSERT INTO app1_accountype(cid_id,accountname,accountbal) VALUES(%s,%s,%s)"
                                        ins_acctype_val= (cmpp_data[0],detype,balance)
                                        fbcursor.execute(ins_acctype_sql,ins_acctype_val)
                                        finsysdb.commit()

                                        if acctype == "Current Assets":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (2,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()

                                            #--------------------------
                                            i_ac_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,deftaxcode,balance,asof,balfordisp,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            i_ac_val = (2,detype,name,description,gst,deftaxcode,balance,asof,balfordisp,cid,pro_data[0],productid)
                                            fbcursor.execute(i_ac_sql,i_ac_val)
                                            finsysdb.commit()
                                        else:
                                            pass

                                        sel_accts1_sql = "SELECT * FROM app1_accounts1 WHERE cid_id=%s"
                                        sel_accts1_val = (cid,)
                                        fbcursor.execute(sel_accts1_sql,sel_accts1_val)
                                        sel_accts1_data = fbcursor.fetchone()

                                        bal = sel_accts1_data[7] + float(balance)
                                        upd_accts1_sql = "UPDATE app1_accounts1 SET balance=%s WHERE cid_id=%s"
                                        upd_accts1_val = (bal,cid,)
                                        fbcursor.execute(upd_accts1_sql,upd_accts1_val)
                                        finsysdb.commit()

                                        pro_frame_2_1.destroy()
                                        pro_frame_2.grid(row=0,column=0,sticky='nsew')

                                p_canvas_2_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly1'))

                                label_1 = Label(p_canvas_2_1,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ialabel1'))

                                p_canvas_2_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iahline'))

                                p_canvas_2_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly2'))

                                label_1 = Label(p_canvas_2_1,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel2'))

                                comb_inv_1_1 = ttk.Combobox(p_canvas_2_1, font=('arial 10'))
                                comb_inv_1_1['values'] = ("Current Assets",)
                                comb_inv_1_1.current(0)
                                window_comb_inv_1_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_1_1,tags=('iacombo1'))         

                                label_1 = Label(p_canvas_2_1,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel4'))

                                def entry_text_1(event):
                                    if comb_inv_1_2.get() == 'Inventory':
                                        entry_inv_1_2.delete(0,END)
                                        entry_inv_1_2.insert(0,'Inventory')

                                comb_inv_1_2 = ttk.Combobox(p_canvas_2_1, font=('arial 10'))
                                comb_inv_1_2['values'] = ("Inventory",)
                                comb_inv_1_2.bind("<<ComboboxSelected>>",entry_text_1)
                                window_comb_inv_1_2 = p_canvas_2_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_1_2,tags=('iacombo2'))

                                label_1 = Label(p_canvas_2_1,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel3'))


                                entry_inv_1_2=Entry(p_canvas_2_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_inv_1_2 = p_canvas_2_1.create_window(0, 0, anchor="nw", height=30,window=entry_inv_1_2,tags=('iaentry1'))

                                label_1 = Label(p_canvas_2_1,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel5'))

                                entry_inv_1_4=Entry(p_canvas_2_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_inv_1_4 = p_canvas_2_1.create_window(0, 0, anchor="nw", height=30,window=entry_inv_1_4,tags=('iaentry2'))

                                inv_text_1 = Text(p_canvas_2_1,width=67, height=14, background='black',foreground='white')
                                inv_text_1.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                                window_inv_text_1 = p_canvas_2_1.create_window(0, 0, anchor="nw",window=inv_text_1,tags=('iatext1'))

                                def sub_check_1():
                                    comb_inv_1_3.config(state=NORMAL if chk_str_inv_1_1.get() else DISABLED)
                                    

                                chk_str_inv_1_1 = IntVar()
                                chkbtn_inv_1_1 = Checkbutton(p_canvas_2_1, text = "Is sub-account", variable = chk_str_inv_1_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=sub_check_1)
                                window_chkbtn_inv_1_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=chkbtn_inv_1_1,tags=('iacheck1'))

                                comb_inv_1_3 = ttk.Combobox(p_canvas_2_1, font=('arial 10'),state=DISABLED)
                                comb_inv_1_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                                window_comb_inv_1_3 = p_canvas_2_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_1_3,tags=('iacombo3'))

                                label_1 = Label(p_canvas_2_1,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel6'))

                                
                                comb_inv_1_4 = ttk.Combobox(p_canvas_2_1, font=('arial 10'))
                                comb_inv_1_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                                window_comb_inv_1_4 = p_canvas_2_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_1_4,tags=('iacombo4'))


                                inv_sub_btn_1_1=Button(p_canvas_2_1,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=inv_ass_acc_create_1)
                                window_inv_sub_btn_1_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=inv_sub_btn_1_1,tags=('iabutton1'))

                                def i_back_1_():
                                    pro_frame_2_1.grid_forget()
                                    pro_frame_2.grid(row=0,column=0,sticky='nsew')

                                bck_btn1=Button(p_canvas_2_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=i_back_1_)
                                window_bck_btn1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('iabutton3'))

                                

                            asset_btn=Button(p_canvas_2,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_acc_create_1)
                            window_asset_btn = p_canvas_2.create_window(0, 0, anchor="nw", window=asset_btn,tags=('ipbutton2'))

                            label_1 = Label(p_canvas_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel13'))

                            entry_inv_item_7=scrolledtext.ScrolledText(p_canvas_2,width=145,background='#2f516f',foreground="white")
                            window_entry_entry_inv_item_7 = p_canvas_2.create_window(0, 0, anchor="nw", height=60,window=entry_inv_item_7,tags=('ipentry7'))

                            label_1 = Label(p_canvas_2,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel14'))

                            def inv_tax_check():
                                if comb_inv_item_t3.get() == '28.0% GST (28%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+28)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '28.0% IGST (28%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+28)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '18.0% GST (18%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+18)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '18.0% IGST (18%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+18)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '15.0% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+15)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '14.5% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+14.5)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '14.00% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+14)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '14.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+14)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '12.36% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+12.36)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '12.0% GST (12%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+12)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '12.0% IGST (12%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+12)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '6.0% GST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '6.0% IGST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '6.0% IGST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '5.0% GST (5%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '5.0% IGST (5%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '5.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '4.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+4)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '3.0% GST (3%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+3)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '3.0% IGST (3%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+3)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '2.0% CST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+2)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '0.25% GST (O.25%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+0.25)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '0.25% IGST (0.25%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+0.25)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '0% GST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == '0% IGST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == 'Exempt GST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == 'Exempt IGST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_t3.get() == 'Out of Scope(0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_inv_item.get() == True:
                                        entry_inv_item_8.delete(0,'end')
                                        entry_inv_item_8.insert(0, np)
                                    else:
                                        pass
                                else:
                                    pass
                            
                            entry_inv_item_8=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_entry_inv_item_8 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_8,tags=('ipentry8'))
                            

                            chk_str_inv_item = BooleanVar()
                            chkbtn_inv_item_1 = Checkbutton(p_canvas_2, text = "Inclusive of tax", variable = chk_str_inv_item,  font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=inv_tax_check)
                            window_chkbtn_inv_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=chkbtn_inv_item_1,tags=('ipcbutton1'))

                            label_1 = Label(p_canvas_2,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel15'))

                            comb_inv_item_t3 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                            comb_inv_item_t3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            comb_inv_item_t3.current(0)
                            window_comb_inv_item_t3 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_t3,tags=('ipcombo3'))

                            label_1 = Label(p_canvas_2,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel16'))

                            sql = "select * from auth_user where username=%s"
                            val = (nm_ent.get(),)
                            fbcursor.execute(sql,val,)
                            udtl = fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (udtl[0],)
                            fbcursor.execute(sql,val,)
                            cdtl = fbcursor.fetchone()


                            sql = "select name from app1_accounts where acctype=%s and detype=%s and cid_id=%s"
                            val = (11,'Sales of Product Income',cdtl[0],)
                            fbcursor.execute(sql,val,)
                            in_ac_data = fbcursor.fetchall()
                            ac_data_2 = ["Choose...","Billable Expense Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales of Product Income","Uncategorised Income"]
                            for i in in_ac_data:
                                ac_data_2.insert(-1,i[0])
                            
                            

                            comb_inv_item_in4 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                            comb_inv_item_in4['values'] = (ac_data_2)
                            comb_inv_item_in4.current(0)
                            window_comb_inv_item_in4 = p_canvas_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_item_in4,tags=('ipcombo4'))

                            def inv_inc_acc_1():
                                pro_frame_2.grid_forget()
                                pro_frame_2_2 = Frame(tab3_4)
                                pro_frame_2_2.grid(row=0,column=0,sticky='nsew')

                                def pro_responsive_widgets_2_2(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("iapoly1",x1 + r1,y1,
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

                                    dcanvas.coords("ialabel1",dwidth/3,dheight/8.24)
                                    dcanvas.coords("iahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.52


                                    dcanvas.coords("iapoly2",x11 + r2,y11,
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

                                    dcanvas.coords("iabutton3",dwidth/23,dheight/3.415)

                                    dcanvas.coords("ialabel2",dwidth/23,dheight/1.91)
                                    dcanvas.coords("ialabel3",dwidth/1.9,dheight/1.91)
                                    dcanvas.coords("ialabel4",dwidth/23.3,dheight/1.41)
                                    dcanvas.coords("ialabel5",dwidth/1.9,dheight/1.41)
                                    dcanvas.coords("ialabel6",dwidth/1.9,dheight/0.95)

                                    dcanvas.coords("iaentry1",dwidth/1.9,dheight/1.74)
                                    dcanvas.coords("iaentry2",dwidth/1.9,dheight/1.32)

                                    dcanvas.coords("iacombo1",dwidth/23,dheight/1.74)
                                    dcanvas.coords("iacombo2",dwidth/23,dheight/1.32)
                                    dcanvas.coords("iacombo3",dwidth/1.9,dheight/1.09)
                                    dcanvas.coords("iacombo4",dwidth/1.9,dheight/0.91)

                                    dcanvas.coords("iatext1",dwidth/23,dheight/1.15)
                                    dcanvas.coords("iacheck1",dwidth/1.9,dheight/1.155)

                                    dcanvas.coords("iabutton1",dwidth/2.3,dheight/0.73)

                                p_canvas_2_2=Canvas(pro_frame_2_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                                pro_frame_2_2.grid_columnconfigure(0,weight=1)
                                pro_frame_2_2.grid_rowconfigure(0,weight=1)
                                
                                vertibar=Scrollbar(pro_frame_2_2, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=p_canvas_2_2.yview)

                                p_canvas_2_2.bind("<Configure>", pro_responsive_widgets_2_2)
                                p_canvas_2_2.config(yscrollcommand=vertibar.set)
                                p_canvas_2_2.grid(row=0,column=0,sticky='nsew')

                                def inv_inc_acc_create_2():
                                    acctype = comb_inv_2_1.get()
                                    detype = comb_inv_2_2.get()
                                    name = entry_inv_2_2.get()
                                    description = entry_inv_2_4.get()
                                    gst = comb_inv_2_3.get()
                                    deftaxcode = comb_inv_2_4.get()
                                    balance = 0
                                    today = datetime.date.today()
                                    asof = today.strftime("%Y-%m-%d")
                                    balfordisp = 0

                                    #----------------------
                                    usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usrp_val = (nm_ent.get(),)
                                    fbcursor.execute(usrp_sql,usrp_val)
                                    usrp_data_1 = fbcursor.fetchone()

                                    cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmpp_val = (usrp_data_1[0],)
                                    fbcursor.execute(cmpp_sql,cmpp_val)
                                    cmpp_data = fbcursor.fetchone()
                                    cid = cmpp_data[0]

                                    #product id --------------
                                    if acctype == "Income":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (11,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_1 = fbcursor.fetchone()
                                    else:
                                        pass
                                    
                                    productid = product_data_1[0]

                                    #-------------------------
                                    acctype_sql = "SELECT accountname FROM app1_accountype WHERE accountname=%s"
                                    acctype_val = (comb_inv_2_2.get(),)
                                    fbcursor.execute(acctype_sql,acctype_val)
                                    acctype_data = fbcursor.fetchone()

                                    acct_sql = "SELECT name,cid_id FROM app1_accounts WHERE name=%s AND cid_id=%s"
                                    acct_val = (entry_inv_2_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct_sql,acct_val)
                                    acct_data = fbcursor.fetchone()

                                    acct1_sql = "SELECT name,cid_id FROM app1_accounts1 WHERE name=%s AND cid_id=%s"
                                    acct1_val = (entry_inv_2_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct1_sql,acct1_val)
                                    acct1_data = fbcursor.fetchone()
                                    print(acct1_data)

                                    if not acctype_data and not acct_data or not acct1_data:
                                        ins_acctype_sql = "INSERT INTO app1_accountype(cid_id,accountname,accountbal) VALUES(%s,%s,%s)"
                                        ins_acctype_val= (cmpp_data[0],detype,balance)
                                        fbcursor.execute(ins_acctype_sql,ins_acctype_val)
                                        finsysdb.commit()

                                        if acctype == "Income":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (11,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()

                                            #--------------------------
                                            i_ac_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,deftaxcode,balance,asof,balfordisp,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            i_ac_val = (11,detype,name,description,gst,deftaxcode,balance,asof,balfordisp,cid,pro_data[0],productid)
                                            fbcursor.execute(i_ac_sql,i_ac_val)
                                            finsysdb.commit()
                                        else:
                                            pass

                                        sel_accts1_sql = "SELECT * FROM app1_accounts1 WHERE cid_id=%s"
                                        sel_accts1_val = (cid,)
                                        fbcursor.execute(sel_accts1_sql,sel_accts1_val)
                                        sel_accts1_data = fbcursor.fetchone()

                                        bal = sel_accts1_data[7] + float(balance)
                                        upd_accts1_sql = "UPDATE app1_accounts1 SET balance=%s WHERE cid_id=%s"
                                        upd_accts1_val = (bal,cid,)
                                        fbcursor.execute(upd_accts1_sql,upd_accts1_val)
                                        finsysdb.commit()

                                        pro_frame_2_2.destroy()
                                        pro_frame_2.grid(row=0,column=0,sticky='nsew')


                                p_canvas_2_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly1'))

                                label_1 = Label(p_canvas_2_2,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1, tags=('ialabel1'))

                                p_canvas_2_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iahline'))

                                p_canvas_2_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly2'))

                                label_1 = Label(p_canvas_2_2,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel2'))

                                comb_inv_2_1 = ttk.Combobox(p_canvas_2_2, font=('arial 10'))
                                comb_inv_2_1['values'] = ("Income",)
                                comb_inv_2_1.current(0)
                                window_comb_inv_2_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_2_1,tags=('iacombo1'))

                                def entry_text_2(event):
                                    if comb_inv_2_2.get() == 'Sales of Product Income':
                                        entry_inv_2_2.delete(0,END)
                                        entry_inv_2_2.insert(0,'Sales of Product Income')


                                label_1 = Label(p_canvas_2_2,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel4'))

                                comb_inv_2_2 = ttk.Combobox(p_canvas_2_2, font=('arial 10'))
                                comb_inv_2_2['values'] = ("Sales of Product Income",)
                                comb_inv_2_2.bind("<<ComboboxSelected>>",entry_text_2)
                                window_comb_inv_2_2 = p_canvas_2_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_2_2,tags=('iacombo2'))

                                label_1 = Label(p_canvas_2_2,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel3'))

                                
                                entry_inv_2_2=Entry(p_canvas_2_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_inv_2_2 = p_canvas_2_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_2_2,tags=('iaentry1'))

                                label_1 = Label(p_canvas_2_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel5'))

                                entry_inv_2_4=Entry(p_canvas_2_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_inv_2_4 = p_canvas_2_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_2_4,tags=('iaentry2'))

                                inv_text_2 = Text(p_canvas_2_2,width=67, height=14, background='black',foreground='white')
                                inv_text_2.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                                window_inv_text_2 = p_canvas_2_2.create_window(0, 0, anchor="nw",window=inv_text_2,tags=('iatext1'))

                                def sub_check_2():
                                    comb_inv_2_3.config(state=NORMAL if chk_str_inv_2_1.get() else DISABLED)

                                chk_str_inv_2_1 = IntVar()
                                chkbtn_inv_2_1 = Checkbutton(p_canvas_2_2, text = "Is sub-account", variable = chk_str_inv_2_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=sub_check_2)
                                window_chkbtn_inv_2_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=chkbtn_inv_2_1,tags=('iacheck1'))

                                comb_inv_2_3 = ttk.Combobox(p_canvas_2_2, font=('arial 10'),state=DISABLED)
                                comb_inv_2_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                                window_comb_inv_2_3 = p_canvas_2_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_2_3,tags=('iacombo3'))

                                label_1 = Label(p_canvas_2_2,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel6'))

                                comb_inv_2_4 = ttk.Combobox(p_canvas_2_2, font=('arial 10'))
                                comb_inv_2_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                                window_comb_inv_2_4 = p_canvas_2_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_2_4,tags=('iacombo4'))

                                inv_sub_btn_2_1=Button(p_canvas_2_2,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=inv_inc_acc_create_2)
                                window_inv_sub_btn_2_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=inv_sub_btn_2_1,tags=('iabutton1'))

                                def i_back_2_():
                                    pro_frame_2_2.grid_forget()
                                    pro_frame_2.grid(row=0,column=0,sticky='nsew')

                                bck_btn1=Button(p_canvas_2_2,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=i_back_2_)
                                window_bck_btn1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('iabutton3'))


                            account_btn=Button(p_canvas_2,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_inc_acc_1)
                            window_account_btn = p_canvas_2.create_window(0, 0, anchor="nw", window=account_btn,tags=('ipbutton3'))

                            p_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iphline1'))

                            label_1 = Label(p_canvas_2,width=22,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel17'))

                            entry_inv_item_9=scrolledtext.ScrolledText(p_canvas_2,width=145,background='#2f516f',foreground="white")
                            window_entry_entry_inv_item_9 = p_canvas_2.create_window(0, 0, anchor="nw", height=60,window=entry_inv_item_9,tags=('ipentry9'))

                            label_1 = Label(p_canvas_2,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel18'))

                            def inv_tax_check_1():
                                if comb_inv_item_pu5.get() == '28.0% GST (28%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+28)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '28.0% IGST (28%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+28)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '18.0% GST (18%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+18)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '18.0% IGST (18%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+18)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '15.0% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+15)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '14.5% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+14.5)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '14.00% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+14)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '14.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+14)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '12.36% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+12.36)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '12.0% GST (12%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+12)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '12.0% IGST (12%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+12)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '6.0% GST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '6.0% IGST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '6.0% IGST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '5.0% GST (5%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    print(gst)
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '5.0% IGST (5%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '5.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '4.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+4)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '3.0% GST (3%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+3)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '3.0% IGST (3%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+3)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '2.0% CST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+2)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '0.25% GST (O.25%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+0.25)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '0.25% IGST (0.25%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+0.25)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '0% GST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == '0% IGST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == 'Exempt GST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == 'Exempt IGST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_inv_item_pu5.get() == 'Out of Scope(0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_inv_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_inv_item_1.get() == True:
                                        entry_inv_item_10.delete(0,'end')
                                        entry_inv_item_10.insert(0, np)
                                    else:
                                        pass
                                else:
                                    pass
                            
                            entry_inv_item_10=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_entry_inv_item_10 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_10,tags=('ipentry10'))

                            chk_str_inv_item_1 = BooleanVar()
                            chkbtn_inv_item_2 = Checkbutton(p_canvas_2, text = "Inclusive of purchase tax", variable = chk_str_inv_item_1,font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=inv_tax_check_1)
                            window_chkbtn_inv_item_2 = p_canvas_2.create_window(0, 0, anchor="nw", window=chkbtn_inv_item_2,tags=('ipcbutton2'))

                            label_1 = Label(p_canvas_2,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(700, 1530, anchor="nw", window=label_1,tags=('iplabel19'))

                            comb_inv_item_pu5 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                            comb_inv_item_pu5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            comb_inv_item_pu5.current(0)
                            window_comb_inv_item_pu5 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_pu5,tags=('ipcombo5'))

                            label_1 = Label(p_canvas_2,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel20'))

                            sql = "select * from auth_user where username=%s"
                            val = (nm_ent.get(),)
                            fbcursor.execute(sql,val,)
                            udtl = fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (udtl[0],)
                            fbcursor.execute(sql,val,)
                            cdtl = fbcursor.fetchone()

                            sql = "select name from app1_accounts where acctype=%s and detype=%s and cid_id=%s"
                            val = (13,'Suppliers and Materials-COS',cdtl[0],)
                            fbcursor.execute(sql,val,)
                            in_ac_data = fbcursor.fetchall()
                            ac_data_3 = ["Cost of sales"]
                            for i in in_ac_data:
                                ac_data_3.insert(-1,i[0])
                        

                            comb_inv_item_ex6 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                            comb_inv_item_ex6['values'] = (ac_data_3)
                            comb_inv_item_ex6.current(0)
                            window_comb_inv_item_ex6 = p_canvas_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_item_ex6,tags=('ipcombo6'))

                            def inv_exp_acc_1():
                                pro_frame_2.grid_forget()
                                pro_frame_2_3 = Frame(tab3_4)
                                pro_frame_2_3.grid(row=0,column=0,sticky='nsew')

                                def pro_responsive_widgets_2_3(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("iapoly1",x1 + r1,y1,
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

                                    dcanvas.coords("ialabel1",dwidth/3,dheight/8.24)
                                    dcanvas.coords("iahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.52


                                    dcanvas.coords("iapoly2",x11 + r2,y11,
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

                                    dcanvas.coords("iabutton3",dwidth/23,dheight/3.415)

                                    dcanvas.coords("ialabel2",dwidth/23,dheight/1.91)
                                    dcanvas.coords("ialabel3",dwidth/1.9,dheight/1.91)
                                    dcanvas.coords("ialabel4",dwidth/23.3,dheight/1.41)
                                    dcanvas.coords("ialabel5",dwidth/1.9,dheight/1.41)
                                    dcanvas.coords("ialabel6",dwidth/1.9,dheight/0.95)

                                    dcanvas.coords("iaentry1",dwidth/1.9,dheight/1.74)
                                    dcanvas.coords("iaentry2",dwidth/1.9,dheight/1.32)

                                    dcanvas.coords("iacombo1",dwidth/23,dheight/1.74)
                                    dcanvas.coords("iacombo2",dwidth/23,dheight/1.32)
                                    dcanvas.coords("iacombo3",dwidth/1.9,dheight/1.09)
                                    dcanvas.coords("iacombo4",dwidth/1.9,dheight/0.91)

                                    dcanvas.coords("iatext1",dwidth/23,dheight/1.15)
                                    dcanvas.coords("iacheck1",dwidth/1.9,dheight/1.155)

                                    dcanvas.coords("iabutton1",dwidth/2.3,dheight/0.73)

                                p_canvas_2_3=Canvas(pro_frame_2_3, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
                                
                                pro_frame_2_3.grid_columnconfigure(0,weight=1)
                                pro_frame_2_3.grid_rowconfigure(0,weight=1)

                                vertibar=Scrollbar(pro_frame_2_3, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=p_canvas_2_3.yview)

                                p_canvas_2_3.bind("<Configure>", pro_responsive_widgets_2_3)
                                p_canvas_2_3.config(yscrollcommand=vertibar.set)
                                p_canvas_2_3.grid(row=0,column=0,sticky='nsew')

                                def inv_exp_acc_create_3():
                                    acctype = comb_inv_3_1.get()
                                    detype = comb_inv_3_2.get()
                                    name = entry_inv_3_2.get()
                                    description = entry_inv_3_4.get()
                                    gst = comb_inv_3_3.get()
                                    deftaxcode = comb_inv_3_4.get()
                                    balance = 0
                                    today = datetime.date.today()
                                    asof = today.strftime("%Y-%m-%d")
                                    balfordisp = 0

                                    #----------------------
                                    usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usrp_val = (nm_ent.get(),)
                                    fbcursor.execute(usrp_sql,usrp_val)
                                    usrp_data_1 = fbcursor.fetchone()

                                    cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmpp_val = (usrp_data_1[0],)
                                    fbcursor.execute(cmpp_sql,cmpp_val)
                                    cmpp_data = fbcursor.fetchone()
                                    cid = cmpp_data[0]

                                    #product id --------------
                                    if acctype == "Cost of Goods Sold":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (13,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_1 = fbcursor.fetchone()
                                    else:
                                        pass
                                    
                                    productid = product_data_1[0]

                                    #-------------------------
                                    acctype_sql = "SELECT accountname FROM app1_accountype WHERE accountname=%s"
                                    acctype_val = (comb_inv_3_2.get(),)
                                    fbcursor.execute(acctype_sql,acctype_val)
                                    acctype_data = fbcursor.fetchone()

                                    acct_sql = "SELECT name,cid_id FROM app1_accounts WHERE name=%s AND cid_id=%s"
                                    acct_val = (entry_inv_3_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct_sql,acct_val)
                                    acct_data = fbcursor.fetchone()

                                    acct1_sql = "SELECT name,cid_id FROM app1_accounts1 WHERE name=%s AND cid_id=%s"
                                    acct1_val = (entry_inv_3_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct1_sql,acct1_val)
                                    acct1_data = fbcursor.fetchone()
                                    print(acct1_data)

                                    if not acctype_data and not acct_data or not acct1_data:
                                        ins_acctype_sql = "INSERT INTO app1_accountype(cid_id,accountname,accountbal) VALUES(%s,%s,%s)"
                                        ins_acctype_val= (cmpp_data[0],detype,balance)
                                        fbcursor.execute(ins_acctype_sql,ins_acctype_val)
                                        finsysdb.commit()

                                        if acctype == "Cost of Goods Sold":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (13,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()

                                            #--------------------------
                                            i_ac_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,deftaxcode,balance,asof,balfordisp,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            i_ac_val = (13,detype,name,description,gst,deftaxcode,balance,asof,balfordisp,cid,pro_data[0],productid)
                                            fbcursor.execute(i_ac_sql,i_ac_val)
                                            finsysdb.commit()
                                        else:
                                            pass

                                        sel_accts1_sql = "SELECT * FROM app1_accounts1 WHERE cid_id=%s"
                                        sel_accts1_val = (cid,)
                                        fbcursor.execute(sel_accts1_sql,sel_accts1_val)
                                        sel_accts1_data = fbcursor.fetchone()

                                        bal = sel_accts1_data[7] + float(balance)
                                        upd_accts1_sql = "UPDATE app1_accounts1 SET balance=%s WHERE cid_id=%s"
                                        upd_accts1_val = (bal,cid,)
                                        fbcursor.execute(upd_accts1_sql,upd_accts1_val)
                                        finsysdb.commit()

                                        pro_frame_2_3.destroy()
                                        pro_frame_2.grid(row=0,column=0,sticky='nsew')


                                p_canvas_2_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly1'))

                                label_1 = Label(p_canvas_2_3,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1, tags=('ialabel1'))

                                p_canvas_2_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iahline'))

                                p_canvas_2_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly2'))

                                label_1 = Label(p_canvas_2_3,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel2'))

                                comb_inv_3_1 = ttk.Combobox(p_canvas_2_3, font=('arial 10'))
                                comb_inv_3_1['values'] = ("Cost of Goods Sold",)
                                comb_inv_3_1.current(0)
                                window_comb_inv_3_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_3_1,tags=('iacombo1'))

                                def entry_text_3(event):
                                    if comb_inv_3_2.get() == 'Suppliers and Materials-COS':
                                        entry_inv_3_2.delete(0,END)
                                        entry_inv_3_2.insert(0,'Suppliers and Materials-COS')



                                label_1 = Label(p_canvas_2_3,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel4'))

                                comb_inv_3_2 = ttk.Combobox(p_canvas_2_3, font=('arial 10'))
                                comb_inv_3_2['values'] = ("Suppliers and Materials-COS",)
                                comb_inv_3_2.bind("<<ComboboxSelected>>",entry_text_3)
                                window_comb_inv_3_2 = p_canvas_2_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_3_2,tags=('iacombo2'))

                                label_1 = Label(p_canvas_2_3,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel3'))

                                
                                entry_inv_3_2=Entry(p_canvas_2_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_inv_3_2 = p_canvas_2_3.create_window(0, 0, anchor="nw", height=30,window=entry_inv_3_2,tags=('iaentry1'))

                                label_1 = Label(p_canvas_2_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel5'))

                                entry_inv_3_4=Entry(p_canvas_2_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_inv_3_4 = p_canvas_2_3.create_window(0, 0, anchor="nw", height=30,window=entry_inv_3_4,tags=('iaentry2'))

                                inv_text_3 = Text(p_canvas_2_3,width=67, height=14, background='black',foreground='white')
                                inv_text_3.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                                window_inv_text_3 = p_canvas_2_3.create_window(0, 0, anchor="nw",window=inv_text_3,tags=('iatext1'))

                                def sub_check_3():
                                    comb_inv_3_3.config(state=NORMAL if chk_str_inv_3_1.get() else DISABLED)
                                    

                                chk_str_inv_3_1 = IntVar()
                                chkbtn_inv_3_1 = Checkbutton(p_canvas_2_3, text = "Is sub-account", variable = chk_str_inv_3_1,  font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=sub_check_3)
                                window_chkbtn_inv_3_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=chkbtn_inv_3_1,tags=('iacheck1'))

                                comb_inv_3_3 = ttk.Combobox(p_canvas_2_3, font=('arial 10'),state=DISABLED)
                                comb_inv_3_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                                window_comb_inv_3_3 = p_canvas_2_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_3_3,tags=('iacombo3'))

                                label_1 = Label(p_canvas_2_3,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel6'))

                                comb_inv_3_4 = ttk.Combobox(p_canvas_2_3, font=('arial 10'))
                                comb_inv_3_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                                window_comb_inv_3_4 = p_canvas_2_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_3_4,tags=('iacombo4'))

                                inv_sub_btn_3_1=Button(p_canvas_2_3,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=inv_exp_acc_create_3)
                                window_inv_sub_btn_3_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=inv_sub_btn_3_1,tags=('iabutton1'))

                                def i_back_3_():
                                    pro_frame_2_3.grid_forget()
                                    pro_frame_2.grid(row=0,column=0,sticky='nsew')

                                bck_btn3=Button(p_canvas_2_3,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=i_back_3_)
                                window_bck_btn3 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=bck_btn3,tags=('iabutton3'))


                            expense_btn=Button(p_canvas_2,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_exp_acc_1)
                            window_expense_btn = p_canvas_2.create_window(0, 0, anchor="nw", window=expense_btn,tags=('ipbutton4'))

                            label_1 = Label(p_canvas_2,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel21'))

                            def p_rc_1(event):
                                if entry_inv_item_11.get()=="0":
                                    entry_inv_item_11.delete(0,END)
                                else:
                                    pass

                            entry_inv_item_11=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_entry_inv_item_11 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_11,tags=('ipentry11'))
                            entry_inv_item_11.insert(0,"0")
                            entry_inv_item_11.bind("<Button-1>",p_rc_1)

                            label_1 = Label(p_canvas_2,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel22'))

                            comb_inv_item_pr7 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                            comb_inv_item_pr7['values'] = ("Select Supplier",)
                            comb_inv_item_pr7.current(0)
                            window_comb_inv_item_pr7 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_pr7,tags=('ipcombo7'))

                            inv_sub_btn1=Button(p_canvas_2,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_new_pro_inv)
                            window_inv_sub_btn1 = p_canvas_2.create_window(0, 0, anchor="nw", window=inv_sub_btn1,tags=('ipbutton5'))

                            entry_inv_item_aod5=DateEntry(p_canvas_2,width=60,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_inv_item_aod5 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_aod5,tags=('ipdate1'))


                        p_btn_1=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=inv_add_item)
                        window_p_btn_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_1,tags=('apbutton1'),state=HIDDEN)

                        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly4"))

                        def noncall(event):
                            p_canvas_1.itemconfig('apimage2',state='hidden')
                            p_canvas_1.itemconfig('aplabel4',state='normal')
                            p_canvas_1.itemconfig('aplabel5',state='normal')
                            p_canvas_1.itemconfig('apbutton2',state='normal')

                        image_n1 = Image.open("images/noninventory.png")
                        resize_image = image_n1.resize((200,150))
                        image_n1 = ImageTk.PhotoImage(resize_image)
                        btlogon = Label(p_canvas_1, width=200, height=150, background="#1b3857", image = image_n1) 
                        window_image = p_canvas_1.create_window(0, 0, anchor="nw", window=btlogon,tags=('apimage2'))
                        btlogon.photo = image_n1
                        btlogon.bind("<Button-1>",noncall)


                        label_1 = Label(p_canvas_1,width=11,height=1,text="Non-Inventory", font=('arial 20'),background="#2f516f",fg="white") 
                        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel4'),state=HIDDEN)

                        label_1 = Label(p_canvas_1,width=46,height=2,text="A non-inventory is a type of product that is procured, sold, \nconsumed in production but we do not keep inventories for it.", font=('arial 12'),background="#2f516f",fg="white") 
                        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel5'),state=HIDDEN)

                        def non_add_item():
                            pro_frame_1.grid_forget()
                            pro_frame_3 = Frame(tab3_4)
                            pro_frame_3.grid(row=0,column=0,sticky='nsew')
                            def pro_responsive_widgets_3(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("nppoly1",x1 + r1,y1,
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

                                dcanvas.coords("nplabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("nphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.29


                                dcanvas.coords("nppoly2",x11 + r2,y11,
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

                                r2 = 25
                                x11 = dwidth/24
                                x21 = dwidth/1.050
                                y11 = dheight/2.1
                                y21 = dheight/1.35


                                dcanvas.coords("nppoly3",x11 + r2,y11,
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

                                dcanvas.coords("nplabel2",dwidth/3,dheight/1.77)
                                dcanvas.coords("npbutton1",dwidth/1.8,dheight/1.77)

                                dcanvas.coords("nplabel3",dwidth/23.2,dheight/1.23)
                                dcanvas.coords("nplabel4",dwidth/23.3,dheight/1.02)
                                dcanvas.coords("nplabel5",dwidth/1.9,dheight/1.02)
                                dcanvas.coords("nplabel6",dwidth/1.9,dheight/0.92)
                                dcanvas.coords("nplabel7",dwidth/27,dheight/0.865)
                                dcanvas.coords("nplabel8",dwidth/1.915,dheight/0.865)
                                dcanvas.coords("nplabel12",dwidth/26,dheight/0.675)
                                dcanvas.coords("nplabel13",dwidth/26.8,dheight/0.606)
                                dcanvas.coords("nplabel14",dwidth/28.3,dheight/0.538)
                                dcanvas.coords("nplabel15",dwidth/1.9,dheight/0.538)
                                dcanvas.coords("nplabel16",dwidth/28.4,dheight/0.485)
                                dcanvas.coords("nplabel17",dwidth/50,dheight/0.438)
                                dcanvas.coords("nplabel18",dwidth/26,dheight/0.420)
                                dcanvas.coords("nplabel20",dwidth/28,dheight/0.368)
                                dcanvas.coords("nplabel21",dwidth/2.6,dheight/0.368)
                                dcanvas.coords("nplabel22",dwidth/1.5,dheight/0.368)

                                dcanvas.coords("nplabel9",dwidth/23.2,dheight/0.392)
                                dcanvas.coords("nplabel10",dwidth/1.9,dheight/0.392)


                                dcanvas.coords("npentry1",dwidth/23.2,dheight/1.165)
                                dcanvas.coords("npentry2",dwidth/23.2,dheight/0.975)
                                dcanvas.coords("npentry3",dwidth/1.9,dheight/0.975)
                                dcanvas.coords("npentry4",dwidth/1.9,dheight/0.83)
                                dcanvas.coords("npentry7",dwidth/23.2,dheight/0.59)
                                dcanvas.coords("npentry8",dwidth/23.2,dheight/0.525)
                                dcanvas.coords("npentry9",dwidth/23.2,dheight/0.43)
                                dcanvas.coords("npentry10",dwidth/23.2,dheight/0.412)
                                dcanvas.coords("npentry11",dwidth/2.6,dheight/0.362)

                                dcanvas.coords("npcentry2",dwidth/23.2,dheight/0.385)
                                dcanvas.coords("npcentry3",dwidth/1.9,dheight/0.385)

                                dcanvas.coords("npcombo1",dwidth/23.2,dheight/0.83)
                                dcanvas.coords("npcombo3",dwidth/1.9,dheight/0.525)
                                dcanvas.coords("npcombo4",dwidth/23.2,dheight/0.474)
                                dcanvas.coords("npcombo6",dwidth/23.2,dheight/0.362)
                                dcanvas.coords("npcombo7",dwidth/1.5,dheight/0.362)

                                dcanvas.coords("npbutton2",dwidth/23.2,dheight/0.654)
                                dcanvas.coords("npbutton3",dwidth/2.45,dheight/0.474)
                                dcanvas.coords("npbutton4",dwidth/3.37,dheight/0.362)
                                dcanvas.coords("npbutton5",dwidth/2.38,dheight/0.345)

                                dcanvas.coords("npcbutton1",dwidth/23.2,dheight/0.51)
                                dcanvas.coords("npcbutton2",dwidth/23.2,dheight/0.378)

                                dcanvas.coords("npline1",dwidth/21,dheight/0.73,dwidth/1.055,dheight/0.73)
                                dcanvas.coords("nphline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)


                            p_canvas_3=Canvas(pro_frame_3, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_3.grid_columnconfigure(0,weight=1)
                            pro_frame_3.grid_rowconfigure(0,weight=1)
                        
                            vertibar=Scrollbar(pro_frame_3, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_3.yview)

                            p_canvas_3.bind("<Configure>", pro_responsive_widgets_3)
                            p_canvas_3.config(yscrollcommand=vertibar.set)
                            p_canvas_3.grid(row=0,column=0,sticky='nsew')

                            def add_new_pro_non():
                                name = entry_non_item_1.get()
                                sku = entry_non_iitem_2.get()
                                hsn = entry_non_item_2.get()
                                unit = comb_inv_item_1.get()
                                category = entry_non_item_3.get()
                                descr = entry_non_item_7.get('1.0', 'end-1c')
                                saleprice = entry_non_item_8.get()
                                income = comb_non_item_4.get()
                                tax = comb_non_item_3.get()
                                purchasedescr = entry_non_item_9.get('1.0', 'end-1c')
                                cost = entry_non_item_10.get()
                                expenseaccount = comb_non_item_6.get()
                                purchasetax = comb_non_item_5.get()
                                revcharge = entry_non_item_11.get()
                                presupplier = comb_non_item_7.get()

                                usrp1_sql = "SELECT id FROM auth_user WHERE username=%s"
                                usrp1_val = (nm_ent.get(),)
                                fbcursor.execute(usrp1_sql,usrp1_val)
                                usrp1_data = fbcursor.fetchone()

                                cmpp1_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                cmpp1_val = (usrp1_data[0],)
                                fbcursor.execute(cmpp1_sql,cmpp1_val)
                                cmpp1_data = fbcursor.fetchone()
                                cid = cmpp1_data[0]

                                n_p_sql = "INSERT INTO app1_noninventory(name,sku,hsn,unit,category,descr,saleprice,income,tax,purchasedescr,cost,expenseaccount,purchasetax,revcharge,presupplier,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                n_p_val = (name,sku,hsn,unit,category,descr,saleprice,income,tax,purchasedescr,cost,expenseaccount,purchasetax,revcharge,presupplier,cid)
                                fbcursor.execute(n_p_sql,n_p_val)
                                finsysdb.commit()

                                #_________Refresh insert tree________#

                                for record in pro_tree.get_children():
                                    pro_tree.delete(record)

        
                                sql_p="select * from auth_user where username=%s"
                                sql_p_val=(nm_ent.get(),)
                                fbcursor.execute(sql_p,sql_p_val,)
                                pr_dt=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dt[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dt=fbcursor.fetchone()

                                p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                p_val_1 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_1,p_val_1,)
                                p_data_1 = fbcursor.fetchall()
                                
                                count0 = 0
                                for i in p_data_1:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                    else:
                                        pass
                                count0 += 1

                                p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                p_val_2 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_2,p_val_2,)
                                p_data_2 = fbcursor.fetchall()

                                count1 = 0
                                for i in p_data_2:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count1 += 1

                                p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                p_val_3 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_3,p_val_3,)
                                p_data_3 = fbcursor.fetchall()
                                

                                count2 = 0
                                for i in p_data_3:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count2 += 1

                                p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                p_val_4 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_4,p_val_4,)
                                p_data_4 = fbcursor.fetchall()
                                

                                count3 = 0
                                for i in p_data_4:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                    else:
                                        pass
                                count3 += 1

                                pro_frame_3.destroy()
                                pro_frame.grid(row=0,column=0,sticky='nsew')
                                


                            p_canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('nppoly1'))

                            label_1 = Label(p_canvas_3,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel1'))

                            p_canvas_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('nphline'))

                            p_canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('nppoly2'))

                            p_canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('nppoly3'))

                            label_1 = Label(p_canvas_3,width=15,height=2,text="NON-INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel2'))

                            btn_non_item_2=Button(p_canvas_3,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
                            window_btn_non_item_2 = p_canvas_3.create_window(0, 0, anchor="nw", window=btn_non_item_2, tags=('npbutton1'))

                            label_1 = Label(p_canvas_3,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel3'))

                            entry_non_item_1=Entry(p_canvas_3,width=200,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_non_item_1 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_1, tags=('npentry1'))

                            label_1 = Label(p_canvas_3,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel4'))

                            def ps_2(event):
                                if entry_non_iitem_2.get()=="N41554":
                                    entry_non_iitem_2.delete(0,END)
                                else:
                                    pass

                            entry_non_iitem_2=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_non_iitem_2 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_iitem_2, tags=('npentry2'))
                            entry_non_iitem_2.insert(0,"N41554")
                            entry_non_iitem_2.bind("<Button-1>",ps_2)

                            label_1 = Label(p_canvas_3,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel5'))

                            entry_non_item_2=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_non_item_2 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_2, tags=('npentry3'))

                            #Define a callback function
                            def callback_1(url):
                                webbrowser.open_new_tab(url)

                            link_2 = Label(p_canvas_3,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
                            window_link_2 = p_canvas_3.create_window(0, 0, anchor="nw", window=link_2, tags=('nplabel6'))
                            link_2.bind("<Button-1>", lambda e:
                            callback_1("https://gstcouncil.gov.in/sites/default/files/goods-rates-booklet-03July2017.pdf"))


                            label_1 = Label(p_canvas_3,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel7'))

                            comb_inv_item_1 = ttk.Combobox(p_canvas_3, font=('arial 10'))
                            comb_inv_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards","OTH Others",)
                            comb_inv_item_1.current(0)
                            window_comb_inv_item_1 = p_canvas_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_1, tags=('npcombo1'))

                            label_1 = Label(p_canvas_3,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel8'))

                            entry_non_item_3=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_inv_item_3 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_3,tags=('npentry4'))

                            p_canvas_3.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('npline1'))

                            label_1 = Label(p_canvas_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel12'))


                            def d_non_check():

                                if chk_str_non_item.get() == True:
                                    p_canvas_3.itemconfig('nplabel13',state='normal')
                                    p_canvas_3.itemconfig('npentry7',state='normal')
                                    p_canvas_3.itemconfig('nplabel14',state='normal')
                                    p_canvas_3.itemconfig('npentry8',state='normal')
                                    p_canvas_3.itemconfig('npcbutton1',state='normal')
                                    p_canvas_3.itemconfig('nplabel15',state='normal')
                                    p_canvas_3.itemconfig('npcombo3',state='normal')
                                    p_canvas_3.itemconfig('nplabel16',state='normal')
                                    p_canvas_3.itemconfig('npcombo4',state='normal')
                                    p_canvas_3.itemconfig('npbutton3',state='normal')
                                else:
                                    pass                     


                            chk_str_non_item = BooleanVar()
                            chkbtn_non_item = Checkbutton(p_canvas_3, text = "I sell this product/service to my customers.", variable = chk_str_non_item, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=d_non_check)
                            window_chkbtn_non_item = p_canvas_3.create_window(0, 0, anchor="nw", window=chkbtn_non_item,tags=('npbutton2'))

                            label_1 = Label(p_canvas_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel13'),state=HIDDEN)

                            entry_non_item_7=scrolledtext.ScrolledText(p_canvas_3,width=145,background='#2f516f',foreground="white")
                            window_entry_non_item_7 = p_canvas_3.create_window(0, 0, anchor="nw", height=60,window=entry_non_item_7,tags=('npentry7'),state=HIDDEN)

                            label_1 = Label(p_canvas_3,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel14'),state=HIDDEN)

                            def non_tax_check():
                                if comb_non_item_3.get() == '28.0% GST (28%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+28)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '28.0% IGST (28%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+28)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '18.0% GST (18%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+18)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '18.0% IGST (18%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+18)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '15.0% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+15)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '14.5% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+14.5)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '14.00% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+14)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '14.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+14)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '12.36% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+12.36)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '12.0% GST (12%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+12)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '12.0% IGST (12%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+12)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '6.0% GST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '6.0% IGST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '6.0% IGST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '5.0% GST (5%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '5.0% IGST (5%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '5.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '4.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+4)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '3.0% GST (3%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+3)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '3.0% IGST (3%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+3)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '2.0% CST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+2)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '0.25% GST (O.25%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+0.25)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '0.25% IGST (0.25%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+0.25)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '0% GST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == '0% IGST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == 'Exempt GST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == 'Exempt IGST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_3.get() == 'Out of Scope(0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_non_item_1.get() == True:
                                        entry_non_item_8.delete(0,'end')
                                        entry_non_item_8.insert(0, np)
                                    else:
                                        pass
                                else:
                                    pass
                            
                            entry_non_item_8=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_non_item_8 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_8,tags=('npentry8'),state=HIDDEN)

                            chk_str_non_item_1 = BooleanVar()
                            chkbtn_non_item_1 = Checkbutton(p_canvas_3, text = "Inclusive of tax", variable = chk_str_non_item_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=non_tax_check)
                            window_chkbtn_non_item_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=chkbtn_non_item_1,tags=('npcbutton1'),state=HIDDEN)

                            label_1 = Label(p_canvas_3,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel15'),state=HIDDEN)

                            comb_non_item_3 = ttk.Combobox(p_canvas_3, font=('arial 10'))
                            comb_non_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            #comb_non_item_3.current(0)
                            window_comb_non_item_3 = p_canvas_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_item_3,tags=('npcombo3'),state=HIDDEN)

                            label_1 = Label(p_canvas_3,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel16'),state=HIDDEN)

                            sql = "select * from auth_user where username=%s"
                            val = (nm_ent.get(),)
                            fbcursor.execute(sql,val,)
                            udtl = fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (udtl[0],)
                            fbcursor.execute(sql,val,)
                            cdtl = fbcursor.fetchone()


                            sql = "select name from app1_accounts where acctype=%s and cid_id=%s"
                            val = (11,cdtl[0],)
                            fbcursor.execute(sql,val,)
                            non_in_ac_data = fbcursor.fetchall()
                            ac_data_4 = ["Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discount","Sales of Product Income","Services","Unapplied Cash Payment Income","Uncategorised Income"]
                            for i in non_in_ac_data:
                                ac_data_4.insert(-1,i[0])
                            

                            comb_non_item_4 = ttk.Combobox(p_canvas_3, font=('arial 10'))
                            comb_non_item_4['values'] = (ac_data_4)
                            window_comb_non_item_4 = p_canvas_3.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_non_item_4,tags=('npcombo4'),state=HIDDEN)

                            def non_inc_acc_1():
                                pro_frame_3.grid_forget()
                                pro_frame_3_1 = Frame(tab3_4)
                                pro_frame_3_1.grid(row=0,column=0,sticky='nsew')

                                def pro_responsive_widgets_non_1(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("napoly1",x1 + r1,y1,
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

                                    dcanvas.coords("nalabel1",dwidth/3,dheight/8.24)
                                    dcanvas.coords("nahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.52


                                    dcanvas.coords("napoly2",x11 + r2,y11,
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

                                    dcanvas.coords("nabutton3",dwidth/23,dheight/3.415)

                                    dcanvas.coords("nalabel2",dwidth/23,dheight/1.91)
                                    dcanvas.coords("nalabel3",dwidth/1.9,dheight/1.91)
                                    dcanvas.coords("nalabel4",dwidth/23.3,dheight/1.41)
                                    dcanvas.coords("nalabel5",dwidth/1.9,dheight/1.41)
                                    dcanvas.coords("nalabel6",dwidth/1.9,dheight/0.95)

                                    dcanvas.coords("naentry1",dwidth/1.9,dheight/1.74)
                                    dcanvas.coords("naentry2",dwidth/1.9,dheight/1.32)

                                    dcanvas.coords("nacombo1",dwidth/23,dheight/1.74)
                                    dcanvas.coords("nacombo2",dwidth/23,dheight/1.32)
                                    dcanvas.coords("nacombo3",dwidth/1.9,dheight/1.09)
                                    dcanvas.coords("nacombo4",dwidth/1.9,dheight/0.91)

                                    dcanvas.coords("natext1",dwidth/23,dheight/1.15)
                                    dcanvas.coords("nacheck1",dwidth/1.9,dheight/1.155)

                                    dcanvas.coords("nabutton1",dwidth/2.3,dheight/0.73)

                                p_canvas_3_1=Canvas(pro_frame_3_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                                pro_frame_3_1.grid_columnconfigure(0,weight=1)
                                pro_frame_3_1.grid_rowconfigure(0,weight=1)
                                
                                vertibar=Scrollbar(pro_frame_3_1, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=p_canvas_3_1.yview)

                                p_canvas_3_1.bind("<Configure>", pro_responsive_widgets_non_1)
                                p_canvas_3_1.config(yscrollcommand=vertibar.set)
                                p_canvas_3_1.grid(row=0,column=0,sticky='nsew')


                                def non_inc_acc_create_1():
                                    acctype = comb_non_2_1.get()
                                    detype = comb_non_2_2.get()
                                    name = entry_non_2_2.get()
                                    description = entry_non_2_4.get()
                                    gst = comb_non_2_3.get()
                                    deftaxcode = comb_non_2_4.get()
                                    balance = 0
                                    today = datetime.date.today()
                                    asof = today.strftime("%Y-%m-%d")
                                    balfordisp = 0

                                    #----------------------
                                    usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usrp_val = (nm_ent.get(),)
                                    fbcursor.execute(usrp_sql,usrp_val)
                                    usrp_data_1 = fbcursor.fetchone()

                                    cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmpp_val = (usrp_data_1[0],)
                                    fbcursor.execute(cmpp_sql,cmpp_val)
                                    cmpp_data = fbcursor.fetchone()
                                    cid = cmpp_data[0]

                                    #product id --------------
                                    if acctype == "Income":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (11,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_1 = fbcursor.fetchone()
                                    else:
                                        pass
                                    
                                    productid = product_data_1[0]

                                    #-------------------------
                                    acctype_sql = "SELECT accountname FROM app1_accountype WHERE accountname=%s"
                                    acctype_val = (comb_non_2_2.get(),)
                                    fbcursor.execute(acctype_sql,acctype_val)
                                    acctype_data = fbcursor.fetchone()

                                    acct_sql = "SELECT name,cid_id FROM app1_accounts WHERE name=%s AND cid_id=%s"
                                    acct_val = (entry_non_2_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct_sql,acct_val)
                                    acct_data = fbcursor.fetchone()

                                    acct1_sql = "SELECT name,cid_id FROM app1_accounts1 WHERE name=%s AND cid_id=%s"
                                    acct1_val = (entry_non_2_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct1_sql,acct1_val)
                                    acct1_data = fbcursor.fetchone()
                                    print(acct1_data)

                                    if not acctype_data and not acct_data or not acct1_data:
                                        ins_acctype_sql = "INSERT INTO app1_accountype(cid_id,accountname,accountbal) VALUES(%s,%s,%s)"
                                        ins_acctype_val= (cmpp_data[0],detype,balance)
                                        fbcursor.execute(ins_acctype_sql,ins_acctype_val)
                                        finsysdb.commit()

                                        if acctype == "Income":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (11,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()

                                            #--------------------------
                                            i_ac_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,deftaxcode,balance,asof,balfordisp,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            i_ac_val = (11,detype,name,description,gst,deftaxcode,balance,asof,balfordisp,cid,pro_data[0],productid)
                                            fbcursor.execute(i_ac_sql,i_ac_val)
                                            finsysdb.commit()
                                        else:
                                            pass

                                        sel_accts1_sql = "SELECT * FROM app1_accounts1 WHERE cid_id=%s"
                                        sel_accts1_val = (cid,)
                                        fbcursor.execute(sel_accts1_sql,sel_accts1_val)
                                        sel_accts1_data = fbcursor.fetchone()

                                        bal = sel_accts1_data[7] + float(balance)
                                        upd_accts1_sql = "UPDATE app1_accounts1 SET balance=%s WHERE cid_id=%s"
                                        upd_accts1_val = (bal,cid,)
                                        fbcursor.execute(upd_accts1_sql,upd_accts1_val)
                                        finsysdb.commit()

                                        pro_frame_3_1.destroy()
                                        pro_frame_3.grid(row=0,column=0,sticky='nsew')


                                
                                p_canvas_3_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('napoly1'))

                                label_1 = Label(p_canvas_3_1,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1, tags=('nalabel1'))

                                p_canvas_3_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('nahline'))

                                p_canvas_3_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('napoly2'))

                                label_1 = Label(p_canvas_3_1,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel2'))

                                comb_non_2_1 = ttk.Combobox(p_canvas_3_1, font=('arial 10') )
                                comb_non_2_1['values'] = ("Income",)
                                comb_non_2_1.current(0)
                                window_comb_non_2_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_2_1,tags=('nacombo1'))


                                label_1 = Label(p_canvas_3_1,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel4'))

                                def entry_text_4(event):
                                    if comb_non_2_2.get() == 'Discounts/Refunds Given':
                                        entry_non_2_2.delete(0,END)
                                        entry_non_2_2.insert(0,'Discounts/Refunds Given')
                                    elif comb_non_2_2.get() == 'Non-Profit Income':
                                        entry_non_2_2.delete(0,END)
                                        entry_non_2_2.insert(0,'Non-Profit Income')
                                    elif comb_non_2_2.get() == 'Other Primary Income':
                                        entry_non_2_2.delete(0,END)
                                        entry_non_2_2.insert(0,'Other Primary Income')
                                    elif comb_non_2_2.get() == 'Revenue-General':
                                        entry_non_2_2.delete(0,END)
                                        entry_non_2_2.insert(0,'Revenue-General')
                                    elif comb_non_2_2.get() == 'Sales-Retail':
                                        entry_non_2_2.delete(0,END)
                                        entry_non_2_2.insert(0,'Sales-Retail')
                                    elif comb_non_2_2.get() == 'Sales-Wholesale':
                                        entry_non_2_2.delete(0,END)
                                        entry_non_2_2.insert(0,'Sales-Wholesale')
                                    elif comb_non_2_2.get() == 'Sales of Product Income':
                                        entry_non_2_2.delete(0,END)
                                        entry_non_2_2.insert(0,'Sales of Product Income')
                                    elif comb_non_2_2.get() == 'Service/Fee Income':
                                        entry_non_2_2.delete(0,END)
                                        entry_non_2_2.insert(0,'Service/Fee Income')
                                    elif comb_non_2_2.get() == 'Unapplied Cash Payment Inncome':
                                        entry_non_2_2.delete(0,END)
                                        entry_non_2_2.insert(0,'Unapplied Cash Payment Inncome')
                                    else:
                                        pass
                                
                                comb_non_2_2 = ttk.Combobox(p_canvas_3_1, font=('arial 10'))
                                comb_non_2_2['values'] = ("Discounts/Refunds Given","Non-Profit Income","Other Primary Income","Revenue-General","Sales-Retail","Sales-Wholesale","Sales of Product Income","Service/Fee Income","Unapplied Cash Payment Inncome",)
                                # comb_non_2_2.current(0)
                                comb_non_2_2.bind("<<ComboboxSelected>>",entry_text_4)
                                window_comb_non_2_2 = p_canvas_3_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_2_2,tags=('nacombo2'))

                                label_1 = Label(p_canvas_3_1,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel3')) 
                                
                                entry_non_2_2=Entry(p_canvas_3_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_non_2_2 = p_canvas_3_1.create_window(0, 0, anchor="nw", height=30,window=entry_non_2_2,tags=('naentry1'))
                                

                                label_1 = Label(p_canvas_3_1,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel5'))

                                entry_non_2_4=Entry(p_canvas_3_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_non_2_4 = p_canvas_3_1.create_window(0, 0, anchor="nw", height=30,window=entry_non_2_4,tags=('naentry2'))

                                non_text_2 = Text(p_canvas_3_1,width=67, height=14, background='black',foreground='white')
                                non_text_2.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                                window_non_text_2 = p_canvas_3_1.create_window(0, 0, anchor="nw",window=non_text_2,tags=('natext1'))

                                def sub_check_4():
                                    comb_non_2_3.config(state=NORMAL if chk_str_non_2_1.get() else DISABLED)

                                chk_str_non_2_1 = IntVar()
                                chkbtn_non_2_1 = Checkbutton(p_canvas_3_1, text = "Is sub-account", variable = chk_str_non_2_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=sub_check_4)
                                window_chkbtn_non_2_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=chkbtn_non_2_1,tags=('nacheck1'))

                                comb_non_2_3 = ttk.Combobox(p_canvas_3_1, font=('arial 10'),state=DISABLED)
                                comb_non_2_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                                window_comb_non_2_3 = p_canvas_3_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_2_3,tags=('nacombo3'))

                                label_1 = Label(p_canvas_3_1,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel6'))

                                comb_non_2_4 = ttk.Combobox(p_canvas_3_1, font=('arial 10'))
                                comb_non_2_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                                window_comb_non_2_4 = p_canvas_3_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_2_4,tags=('nacombo4'))

                                non_sub_btn_2_1=Button(p_canvas_3_1,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=non_inc_acc_create_1)
                                window_non_sub_btn_2_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=non_sub_btn_2_1,tags=('nabutton1'))

                                def n_back_1_():
                                    pro_frame_3_1.grid_forget()
                                    pro_frame_3.grid(row=0,column=0,sticky='nsew')

                                nbck_btn1=Button(p_canvas_3_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=n_back_1_)
                                window_nbck_btn1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=nbck_btn1,tags=('nabutton3'))

                            account_non_btn=Button(p_canvas_3,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=non_inc_acc_1)
                            window_account_non_btn = p_canvas_3.create_window(0, 0, anchor="nw", window=account_non_btn,tags=('npbutton3'),state=HIDDEN)

                            p_canvas_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('nphline1'))

                            label_1 = Label(p_canvas_3,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(26, 1300, anchor="nw", window=label_1,tags=('nplabel17'))

                            def p_non_check():
                                
                                if chk_str_non_pitem.get() == True:
                                    p_canvas_3.itemconfig('nplabel18',state='normal')
                                    p_canvas_3.itemconfig('npentry10',state='normal')
                                    p_canvas_3.itemconfig('nplabel9',state='normal')
                                    p_canvas_3.itemconfig('npcentry2',state='normal')
                                    p_canvas_3.itemconfig('npcbutton2',state='normal')
                                    p_canvas_3.itemconfig('nplabel10',state='normal')
                                    p_canvas_3.itemconfig('npcentry3',state='normal')
                                    p_canvas_3.itemconfig('nplabel20',state='normal')
                                    p_canvas_3.itemconfig('npcombo6',state='normal')
                                    p_canvas_3.itemconfig('npbutton4',state='normal')
                                    p_canvas_3.itemconfig('nplabel21',state='normal')
                                    p_canvas_3.itemconfig('npentry11',state='normal')
                                    p_canvas_3.itemconfig('nplabel22',state='normal')
                                    p_canvas_3.itemconfig('npcombo7',state='normal')
                                else:
                                    pass

                            chk_str_non_pitem = BooleanVar()
                            chkbtn_non_pitem = Checkbutton(p_canvas_3, text = "I Purchase this product/service from Supplier.", variable = chk_str_non_pitem, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=p_non_check)
                            window_chkbtn_non_pitem = p_canvas_3.create_window(0, 0, anchor="nw", window=chkbtn_non_pitem,tags=('npentry9'))


                            label_1 = Label(p_canvas_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel18'),state=HIDDEN)

                            entry_non_item_9=scrolledtext.ScrolledText(p_canvas_3,width=145,background='#2f516f',foreground="white")
                            window_entry_non_item_9 = p_canvas_3.create_window(0, 0, anchor="nw", height=60,window=entry_non_item_9,tags=('npentry10'),state=HIDDEN)

                            label_1 = Label(p_canvas_3,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel9'),state=HIDDEN)

                            def non_tax_check_1():
                                if comb_non_item_5.get() == '28.0% GST (28%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+28)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '28.0% IGST (28%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+28)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '18.0% GST (18%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+18)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '18.0% IGST (18%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+18)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '15.0% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+15)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '14.5% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+14.5)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '14.00% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+14)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '14.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+14)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '12.36% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+12.36)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '12.0% GST (12%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+12)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '12.0% IGST (12%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+12)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '6.0% GST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '6.0% IGST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '6.0% IGST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '5.0% GST (5%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '5.0% IGST (5%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '5.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '4.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+4)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '3.0% GST (3%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+3)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '3.0% IGST (3%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+3)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '2.0% CST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+2)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '0.25% GST (O.25%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+0.25)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '0.25% IGST (0.25%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+0.25)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '0% GST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == '0% IGST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == 'Exempt GST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == 'Exempt IGST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_non_item_5.get() == 'Out of Scope(0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_non_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_non_item_2.get() == True:
                                        entry_non_item_10.delete(0,'end')
                                        entry_non_item_10.insert(0, np)
                                    else:
                                        pass
                                else:
                                    pass
                            
                            entry_non_item_10=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_non_item_10 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_10,tags=('npcentry2'),state=HIDDEN)

                            chk_str_non_item_2 = BooleanVar()
                            chkbtn_non_item_2 = Checkbutton(p_canvas_3, text = "Inclusive of purchase tax", variable = chk_str_non_item_2, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=non_tax_check_1)
                            window_chkbtn_non_item_2 = p_canvas_3.create_window(0, 0, anchor="nw", window=chkbtn_non_item_2,tags=('npcbutton2'),state=HIDDEN)

                            label_1 = Label(p_canvas_3,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel10'),state=HIDDEN)

                            comb_non_item_5 = ttk.Combobox(p_canvas_3, font=('arial 10'))
                            comb_non_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            #comb_non_item_5.current(0)
                            window_comb_non_item_5 = p_canvas_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_item_5,tags=('npcentry3'),state=HIDDEN)

                            label_1 = Label(p_canvas_3,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel20'),state=HIDDEN)

                            sql = "select * from auth_user where username=%s"
                            val = (nm_ent.get(),)
                            fbcursor.execute(sql,val,)
                            udtl = fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (udtl[0],)
                            fbcursor.execute(sql,val,)
                            cdtl = fbcursor.fetchone()

                            sql = "select name from app1_accounts where acctype=%s and cid_id=%s"
                            val = (14,cdtl[0],)
                            fbcursor.execute(sql,val,)
                            ex_ac_data = fbcursor.fetchall()
                            ac_data_5 = ["Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities"]
                            for i in ex_ac_data:
                                ac_data_5.insert(-1,i[0])
                            

                            comb_non_item_6 = ttk.Combobox(p_canvas_3, font=('arial 10'))
                            comb_non_item_6['values'] = (ac_data_5)
                            window_comb_non_item_6 = p_canvas_3.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_non_item_6,tags=('npcombo6'),state=HIDDEN)

                            def non_exp_acc_1():
                                pro_frame_3.grid_forget()
                                pro_frame_3_2 = Frame(tab3_4)
                                pro_frame_3_2.grid(row=0,column=0,sticky='nsew')

                                def pro_responsive_widgets_non_2(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("eapoly1",x1 + r1,y1,
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

                                    dcanvas.coords("ealabel1",dwidth/3,dheight/8.24)
                                    dcanvas.coords("eahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.52


                                    dcanvas.coords("eapoly2",x11 + r2,y11,
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

                                    dcanvas.coords("eabutton3",dwidth/23,dheight/3.415)

                                    dcanvas.coords("ealabel2",dwidth/23,dheight/1.91)
                                    dcanvas.coords("ealabel3",dwidth/1.9,dheight/1.91)
                                    dcanvas.coords("ealabel4",dwidth/23.3,dheight/1.41)
                                    dcanvas.coords("ealabel5",dwidth/1.9,dheight/1.41)
                                    dcanvas.coords("ealabel6",dwidth/1.9,dheight/0.95)

                                    dcanvas.coords("eaentry1",dwidth/1.9,dheight/1.74)
                                    dcanvas.coords("eaentry2",dwidth/1.9,dheight/1.32)

                                    dcanvas.coords("eacombo1",dwidth/23,dheight/1.74)
                                    dcanvas.coords("eacombo2",dwidth/23,dheight/1.32)
                                    dcanvas.coords("eacombo3",dwidth/1.9,dheight/1.09)
                                    dcanvas.coords("eacombo4",dwidth/1.9,dheight/0.91)

                                    dcanvas.coords("eatext1",dwidth/23,dheight/1.15)
                                    dcanvas.coords("eacheck1",dwidth/1.9,dheight/1.155)

                                    dcanvas.coords("eabutton1",dwidth/2.3,dheight/0.73)

                                p_canvas_3_2=Canvas(pro_frame_3_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                                pro_frame_3_2.grid_columnconfigure(0,weight=1)
                                pro_frame_3_2.grid_rowconfigure(0,weight=1)
                                
                                vertibar=Scrollbar(pro_frame_3_2, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=p_canvas_3_2.yview)

                                p_canvas_3_2.bind("<Configure>", pro_responsive_widgets_non_2)
                                p_canvas_3_2.config(yscrollcommand=vertibar.set)
                                p_canvas_3_2.grid(row=0,column=0,sticky='nsew')

                                def non_exp_acc_create_2():
                                    acctype = comb_non_3_1.get()
                                    detype = comb_non_3_2.get()
                                    name = entry_non_3_2.get()
                                    description = entry_non_3_4.get()
                                    gst = comb_non_3_3.get()
                                    deftaxcode = comb_non_3_4.get()
                                    balance = 0
                                    today = datetime.date.today()
                                    asof = today.strftime("%Y-%m-%d")
                                    balfordisp = 0

                                    #----------------------
                                    usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usrp_val = (nm_ent.get(),)
                                    fbcursor.execute(usrp_sql,usrp_val)
                                    usrp_data_1 = fbcursor.fetchone()

                                    cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmpp_val = (usrp_data_1[0],)
                                    fbcursor.execute(cmpp_sql,cmpp_val)
                                    cmpp_data = fbcursor.fetchone()
                                    cid = cmpp_data[0]

                                    #product id --------------
                                    if acctype == "Expenses":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (14,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_2 = fbcursor.fetchone()
                                    else:
                                        pass
                                    
                                    productid = product_data_2[0]

                                    #-------------------------
                                    acctype_sql = "SELECT accountname FROM app1_accountype WHERE accountname=%s"
                                    acctype_val = (comb_non_3_2.get(),)
                                    fbcursor.execute(acctype_sql,acctype_val)
                                    acctype_data = fbcursor.fetchone()

                                    acct_sql = "SELECT name,cid_id FROM app1_accounts WHERE name=%s AND cid_id=%s"
                                    acct_val = (entry_non_3_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct_sql,acct_val)
                                    acct_data = fbcursor.fetchone()

                                    acct1_sql = "SELECT name,cid_id FROM app1_accounts1 WHERE name=%s AND cid_id=%s"
                                    acct1_val = (entry_non_3_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct1_sql,acct1_val)
                                    acct1_data = fbcursor.fetchone()
                                    print(acct1_data)

                                    if not acctype_data and not acct_data or not acct1_data:
                                        ins_acctype_sql = "INSERT INTO app1_accountype(cid_id,accountname,accountbal) VALUES(%s,%s,%s)"
                                        ins_acctype_val= (cmpp_data[0],detype,balance)
                                        fbcursor.execute(ins_acctype_sql,ins_acctype_val)
                                        finsysdb.commit()

                                        if acctype == "Expenses":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (14,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()

                                            #--------------------------
                                            i_ac_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,deftaxcode,balance,asof,balfordisp,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            i_ac_val = (14,detype,name,description,gst,deftaxcode,balance,asof,balfordisp,cid,pro_data[0],productid)
                                            fbcursor.execute(i_ac_sql,i_ac_val)
                                            finsysdb.commit()
                                        else:
                                            pass

                                        sel_accts1_sql = "SELECT * FROM app1_accounts1 WHERE cid_id=%s"
                                        sel_accts1_val = (cid,)
                                        fbcursor.execute(sel_accts1_sql,sel_accts1_val)
                                        sel_accts1_data = fbcursor.fetchone()

                                        bal = sel_accts1_data[7] + float(balance)
                                        upd_accts1_sql = "UPDATE app1_accounts1 SET balance=%s WHERE cid_id=%s"
                                        upd_accts1_val = (bal,cid,)
                                        fbcursor.execute(upd_accts1_sql,upd_accts1_val)
                                        finsysdb.commit()

                                        pro_frame_3_2.destroy()
                                        pro_frame_3.grid(row=0,column=0,sticky='nsew')


                                p_canvas_3_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('eapoly1'))

                                label_1 = Label(p_canvas_3_2,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1, tags=('ealabel1'))

                                p_canvas_3_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('eahline'))

                                p_canvas_3_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('eapoly2'))

                                label_1 = Label(p_canvas_3_2,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel2'))

                                comb_non_3_1 = ttk.Combobox(p_canvas_3_2, font=('arial 10'))
                                comb_non_3_1['values'] = ("Expenses",)
                                comb_non_3_1.current(0)
                                window_comb_non_3_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_3_1,tags=('eacombo1'))

                                
                                label_1 = Label(p_canvas_3_2,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel4'))

                                def entry_text_5(event):
                                    if comb_non_3_2.get() == 'Advertising/Promotional':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Advertising/Promotional')
                                    elif comb_non_3_2.get() == 'Amortisation Expense':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Amortisation Expense')
                                    elif comb_non_3_2.get() == 'Auto':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Auto')
                                    elif comb_non_3_2.get() == 'Bad Debts':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Bad Debts')
                                    elif comb_non_3_2.get() == 'Bank Charges':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Bank Charges')
                                    elif comb_non_3_2.get() == 'Borrowing Cost':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Borrowing Cost')
                                    elif comb_non_3_2.get() == 'Charitable Contributions':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Charitable Contributions')
                                    elif comb_non_3_2.get() == 'Commision and Fees':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Commision and Fees')
                                    elif comb_non_3_2.get() == 'Cost of Labour':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Cost of Labour')
                                    elif comb_non_3_2.get() == 'Dues and Subscriptions':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Dues and Subscriptions')
                                    elif comb_non_3_2.get() == 'Equipment Rental':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Equipment Rental')
                                    elif comb_non_3_2.get() == 'Finance Costs':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Finance Costs')
                                    elif comb_non_3_2.get() == 'Income Tax Expense':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Income Tax Expense')
                                    elif comb_non_3_2.get() == 'Insurance':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Insurance')
                                    elif comb_non_3_2.get() == 'Interest Paid':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Interest Paid')
                                    elif comb_non_3_2.get() == 'Legal and Professional Fees':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Legal and Professional Fees')
                                    elif comb_non_3_2.get() == 'Loss on Discontinued Operations, Net of Tax':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Loss on Discontinued Operations, Net of Tax')
                                    elif comb_non_3_2.get() == 'Management Compensation':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Management Compensation')
                                    elif comb_non_3_2.get() == 'Meals and Entertainment':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Meals and Entertainment')
                                    elif comb_non_3_2.get() == 'Office/General Administrative Expenses':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Office/General Administrative Expenses')
                                    elif comb_non_3_2.get() == 'Other Miscellaneous Service Cost':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Other Miscellaneous Service Cost')
                                    elif comb_non_3_2.get() == 'Other Selling Expenses':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Other Selling Expenses')
                                    elif comb_non_3_2.get() == 'Payroll Expenses':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Payroll Expenses')
                                    elif comb_non_3_2.get() == 'Rent or Lease of Building':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Rent or Lease of Building')
                                    elif comb_non_3_2.get() == 'Repair and Maintanance':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Repair and Maintanance')
                                    elif comb_non_3_2.get() == 'Shipping and Delivery Expense':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Shipping and Delivery Expense')
                                    elif comb_non_3_2.get() == 'Shipping, Freight and Delivery':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Shipping, Freight and Delivery')
                                    elif comb_non_3_2.get() == 'Supplies and Materials':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Supplies and Materials')
                                    elif comb_non_3_2.get() == 'Taxes Paid':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Taxes Paid')
                                    elif comb_non_3_2.get() == 'Travel Expenses-Gereral and Admin Expenses':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Travel Expenses-Gereral and Admin Expenses')
                                    elif comb_non_3_2.get() == 'Travel Expenses-Selling Expense':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Travel Expenses-Selling Expense')
                                    elif comb_non_3_2.get() == 'Unapplied Cash Bill Payment Expense':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Unapplied Cash Bill Payment Expense')
                                    elif comb_non_3_2.get() == 'Utilities':
                                        entry_non_3_2.delete(0,END)
                                        entry_non_3_2.insert(0,'Utilities')
                                    else:
                                        pass


                                comb_non_3_2 = ttk.Combobox(p_canvas_3_2, font=('arial 10'))
                                comb_non_3_2['values'] = ("Advertising/Promotional","Amortisation Expense","Auto","Bad Debts","Bank Charges","Borrowing Cost","Charitable Contributions","Commision and Fees","Cost of Labour","Dues and Subscriptions","Equipment Rental","Finance Costs","Income Tax Expense","Insurance","Interest Paid","Legal and Professional Fees","Loss on Discontinued Operations, Net of Tax","Management Compensation","Meals and Entertainment","Office/General Administrative Expenses","Other Miscellaneous Service Cost","Other Selling Expenses","Payroll Expenses","Rent or Lease of Building","Repair and Maintanance","Shipping and Delivery Expense","Shipping, Freight and Delivery","Supplies and Materials","Taxes Paid","Travel Expenses-Gereral and Admin Expenses","Travel Expenses-Selling Expense","Unapplied Cash Bill Payment Expense","Utilities",)
                                comb_non_3_2.bind("<<ComboboxSelected>>",entry_text_5)
                                window_comb_non_3_2 = p_canvas_3_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_3_2,tags=('eacombo2'))

                                label_1 = Label(p_canvas_3_2,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel3'))


                                entry_non_3_2=Entry(p_canvas_3_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_non_3_2 = p_canvas_3_2.create_window(0, 0, anchor="nw", height=30,window=entry_non_3_2,tags=('eaentry1'))

                                label_1 = Label(p_canvas_3_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel5'))

                                entry_non_3_4=Entry(p_canvas_3_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_non_3_4 = p_canvas_3_2.create_window(0, 0, anchor="nw", height=30,window=entry_non_3_4,tags=('eaentry2'))

                                non_text_3 = Text(p_canvas_3_2,width=67, height=14, background='black',foreground='white')
                                non_text_3.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                                window_non_text_3 = p_canvas_3_2.create_window(0, 0, anchor="nw",window=non_text_3,tags=('eatext1'))

                                def sub_check_5():
                                    comb_non_3_3.config(state=NORMAL if chk_str_non_3_1.get() else DISABLED)

                                chk_str_non_3_1 = IntVar()
                                chkbtn_non_3_1 = Checkbutton(p_canvas_3_2, text = "Is sub-account", variable = chk_str_non_3_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=sub_check_5)
                                window_chkbtn_non_3_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=chkbtn_non_3_1,tags=('eacheck1'))

                                comb_non_3_3 = ttk.Combobox(p_canvas_3_2, font=('arial 10'),state=DISABLED)
                                comb_non_3_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                                window_comb_non_3_3 = p_canvas_3_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_3_3,tags=('eacombo3'))

                                label_1 = Label(p_canvas_3_2,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel6'))

                                comb_non_3_4 = ttk.Combobox(p_canvas_3_2, font=('arial 10'))
                                comb_non_3_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                                window_comb_non_3_4 = p_canvas_3_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_3_4,tags=('eacombo4'))

                                non_sub_btn_3_1=Button(p_canvas_3_2,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=non_exp_acc_create_2)
                                window_non_sub_btn_3_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=non_sub_btn_3_1,tags=('eabutton1'))

                                def n_back_2_():
                                    pro_frame_3_2.grid_forget()
                                    pro_frame_3.grid(row=0,column=0,sticky='nsew')

                                ebck_btn1=Button(p_canvas_3_2,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=n_back_2_)
                                window_ebck_btn1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=ebck_btn1,tags=('eabutton3'))

                            expense_non_btn=Button(p_canvas_3,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=non_exp_acc_1)
                            window_expense_non_btn = p_canvas_3.create_window(0, 0, anchor="nw", window=expense_non_btn,tags=('npbutton4'),state=HIDDEN)

                            label_1 = Label(p_canvas_3,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel21'),state=HIDDEN)

                            def pr_2(event):
                                if entry_non_item_11.get()=="0":
                                    entry_non_item_11.delete(0,END)
                                else:
                                    pass

                            entry_non_item_11=Entry(p_canvas_3,width=50,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_non_item_11 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_11,tags=('npentry11'),state=HIDDEN)
                            entry_non_item_11.insert(0,"0")
                            entry_non_item_11.bind("<Button-1>",pr_2)


                            label_1 = Label(p_canvas_3,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel22'),state=HIDDEN)

                            comb_non_item_7 = ttk.Combobox(p_canvas_3, font=('arial 10'))
                            comb_non_item_7['values'] = ("Select Supplier",)
                            #comb_non_item_7.current(0)
                            window_comb_non_item_7 = p_canvas_3.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_non_item_7,tags=('npcombo7'),state=HIDDEN)

                            non_sub_btn1=Button(p_canvas_3,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_new_pro_non)
                            window_non_sub_btn1 = p_canvas_3.create_window(0, 0, anchor="nw", window=non_sub_btn1,tags=('npbutton5'))

                        p_btn_2=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=non_add_item)
                        window_p_btn_2 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_2,tags=('apbutton2'),state=HIDDEN)

                        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly5"))

                        def sercall(event):
                            p_canvas_1.itemconfig('apimage3',state='hidden')
                            p_canvas_1.itemconfig('aplabel6',state='normal')
                            p_canvas_1.itemconfig('aplabel7',state='normal')
                            p_canvas_1.itemconfig('apbutton3',state='normal')

                        image_s1 = Image.open("images/service.png")
                        resize_image = image_s1.resize((200,150))
                        image_s1 = ImageTk.PhotoImage(resize_image)
                        btlogos = Label(p_canvas_1, width=200, height=150, background="#1b3857", image = image_s1) 
                        window_image = p_canvas_1.create_window(0, 0, anchor="nw", window=btlogos,tags=('apimage3'))
                        btlogos.photo = image_s1
                        btlogos.bind("<Button-1>",sercall)


                        label_1 = Label(p_canvas_1,width=10,height=1,text="Services", font=('arial 20'),background="#2f516f",fg="white") 
                        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel6'),state=HIDDEN)

                        label_1 = Label(p_canvas_1,width=45,height=2,text="A service is a transaction in which no physical goods are \ntransferred from the seller to the buyer.", font=('arial 12'),background="#2f516f",fg="white") 
                        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel7'),state=HIDDEN)

                        def ser_add_item():
                            pro_frame_1.grid_forget()
                            pro_frame_4 = Frame(tab3_4)
                            pro_frame_4.grid(row=0,column=0,sticky='nsew')

                            def pro_responsive_widgets_4(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("sppoly1",x1 + r1,y1,
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

                                dcanvas.coords("splabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("sphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.29


                                dcanvas.coords("sppoly2",x11 + r2,y11,
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

                                r2 = 25
                                x11 = dwidth/24
                                x21 = dwidth/1.050
                                y11 = dheight/2.1
                                y21 = dheight/1.35


                                dcanvas.coords("sppoly3",x11 + r2,y11,
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

                                dcanvas.coords("splabel2",dwidth/3,dheight/1.77)
                                dcanvas.coords("spbutton1",dwidth/1.8,dheight/1.77)

                                dcanvas.coords("splabel3",dwidth/23.2,dheight/1.23)
                                dcanvas.coords("splabel4",dwidth/23.3,dheight/1.02)
                                dcanvas.coords("splabel5",dwidth/1.9,dheight/1.02)
                                dcanvas.coords("splabel7",dwidth/27,dheight/0.865)
                                dcanvas.coords("splabel8",dwidth/1.915,dheight/0.865)
                                dcanvas.coords("splabel12",dwidth/26,dheight/0.675)
                                dcanvas.coords("splabel13",dwidth/26.8,dheight/0.606)
                                dcanvas.coords("splabel14",dwidth/28.3,dheight/0.538)
                                dcanvas.coords("splabel15",dwidth/1.9,dheight/0.538)
                                dcanvas.coords("splabel16",dwidth/28.4,dheight/0.485)
                                dcanvas.coords("splabel17",dwidth/50,dheight/0.438)
                                dcanvas.coords("splabel18",dwidth/26,dheight/0.420)
                                dcanvas.coords("splabel9",dwidth/23.2,dheight/0.392)
                                dcanvas.coords("splabel10",dwidth/1.9,dheight/0.392)
                                dcanvas.coords("splabel20",dwidth/28,dheight/0.368)
                                dcanvas.coords("splabel21",dwidth/2.6,dheight/0.368)
                                dcanvas.coords("splabel22",dwidth/1.5,dheight/0.368)

                                dcanvas.coords("splabel23",dwidth/2.6,dheight/0.485)

                                dcanvas.coords("splabel24",dwidth/1.53,dheight/0.485)
                                

                                dcanvas.coords("spentry1",dwidth/23.2,dheight/1.165)
                                dcanvas.coords("spentry2",dwidth/23.2,dheight/0.975)
                                dcanvas.coords("spentry3",dwidth/1.9,dheight/0.975)
                                dcanvas.coords("spentry4",dwidth/1.9,dheight/0.83)
                                dcanvas.coords("spentry7",dwidth/23.2,dheight/0.59)
                                dcanvas.coords("spentry8",dwidth/23.2,dheight/0.525)
                                dcanvas.coords("spentry9",dwidth/23.2,dheight/0.43)
                                dcanvas.coords("spentry10",dwidth/23.2,dheight/0.412)
                                dcanvas.coords("spentry11",dwidth/2.6,dheight/0.362)

                                dcanvas.coords("spentry12",dwidth/2.6,dheight/0.474)

                                dcanvas.coords("spcentry2",dwidth/23.2,dheight/0.385)
                                dcanvas.coords("spcentry3",dwidth/1.9,dheight/0.385)

                                dcanvas.coords("spcombo1",dwidth/23.2,dheight/0.83)
                                dcanvas.coords("spcombo3",dwidth/1.9,dheight/0.525)
                                dcanvas.coords("spcombo4",dwidth/23.2,dheight/0.474)
                                dcanvas.coords("spcombo6",dwidth/23.2,dheight/0.362)
                                dcanvas.coords("spcombo7",dwidth/1.5,dheight/0.362)

                                dcanvas.coords("spcombo8",dwidth/1.5,dheight/0.474)

                                dcanvas.coords("spbutton2",dwidth/23.2,dheight/0.654)
                                dcanvas.coords("spbutton3",dwidth/3.37,dheight/0.474)
                                dcanvas.coords("spbutton4",dwidth/3.37,dheight/0.362)
                                dcanvas.coords("spbutton5",dwidth/2.38,dheight/0.345)

                                dcanvas.coords("spcbutton1",dwidth/23.2,dheight/0.51)
                                dcanvas.coords("spcbutton2",dwidth/23.2,dheight/0.378)

                                dcanvas.coords("spline1",dwidth/21,dheight/0.73,dwidth/1.055,dheight/0.73)

                                dcanvas.coords("sphline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)

                            p_canvas_4=Canvas(pro_frame_4, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_4.grid_columnconfigure(0,weight=1)
                            pro_frame_4.grid_rowconfigure(0,weight=1)
                    
                            vertibar=Scrollbar(pro_frame_4, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_4.yview)

                            p_canvas_4.bind("<Configure>", pro_responsive_widgets_4)
                            p_canvas_4.config(yscrollcommand=vertibar.set)
                            p_canvas_4.grid(row=0,column=0,sticky='nsew')

                            def add_new_pro_ser():
                                name = entry_ser_item_1.get()
                                sku = entry_ser_iitem_2.get()
                                sac = entry_ser_item_2.get()
                                unit = comb_ser_item_1.get()
                                categ = entry_ser_item_3.get()
                                descr = entry_ser_item_7.get('1.0', 'end-1c')
                                saleprice = entry_ser_item_s8.get()
                                income = comb_ser_item_6.get()
                                tax = comb_ser_item_3.get()
                                abatement = entry_ser_iitem_11.get()
                                sertype = comb_ser_iitem_7.get()
                                purchasedescr = entry_ser_item_9.get('1.0', 'end-1c')
                                cost = entry_ser_item_10.get()
                                expenseaccount = comb_ser_item_e6.get()
                                purchasetax = comb_ser_item_5.get()
                                revcharge = entry_sser_item_11.get()
                                presupplier = comb_ser_item_ps7.get()

                                usrp2_sql = "SELECT id FROM auth_user WHERE username=%s"
                                usrp2_val = (nm_ent.get(),)
                                fbcursor.execute(usrp2_sql,usrp2_val)
                                usrp2_data = fbcursor.fetchone()

                                cmpp2_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                cmpp2_val = (usrp2_data[0],)
                                fbcursor.execute(cmpp2_sql,cmpp2_val)
                                cmpp2_data = fbcursor.fetchone()
                                cid = cmpp2_data[0]

                                s_p_sql = "INSERT INTO app1_service(name,sku,sac,unit,categ,descr,saleprice,income,tax,abatement,sertype,purchasedescr,cost,expenseaccount,purchasetax,revcharge,presupplier,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                s_p_val = (name,sku,sac,unit,categ,descr,saleprice,income,tax,abatement,sertype,purchasedescr,cost,expenseaccount,purchasetax,revcharge,presupplier,cid)
                                fbcursor.execute(s_p_sql,s_p_val)
                                finsysdb.commit()

                                #_________Refresh insert tree________#

                                for record in pro_tree.get_children():
                                    pro_tree.delete(record)

        
                                sql_p="select * from auth_user where username=%s"
                                sql_p_val=(nm_ent.get(),)
                                fbcursor.execute(sql_p,sql_p_val,)
                                pr_dt=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dt[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dt=fbcursor.fetchone()

                                p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                p_val_1 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_1,p_val_1,)
                                p_data_1 = fbcursor.fetchall()
                                
                                count0 = 0
                                for i in p_data_1:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                    else:
                                        pass
                                count0 += 1

                                p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                p_val_2 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_2,p_val_2,)
                                p_data_2 = fbcursor.fetchall()

                                count1 = 0
                                for i in p_data_2:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count1 += 1

                                p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                p_val_3 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_3,p_val_3,)
                                p_data_3 = fbcursor.fetchall()
                                

                                count2 = 0
                                for i in p_data_3:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count2 += 1

                                p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                p_val_4 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_4,p_val_4,)
                                p_data_4 = fbcursor.fetchall()
                                

                                count3 = 0
                                for i in p_data_4:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                    else:
                                        pass
                                count3 += 1

                                pro_frame_4.destroy()
                                pro_frame.grid(row=0,column=0,sticky='nsew')


                            p_canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sppoly1'))

                            label_1 = Label(p_canvas_4,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel1'))

                            p_canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sphline'))

                            p_canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sppoly2'))

                            p_canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('sppoly3'))

                            label_1 = Label(p_canvas_4,width=15,height=2,text="SERVICES", font=('arial 20'),background="#2f516f",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel2'))

                            btn_ser_item_2=Button(p_canvas_4,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
                            window_btn_ser_item_2 = p_canvas_4.create_window(0, 0, anchor="nw", window=btn_ser_item_2, tags=('spbutton1'))

                            label_1 = Label(p_canvas_4,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel3'))

                            entry_ser_item_1=Entry(p_canvas_4,width=200,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ser_item_1 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_item_1, tags=('spentry1'))

                            label_1 = Label(p_canvas_4,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel4'))

                            def ps_3(event):
                                if entry_ser_iitem_2.get()=="N41554":
                                    entry_ser_iitem_2.delete(0,END)
                                else:
                                    pass

                            entry_ser_iitem_2=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ser_iitem_2 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_iitem_2, tags=('spentry2'))
                            entry_ser_iitem_2.insert(0,"N41554")
                            entry_ser_iitem_2.bind("<Button-1>",ps_3)

                            label_1 = Label(p_canvas_4,width=9,height=1,text="SAC Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel5'))

                            def p_sac_1(event):
                                if entry_ser_item_2.get()=="Eg: 998841-Coke and refined petroleum product manufacturing services":
                                    entry_ser_item_2.delete(0,END)
                                else:
                                    pass
                            entry_ser_item_2=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ser_item_2 = p_canvas_4.create_window(710, 630, anchor="nw", height=30,window=entry_ser_item_2, tags=('spentry3'))
                            entry_ser_item_2.insert(0,"Eg: 998841-Coke and refined petroleum product manufacturing services")
                            entry_ser_item_2.bind("<Button-1>",p_sac_1)


                            label_1 = Label(p_canvas_4,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel7'))

                            comb_ser_item_1 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                            comb_ser_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG-BAGS","BAL-BALE","BDL-BUNDLES","BKL-BUCKLES","BOX-BOX","BOU-BILLIONS OF UNITS","BTL-BOTTLES","BUN-BUNCHES","CAN-CANS","CBM-CUBIC METER","CMS-CENTIMETER","CCM-CUBIC CENTIMETER","CTN-CARTONS","DOZ-DOZEN","DRM-DRUM","GGR-GREAT GROSS","GMS-GRAMS","GRS-GROSS","GYD-GRODD YARDS","KGS-KILOGRAMS","KLR-KILOLITER","KME-KILOMETRE","MTS-METRIC TON","MLT-MILLILITRE","MTR-METERS","NOS-NUMBER","PAC-PACKS","PCS-PIECES","PRS-PAIRS","QTL-QUINTAL","ROL-ROLLS","SQF-SQUARE FEET","SET-SETS","SQM-SQUARE METERS","SQY-SQUARE YARDS","TBS-TABLETS","TGM-TEN GROSS","THD-THOUSAND","TON-TONNES","TUB-TUBES","UGS-US GALLONS","UNT-UNITS","YDS-YARDS","OTH-OTHERS",)
                            comb_ser_item_1.current(0)
                            window_comb_ser_item_1 = p_canvas_4.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_item_1, tags=('spcombo1'))

                            label_1 = Label(p_canvas_4,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(705, 710, anchor="nw", window=label_1,tags=('splabel8'))

                            entry_ser_item_3=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ser_item_3 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_item_3,tags=('spentry4'))

                            p_canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('spline1'))


                            label_1 = Label(p_canvas_4,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel12'))

                            def d_ser_check():

                                if chk_str_ser_item.get() == True:
                                    p_canvas_4.itemconfig('splabel13',state='normal')
                                    p_canvas_4.itemconfig('spentry7',state='normal')
                                    p_canvas_4.itemconfig('splabel14',state='normal')
                                    p_canvas_4.itemconfig('spentry8',state='normal')
                                    p_canvas_4.itemconfig('spcbutton1',state='normal')
                                    p_canvas_4.itemconfig('splabel15',state='normal')
                                    p_canvas_4.itemconfig('spcombo3',state='normal')
                                    p_canvas_4.itemconfig('splabel16',state='normal')
                                    p_canvas_4.itemconfig('spcombo4',state='normal')
                                    p_canvas_4.itemconfig('spbutton3',state='normal')
                                    p_canvas_4.itemconfig('splabel23',state='normal')
                                    p_canvas_4.itemconfig('spentry12',state='normal')
                                    p_canvas_4.itemconfig('splabel24',state='normal')
                                    p_canvas_4.itemconfig('spcombo8',state='normal')
                                else:
                                    pass

                            chk_str_ser_item = BooleanVar()
                            chkbtn_ser_item = Checkbutton(p_canvas_4, text = "I sell this product/service to my customers.", variable = chk_str_ser_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=d_ser_check)
                            window_chkbtn_ser_item = p_canvas_4.create_window(0, 0, anchor="nw", window=chkbtn_ser_item,tags=('spbutton2'))

                            label_d1 = Label(p_canvas_4,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_d1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_d1,tags=('splabel13'),state=HIDDEN)

                            entry_ser_item_7=scrolledtext.ScrolledText(p_canvas_4,width=145,background='#2f516f',foreground="white")
                            window_entry_ser_item_7 = p_canvas_4.create_window(0, 0, anchor="nw", height=60,window=entry_ser_item_7,tags=('spentry7'),state=HIDDEN)


                            label_1 = Label(p_canvas_4,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel14'),state=HIDDEN)

                            def ser_tax_check():
                                if comb_ser_item_3.get() == '28.0% GST (28%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+28)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '28.0% IGST (28%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+28)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '18.0% GST (18%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+18)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '18.0% IGST (18%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+18)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '15.0% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+15)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '14.5% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+14.5)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '14.00% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+14)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '14.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+14)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '12.36% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+12.36)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '12.0% GST (12%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+12)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '12.0% IGST (12%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+12)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '6.0% GST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '6.0% IGST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '6.0% IGST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '5.0% GST (5%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '5.0% IGST (5%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '5.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '4.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+4)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '3.0% GST (3%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+3)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '3.0% IGST (3%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+3)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '2.0% CST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+2)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '0.25% GST (O.25%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+0.25)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '0.25% IGST (0.25%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+0.25)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '0% GST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == '0% IGST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == 'Exempt GST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == 'Exempt IGST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_3.get() == 'Out of Scope(0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_s8.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_ser_item_1.get() == True:
                                        entry_ser_item_s8.delete(0,'end')
                                        entry_ser_item_s8.insert(0, np)
                                    else:
                                        pass
                                else:
                                    pass
                            
                            entry_ser_item_s8=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ser_item_s8 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_item_s8,tags=('spentry8'),state=HIDDEN)

                            chk_str_ser_item_1 = BooleanVar()
                            chkbtn_ser_item_1 = Checkbutton(p_canvas_4, text = "Inclusive of tax", variable = chk_str_ser_item_1,  font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=ser_tax_check)
                            window_chkbtn_ser_item_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=chkbtn_ser_item_1,tags=('spcbutton1'),state=HIDDEN)

                            label_1 = Label(p_canvas_4,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel15'),state=HIDDEN)

                            comb_ser_item_3 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                            comb_ser_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            comb_ser_item_3.current(0)
                            window_comb_ser_item_3 = p_canvas_4.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_item_3,tags=('spcombo3'),state=HIDDEN)

                            label_1 = Label(p_canvas_4,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel16'),state=HIDDEN)

                            sql = "select * from auth_user where username=%s"
                            val = (nm_ent.get(),)
                            fbcursor.execute(sql,val,)
                            udtl = fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (udtl[0],)
                            fbcursor.execute(sql,val,)
                            cdtl = fbcursor.fetchone()


                            sql = "select name from app1_accounts where detype=%s and cid_id=%s"
                            val = ('Account Receivable(Debtors)',cdtl[0],)
                            fbcursor.execute(sql,val,)
                            ser_in_ac_data = fbcursor.fetchall()
                            ac_data_6 = ["Choose...","Billable Expense income","Product Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discounts","Sales of Product Income","Cost of sales","Equipment Rental for Jobs","Uncategorised Income","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Depreciation Expense","Dues and Subscriptions","Housekeeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Internet Expenses","Meals and Enetrtainments","Office Suppliers","Postage and Delivery","Printing and Reprooduction","Professional Fees","Purchases","Rent Expense","Repair and Maintananace","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities","Finance charge Income","Insurance Proceeds Received","Interest Income","Proceeds From Sale os Assets","Shipping and delivery Income","Ask My Accountant","CGST Write-off","GST Write-off","IGST Write-off","Miscellaneous Expense","Political Contributions","Reconcilation Discrepancies","SGST Write-off","Vehicles","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi kalyan Cess","Input Krishi kalyan Cess RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Krishi Kalyan Cess Payable","Input VAT 5%","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output SGST Tax RCM","Output Service Tax","Output Service Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","SGST Payable","Service Tax Payable","Srvice Tax Suspense","Swachh Barath Cess Payable","TDS Payable","VAT Payable","VAT Suspense","Deferred CGST","Deferred GST Input credit","Deferred IGST","Deferred SGST","Deferred Service Tax Input Credit","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Sevice Tax Refund","TDS Receivable","Uncategorised Asset","Undeposited Fund","Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and maintanance","Sales Discount","Sales of Product Income","Uncategorised Income","accumulated Depreciation","Building and Improvements","Furniture and Equipments","Land","Leasehold Improvements","Vehicles","Retained Earnings","Cost of Sales","Equipment Rental for Jobs","Freight and Shipping Costs","Merchant Account Fees","Purchases-Hardware for Resales","Purchases-Software for Resales","Subcontracted Services","Tools and Craft Suppliers"]
                            for i in ser_in_ac_data:
                                ac_data_6.insert(-1,i[0])
                            

                            
                            comb_ser_item_6 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                            comb_ser_item_6['values'] = (ac_data_6)
                            comb_ser_item_6.current(0)
                            window_comb_ser_item_6 = p_canvas_4.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_ser_item_6,tags=('spcombo4'),state=HIDDEN)

                            def ser_inc_acc_1():
                                pro_frame_4.grid_forget()
                                pro_frame_4_1 = Frame(tab3_4)
                                pro_frame_4_1.grid(row=0,column=0,sticky='nsew')

                                def pro_responsive_widgets_4_1(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("sapoly1",x1 + r1,y1,
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

                                    dcanvas.coords("salabel1",dwidth/3,dheight/8.24)
                                    dcanvas.coords("sahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.52


                                    dcanvas.coords("sapoly2",x11 + r2,y11,
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

                                    dcanvas.coords("sabutton3",dwidth/23,dheight/3.415)

                                    dcanvas.coords("salabel2",dwidth/23,dheight/1.91)
                                    dcanvas.coords("salabel3",dwidth/1.9,dheight/1.91)
                                    dcanvas.coords("salabel4",dwidth/23.3,dheight/1.41)
                                    dcanvas.coords("salabel5",dwidth/1.9,dheight/1.41)
                                    dcanvas.coords("salabel6",dwidth/1.9,dheight/0.95)

                                    dcanvas.coords("saentry1",dwidth/1.9,dheight/1.74)
                                    dcanvas.coords("saentry2",dwidth/1.9,dheight/1.32)

                                    dcanvas.coords("sacombo1",dwidth/23,dheight/1.74)
                                    dcanvas.coords("sacombo2",dwidth/23,dheight/1.32)
                                    dcanvas.coords("sacombo3",dwidth/1.9,dheight/1.09)
                                    dcanvas.coords("sacombo4",dwidth/1.9,dheight/0.91)

                                    dcanvas.coords("satext1",dwidth/23,dheight/1.15)
                                    dcanvas.coords("sacheck1",dwidth/1.9,dheight/1.155)

                                    dcanvas.coords("sabutton1",dwidth/2.3,dheight/0.73)

                                p_canvas_4_1=Canvas(pro_frame_4_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                                pro_frame_4_1.grid_columnconfigure(0,weight=1)
                                pro_frame_4_1.grid_rowconfigure(0,weight=1)
                                
                                vertibar=Scrollbar(pro_frame_4_1, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=p_canvas_4_1.yview)

                                p_canvas_4_1.bind("<Configure>", pro_responsive_widgets_4_1)
                                p_canvas_4_1.config(yscrollcommand=vertibar.set)
                                p_canvas_4_1.grid(row=0,column=0,sticky='nsew')

                                def ser_inc_acc_create_1():
                                    acctype = comb_ser_2_1.get()
                                    detype = comb_ser_2_2.get()
                                    name = entry_ser_2_2.get()
                                    description = entry_ser_2_4.get()
                                    gst = comb_ser_2_3.get()
                                    deftaxcode = comb_ser_2_4.get()
                                    balance = 0
                                    today = datetime.date.today()
                                    asof = today.strftime("%Y-%m-%d")
                                    balfordisp = 0

                                    #----------------------
                                    usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usrp_val = (nm_ent.get(),)
                                    fbcursor.execute(usrp_sql,usrp_val)
                                    usrp_data_1 = fbcursor.fetchone()

                                    cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmpp_val = (usrp_data_1[0],)
                                    fbcursor.execute(cmpp_sql,cmpp_val)
                                    cmpp_data = fbcursor.fetchone()
                                    cid = cmpp_data[0]

                                    #product id --------------
                                    if acctype == "Account Receivable(Debtors)":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (1,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Current Assets":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (2,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Bank":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (3,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Fixed Assets":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (4,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Non-Current Assets":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (5,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Accounts Payable(Creditors)":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (6,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Credit Card":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (7,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Current Liabilities":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (8,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Non-Current Liabilities":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (9,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Equity":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (10,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Income":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (11,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Other Income":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (12,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Cost of Goods Sold":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (13,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Expenses":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (14,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Other Expenses":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (15,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    else:
                                        pass
                                    
                                    productid = product_data_3[0]
                                    #-----------------

                                    acctype_sql = "SELECT accountname FROM app1_accountype WHERE accountname=%s"
                                    acctype_val = (comb_ser_2_2.get(),)
                                    fbcursor.execute(acctype_sql,acctype_val)
                                    acctype_data = fbcursor.fetchone()

                                    acct_sql = "SELECT name,cid_id FROM app1_accounts WHERE name=%s AND cid_id=%s"
                                    acct_val = (entry_ser_2_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct_sql,acct_val)
                                    acct_data = fbcursor.fetchone()

                                    acct1_sql = "SELECT name,cid_id FROM app1_accounts1 WHERE name=%s AND cid_id=%s"
                                    acct1_val = (entry_ser_2_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct1_sql,acct1_val)
                                    acct1_data = fbcursor.fetchone()
                                    

                                    if not acctype_data and not acct_data or not acct1_data:
                                        ins_acctype_sql = "INSERT INTO app1_accountype(cid_id,accountname,accountbal) VALUES(%s,%s,%s)"
                                        ins_acctype_val= (cmpp_data[0],detype,balance)
                                        fbcursor.execute(ins_acctype_sql,ins_acctype_val)
                                        finsysdb.commit()

                                        if acctype == "Account Receivable(Debtors)":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (1,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (1,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Current Assets":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (2,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------

                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (2,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Bank":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (3,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (3,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Fixed Assets":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (4,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (4,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Non-Current Assets":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (5,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (5,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Accounts Payable(Creditors)":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (6,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (6,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Credit Card":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (7,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (7,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Current Liabilities":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (8,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (8,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Non-Current Liabilities":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (9,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (9,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Equity":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (10,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (10,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Income":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (11,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (11,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Other Income":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (12,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (12,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Cost of Goods Sold":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (13,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (13,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Expenses":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (14,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (14,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Other Expenses":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (15,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (15,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        else:
                                            pass

                                        sel_accts1_sql = "SELECT * FROM app1_accounts1 WHERE cid_id=%s"
                                        sel_accts1_val = (cid,)
                                        fbcursor.execute(sel_accts1_sql,sel_accts1_val)
                                        sel_accts1_data = fbcursor.fetchone()

                                        bal = sel_accts1_data[7] + float(balance)
                                        upd_accts1_sql = "UPDATE app1_accounts1 SET balance=%s WHERE cid_id=%s"
                                        upd_accts1_val = (bal,cid,)
                                        fbcursor.execute(upd_accts1_sql,upd_accts1_val)
                                        finsysdb.commit()

                                        pro_frame_4_1.destroy()
                                        pro_frame_4.grid(row=0,column=0,sticky='nsew')



                                p_canvas_4_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sapoly1'))

                                label_1 = Label(p_canvas_4_1,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1, tags=('salabel1'))

                                p_canvas_4_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sahline'))

                                p_canvas_4_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sapoly2'))

                                label_1 = Label(p_canvas_4_1,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel2'))

                                comb_ser_2_1 = ttk.Combobox(p_canvas_4_1, font=('arial 10'))
                                comb_ser_2_1['values'] = ("Account Receivable(Debtors)","Current Assets","Bank","Fixed Assets","Non-Current Assets","Accounts Payable(Creditors)","Credit Card","Current Liabilities","Non-Current Liabilities","Equity","Income","Other Income","Cost of Goods Sold","Expenses","Other Expenses",)
                                comb_ser_2_1.current(0)
                                window_comb_ser_2_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_2_1,tags=('sacombo1'))

                                label_1 = Label(p_canvas_4_1,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel4'))

                                def entry_text_6(event):
                                    if comb_ser_2_2.get() == 'Account Receivable(Debtors)':
                                        entry_ser_2_2.delete(0,END)
                                        entry_ser_2_2.insert(0,'Account Receivable(Debtors)')

                                comb_ser_2_2 = ttk.Combobox(p_canvas_4_1, font=('arial 10'))
                                comb_ser_2_2['values'] = ("Account Receivable(Debtors)",)
                                comb_ser_2_2.bind("<<ComboboxSelected>>",entry_text_6)
                                window_comb_ser_2_2 = p_canvas_4_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_2_2,tags=('sacombo2'))

                                label_1 = Label(p_canvas_4_1,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel3'))


                                entry_ser_2_2=Entry(p_canvas_4_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_ser_2_2 = p_canvas_4_1.create_window(0, 0, anchor="nw", height=30,window=entry_ser_2_2,tags=('saentry1'))

                                label_1 = Label(p_canvas_4_1,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel5'))

                                entry_ser_2_4=Entry(p_canvas_4_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_ser_2_4 = p_canvas_4_1.create_window(0, 0, anchor="nw", height=30,window=entry_ser_2_4,tags=('saentry2'))

                                ser_text_2 = Text(p_canvas_4_1,width=67, height=14, background='black',foreground='white')
                                ser_text_2.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                                window_ser_text_2 = p_canvas_4_1.create_window(0, 0, anchor="nw",window=ser_text_2,tags=('satext1'))

                                def sub_check_6():
                                    comb_ser_2_3.config(state=NORMAL if chk_str_ser_2_1.get() else DISABLED)

                                chk_str_ser_2_1 = IntVar()
                                chkbtn_ser_2_1 = Checkbutton(p_canvas_4_1, text = "Is sub-account", variable = chk_str_ser_2_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=sub_check_6)
                                window_chkbtn_ser_2_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=chkbtn_ser_2_1,tags=('sacheck1'))

                                comb_ser_2_3 = ttk.Combobox(p_canvas_4_1, font=('arial 10'),state=DISABLED)
                                comb_ser_2_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                                window_comb_ser_2_3 = p_canvas_4_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_2_3,tags=('sacombo3'))

                                label_1 = Label(p_canvas_4_1,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel6'))

                                comb_ser_2_4 = ttk.Combobox(p_canvas_4_1, font=('arial 10'))
                                comb_ser_2_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                                window_comb_ser_2_4 = p_canvas_4_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_2_4,tags=('sacombo4'))

                                ser_sub_btn_2_1=Button(p_canvas_4_1,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=ser_inc_acc_create_1)
                                window_ser_sub_btn_2_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=ser_sub_btn_2_1,tags=('sabutton1'))

                                def s_back_1_():
                                    pro_frame_4_1.grid_forget()
                                    pro_frame_4.grid(row=0,column=0,sticky='nsew')

                                bck_btn1=Button(p_canvas_4_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=s_back_1_)
                                window_bck_btn1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('sabutton3'))

                            income_ser_btn=Button(p_canvas_4,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=ser_inc_acc_1)
                            window_income_ser_btn = p_canvas_4.create_window(0, 0, anchor="nw", window=income_ser_btn,tags=('spbutton3'),state=HIDDEN)

                            label_1 = Label(p_canvas_4,width=10,height=1,text="Abatement %", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel23'),state=HIDDEN)

                            def pa_1(event):
                                if entry_ser_iitem_11.get()=="0":
                                    entry_ser_iitem_11.delete(0,END)
                                else:
                                    pass

                            entry_ser_iitem_11=Entry(p_canvas_4,width=50,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ser_iitem_11 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_iitem_11,tags=('spentry12'),state=HIDDEN)
                            entry_ser_iitem_11.insert(0,"0")
                            entry_ser_iitem_11.bind("<Button-1>",pa_1)

                            label_1 = Label(p_canvas_4,width=14,height=1,text="Service Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel24'),state=HIDDEN)

                            comb_ser_iitem_7 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                            comb_ser_iitem_7['values'] = ("Choose...","Stock Broking","Genral Insurance","Courier","Advertsing Agency","Consulting Engineer","Custom House Agent","Steamer Agent","Clearing and Forwarding","Man power Recruiting","Air Travel Agent","Tour operator","Rent a Cab","Architect","Interior Director","Management Consultment","Chartered Accountant","Cost Accountant","Company Scretary","Real Estate Agent","Security Agency","Credit Rating Agency","Market Research Agency","Underwriter","Beauty Parlor","Cargo Handling","Cable Operators","Dry Cleaning","Event Management","Fashion Designer","Life Insurance","Scientific and Technical Consultancy","Photography","Convention Services","Video Tape Production","Sound Recording","Broadcating","Insurance Auxilary Service","banking and Other Financial","Port Services","Authorised Service Station","Health Club and Fitness Centres","Rail Travel Agent","Storage and Warehousing","Business Auxilary","Commercial Coaching","Erection or Installation","Franchise Service","Internet Cafe","Maintanance or Repair","Technical Testing","Technical Inspection","Foreign Exchange Broking","Port","Airport Services","Air Transport","Business Exhibition","Goods Transport","Construction of Commerce Complex","Intellectual Property Service","Opinion Poll Service","Outdoor Catering","Television and Radio Program Production","Survey and Exploration of Minerals","Pandal and Shamiana","Travel Agent","Forward Contract Brokerage","Transport Through Pipeline","Site Preparation","Dredging","Survey and Map Making","Cleaning Service","Clubs and Association Service","Packaging Service","Mailing List Compilation","Residential Complex Construction","Share Transfer Agent","ATM Maintanance","Recovery Agent","Sale of Space for Advertisement","Sponsorship","International Air Travel","Containerised Rail Transport","Business Support Service","Action Service","Public Relation Management","Ship Management","Internet Telephony","Cruise Ship Tour","Credit Card","Telecommunication Service","Mining of Minerals, Oil or Gas","Recting Immovable Property","Works Contract","Development of Consent","Asset Management","Design Services","Information Technology Services","ULIP Management","Stock Exchange Service","Service for Transaction in Goods","Clearing House Services","Supply of Tangiable","Online Inforamtion Retrieval","Mandap keeper",)
                            comb_ser_iitem_7.current(0)
                            window_comb_ser_iitem_7 = p_canvas_4.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_ser_iitem_7,tags=('spcombo8'),state=HIDDEN)

                            p_canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sphline1'))

                            label_1 = Label(p_canvas_4,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel17'))

                            def p_ser_check():

                                if chk_str_ser_pitem.get() == True:
                                    p_canvas_4.itemconfig('splabel18',state='normal')
                                    p_canvas_4.itemconfig('spentry10',state='normal')
                                    p_canvas_4.itemconfig('splabel9',state='normal')
                                    p_canvas_4.itemconfig('spcentry2',state='normal')
                                    p_canvas_4.itemconfig('spcbutton2',state='normal')
                                    p_canvas_4.itemconfig('splabel10',state='normal')
                                    p_canvas_4.itemconfig('spcentry3',state='normal')
                                    p_canvas_4.itemconfig('splabel20',state='normal')
                                    p_canvas_4.itemconfig('spcombo6',state='normal')
                                    p_canvas_4.itemconfig('spbutton4',state='normal')
                                    p_canvas_4.itemconfig('splabel21',state='normal')
                                    p_canvas_4.itemconfig('spentry11',state='normal')
                                    p_canvas_4.itemconfig('splabel22',state='normal')
                                    p_canvas_4.itemconfig('spcombo7',state='normal')
                                else:
                                    pass

                            chk_str_ser_pitem = BooleanVar()
                            chkbtn_ser_pitem = Checkbutton(p_canvas_4, text = "I Purchase this product/service from Supplier.", variable = chk_str_ser_pitem, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=p_ser_check)
                            window_chkbtn_ser_pitem = p_canvas_4.create_window(0, 0, anchor="nw", window=chkbtn_ser_pitem,tags=('spentry9'))


                            label_1 = Label(p_canvas_4,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel18'),state=HIDDEN)

                            entry_ser_item_9=scrolledtext.ScrolledText(p_canvas_4,width=145,background='#2f516f',foreground="white")
                            window_entry_ser_item_9 = p_canvas_4.create_window(0, 0, anchor="nw", height=60,window=entry_ser_item_9,tags=('spentry10'),state=HIDDEN)

                            label_1 = Label(p_canvas_4,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel9'),state=HIDDEN)

                            def ser_tax_check_1():
                                if comb_ser_item_5.get() == '28.0% GST (28%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+28)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '28.0% IGST (28%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+28)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '18.0% GST (18%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+18)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '18.0% IGST (18%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+18)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '15.0% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+15)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '14.5% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+14.5)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '14.00% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+14)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '14.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+14)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '12.36% ST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+12.36)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '12.0% GST (12%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+12)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '12.0% IGST (12%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+12)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '6.0% GST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '6.0% IGST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '6.0% IGST (6%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+6)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '5.0% GST (5%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '5.0% IGST (5%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '5.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+5)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '4.0% VAT (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+4)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '3.0% GST (3%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+3)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '3.0% IGST (3%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+3)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '2.0% CST (100%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+2)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '0.25% GST (O.25%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+0.25)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '0.25% IGST (0.25%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+0.25)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '0% GST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == '0% IGST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == 'Exempt GST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == 'Exempt IGST (0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                elif comb_ser_item_5.get() == 'Out of Scope(0%)':
                                    gst = 0.0
                                    np = 0.0
                                    n1 = float(entry_ser_item_10.get())
                                    gst = n1-(n1*(100/(100+0)))
                                    np = n1-gst
                                    if chk_str_sser_item_2.get() == True:
                                        entry_ser_item_10.delete(0,'end')
                                        entry_ser_item_10.insert(0, np)
                                    else:
                                        pass
                                else:
                                    pass
                            
                            
                            entry_ser_item_10=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ser_item_10 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_item_10,tags=('spcentry2'),state=HIDDEN)

                            chk_str_sser_item_2 = BooleanVar()
                            chkbtn_sser_item_2 = Checkbutton(p_canvas_4, text = "Inclusive of Tax", variable = chk_str_sser_item_2,font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=ser_tax_check_1)
                            window_chkbtn_sser_item_2 = p_canvas_4.create_window(0, 0, anchor="nw", window=chkbtn_sser_item_2,tags=('spcbutton2'),state=HIDDEN)

                            label_1 = Label(p_canvas_4,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel10'),state=HIDDEN)

                            comb_ser_item_5 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                            comb_ser_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            comb_ser_item_5.current(0)
                            window_comb_ser_item_5 = p_canvas_4.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_item_5,tags=('spcentry3'),state=HIDDEN)

                            label_1 = Label(p_canvas_4,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel20'),state=HIDDEN)

                            sql = "select * from auth_user where username=%s"
                            val = (nm_ent.get(),)
                            fbcursor.execute(sql,val,)
                            udtl = fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (udtl[0],)
                            fbcursor.execute(sql,val,)
                            cdtl = fbcursor.fetchone()


                            sql = "select name from app1_accounts where detype=%s and cid_id=%s"
                            val = ('Account Receivable(Debtors)',cdtl[0],)
                            fbcursor.execute(sql,val,)
                            ser_ex_ac_data = fbcursor.fetchall()
                            ac_data_7 = ["Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities"]
                            for i in ser_ex_ac_data:
                                ac_data_7.insert(-1,i[0])
                            

                            comb_ser_item_e6 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                            comb_ser_item_e6['values'] = (ac_data_7)
                            comb_ser_item_e6.current(0)
                            window_comb_ser_item_e6 = p_canvas_4.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_ser_item_e6,tags=('spcombo6'),state=HIDDEN)

                            def ser_exp_acc_1():
                                pro_frame_4.grid_forget()
                                pro_frame_4_2 = Frame(tab3_4)
                                pro_frame_4_2.grid(row=0,column=0,sticky='nsew')

                                def pro_responsive_widgets_4_2(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("xapoly1",x1 + r1,y1,
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

                                    dcanvas.coords("xalabel1",dwidth/3,dheight/8.24)
                                    dcanvas.coords("xahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.52


                                    dcanvas.coords("xapoly2",x11 + r2,y11,
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

                                    dcanvas.coords("xabutton3",dwidth/23,dheight/3.415)

                                    dcanvas.coords("xalabel2",dwidth/23,dheight/1.91)
                                    dcanvas.coords("xalabel3",dwidth/1.9,dheight/1.91)
                                    dcanvas.coords("xalabel4",dwidth/23.3,dheight/1.41)
                                    dcanvas.coords("xalabel5",dwidth/1.9,dheight/1.41)
                                    dcanvas.coords("xalabel6",dwidth/1.9,dheight/0.95)

                                    dcanvas.coords("xaentry1",dwidth/1.9,dheight/1.74)
                                    dcanvas.coords("xaentry2",dwidth/1.9,dheight/1.32)

                                    dcanvas.coords("xacombo1",dwidth/23,dheight/1.74)
                                    dcanvas.coords("xacombo2",dwidth/23,dheight/1.32)
                                    dcanvas.coords("xacombo3",dwidth/1.9,dheight/1.09)
                                    dcanvas.coords("xacombo4",dwidth/1.9,dheight/0.91)

                                    dcanvas.coords("xatext1",dwidth/23,dheight/1.15)
                                    dcanvas.coords("xacheck1",dwidth/1.9,dheight/1.155)

                                    dcanvas.coords("xabutton1",dwidth/2.3,dheight/0.73)

                                p_canvas_4_2=Canvas(pro_frame_4_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                                pro_frame_4_2.grid_columnconfigure(0,weight=1)
                                pro_frame_4_2.grid_rowconfigure(0,weight=1)
                                
                                vertibar=Scrollbar(pro_frame_4_2, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=p_canvas_4_2.yview)

                                p_canvas_4_2.bind("<Configure>", pro_responsive_widgets_4_2)
                                p_canvas_4_2.config(yscrollcommand=vertibar.set)
                                p_canvas_4_2.grid(row=0,column=0,sticky='nsew')

                                def ser_exp_acc_create_2():
                                    acctype = comb_ser_3_1.get()
                                    detype = comb_ser_3_2.get()
                                    name = entry_ser_3_2.get()
                                    description = entry_ser_3_4.get()
                                    gst = comb_ser_3_3.get()
                                    deftaxcode = comb_ser_3_4.get()
                                    balance = 0
                                    today = datetime.date.today()
                                    asof = today.strftime("%Y-%m-%d")
                                    balfordisp = 0

                                    #----------------------
                                    usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usrp_val = (nm_ent.get(),)
                                    fbcursor.execute(usrp_sql,usrp_val)
                                    usrp_data_1 = fbcursor.fetchone()

                                    cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmpp_val = (usrp_data_1[0],)
                                    fbcursor.execute(cmpp_sql,cmpp_val)
                                    cmpp_data = fbcursor.fetchone()
                                    cid = cmpp_data[0]

                                    #product id --------------
                                    if acctype == "Account Receivable(Debtors)":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (1,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Current Assets":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (2,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Bank":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (3,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Fixed Assets":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (4,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Non-Current Assets":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (5,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Accounts Payable(Creditors)":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (6,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Credit Card":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (7,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Current Liabilities":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (8,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Non-Current Liabilities":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (9,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Equity":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (10,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Income":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (11,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Other Income":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (12,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Cost of Goods Sold":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (13,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Expenses":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (14,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    elif acctype == "Other Expenses":
                                        pro_sql = "SELECT * FROM producttable WHERE Pid=%s"
                                        pro_val = (15,)
                                        fbcursor.execute(pro_sql,pro_val)
                                        product_data_3 = fbcursor.fetchone()
                                    else:
                                        pass
                                    
                                    productid = product_data_3[0]
                                    #-----------------

                                    acctype_sql = "SELECT accountname FROM app1_accountype WHERE accountname=%s"
                                    acctype_val = (comb_ser_3_2.get(),)
                                    fbcursor.execute(acctype_sql,acctype_val)
                                    acctype_data = fbcursor.fetchone()

                                    acct_sql = "SELECT name,cid_id FROM app1_accounts WHERE name=%s AND cid_id=%s"
                                    acct_val = (entry_ser_3_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct_sql,acct_val)
                                    acct_data = fbcursor.fetchone()

                                    acct1_sql = "SELECT name,cid_id FROM app1_accounts1 WHERE name=%s AND cid_id=%s"
                                    acct1_val = (entry_ser_3_2.get(),cmpp_data[0])
                                    fbcursor.execute(acct1_sql,acct1_val)
                                    acct1_data = fbcursor.fetchone()
                                    

                                    if not acctype_data and not acct_data or not acct1_data:
                                        ins_acctype_sql = "INSERT INTO app1_accountype(cid_id,accountname,accountbal) VALUES(%s,%s,%s)"
                                        ins_acctype_val= (cmpp_data[0],detype,balance)
                                        fbcursor.execute(ins_acctype_sql,ins_acctype_val)
                                        finsysdb.commit()

                                        if acctype == "Account Receivable(Debtors)":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (1,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (1,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Current Assets":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (2,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------

                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (2,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Bank":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (3,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (3,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Fixed Assets":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (4,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (4,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Non-Current Assets":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (5,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (5,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Accounts Payable(Creditors)":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (6,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (6,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Credit Card":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (7,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (7,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Current Liabilities":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (8,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (8,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Non-Current Liabilities":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (9,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (9,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Equity":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (10,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (10,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Income":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (11,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (11,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Other Income":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (12,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (12,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Cost of Goods Sold":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (13,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (13,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Expenses":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (14,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (14,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        elif acctype == "Other Expenses":
                                            #pro id ------------
                                            pro_sql = "SELECT * FROM app1_accountype WHERE accountypeid=%s"
                                            pro_val = (15,)
                                            fbcursor.execute(pro_sql,pro_val)
                                            pro_data = fbcursor.fetchone()
                                            #--------------------
                                            ins_accts_sql = "INSERT INTO app1_accounts(acctype,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid_id,proid_id,productid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            ins_accts_val = (15,detype,name,description,gst,balfordisp,deftaxcode,balance,asof,cid,pro_data[0],productid)
                                            fbcursor.execute(ins_accts_sql,ins_accts_val)
                                            finsysdb.commit()
                                        else:
                                            pass

                                        sel_accts1_sql = "SELECT * FROM app1_accounts1 WHERE cid_id=%s"
                                        sel_accts1_val = (cid,)
                                        fbcursor.execute(sel_accts1_sql,sel_accts1_val)
                                        sel_accts1_data = fbcursor.fetchone()

                                        bal = sel_accts1_data[7] + float(balance)
                                        upd_accts1_sql = "UPDATE app1_accounts1 SET balance=%s WHERE cid_id=%s"
                                        upd_accts1_val = (bal,cid,)
                                        fbcursor.execute(upd_accts1_sql,upd_accts1_val)
                                        finsysdb.commit()

                                        pro_frame_4_2.destroy()
                                        pro_frame_4.grid(row=0,column=0,sticky='nsew')



                                p_canvas_4_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('xapoly1'))

                                label_1 = Label(p_canvas_4_2,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1, tags=('xalabel1'))

                                p_canvas_4_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('xahline'))

                                p_canvas_4_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('xapoly2'))

                                label_1 = Label(p_canvas_4_2,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel2'))

                                comb_ser_3_1 = ttk.Combobox(p_canvas_4_2, font=('arial 10'))
                                comb_ser_3_1['values'] = ("Account Receivable(Debtors)","Current Assets","Bank","Fixed Assets","Non-Current Assets","Accounts Payable(Creditors)","Credit Card","Current Liabilities","Non-Current Liabilities","Equity","Income","Other Income","Cost of Goods Sold","Expenses","Other Expenses",)
                                comb_ser_3_1.current(0)
                                window_comb_ser_3_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_3_1,tags=('xacombo1'))

                                
                                label_1 = Label(p_canvas_4_2,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel4'))

                                def entry_text_7(event):
                                    if comb_ser_3_2.get() == 'Account Receivable(Debtors)':
                                        entry_ser_3_2.delete(0,END)
                                        entry_ser_3_2.insert(0,'Account Receivable(Debtors)')


                                comb_ser_3_2 = ttk.Combobox(p_canvas_4_2, font=('arial 10'))
                                comb_ser_3_2['values'] = ("Account Receivable(Debtors)",)
                                comb_ser_3_2.bind("<<ComboboxSelected>>",entry_text_7)
                                window_comb_ser_3_2 = p_canvas_4_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_3_2,tags=('xacombo2'))

                                label_1 = Label(p_canvas_4_2,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel3'))

                                
                                entry_ser_3_2=Entry(p_canvas_4_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_ser_3_2 = p_canvas_4_2.create_window(0, 0, anchor="nw", height=30,window=entry_ser_3_2,tags=('xaentry1'))


                                label_1 = Label(p_canvas_4_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel5'))

                                entry_ser_3_4=Entry(p_canvas_4_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_ser_3_4 = p_canvas_4_2.create_window(0, 0, anchor="nw", height=30,window=entry_ser_3_4,tags=('xaentry2'))

                                ser_text_3 = Text(p_canvas_4_2,width=67, height=14, background='black',foreground='white')
                                ser_text_3.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                                window_ser_text_3 = p_canvas_4_2.create_window(0, 0, anchor="nw",window=ser_text_3,tags=('xatext1'))

                                def sub_check_7():
                                    comb_ser_3_3.config(state=NORMAL if chk_str_ser_3_1.get() else DISABLED)

                                chk_str_ser_3_1 = IntVar()
                                chkbtn_ser_3_1 = Checkbutton(p_canvas_4_2, text = "Is sub-account", variable = chk_str_ser_3_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                                window_chkbtn_ser_3_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=chkbtn_ser_3_1,tags=('xacheck1'))

                                comb_ser_3_3 = ttk.Combobox(p_canvas_4_2, font=('arial 10'),state=DISABLED)
                                comb_ser_3_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                                window_comb_ser_3_3 = p_canvas_4_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_3_3,tags=('xacombo3'))

                                label_1 = Label(p_canvas_4_2,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel6'))

                                comb_ser_3_4 = ttk.Combobox(p_canvas_4_2, font=('arial 10'))
                                comb_ser_3_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                                comb_ser_3_4.current(0)
                                window_comb_ser_3_4 = p_canvas_4_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_3_4,tags=('xacombo4'))

                                ser_sub_btn_3_1=Button(p_canvas_4_2,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=ser_exp_acc_create_2)
                                window_ser_sub_btn_3_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=ser_sub_btn_3_1,tags=('xabutton1'))

                                def s_back_2_():
                                    pro_frame_4_2.grid_forget()
                                    pro_frame_4.grid(row=0,column=0,sticky='nsew')

                                sbck_btn2=Button(p_canvas_4_2,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=s_back_2_)
                                window_sbck_btn2 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=sbck_btn2,tags=('xabutton3'))

                            expense_ser_btn=Button(p_canvas_4,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=ser_exp_acc_1)
                            window_expense_ser_btn = p_canvas_4.create_window(0, 0, anchor="nw", window=expense_ser_btn,tags=('spbutton4'),state=HIDDEN)

                            label_1 = Label(p_canvas_4,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel21'),state=HIDDEN)

                            def pr_3(event):
                                if entry_sser_item_11.get()=="0":
                                    entry_sser_item_11.delete(0,END)
                                else:
                                    pass

                            entry_sser_item_11=Entry(p_canvas_4,width=50,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_sser_item_11 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_sser_item_11,tags=('spentry11'),state=HIDDEN)
                            entry_sser_item_11.insert(0,"0")
                            entry_sser_item_11.bind("<Button-1>",pr_3)

                            label_1 = Label(p_canvas_4,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel22'),state=HIDDEN)

                            comb_ser_item_ps7 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                            comb_ser_item_ps7['values'] = ("Select Supplier",)
                            comb_ser_item_ps7.current(0)
                            window_comb_ser_item_ps7 = p_canvas_4.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_ser_item_ps7,tags=('spcombo7'),state=HIDDEN)

                            ser_sub_btn1=Button(p_canvas_4,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_new_pro_ser)
                            window_ser_sub_btn1 = p_canvas_4.create_window(0, 0, anchor="nw", window=ser_sub_btn1,tags=('spbutton5'))

                        p_btn_3=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=ser_add_item)
                        window_p_btn_3 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_3,tags=('apbutton3'),state=HIDDEN)

                        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly6"))

                        def buncall(event):
                            p_canvas_1.itemconfig('apimage4',state='hidden')
                            p_canvas_1.itemconfig('aplabel8',state='normal')
                            p_canvas_1.itemconfig('aplabel9',state='normal')
                            p_canvas_1.itemconfig('apbutton4',state='normal')

                        image_b1 = Image.open("images/bundle.png")
                        resize_image = image_b1.resize((200,150))
                        image_b1 = ImageTk.PhotoImage(resize_image)
                        btlogob = Label(p_canvas_1, width=200, height=150, background="#1b3857", image = image_b1) 
                        window_image = p_canvas_1.create_window(0, 0, anchor="nw", window=btlogob,tags=('apimage4'))
                        btlogob.photo = image_b1
                        btlogob.bind("<Button-1>",buncall)

                        label_1 = Label(p_canvas_1,width=10,height=1,text="Bundle", font=('arial 20'),background="#2f516f",fg="white") 
                        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel8'),state=HIDDEN)

                        label_1 = Label(p_canvas_1,width=46,height=2,text="A bundle is a group of software programs or hardware \ndevices that are grouped together and sold as one.", font=('arial 12'),background="#2f516f",fg="white") 
                        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel9'),state=HIDDEN)

                        def bun_add_item():
                            pro_frame_1.grid_forget()
                            pro_frame_5 = Frame(tab3_4)
                            pro_frame_5.grid(row=0,column=0,sticky='nsew')
                            
                            def pro_responsive_widgets_5(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("bppoly1",x1 + r1,y1,
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

                                dcanvas.coords("bplabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("bphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.45


                                dcanvas.coords("bppoly2",x11 + r2,y11,
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

                                r2 = 25
                                x11 = dwidth/24
                                x21 = dwidth/1.050
                                y11 = dheight/2.1
                                y21 = dheight/1.35


                                dcanvas.coords("bppoly3",x11 + r2,y11,
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

                                dcanvas.coords("bplabel2",dwidth/3,dheight/1.77)
                                dcanvas.coords("bpbutton1",dwidth/1.8,dheight/1.77)

                                dcanvas.coords("bplabel3",dwidth/23.2,dheight/1.23)
                                dcanvas.coords("bplabel4",dwidth/1.9,dheight/1.23)
                                dcanvas.coords("bplabel5",dwidth/25,dheight/1.02)
                                dcanvas.coords("bplabel6",dwidth/22.7,dheight/0.8)


                                dcanvas.coords("bpentry1",dwidth/23.2,dheight/1.165)
                                dcanvas.coords("bpentry2",dwidth/1.9,dheight/1.165)
                                dcanvas.coords("bpentry3",dwidth/23.2,dheight/0.97)

                                #-----------------------------H Lines---------------------------------#
                                dcanvas.coords("bpline1",dwidth/21.5,dheight/0.77,dwidth/1.075,dheight/0.77)
                                dcanvas.coords("bpline2",dwidth/21.5,dheight/0.72,dwidth/1.075,dheight/0.72)
                                dcanvas.coords("bpline3",dwidth/21.5,dheight/0.67,dwidth/1.075,dheight/0.67)
                                dcanvas.coords("bpline4",dwidth/21.5,dheight/0.619,dwidth/1.075,dheight/0.619)
                                dcanvas.coords("bpline5",dwidth/21.5,dheight/0.57,dwidth/1.075,dheight/0.57)
                                dcanvas.coords("bpline6",dwidth/21.5,dheight/0.535,dwidth/1.075,dheight/0.535)
                                #-----------------------------V Lines---------------------------------#
                                dcanvas.coords("bpline7",dwidth/21.5,dheight/0.77,dwidth/21.5,dheight/0.535)
                                dcanvas.coords("bpline8",dwidth/1.075,dheight/0.77,dwidth/1.075,dheight/0.535)
                                dcanvas.coords("bpline9",dwidth/4.8,dheight/0.77,dwidth/4.8,dheight/0.535)
                                dcanvas.coords("bpline10",dwidth/2.7,dheight/0.77,dwidth/2.7,dheight/0.535)
                                dcanvas.coords("bpline11",dwidth/1.84,dheight/0.77,dwidth/1.84,dheight/0.535)
                                dcanvas.coords("bpline12",dwidth/1.575,dheight/0.77,dwidth/1.575,dheight/0.535)
                                dcanvas.coords("bpline13",dwidth/1.366,dheight/0.77,dwidth/1.366,dheight/0.535)
                                dcanvas.coords("bpline14",dwidth/1.21,dheight/0.77,dwidth/1.21,dheight/0.535)

                                dcanvas.coords("bplabel7",dwidth/13,dheight/0.754)
                                dcanvas.coords("bplabel8",dwidth/3.85,dheight/0.754)
                                dcanvas.coords("bplabel9",dwidth/2.35,dheight/0.754)
                                dcanvas.coords("bplabel10",dwidth/1.75,dheight/0.754)
                                dcanvas.coords("bplabel11",dwidth/1.515,dheight/0.754)
                                dcanvas.coords("bplabel12",dwidth/1.325,dheight/0.754)
                                dcanvas.coords("bplabel13",dwidth/1.17,dheight/0.754)

                                dcanvas.coords("bpcombo1",dwidth/17,dheight/0.709)
                                dcanvas.coords("bpcombo2",dwidth/17,dheight/0.651)
                                dcanvas.coords("bpcombo3",dwidth/17,dheight/0.604)
                                dcanvas.coords("bpcombo4",dwidth/17,dheight/0.56)

                                dcanvas.coords("bpentry4",dwidth/4.6,dheight/0.709)
                                dcanvas.coords("bpentry5",dwidth/4.6,dheight/0.651)
                                dcanvas.coords("bpentry6",dwidth/4.6,dheight/0.604)
                                dcanvas.coords("bpentry7",dwidth/4.6,dheight/0.56)

                                dcanvas.coords("bpentry8",dwidth/2.6,dheight/0.709)
                                dcanvas.coords("bpentry9",dwidth/2.6,dheight/0.651)
                                dcanvas.coords("bpentry10",dwidth/2.6,dheight/0.604)
                                dcanvas.coords("bpentry11",dwidth/2.6,dheight/0.56)

                                dcanvas.coords("bpspin1",dwidth/1.81,dheight/0.709)
                                dcanvas.coords("bpspin2",dwidth/1.81,dheight/0.651)
                                dcanvas.coords("bpspin3",dwidth/1.81,dheight/0.604)
                                dcanvas.coords("bpspin4",dwidth/1.81,dheight/0.56)

                                dcanvas.coords("bpspin5",dwidth/1.56,dheight/0.709)
                                dcanvas.coords("bpspin6",dwidth/1.56,dheight/0.651)
                                dcanvas.coords("bpspin7",dwidth/1.56,dheight/0.604)
                                dcanvas.coords("bpspin8",dwidth/1.56,dheight/0.56)

                                dcanvas.coords("bpspin9",dwidth/1.351,dheight/0.709)
                                dcanvas.coords("bpspin10",dwidth/1.351,dheight/0.651)
                                dcanvas.coords("bpspin11",dwidth/1.351,dheight/0.604)
                                dcanvas.coords("bpspin12",dwidth/1.351,dheight/0.56)

                                dcanvas.coords("bpspin13",dwidth/1.195,dheight/0.709)
                                dcanvas.coords("bpspin14",dwidth/1.195,dheight/0.651)
                                dcanvas.coords("bpspin15",dwidth/1.195,dheight/0.604)
                                dcanvas.coords("bpspin16",dwidth/1.195,dheight/0.56)

                                dcanvas.coords("bpbutton2",dwidth/2.3,dheight/0.52)




                            p_canvas_5=Canvas(pro_frame_5, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_5.grid_columnconfigure(0,weight=1)
                            pro_frame_5.grid_rowconfigure(0,weight=1)
                            
                            vertibar=Scrollbar(pro_frame_5, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_5.yview)

                            p_canvas_5.bind("<Configure>", pro_responsive_widgets_5)
                            p_canvas_5.config(yscrollcommand=vertibar.set)
                            p_canvas_5.grid(row=0,column=0,sticky='nsew')

                            def add_new_pro_bun():

                                name = entry_bun_item_1.get()
                                sku = entry_bun_iitem_2.get()
                                description = entry_bun_item_7.get('1.0', 'end-1c')
                                product1 = bun_comb_1.get()
                                product2 = bun_comb_2.get()
                                product3 = bun_comb_3.get()
                                product4 = bun_comb_4.get()
                                hsn1 = bun_entry_1.get()
                                hsn2 = bun_entry_2.get()
                                hsn3 = bun_entry_3.get()
                                hsn4 = bun_entry_4.get()
                                description1 = bun_entry_5.get('1.0', 'end-1c')
                                description2 = bun_entry_6.get('1.0', 'end-1c')
                                description3 = bun_entry_7.get('1.0', 'end-1c')
                                description4 = bun_entry_8.get('1.0', 'end-1c')
                                qty1 = bun_entry_9.get()
                                qty2 = bun_entry_10.get()
                                qty3 = bun_entry_11.get()
                                qty4 = bun_entry_12.get()
                                price1 = bun_entry_13.get()
                                price2 = bun_entry_14.get()
                                price3 = bun_entry_15.get()
                                price4 = bun_entry_16.get()
                                total1 = bun_entry_17.get()
                                total2 = bun_entry_18.get()
                                total3 = bun_entry_19.get()
                                total4 = bun_entry_20.get()
                                tax1 = bun_entry_21.get()
                                tax2 = bun_entry_22.get()
                                tax3 = bun_entry_23.get()
                                tax4 = bun_entry_24.get()


                                usrp3_sql = "SELECT id FROM auth_user WHERE username=%s"
                                usrp3_val = (nm_ent.get(),)
                                fbcursor.execute(usrp3_sql,usrp3_val)
                                usrp3_data = fbcursor.fetchone()

                                cmpp3_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                cmpp3_val = (usrp3_data[0],)
                                fbcursor.execute(cmpp3_sql,cmpp3_val)
                                cmpp3_data = fbcursor.fetchone()
                                cid = cmpp3_data[0]

                                b_p_sql = "INSERT INTO app1_bundle(name,sku,description,product1,product2,product3,product4,hsn1,hsn2,hsn3,hsn4,description1,description2,description3,description4,qty1,qty2,qty3,qty4,price1,price2,price3,price4,total1,total2,total3,total4,tax1,tax2,tax3,tax4,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                b_p_val = (name,sku,description,product1,product2,product3,product4,hsn1,hsn2,hsn3,hsn4,description1,description2,description3,description4,qty1,qty2,qty3,qty4,price1,price2,price3,price4,total1,total2,total3,total4,tax1,tax2,tax3,tax4,cid)
                                fbcursor.execute(b_p_sql,b_p_val)
                                finsysdb.commit()

                                #_________Refresh insert tree________#

                                for record in pro_tree.get_children():
                                    pro_tree.delete(record)

        
                                sql_p="select * from auth_user where username=%s"
                                sql_p_val=(nm_ent.get(),)
                                fbcursor.execute(sql_p,sql_p_val,)
                                pr_dt=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dt[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dt=fbcursor.fetchone()

                                p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                p_val_1 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_1,p_val_1,)
                                p_data_1 = fbcursor.fetchall()
                                
                                count0 = 0
                                for i in p_data_1:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                    else:
                                        pass
                                count0 += 1

                                p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                p_val_2 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_2,p_val_2,)
                                p_data_2 = fbcursor.fetchall()

                                count1 = 0
                                for i in p_data_2:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count1 += 1

                                p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                p_val_3 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_3,p_val_3,)
                                p_data_3 = fbcursor.fetchall()
                                

                                count2 = 0
                                for i in p_data_3:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count2 += 1

                                p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                p_val_4 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_4,p_val_4,)
                                p_data_4 = fbcursor.fetchall()
                                

                                count3 = 0
                                for i in p_data_4:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                    else:
                                        pass
                                count3 += 1

                                pro_frame_5.destroy()
                                pro_frame.grid(row=0,column=0,sticky='nsew')


                            p_canvas_5.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('bppoly1'))

                            label_1 = Label(p_canvas_5,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel1'))

                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('bphline'))

                            p_canvas_5.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('bppoly2'))

                            p_canvas_5.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('bppoly3'))
                            
                            label_1 = Label(p_canvas_5,width=15,height=2,text="BUNDLE", font=('arial 20'),background="#2f516f",fg="white") 
                            window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel2'))

                            btn_bun_item_2=Button(p_canvas_5,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
                            window_btn_bun_item_2 = p_canvas_5.create_window(0, 0, anchor="nw", window=btn_bun_item_2, tags=('bpbutton1'))

                            label_1 = Label(p_canvas_5,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel3'))

                            entry_bun_item_1=Entry(p_canvas_5,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_bun_item_1 = p_canvas_5.create_window(55, 530, anchor="nw", height=30,window=entry_bun_item_1, tags=('bpentry1'))

                            label_1 = Label(p_canvas_5,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel4'))

                            def ps_4(event):
                                if entry_bun_iitem_2.get()=="N41554":
                                    entry_bun_iitem_2.delete(0,END)
                                else:
                                    pass

                            entry_bun_iitem_2=Entry(p_canvas_5,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_bun_iitem_2 = p_canvas_5.create_window(0, 0, anchor="nw", height=30,window=entry_bun_iitem_2, tags=('bpentry2'))
                            entry_bun_iitem_2.insert(0,"N41554")
                            entry_bun_iitem_2.bind("<Button-1>",ps_4)


                            label_1 = Label(p_canvas_5,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel5'))

                            entry_bun_item_7=scrolledtext.ScrolledText(p_canvas_5,width=146,background='#2f516f',foreground="white")
                            window_entry_bun_item_7 = p_canvas_5.create_window(0, 0, anchor="nw", height=60,window=entry_bun_item_7, tags=('bpentry3'))

                            label_1 = Label(p_canvas_5,width=30,height=1,text="Products/services included in the bundle", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel6'))

                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline1'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline2'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline3'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline4'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline5'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline6'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline7'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline8'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline9'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline10'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline11'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline12'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline13'))
                            p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline14'))
                            

                            label_3 = Label(p_canvas_5,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_3 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_3,tags=('bplabel7'))

                            label_4 = Label(p_canvas_5,width=10,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_4 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_4,tags=('bplabel8'))

                            label_4 = Label(p_canvas_5,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_4 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_4,tags=('bplabel9'))

                            label_4 = Label(p_canvas_5,width=5,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_4 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_4,tags=('bplabel10'))

                            label_4 = Label(p_canvas_5,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_4 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_4,tags=('bplabel11'))

                            label_4 = Label(p_canvas_5,width=8,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_4 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_4,tags=('bplabel12'))

                            label_4 = Label(p_canvas_5,width=8,height=1,text="TAX", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_4 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_4,tags=('bplabel13'))

                            def bun_details_1(event):
                                bun_to_str_1 = bun_comb_1.get()
                                try:
                                    sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                    val = (bun_to_str_1,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    bun_sel_1 = fbcursor.fetchone()
                                    bun_entry_1.delete(0,END)
                                    bun_entry_1.insert(0,bun_sel_1[4])
                                    bun_entry_5.delete('1.0',END)
                                    bun_entry_5.insert('1.0',bun_sel_1[11])
                                    bun_entry_13.delete(0,END)
                                    bun_entry_13.insert(0,bun_sel_1[12])
                                    bun_entry_21.delete(0,END)
                                    bun_entry_21.insert(0,bun_sel_1[14])
                                except:
                                    sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                    val = (bun_to_str_1,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    bun_sel_1 = fbcursor.fetchone()
                                    bun_entry_1.delete(0,END)
                                    bun_entry_1.insert(0,bun_sel_1[4])
                                    bun_entry_5.delete('1.0',END)
                                    bun_entry_5.insert('1.0',bun_sel_1[7])
                                    bun_entry_13.delete(0,END)
                                    bun_entry_13.insert(0,bun_sel_1[8])
                                    bun_entry_21.delete(0,END)
                                    bun_entry_21.insert(0,bun_sel_1[10])

                            def bun_details_2(event):
                                bun_to_str_2 = bun_comb_2.get()
                                try:
                                    sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                    val = (bun_to_str_2,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    bun_sel_2 = fbcursor.fetchone()
                                    bun_entry_2.delete(0,END)
                                    bun_entry_2.insert(0,bun_sel_2[4])
                                    bun_entry_6.delete('1.0',END)
                                    bun_entry_6.insert('1.0',bun_sel_2[11])
                                    bun_entry_14.delete(0,END)
                                    bun_entry_14.insert(0,bun_sel_2[12])
                                    bun_entry_22.delete(0,END)
                                    bun_entry_22.insert(0,bun_sel_2[14])
                                except:
                                    sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                    val = (bun_to_str_2,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    bun_sel_2 = fbcursor.fetchone()
                                    bun_entry_2.delete(0,END)
                                    bun_entry_2.insert(0,bun_sel_2[4])
                                    bun_entry_6.delete('1.0',END)
                                    bun_entry_6.insert('1.0',bun_sel_2[7])
                                    bun_entry_14.delete(0,END)
                                    bun_entry_14.insert(0,bun_sel_2[8])
                                    bun_entry_22.delete(0,END)
                                    bun_entry_22.insert(0,bun_sel_2[10])

                            def bun_details_3(event):
                                bun_to_str_3 = bun_comb_3.get()
                                try:
                                    sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                    val = (bun_to_str_3,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    bun_sel_3 = fbcursor.fetchone()
                                    bun_entry_3.delete(0,END)
                                    bun_entry_3.insert(0,bun_sel_3[4])
                                    bun_entry_7.delete('1.0',END)
                                    bun_entry_7.insert('1.0',bun_sel_3[11])
                                    bun_entry_15.delete(0,END)
                                    bun_entry_15.insert(0,bun_sel_3[12])
                                    bun_entry_23.delete(0,END)
                                    bun_entry_23.insert(0,bun_sel_3[14])
                                except:
                                    sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                    val = (bun_to_str_3,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    bun_sel_3 = fbcursor.fetchone()
                                    bun_entry_3.delete(0,END)
                                    bun_entry_3.insert(0,bun_sel_3[4])
                                    bun_entry_7.delete('1.0',END)
                                    bun_entry_7.insert('1.0',bun_sel_3[7])
                                    bun_entry_15.delete(0,END)
                                    bun_entry_15.insert(0,bun_sel_3[8])
                                    bun_entry_23.delete(0,END)
                                    bun_entry_23.insert(0,bun_sel_3[10])

                            def bun_details_4(event):
                                bun_to_str_4 = bun_comb_4.get()
                                try:
                                    sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                    val = (bun_to_str_4,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    bun_sel_4 = fbcursor.fetchone()
                                    bun_entry_4.delete(0,END)
                                    bun_entry_4.insert(0,bun_sel_4[4])
                                    bun_entry_8.delete('1.0',END)
                                    bun_entry_8.insert('1.0',bun_sel_4[11])
                                    bun_entry_16.delete(0,END)
                                    bun_entry_16.insert(0,bun_sel_4[12])
                                    bun_entry_24.delete(0,END)
                                    bun_entry_24.insert(0,bun_sel_4[14])
                                except:
                                    sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                    val = (bun_to_str_4,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    bun_sel_4 = fbcursor.fetchone()
                                    bun_entry_4.delete(0,END)
                                    bun_entry_4.insert(0,bun_sel_4[4])
                                    bun_entry_8.delete('1.0',END)
                                    bun_entry_8.insert('1.0',bun_sel_4[7])
                                    bun_entry_16.delete(0,END)
                                    bun_entry_16.insert(0,bun_sel_4[8])
                                    bun_entry_24.delete(0,END)
                                    bun_entry_24.insert(0,bun_sel_4[10])
                                

                            sql_pi="select * from auth_user where username=%s"
                            pi_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pi,pi_val,)
                            pi_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pi_dtl[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dtli=fbcursor.fetchone()
                            print(cmp_dtli)

                            bi_sql = "SELECT name FROM app1_inventory where cid_id=%s"
                            bi_val = (cmp_dtli[0],)
                            fbcursor.execute(bi_sql,bi_val)
                            bi_data = fbcursor.fetchall()
                        
                            bii_sql = "SELECT name FROM app1_noninventory where cid_id=%s"
                            bii_val = (cmp_dtli[0],)
                            fbcursor.execute(bii_sql,bii_val)
                            bii_data = fbcursor.fetchall()

                            b_data = []   
                            
                            for i in bi_data:
                                b_data.append(i[0])
                            for i in bii_data:
                                b_data.append(i[0])
                                


                            bun_comb_1 = ttk.Combobox(p_canvas_5, font=('arial 10'),values=b_data)
                            # bun_comb_1['values'] = ("Choose",b_data,)
                            bun_comb_1.bind("<<ComboboxSelected>>",bun_details_1)
                            window_bun_comb_1 = p_canvas_5.create_window(0, 0, anchor="nw", width=180, height=30,window=bun_comb_1,tags=('bpcombo1'))

                            bun_comb_2 = ttk.Combobox(p_canvas_5, font=('arial 10'),values=b_data)
                            # bun_comb_2['values'] = ("Choose",b_data,)
                            bun_comb_2.bind("<<ComboboxSelected>>",bun_details_2)
                            window_bun_comb_2 = p_canvas_5.create_window(0, 0, anchor="nw", width=180, height=30,window=bun_comb_2,tags=('bpcombo2'))

                            bun_comb_3 = ttk.Combobox(p_canvas_5, font=('arial 10'),values=b_data)
                            # bun_comb_3['values'] = ("Choose",b_data,)
                            bun_comb_3.bind("<<ComboboxSelected>>",bun_details_3)
                            window_bun_comb_3 = p_canvas_5.create_window(0, 0, anchor="nw", width=180, height=30,window=bun_comb_3,tags=('bpcombo3'))

                            bun_comb_4 = ttk.Combobox(p_canvas_5, font=('arial 10'),values=b_data)
                            # bun_comb_4['values'] = ("Choose",b_data,)
                            bun_comb_4.bind("<<ComboboxSelected>>",bun_details_4)
                            window_bun_comb_4 = p_canvas_5.create_window(0, 0, anchor="nw", width=180, height=30,window=bun_comb_4,tags=('bpcombo4'))

                        

                            bun_entry_1=Entry(p_canvas_5,width=30,justify=LEFT,background='#2f516f',foreground="white")
                            window_bun_entry_1 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_1,tags=('bpentry4'))
                            

                            bun_entry_2=Entry(p_canvas_5,width=30,justify=LEFT,background='#2f516f',foreground="white")
                            window_bun_entry_2 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_2,tags=('bpentry5'))
                            

                            bun_entry_3=Entry(p_canvas_5,width=30,justify=LEFT,background='#2f516f',foreground="white")
                            window_bun_entry_3 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_3,tags=('bpentry6'))
                            
                            bun_entry_4=Entry(p_canvas_5,width=30,justify=LEFT,background='#2f516f',foreground="white")
                            window_bun_entry_4 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_4,tags=('bpentry7'))



                            bun_entry_5=scrolledtext.ScrolledText(p_canvas_5,width=23,background='#2f516f',foreground="white")
                            window_bun_entry_5 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_5,tags=('bpentry8'))

                            bun_entry_6=scrolledtext.ScrolledText(p_canvas_5,width=23,background='#2f516f',foreground="white")
                            window_bun_entry_6 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_6,tags=('bpentry9'))

                            bun_entry_7=scrolledtext.ScrolledText(p_canvas_5,width=23,background='#2f516f',foreground="white")
                            window_bun_entry_7 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_7,tags=('bpentry10'))

                            bun_entry_8=scrolledtext.ScrolledText(p_canvas_5,width=23,background='#2f516f',foreground="white")
                            window_bun_entry_8 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_8,tags=('bpentry11'))


                            bun_entry_9=Spinbox(p_canvas_5,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_9 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_9,tags=('bpspin1'))
                            bun_entry_9.delete(0, END)
                            bun_entry_9.insert(0, '0')

                            bun_entry_10=Spinbox(p_canvas_5,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_10 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_10,tags=('bpspin2'))
                            bun_entry_10.delete(0, END)
                            bun_entry_10.insert(0, '0')

                            bun_entry_11=Spinbox(p_canvas_5,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_11 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_11,tags=('bpspin3'))
                            bun_entry_11.delete(0, END)
                            bun_entry_11.insert(0, '0')

                            bun_entry_12=Spinbox(p_canvas_5,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_12 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_12,tags=('bpspin4'))
                            bun_entry_12.delete(0, END)
                            bun_entry_12.insert(0, '0')

                            
                            bun_entry_13=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_13 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_13,tags=('bpspin5'))
                            bun_entry_13.delete(0, END)
                            bun_entry_13.insert(0, '0.0')
                            
                            bun_entry_14=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_14 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_14,tags=('bpspin6'))
                            bun_entry_14.delete(0, END)
                            bun_entry_14.insert(0, '0.0')

                            bun_entry_15=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_15 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_15,tags=('bpspin7'))
                            bun_entry_15.delete(0, END)
                            bun_entry_15.insert(0, '0.0')

                            bun_entry_16=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_16 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_16,tags=('bpspin8'))
                            bun_entry_16.delete(0, END)
                            bun_entry_16.insert(0, '0.0')

                            def multiply_num_1(event):
                                num1= float(bun_entry_9.get())
                                num2= float(bun_entry_13.get())
                                mul= round(num1 * num2)
                                bun_entry_17.delete(0, END)
                                bun_entry_17.insert(0,mul)
                            
                            bun_entry_17=Entry(p_canvas_5,width=16,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_17 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_17,tags=('bpspin9'))
                            bun_entry_17.bind("<Button-1>",multiply_num_1)

                            def multiply_num_2(event):
                                num1= float(bun_entry_10.get())
                                num2= float(bun_entry_14.get())
                                mul= round(num1 * num2)
                                bun_entry_18.delete(0, END)
                                bun_entry_18.insert(0,mul)
                        
                            
                            bun_entry_18=Entry(p_canvas_5,width=16,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_18 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_18,tags=('bpspin10'))
                            bun_entry_18.bind("<Button-1>",multiply_num_2)

                            def multiply_num_3(event):
                                num1= float(bun_entry_11.get())
                                num2= float(bun_entry_15.get())
                                mul= round(num1 * num2)
                                bun_entry_19.delete(0, END)
                                bun_entry_19.insert(0,mul)
                            
                            bun_entry_19=Entry(p_canvas_5,width=16,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_19 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_19,tags=('bpspin11'))
                            bun_entry_19.bind("<Button-1>",multiply_num_3)

                            def multiply_num_4(event):
                                num1= float(bun_entry_12.get())
                                num2= float(bun_entry_16.get())
                                mul= round(num1 * num2)
                                bun_entry_20.delete(0, END)
                                bun_entry_20.insert(0,mul)
                        
                            bun_entry_20=Entry(p_canvas_5,width=16,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_20 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_20,tags=('bpspin12'))
                            bun_entry_20.bind("<Button-1>",multiply_num_4)

                            
                            bun_entry_21=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_21 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_21,tags=('bpspin13'))
                            bun_entry_21.delete(0, END)
                            bun_entry_21.insert(0, '0.0')

                            bun_entry_22=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_22 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_22,tags=('bpspin14'))
                            bun_entry_22.delete(0, END)
                            bun_entry_22.insert(0, '0.0')

                            bun_entry_23=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_23 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_23,tags=('bpspin15'))
                            bun_entry_23.delete(0, END)
                            bun_entry_23.insert(0, '0.0')

                            bun_entry_24=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_bun_entry_24 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_24,tags=('bpspin16'))
                            bun_entry_24.delete(0, END)
                            bun_entry_24.insert(0, '0.0')

                            bun_sub_btn1=Button(p_canvas_5,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_new_pro_bun)
                            window_bun_sub_btn1 = p_canvas_5.create_window(0, 0, anchor="nw", window=bun_sub_btn1,tags=('bpbutton2'))


                        p_btn_4=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=bun_add_item)
                        window_p_btn_4 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_4,tags=('apbutton4'),state=HIDDEN)

                        def pro_back_1():
                            pro_frame_1.grid_forget()
                            pro_frame.grid(row=0,column=0,sticky='nsew')

                        pbck_btn1=Button(p_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=pro_back_1)
                        window_pbck_btn1 = p_canvas_1.create_window(0, 0, anchor="nw", window=pbck_btn1,tags=('apbutton5'))


                    pbtn1=Button(pro_canvas,text='Add Products', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_product)
                    window_pbtn1 = pro_canvas.create_window(0, 0, anchor="nw", window=pbtn1,tags=('pbutton2'))

                    def pro_edit_item(event):
                        if pro_comb_1.get() == 'Edit':
                            if pro_tree.item(pro_tree.focus())["values"][1] == 'Inventory':
                                pro_frame.grid_forget()
                                pro_frame_edit_1 = Frame(tab3_4)
                                pro_frame_edit_1.grid(row=0,column=0,sticky='nsew')

                                def pro_responsive_widgets_2(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("ieppoly1",x1 + r1,y1,
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

                                    dcanvas.coords("ieplabel1",dwidth/3,dheight/8.24)
                                    dcanvas.coords("iephline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.29


                                    dcanvas.coords("ieppoly2",x11 + r2,y11,
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

                                    r2 = 25
                                    x11 = dwidth/24
                                    x21 = dwidth/1.050
                                    y11 = dheight/2.1
                                    y21 = dheight/1.35


                                    dcanvas.coords("ieppoly3",x11 + r2,y11,
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

                                    dcanvas.coords("ieplabel2",dwidth/2.4,dheight/1.77)
                                    dcanvas.coords("iepbutton1",dwidth/1.8,dheight/1.77)

                                    dcanvas.coords("ieplabel3",dwidth/23.2,dheight/1.23)
                                    dcanvas.coords("ieplabel4",dwidth/23.3,dheight/1.02)
                                    dcanvas.coords("ieplabel5",dwidth/1.9,dheight/1.02)
                                    dcanvas.coords("ieplabel6",dwidth/1.9,dheight/0.92)
                                    dcanvas.coords("ieplabel7",dwidth/27,dheight/0.865)
                                    dcanvas.coords("ieplabel8",dwidth/1.915,dheight/0.865)
                                    dcanvas.coords("ieplabel9",dwidth/50,dheight/0.76)
                                    dcanvas.coords("ieplabel10",dwidth/2.95,dheight/0.76)
                                    dcanvas.coords("ieplabel11",dwidth/1.54,dheight/0.76)
                                    dcanvas.coords("ieplabel12",dwidth/38,dheight/0.675)
                                    dcanvas.coords("ieplabel13",dwidth/26.8,dheight/0.606)
                                    dcanvas.coords("ieplabel14",dwidth/28.3,dheight/0.538)
                                    dcanvas.coords("ieplabel15",dwidth/1.9,dheight/0.538)
                                    dcanvas.coords("ieplabel16",dwidth/28.4,dheight/0.485)
                                    dcanvas.coords("ieplabel17",dwidth/29.3,dheight/0.438)
                                    dcanvas.coords("ieplabel18",dwidth/28,dheight/0.401)
                                    dcanvas.coords("ieplabel19",dwidth/1.91,dheight/0.401)
                                    dcanvas.coords("ieplabel20",dwidth/28,dheight/0.37)
                                    dcanvas.coords("ieplabel21",dwidth/26,dheight/0.35)
                                    dcanvas.coords("ieplabel22",dwidth/1.9,dheight/0.35)

                                    dcanvas.coords("iepentry1",dwidth/23.2,dheight/1.165)
                                    dcanvas.coords("iepentry2",dwidth/23.2,dheight/0.975)
                                    dcanvas.coords("iepentry3",dwidth/1.9,dheight/0.975)
                                    dcanvas.coords("iepentry4",dwidth/1.9,dheight/0.83)
                                    dcanvas.coords("iepentry5",dwidth/23.2,dheight/0.73)
                                    dcanvas.coords("iepentry6",dwidth/1.52,dheight/0.73)
                                    dcanvas.coords("iepentry7",dwidth/23.2,dheight/0.59)
                                    dcanvas.coords("iepentry8",dwidth/23.2,dheight/0.525)
                                    dcanvas.coords("iepentry9",dwidth/23.2,dheight/0.43)
                                    dcanvas.coords("iepentry10",dwidth/23.2,dheight/0.394)
                                    dcanvas.coords("iepentry11",dwidth/23.2,dheight/0.344)

                                    dcanvas.coords("iepcombo1",dwidth/23.2,dheight/0.83)
                                    dcanvas.coords("iepcombo2",dwidth/23.2,dheight/0.654)
                                    dcanvas.coords("iepcombo3",dwidth/1.9,dheight/0.525)
                                    dcanvas.coords("iepcombo4",dwidth/23.2,dheight/0.474)
                                    dcanvas.coords("iepcombo5",dwidth/1.89,dheight/0.394)
                                    dcanvas.coords("iepcombo6",dwidth/23.2,dheight/0.364)
                                    dcanvas.coords("iepcombo7",dwidth/1.89,dheight/0.344)

                                    dcanvas.coords("iepcbutton1",dwidth/23.2,dheight/0.51)
                                    dcanvas.coords("iepcbutton2",dwidth/23.2,dheight/0.385)

                                    dcanvas.coords("iepbutton2",dwidth/2.45,dheight/0.654)
                                    dcanvas.coords("iepbutton3",dwidth/2.45,dheight/0.474)
                                    dcanvas.coords("iepbutton4",dwidth/2.45,dheight/0.364)
                                    dcanvas.coords("iepbutton5",dwidth/2.38,dheight/0.325)

                                    dcanvas.coords("iepbuttn1",dwidth/23,dheight/3.415)

                                    dcanvas.coords("iephline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)

                                    try:
                                        dcanvas.coords("iepdate1",dwidth/2.9,dheight/0.73)
                                    except:
                                        pass


                                p_canvas_edit_1=Canvas(pro_frame_edit_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                                pro_frame_edit_1.grid_columnconfigure(0,weight=1)
                                pro_frame_edit_1.grid_rowconfigure(0,weight=1)
                            
                                vertibar=Scrollbar(pro_frame_edit_1, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=p_canvas_edit_1.yview)

                                p_canvas_edit_1.bind("<Configure>", pro_responsive_widgets_2)
                                p_canvas_edit_1.config(yscrollcommand=vertibar.set)
                                p_canvas_edit_1.grid(row=0,column=0,sticky='nsew')

                                inv_peditid = pro_tree.item(pro_tree.focus())["values"][2]
                                print(inv_peditid)

                                inv_peditid_1 = pro_tree.item(pro_tree.focus())["values"][3]
                                print(inv_peditid_1)

                                sql_pi="select * from auth_user where username=%s"
                                pi_val=(nm_ent.get(),)
                                fbcursor.execute(sql_pi,pi_val,)
                                pi_dtl=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pi_dtl[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dtli=fbcursor.fetchone()
                                print(cmp_dtli)

                                sql = 'select * from app1_inventory where name = %s and sku = %s and cid_id = %s'
                                val =  (inv_peditid,inv_peditid_1,cmp_dtli[0],)
                                fbcursor.execute(sql,val)
                                edit_pinv = fbcursor.fetchone()

                                def edit_new_pro_inv():
                                    name = edit_inv_pitem_1.get()
                                    sku = edit_inv_pitem_2.get()
                                    hsn = edit_inv_pitem_h1.get()
                                    unit = comb_inv_edit_p1.get()
                                    category = edit_inv_pitem_3.get()
                                    initialqty = edit_inv_pitem_4.get()
                                    date = edit_inv_pitem_aod5.get_date()
                                    stockalrt = edit_inv_pitem_6.get()
                                    invacnt = comb_inv_edit_i2.get()
                                    description = edit_inv_pitem_7.get('1.0', 'end-1c')
                                    salesprice = edit_inv_pitem_8.get()
                                    incomeacnt = comb_inv_edit_in4.get()
                                    tax = comb_inv_edit_t3.get()
                                    purchaseinfo = edit_inv_pitem_9.get('1.0', 'end-1c')
                                    cost = edit_inv_pitem_10.get()
                                    expacnt = comb_inv_edit_ex6.get()
                                    purtax = comb_inv_edit_pu5.get()
                                    revcharge = edit_inv_pitem_11.get()
                                    presupplier = comb_inv_edit_pr7.get()

                                    usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usrp_val = (nm_ent.get(),)
                                    fbcursor.execute(usrp_sql,usrp_val)
                                    usrp_data = fbcursor.fetchone()

                                    cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmpp_val = (usrp_data[0],)
                                    fbcursor.execute(cmpp_sql,cmpp_val)
                                    cmpp_data = fbcursor.fetchone()
                                    cid = cmpp_data[0]
                                    
                                    i_p_sql = "UPDATE app1_inventory set  name=%s,sku=%s,hsn=%s,unit=%s,category=%s,initialqty=%s,date=%s,stockalrt=%s,invacnt=%s,description=%s,salesprice=%s,incomeacnt=%s,tax=%s,purchaseinfo=%s,cost=%s,expacnt=%s,purtax=%s,revcharge=%s,presupplier=%s,cid_id=%s where name=%s and sku = %s"
                                    i_p_val = (name,sku,hsn,unit,category,initialqty,date,stockalrt,invacnt,description,salesprice,incomeacnt,tax,purchaseinfo,cost,expacnt,purtax,revcharge,presupplier,cid,inv_peditid,inv_peditid_1)
                                    fbcursor.execute(i_p_sql,i_p_val)
                                    finsysdb.commit()

                                    #_________Refresh insert tree________#
                
                                    for record in pro_tree.get_children():
                                        pro_tree.delete(record)


                                    sql_p="select * from auth_user where username=%s"
                                    sql_p_val=(nm_ent.get(),)
                                    fbcursor.execute(sql_p,sql_p_val,)
                                    pr_dt=fbcursor.fetchone()

                                    sql = "select * from app1_company where id_id=%s"
                                    val = (pr_dt[0],)
                                    fbcursor.execute(sql, val,)
                                    cmp_dt=fbcursor.fetchone()

                                    p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                    p_val_1 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_1,p_val_1,)
                                    p_data_1 = fbcursor.fetchall()
                                    
                                    count0 = 0
                                    for i in p_data_1:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                        else:
                                            pass
                                    count0 += 1

                                    p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                    p_val_2 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_2,p_val_2,)
                                    p_data_2 = fbcursor.fetchall()

                                    count1 = 0
                                    for i in p_data_2:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                        else:
                                            pass
                                    count1 += 1

                                    p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                    p_val_3 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_3,p_val_3,)
                                    p_data_3 = fbcursor.fetchall()
                                    

                                    count2 = 0
                                    for i in p_data_3:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                        else:
                                            pass
                                    count2 += 1

                                    p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                    p_val_4 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_4,p_val_4,)
                                    p_data_4 = fbcursor.fetchall()
                                    

                                    count3 = 0
                                    for i in p_data_4:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                        else:
                                            pass
                                    count3 += 1

                                    pro_frame_edit_1.destroy()
                                    pro_frame.grid(row=0,column=0,sticky='nsew')



                                p_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('ieppoly1'))

                                label_1 = Label(p_canvas_edit_1,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ieplabel1'))

                                p_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iephline'))

                                p_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('ieppoly2'))

                                p_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('ieppoly3'))

                                label_1 = Label(p_canvas_edit_1,width=10,height=2,text="INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ieplabel2'))


                                label_1 = Label(p_canvas_edit_1,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ieplabel3'))

                                edit_inv_pitem_1=Entry(p_canvas_edit_1,width=200,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_inv_pitem_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_1, tags=('iepentry1'))
                                edit_inv_pitem_1.delete(0,'end')
                                edit_inv_pitem_1.insert(0, edit_pinv[2])

                                label_1 = Label(p_canvas_edit_1,width=4,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ieplabel4'))

                                def pei_sku_1(event):
                                    if edit_inv_pitem_2.get()==edit_pinv[3]:
                                        edit_inv_pitem_2.delete(0,END)
                                    else:
                                        pass
                                
                                edit_inv_pitem_2=Entry(p_canvas_edit_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_inv_pitem_2 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_2, tags=('iepentry2'))
                                # edit_inv_pitem_2.insert(0,"N41554")
                                edit_inv_pitem_2.bind("<Button-1>",pei_sku_1)
                                edit_inv_pitem_2.delete(0,'end')
                                edit_inv_pitem_2.insert(0, edit_pinv[3])


                                label_1 = Label(p_canvas_edit_1,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ieplabel5'))

                                edit_inv_pitem_h1=Entry(p_canvas_edit_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_inv_pitem_h1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_h1, tags=('iepentry3'))
                                edit_inv_pitem_h1.delete(0,'end')
                                edit_inv_pitem_h1.insert(0, edit_pinv[4])

                                #Define a callback function
                                def ecallback(url):
                                    webbrowser.open_new_tab(url)

                                link_e1 = Label(p_canvas_edit_1,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
                                window_link_e1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=link_e1, tags=('ieplabel6'))
                                link_e1.bind("<Button-1>", lambda e:
                                ecallback("https://gstcouncil.gov.in/sites/default/files/goods-rates-booklet-03July2017.pdf"))

                                label_1 = Label(p_canvas_edit_1,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ieplabel7'))

                                comb_inv_edit_p1 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                                comb_inv_edit_p1['values'] = ("Choose...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards",)
                                comb_inv_edit_p1.current(0)
                                window_comb_inv_edit_p1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_edit_p1, tags=('iepcombo1'))
                                comb_inv_edit_p1.delete(0,'end')
                                comb_inv_edit_p1.insert(0, edit_pinv[5])


                                label_1 = Label(p_canvas_edit_1,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel8'))

                                edit_inv_pitem_3=Entry(p_canvas_edit_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_inv_pitem_3 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_3,tags=('iepentry4'))
                                edit_inv_pitem_3.delete(0,'end')
                                edit_inv_pitem_3.insert(0, edit_pinv[6])

                                label_1 = Label(p_canvas_edit_1,width=24,height=1,text="Initial quantity on hand", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel9'))

                                edit_inv_pitem_4=Entry(p_canvas_edit_1,width=60,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_inv_pitem_4 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_4,tags=('iepentry5'))
                                edit_inv_pitem_4.delete(0,'end')
                                edit_inv_pitem_4.insert(0, edit_pinv[7])

                                label_1 = Label(p_canvas_edit_1,width=10,height=1,text="As of date", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel10'))
                    
                                label_1 = Label(p_canvas_edit_1,width=14,height=1,text="Low stock alert", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel11'))

                                edit_inv_pitem_6=Entry(p_canvas_edit_1,width=60,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_inv_pitem_6 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_6,tags=('iepentry6'))
                                edit_inv_pitem_6.delete(0,'end')
                                edit_inv_pitem_6.insert(0, edit_pinv[9])

                                label_1 = Label(p_canvas_edit_1,width=22,height=1,text="Inventory asset account", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(35, 910, anchor="nw", window=label_1,tags=('ieplabel12'))

                                sql = "select * from auth_user where username=%s"
                                val = (nm_ent.get(),)
                                fbcursor.execute(sql,val,)
                                udtl = fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (udtl[0],)
                                fbcursor.execute(sql,val,)
                                cdtl = fbcursor.fetchone()

                                sql = "select name from app1_accounts where acctype=%s and detype=%s and cid_id=%s"
                                val = (2,'Inventory',cdtl[0],)
                                fbcursor.execute(sql,val,)
                                is_ac_data = fbcursor.fetchall()
                                ac_data_1 = ["Inventory Asset"]
                                for i in is_ac_data:
                                    ac_data_1.insert(-1,i[0])


                                comb_inv_edit_i2 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                                comb_inv_edit_i2['values'] = (ac_data_1)
                                comb_inv_edit_i2.current(0)
                                window_comb_inv_edit_i2 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_edit_i2,tags=('iepcombo2'))
                                comb_inv_edit_i2.delete(0,'end')
                                comb_inv_edit_i2.insert(0, edit_pinv[10])

                                
                                label_1 = Label(p_canvas_edit_1,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel13'))

                                edit_inv_pitem_7=scrolledtext.ScrolledText(p_canvas_edit_1,width=145,background='#2f516f',foreground="white")
                                window_edit_inv_pitem_7 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=60,window=edit_inv_pitem_7,tags=('iepentry7'))
                                edit_inv_pitem_7.insert(1.0,edit_pinv[11])

                                label_1 = Label(p_canvas_edit_1,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel14'))

                                def edit_inv_tax_check_1():
                                    if comb_inv_edit_t3.get() == '28.0% GST (28%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+28)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '28.0% IGST (28%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+28)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '18.0% GST (18%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+18)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '18.0% IGST (18%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+18)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '15.0% ST (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+15)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '14.5% ST (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+14.5)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '14.00% ST (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+14)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '14.0% VAT (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+14)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '12.36% ST (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+12.36)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '12.0% GST (12%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+12)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '12.0% IGST (12%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+12)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '6.0% GST (6%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+6)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '6.0% IGST (6%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+6)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '6.0% IGST (6%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+6)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '5.0% GST (5%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+5)))
                                        print(gst)
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '5.0% IGST (5%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+5)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '5.0% VAT (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+5)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '4.0% VAT (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+4)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '3.0% GST (3%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+3)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '3.0% IGST (3%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+3)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '2.0% CST (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+2)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '0.25% GST (O.25%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+0.25)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '0.25% IGST (0.25%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+0.25)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '0% GST (0%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+0)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == '0% IGST (0%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+0)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == 'Exempt GST (0%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+0)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == 'Exempt IGST (0%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+0)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_t3.get() == 'Out of Scope(0%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_8.get())
                                        gst = n1-(n1*(100/(100+0)))
                                        np = n1-gst
                                        if chk_str_einv_item.get() == True:
                                            edit_inv_pitem_8.delete(0,'end')
                                            edit_inv_pitem_8.insert(0, np)
                                        else:
                                            pass
                                    else:
                                        pass
                                
                                edit_inv_pitem_8=Entry(p_canvas_edit_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_inv_pitem_8 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_8,tags=('iepentry8'))
                                edit_inv_pitem_8.delete(0,'end')
                                edit_inv_pitem_8.insert(0, edit_pinv[12])

                                chk_str_einv_item = BooleanVar()
                                chkbtn_inv_pitem_1 = Checkbutton(p_canvas_edit_1, text = "Inclusive of tax", variable = chk_str_einv_item,font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=edit_inv_tax_check_1)
                                window_chkbtn_inv_pitem_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=chkbtn_inv_pitem_1,tags=('iepcbutton1'))

                                label_1 = Label(p_canvas_edit_1,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel15'))

                                comb_inv_edit_t3 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                                comb_inv_edit_t3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                                comb_inv_edit_t3.current(0)
                                window_comb_inv_edit_t3 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_edit_t3,tags=('iepcombo3'))
                                comb_inv_edit_t3.delete(0,'end')
                                comb_inv_edit_t3.insert(0, edit_pinv[14])

                                label_1 = Label(p_canvas_edit_1,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel16'))

                                sql = "select * from auth_user where username=%s"
                                val = (nm_ent.get(),)
                                fbcursor.execute(sql,val,)
                                udtl = fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (udtl[0],)
                                fbcursor.execute(sql,val,)
                                cdtl = fbcursor.fetchone()


                                sql = "select name from app1_accounts where acctype=%s and detype=%s and cid_id=%s"
                                val = (11,'Sales of Product Income',cdtl[0],)
                                fbcursor.execute(sql,val,)
                                in_ac_data = fbcursor.fetchall()
                                ac_data_2 = ["Choose...","Billable Expense Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales of Product Income","Uncategorised Income"]
                                for i in in_ac_data:
                                    ac_data_2.insert(-1,i[0])

                                comb_inv_edit_in4 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                                comb_inv_edit_in4['values'] = (ac_data_2)
                                comb_inv_edit_in4.current(0)
                                window_comb_inv_edit_in4 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_edit_in4,tags=('iepcombo4'))
                                comb_inv_edit_in4.delete(0,'end')
                                comb_inv_edit_in4.insert(0, edit_pinv[13])


                                p_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iephline1'))

                                label_1 = Label(p_canvas_edit_1,width=22,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel17'))

                                edit_inv_pitem_9=scrolledtext.ScrolledText(p_canvas_edit_1,width=145,background='#2f516f',foreground="white")
                                window_edit_inv_pitem_9 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=60,window=edit_inv_pitem_9,tags=('iepentry9'))
                                edit_inv_pitem_9.insert(1.0,edit_pinv[15])

                                label_1 = Label(p_canvas_edit_1,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel18'))

                                def edit_inv_tax_check_2():
                                    if comb_inv_edit_pu5.get() == '28.0% GST (28%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+28)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '28.0% IGST (28%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+28)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '18.0% GST (18%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+18)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '18.0% IGST (18%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+18)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '15.0% ST (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+15)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '14.5% ST (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+14.5)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '14.00% ST (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+14)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '14.0% VAT (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+14)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '12.36% ST (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+12.36)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '12.0% GST (12%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+12)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '12.0% IGST (12%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+12)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '6.0% GST (6%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+6)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '6.0% IGST (6%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+6)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '6.0% IGST (6%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+6)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '5.0% GST (5%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+5)))
                                        print(gst)
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '5.0% IGST (5%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+5)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '5.0% VAT (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+5)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '4.0% VAT (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+4)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '3.0% GST (3%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+3)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '3.0% IGST (3%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+3)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '2.0% CST (100%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+2)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '0.25% GST (O.25%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+0.25)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '0.25% IGST (0.25%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+0.25)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '0% GST (0%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+0)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == '0% IGST (0%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+0)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == 'Exempt GST (0%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+0)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == 'Exempt IGST (0%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+0)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    elif comb_inv_edit_pu5.get() == 'Out of Scope(0%)':
                                        gst = 0.0
                                        np = 0.0
                                        n1 = float(edit_inv_pitem_10.get())
                                        gst = n1-(n1*(100/(100+0)))
                                        np = n1-gst
                                        if chk_str_inv_pitem_1.get() == True:
                                            edit_inv_pitem_10.delete(0,'end')
                                            edit_inv_pitem_10.insert(0, np)
                                        else:
                                            pass
                                    else:
                                        pass
                                
                                edit_inv_pitem_10=Entry(p_canvas_edit_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_inv_pitem_10 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_10,tags=('iepentry10'))
                                edit_inv_pitem_10.delete(0,'end')
                                edit_inv_pitem_10.insert(0, edit_pinv[16])


                                chk_str_inv_pitem_1 = BooleanVar()
                                chkbtn_inv_pitem_2 = Checkbutton(p_canvas_edit_1, text = "Inclusive of purchase tax", variable = chk_str_inv_pitem_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=edit_inv_tax_check_2)
                                window_chkbtn_inv_pitem_2 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=chkbtn_inv_pitem_2,tags=('iepcbutton2'))

                                label_1 = Label(p_canvas_edit_1,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(700, 1530, anchor="nw", window=label_1,tags=('ieplabel19'))

                                comb_inv_edit_pu5 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                                comb_inv_edit_pu5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                                comb_inv_edit_pu5.current(0)
                                window_comb_inv_edit_pu5 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_edit_pu5,tags=('iepcombo5'))
                                comb_inv_edit_pu5.delete(0,'end')
                                comb_inv_edit_pu5.insert(0, edit_pinv[18])

                                label_1 = Label(p_canvas_edit_1,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel20'))

                                sql = "select * from auth_user where username=%s"
                                val = (nm_ent.get(),)
                                fbcursor.execute(sql,val,)
                                udtl = fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (udtl[0],)
                                fbcursor.execute(sql,val,)
                                cdtl = fbcursor.fetchone()

                                sql = "select name from app1_accounts where acctype=%s and detype=%s and cid_id=%s"
                                val = (13,'Suppliers and Materials-COS',cdtl[0],)
                                fbcursor.execute(sql,val,)
                                in_ac_data = fbcursor.fetchall()
                                ac_data_3 = ["Cost of sales"]
                                for i in in_ac_data:
                                    ac_data_3.insert(-1,i[0])

                                comb_inv_edit_ex6 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                                comb_inv_edit_ex6['values'] = (ac_data_3)
                                comb_inv_edit_ex6.current(0)
                                window_comb_inv_edit_ex6 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_edit_ex6,tags=('iepcombo6'))
                                comb_inv_edit_ex6.delete(0,'end')
                                comb_inv_edit_ex6.insert(0, edit_pinv[17])

                                label_1 = Label(p_canvas_edit_1,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel21'))

                                def p_erc_1(event):
                                    if edit_inv_pitem_11.get()=="0":
                                        edit_inv_pitem_11.delete(0,END)
                                    else:
                                        pass

                                edit_inv_pitem_11=Entry(p_canvas_edit_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_inv_pitem_11 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_11,tags=('iepentry11'))
                                # edit_inv_pitem_11.insert(0,"0")
                                edit_inv_pitem_11.bind("<Button-1>",p_erc_1)
                                edit_inv_pitem_11.delete(0,'end')
                                edit_inv_pitem_11.insert(0, edit_pinv[19])
                                

                                label_1 = Label(p_canvas_edit_1,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel22'))

                                comb_inv_edit_pr7 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                                comb_inv_edit_pr7['values'] = ("Select Supplier",)
                                comb_inv_edit_pr7.current(0)
                                window_comb_inv_edit_pr7 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_edit_pr7,tags=('iepcombo7'))
                                comb_inv_edit_pr7.delete(0,'end')
                                comb_inv_edit_pr7.insert(0, edit_pinv[20])

                                einv_sub_btn1=Button(p_canvas_edit_1,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=edit_new_pro_inv)
                                window_einv_sub_btn1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=einv_sub_btn1,tags=('iepbutton5'))

                                def i_eback_1_():
                                    pro_frame_edit_1.grid_forget()
                                    pro_frame.grid(row=0,column=0,sticky='nsew')

                                bck_eibtn1=Button(p_canvas_edit_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=i_eback_1_)
                                window_bck_eibtn1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=bck_eibtn1,tags=('iepbuttn1'))

                                edit_inv_pitem_aod5=DateEntry(p_canvas_edit_1,width=60,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_inv_pitem_aod5 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_aod5,tags=('iepdate1'))
                                edit_inv_pitem_aod5.delete(0, 'end')
                                edit_inv_pitem_aod5.insert(0, edit_pinv[8])

                            elif pro_tree.item(pro_tree.focus())["values"][1] == 'Noninventory':
                                pro_frame.grid_forget()
                                pro_frame_edit_2 = Frame(tab3_4)
                                pro_frame_edit_2.grid(row=0,column=0,sticky='nsew')

                                def pro_responsive_widgets_e3(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("neppoly1",x1 + r1,y1,
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

                                    dcanvas.coords("neplabel1",dwidth/3,dheight/8.24)
                                    dcanvas.coords("nephline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.29


                                    dcanvas.coords("neppoly2",x11 + r2,y11,
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

                                    r2 = 25
                                    x11 = dwidth/24
                                    x21 = dwidth/1.050
                                    y11 = dheight/2.1
                                    y21 = dheight/1.35


                                    dcanvas.coords("neppoly3",x11 + r2,y11,
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

                                    dcanvas.coords("neplabel2",dwidth/2.4,dheight/1.77)
                                    dcanvas.coords("nepbutton1",dwidth/1.8,dheight/1.77)

                                    dcanvas.coords("neplabel3",dwidth/23.2,dheight/1.23)
                                    dcanvas.coords("neplabel4",dwidth/23.3,dheight/1.02)
                                    dcanvas.coords("neplabel5",dwidth/1.9,dheight/1.02)
                                    dcanvas.coords("neplabel6",dwidth/1.9,dheight/0.92)
                                    dcanvas.coords("neplabel7",dwidth/27,dheight/0.865)
                                    dcanvas.coords("neplabel8",dwidth/1.915,dheight/0.865)
                                    dcanvas.coords("neplabel12",dwidth/26,dheight/0.675)
                                    dcanvas.coords("neplabel13",dwidth/26.8,dheight/0.606)
                                    dcanvas.coords("neplabel14",dwidth/28.3,dheight/0.538)
                                    dcanvas.coords("neplabel15",dwidth/1.9,dheight/0.538)
                                    dcanvas.coords("neplabel16",dwidth/28.4,dheight/0.485)
                                    dcanvas.coords("neplabel17",dwidth/50,dheight/0.438)
                                    dcanvas.coords("neplabel18",dwidth/26,dheight/0.420)
                                    dcanvas.coords("neplabel20",dwidth/28,dheight/0.368)
                                    dcanvas.coords("neplabel21",dwidth/2.6,dheight/0.368)
                                    dcanvas.coords("neplabel22",dwidth/1.5,dheight/0.368)

                                    dcanvas.coords("neplabel9",dwidth/23.2,dheight/0.392)
                                    dcanvas.coords("neplabel10",dwidth/1.9,dheight/0.392)


                                    dcanvas.coords("nepentry1",dwidth/23.2,dheight/1.165)
                                    dcanvas.coords("nepentry2",dwidth/23.2,dheight/0.975)
                                    dcanvas.coords("nepentry3",dwidth/1.9,dheight/0.975)
                                    dcanvas.coords("nepentry4",dwidth/1.9,dheight/0.83)
                                    dcanvas.coords("nepentry7",dwidth/23.2,dheight/0.59)
                                    dcanvas.coords("nepentry8",dwidth/23.2,dheight/0.525)
                                    dcanvas.coords("nepentry9",dwidth/23.2,dheight/0.43)
                                    dcanvas.coords("nepentry10",dwidth/23.2,dheight/0.412)
                                    dcanvas.coords("nepentry11",dwidth/2.6,dheight/0.362)

                                    dcanvas.coords("nepcentry2",dwidth/23.2,dheight/0.385)
                                    dcanvas.coords("nepcentry3",dwidth/1.9,dheight/0.385)

                                    dcanvas.coords("nepcombo1",dwidth/23.2,dheight/0.83)
                                    dcanvas.coords("nepcombo3",dwidth/1.9,dheight/0.525)
                                    dcanvas.coords("nepcombo4",dwidth/23.2,dheight/0.474)
                                    dcanvas.coords("nepcombo6",dwidth/23.2,dheight/0.362)
                                    dcanvas.coords("nepcombo7",dwidth/1.5,dheight/0.362)

                                    dcanvas.coords("nepbutton2",dwidth/23.2,dheight/0.654)
                                    dcanvas.coords("nepbutton3",dwidth/2.45,dheight/0.474)
                                    dcanvas.coords("nepbutton4",dwidth/3.37,dheight/0.362)
                                    dcanvas.coords("nepbutton5",dwidth/2.38,dheight/0.345)

                                    dcanvas.coords("nepcbutton1",dwidth/23.2,dheight/0.51)
                                    dcanvas.coords("nepcbutton2",dwidth/23.2,dheight/0.378)

                                    dcanvas.coords("nepline1",dwidth/21,dheight/0.73,dwidth/1.055,dheight/0.73)
                                    dcanvas.coords("nephline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)

                                    dcanvas.coords("nepbuttn1",dwidth/23,dheight/3.415)

                                    

                                p_canvas_edit_2=Canvas(pro_frame_edit_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                                pro_frame_edit_2.grid_columnconfigure(0,weight=1)
                                pro_frame_edit_2.grid_rowconfigure(0,weight=1)
                            
                                vertibar=Scrollbar(pro_frame_edit_2, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=p_canvas_edit_2.yview)

                                p_canvas_edit_2.bind("<Configure>", pro_responsive_widgets_e3)
                                p_canvas_edit_2.config(yscrollcommand=vertibar.set)
                                p_canvas_edit_2.grid(row=0,column=0,sticky='nsew')

                                non_peditid = pro_tree.item(pro_tree.focus())["values"][2]
                                print(non_peditid)

                                non_peditid_1 = pro_tree.item(pro_tree.focus())["values"][3]
                                print(non_peditid_1)

                                sql_pn="select * from auth_user where username=%s"
                                pn_val=(nm_ent.get(),)
                                fbcursor.execute(sql_pn,pn_val,)
                                pn_dtl=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pn_dtl[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dtln=fbcursor.fetchone()
                                print(cmp_dtln)

                                sql = 'select * from app1_noninventory where name = %s and sku = %s and cid_id = %s'
                                val =  (non_peditid,non_peditid_1,cmp_dtln[0],)
                                fbcursor.execute(sql,val)
                                edit_pnon = fbcursor.fetchone()

                                def edit_new_pro_non():
                                    name = edit_non_item_1.get()
                                    sku = edit_non_iitem_2.get()
                                    hsn = edit_non_item_2.get()
                                    unit = comb_enon_item_1.get()
                                    category = edit_non_item_3.get()
                                    descr = edit_non_item_7.get('1.0', 'end-1c')
                                    saleprice = edit_non_item_8.get()
                                    income = comb_enon_item_4.get()
                                    tax = comb_enon_item_3.get()
                                    purchasedescr = edit_non_item_9.get('1.0', 'end-1c')
                                    cost = edit_non_item_10.get()
                                    expenseaccount = comb_enon_item_6.get()
                                    purchasetax = comb_enon_item_5.get()
                                    revcharge = edit_non_item_11.get()
                                    presupplier = comb_enon_item_7.get()

                                    usrp1_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usrp1_val = (nm_ent.get(),)
                                    fbcursor.execute(usrp1_sql,usrp1_val)
                                    usrp1_data = fbcursor.fetchone()

                                    cmpp1_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmpp1_val = (usrp1_data[0],)
                                    fbcursor.execute(cmpp1_sql,cmpp1_val)
                                    cmpp1_data = fbcursor.fetchone()
                                    cid = cmpp1_data[0]

                                    n_p_sql = "UPDATE app1_noninventory set name=%s,sku=%s,hsn=%s,unit=%s,category=%s,descr=%s,saleprice=%s,income=%s,tax=%s,purchasedescr=%s,cost=%s,expenseaccount=%s,purchasetax=%s,revcharge=%s,presupplier=%s,cid_id=%s where name=%s and sku = %s"
                                    n_p_val = (name,sku,hsn,unit,category,descr,saleprice,income,tax,purchasedescr,cost,expenseaccount,purchasetax,revcharge,presupplier,cid,non_peditid,non_peditid_1)
                                    fbcursor.execute(n_p_sql,n_p_val)
                                    finsysdb.commit()

                                    #_________Refresh insert tree________#

                                    for record in pro_tree.get_children():
                                        pro_tree.delete(record)

            
                                    sql_p="select * from auth_user where username=%s"
                                    sql_p_val=(nm_ent.get(),)
                                    fbcursor.execute(sql_p,sql_p_val,)
                                    pr_dt=fbcursor.fetchone()

                                    sql = "select * from app1_company where id_id=%s"
                                    val = (pr_dt[0],)
                                    fbcursor.execute(sql, val,)
                                    cmp_dt=fbcursor.fetchone()

                                    p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                    p_val_1 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_1,p_val_1,)
                                    p_data_1 = fbcursor.fetchall()
                                    
                                    count0 = 0
                                    for i in p_data_1:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                        else:
                                            pass
                                    count0 += 1

                                    p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                    p_val_2 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_2,p_val_2,)
                                    p_data_2 = fbcursor.fetchall()

                                    count1 = 0
                                    for i in p_data_2:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                        else:
                                            pass
                                    count1 += 1

                                    p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                    p_val_3 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_3,p_val_3,)
                                    p_data_3 = fbcursor.fetchall()
                                    

                                    count2 = 0
                                    for i in p_data_3:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                        else:
                                            pass
                                    count2 += 1

                                    p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                    p_val_4 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_4,p_val_4,)
                                    p_data_4 = fbcursor.fetchall()
                                    

                                    count3 = 0
                                    for i in p_data_4:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                        else:
                                            pass
                                    count3 += 1

                                    pro_frame_edit_2.destroy()
                                    pro_frame.grid(row=0,column=0,sticky='nsew')

                                p_canvas_edit_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('neppoly1'))

                                label_1 = Label(p_canvas_edit_2,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1, tags=('neplabel1'))

                                p_canvas_edit_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iephline'))

                                p_canvas_edit_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('neppoly2'))

                                p_canvas_edit_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('neppoly3'))

                                label_1 = Label(p_canvas_edit_2,width=13,height=2,text="NONINVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
                                window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1, tags=('neplabel2'))

                                label_1 = Label(p_canvas_edit_2,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1, tags=('neplabel3'))

                                edit_non_item_1=Entry(p_canvas_edit_2,width=200,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_non_item_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_1, tags=('nepentry1'))
                                edit_non_item_1.delete(0,'end')
                                edit_non_item_1.insert(0, edit_pnon[2])

                                label_1 = Label(p_canvas_edit_2,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1, tags=('neplabel4'))

                                def pns_2(event):
                                    if edit_non_iitem_2.get()==edit_pnon[3]:
                                        edit_non_iitem_2.delete(0,END)
                                    else:
                                        pass

                                edit_non_iitem_2=Entry(p_canvas_edit_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_non_iitem_2 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_iitem_2, tags=('nepentry2'))
                                edit_non_iitem_2.insert(0,"N41554")
                                edit_non_iitem_2.bind("<Button-1>",pns_2)
                                edit_non_iitem_2.delete(0,'end')
                                edit_non_iitem_2.insert(0, edit_pnon[3])

                                label_1 = Label(p_canvas_edit_2,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1, tags=('neplabel5'))

                                edit_non_item_2=Entry(p_canvas_edit_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_non_item_2 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_2, tags=('nepentry3'))
                                edit_non_item_2.delete(0,'end')
                                edit_non_item_2.insert(0, edit_pnon[4])

                                #Define a callback function
                                def ncallback_1(url):
                                    webbrowser.open_new_tab(url)

                                link_2 = Label(p_canvas_edit_2,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
                                window_link_2 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=link_2, tags=('neplabel6'))
                                link_2.bind("<Button-1>", lambda e:
                                ncallback_1("https://gstcouncil.gov.in/sites/default/files/goods-rates-booklet-03July2017.pdf"))


                                label_1 = Label(p_canvas_edit_2,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1, tags=('neplabel7'))

                                comb_enon_item_1 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                                comb_enon_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards","OTH Others",)
                                comb_enon_item_1.current(0)
                                window_comb_enon_item_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_enon_item_1, tags=('nepcombo1'))
                                comb_enon_item_1.delete(0,'end')
                                comb_enon_item_1.insert(0, edit_pnon[5])
                                

                                label_1 = Label(p_canvas_edit_2,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel8'))

                                edit_non_item_3=Entry(p_canvas_edit_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_inv_item_3 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_3,tags=('nepentry4'))
                                edit_non_item_3.delete(0,'end')
                                edit_non_item_3.insert(0, edit_pnon[6])

                                p_canvas_edit_2.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('nepline1'))

                                label_1 = Label(p_canvas_edit_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel12'))


                                def d_enon_check():

                                    if chk_str_enon_item.get() == True:
                                        p_canvas_edit_2.itemconfig('neplabel13',state='normal')
                                        p_canvas_edit_2.itemconfig('nepentry7',state='normal')
                                        p_canvas_edit_2.itemconfig('neplabel14',state='normal')
                                        p_canvas_edit_2.itemconfig('nepentry8',state='normal')
                                        p_canvas_edit_2.itemconfig('nepcbutton1',state='normal')
                                        p_canvas_edit_2.itemconfig('neplabel15',state='normal')
                                        p_canvas_edit_2.itemconfig('nepcombo3',state='normal')
                                        p_canvas_edit_2.itemconfig('neplabel16',state='normal')
                                        p_canvas_edit_2.itemconfig('nepcombo4',state='normal')
                                        p_canvas_edit_2.itemconfig('nepbutton3',state='normal')
                                    else:
                                        pass                     


                                chk_str_enon_item = BooleanVar()
                                chkbtn_enon_item = Checkbutton(p_canvas_edit_2, text = "I sell this product/service to my customers.", variable = chk_str_enon_item, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=d_enon_check)
                                if edit_pnon[7] == None:

                                    chkbtn_enon_item.deselect()

                                else:
                                    chkbtn_enon_item.select()
                                    

                                window_chkbtn_enon_item = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=chkbtn_enon_item,tags=('nepbutton2'))
                                
                                if chk_str_enon_item.get() == True:

                                    label_1 = Label(p_canvas_edit_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel13'))
                                

                                    edit_non_item_7=scrolledtext.ScrolledText(p_canvas_edit_2,width=145,background='#2f516f',foreground="white")
                                    window_edit_non_item_7 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=60,window=edit_non_item_7,tags=('nepentry7'))
                                    edit_non_item_7.insert(1.0,edit_pnon[7])

                                    label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel14'))

                                    def edit_non_tax_check_1():
                                        if comb_enon_item_3.get() == '28.0% GST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '28.0% IGST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '18.0% GST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '18.0% IGST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '15.0% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+15)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '14.5% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+14.5)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '14.00% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '14.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '12.36% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+12.36)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '12.0% GST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '12.0% IGST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '6.0% GST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '5.0% GST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            print(gst)
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '5.0% IGST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '5.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '4.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+4)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '3.0% GST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '3.0% IGST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '2.0% CST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+2)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '0.25% GST (O.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '0.25% IGST (0.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '0% GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '0% IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == 'Exempt GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == 'Exempt IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == 'Out of Scope(0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        else:
                                            pass

                                    edit_non_item_8=Entry(p_canvas_edit_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_non_item_8 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_8,tags=('nepentry8'))
                                    edit_non_item_8.delete(0,'end')
                                    edit_non_item_8.insert(0, edit_pnon[8])


                                    chk_str_non_item_e1 = BooleanVar()
                                    chkbtn_non_item_e1 = Checkbutton(p_canvas_edit_2, text = "Inclusive of tax", variable = chk_str_non_item_e1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=edit_non_tax_check_1)
                                    window_chkbtn_non_item_e1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=chkbtn_non_item_e1,tags=('nepcbutton1'))

                                    label_1 = Label(p_canvas_edit_2,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel15'))

                                    comb_enon_item_3 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                                    comb_enon_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                                    #comb_non_item_3.current(0)
                                    window_comb_enon_item_3 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_enon_item_3,tags=('nepcombo3'))
                                    comb_enon_item_3.delete(0,'end')
                                    comb_enon_item_3.insert(0, edit_pnon[10])

                                    label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel16'))

                                    sql = "select * from auth_user where username=%s"
                                    val = (nm_ent.get(),)
                                    fbcursor.execute(sql,val,)
                                    udtl = fbcursor.fetchone()

                                    sql = "select * from app1_company where id_id=%s"
                                    val = (udtl[0],)
                                    fbcursor.execute(sql,val,)
                                    cdtl = fbcursor.fetchone()


                                    sql = "select name from app1_accounts where acctype=%s and cid_id=%s"
                                    val = (11,cdtl[0],)
                                    fbcursor.execute(sql,val,)
                                    non_in_ac_data = fbcursor.fetchall()
                                    ac_data_4 = ["Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discount","Sales of Product Income","Services","Unapplied Cash Payment Income","Uncategorised Income"]
                                    for i in non_in_ac_data:
                                        ac_data_4.insert(-1,i[0])

                                    comb_enon_item_4 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                                    comb_enon_item_4['values'] = (ac_data_4)
                                    #comb_non_item_4.current(0)
                                    window_comb_enon_item_4 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_enon_item_4,tags=('nepcombo4'))
                                    comb_enon_item_4.delete(0,'end')
                                    comb_enon_item_4.insert(0, edit_pnon[9])

                                else:   
                                

                                    label_1 = Label(p_canvas_edit_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel13'),state=HIDDEN)
                                    

                                    edit_non_item_7=scrolledtext.ScrolledText(p_canvas_edit_2,width=145,background='#2f516f',foreground="white")
                                    window_edit_non_item_7 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=60,window=edit_non_item_7,tags=('nepentry7'),state=HIDDEN)
                                    edit_non_item_7.insert(1.0,edit_pnon[7])

                                    label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel14'),state=HIDDEN)

                                    def edit_non_tax_check_1():
                                        if comb_enon_item_3.get() == '28.0% GST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '28.0% IGST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '18.0% GST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '18.0% IGST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '15.0% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+15)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '14.5% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+14.5)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '14.00% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '14.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '12.36% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+12.36)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '12.0% GST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '12.0% IGST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '6.0% GST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '5.0% GST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            print(gst)
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '5.0% IGST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '5.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '4.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+4)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '3.0% GST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '3.0% IGST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '2.0% CST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+2)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '0.25% GST (O.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '0.25% IGST (0.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '0% GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == '0% IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == 'Exempt GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == 'Exempt IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_3.get() == 'Out of Scope(0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_non_item_e1.get() == True:
                                                edit_non_item_8.delete(0,'end')
                                                edit_non_item_8.insert(0, np)
                                            else:
                                                pass
                                        else:
                                            pass
                                    
                                    edit_non_item_8=Entry(p_canvas_edit_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_non_item_8 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_8,tags=('nepentry8'),state=HIDDEN)
                                    edit_non_item_8.delete(0,'end')
                                    edit_non_item_8.insert(0, edit_pnon[8])

                                    chk_str_non_item_e1 = BooleanVar()
                                    chkbtn_non_item_e1 = Checkbutton(p_canvas_edit_2, text = "Inclusive of tax", variable = chk_str_non_item_e1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=edit_non_tax_check_1)
                                    window_chkbtn_non_item_e1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=chkbtn_non_item_e1,tags=('nepcbutton1'),state=HIDDEN)

                                    label_1 = Label(p_canvas_edit_2,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel15'),state=HIDDEN)

                                    comb_enon_item_3 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                                    comb_enon_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                                    #comb_non_item_3.current(0)
                                    window_comb_enon_item_3 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_enon_item_3,tags=('nepcombo3'),state=HIDDEN)
                                    comb_enon_item_3.delete(0,'end')
                                    comb_enon_item_3.insert(0, edit_pnon[10])

                                    label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel16'),state=HIDDEN)

                                    comb_enon_item_4 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                                    comb_enon_item_4['values'] = ("Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discount","Sales of Product Income","Services","Unapplied Cash Payment Income","Uncategorised Income",)
                                    #comb_non_item_4.current(0)
                                    window_comb_enon_item_4 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_enon_item_4,tags=('nepcombo4'),state=HIDDEN)
                                    comb_enon_item_4.delete(0,'end')
                                    comb_enon_item_4.insert(0, edit_pnon[9])

                                p_canvas_edit_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('nephline1'))

                                label_1 = Label(p_canvas_edit_2,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_2.create_window(26, 1300, anchor="nw", window=label_1,tags=('neplabel17'))

                                def p_enon_check():
                                    
                                    if chk_str_enon_pitem.get() == True:
                                        p_canvas_edit_2.itemconfig('neplabel18',state='normal')
                                        p_canvas_edit_2.itemconfig('nepentry10',state='normal')
                                        p_canvas_edit_2.itemconfig('neplabel9',state='normal')
                                        p_canvas_edit_2.itemconfig('nepcentry2',state='normal')
                                        p_canvas_edit_2.itemconfig('nepcbutton2',state='normal')
                                        p_canvas_edit_2.itemconfig('neplabel10',state='normal')
                                        p_canvas_edit_2.itemconfig('nepcentry3',state='normal')
                                        p_canvas_edit_2.itemconfig('neplabel20',state='normal')
                                        p_canvas_edit_2.itemconfig('nepcombo6',state='normal')
                                        p_canvas_edit_2.itemconfig('nepbutton4',state='normal')
                                        p_canvas_edit_2.itemconfig('neplabel21',state='normal')
                                        p_canvas_edit_2.itemconfig('nepentry11',state='normal')
                                        p_canvas_edit_2.itemconfig('neplabel22',state='normal')
                                        p_canvas_edit_2.itemconfig('nepcombo7',state='normal')
                                    else:
                                        pass

                                chk_str_enon_pitem = BooleanVar()
                                chkbtn_enon_pitem = Checkbutton(p_canvas_edit_2, text = "I Purchase this product/service from Supplier.", variable = chk_str_enon_pitem, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=p_enon_check)
                                if edit_pnon[11] == None:
                                    chkbtn_enon_pitem.deselect()
                                else:
                                    chkbtn_enon_pitem.select()
                                window_chkbtn_enon_pitem = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=chkbtn_enon_pitem,tags=('nepentry9'))

                                if chk_str_enon_pitem.get() == True:
                                    label_1 = Label(p_canvas_edit_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel18'))

                                    edit_non_item_9=scrolledtext.ScrolledText(p_canvas_edit_2,width=145,background='#2f516f',foreground="white")
                                    window_edit_non_item_9 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=60,window=edit_non_item_9,tags=('nepentry10'))
                                    edit_non_item_9.insert(1.0,edit_pnon[11])

                                    label_1 = Label(p_canvas_edit_2,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel9'))

                                    def edit_non_tax_check_2():
                                        if comb_enon_item_5.get() == '28.0% GST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '28.0% IGST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '18.0% GST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '18.0% IGST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '15.0% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+15)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '14.5% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+14.5)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '14.00% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '14.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '12.36% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+12.36)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '12.0% GST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '12.0% IGST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '6.0% GST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '5.0% GST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            print(gst)
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '5.0% IGST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '5.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '4.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+4)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '3.0% GST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '3.0% IGST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '2.0% CST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+2)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '0.25% GST (O.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '0.25% IGST (0.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '0% GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '0% IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == 'Exempt GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == 'Exempt IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == 'Out of Scope(0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        else:
                                            pass
                                    
                                    edit_non_item_10=Entry(p_canvas_edit_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_non_item_10 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_10,tags=('nepcentry2'))
                                    edit_non_item_10.delete(0,'end')
                                    edit_non_item_10.insert(0, edit_pnon[12])

                                    chk_str_enon_item_2 = BooleanVar()
                                    chkbtn_enon_item_2 = Checkbutton(p_canvas_edit_2, text = "Inclusive of purchase tax", variable = chk_str_enon_item_2, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=edit_non_tax_check_2)
                                    window_chkbtn_enon_item_2 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=chkbtn_enon_item_2,tags=('nepcbutton2'))

                                    label_1 = Label(p_canvas_edit_2,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel10'))

                                    comb_enon_item_5 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                                    comb_enon_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                                    #comb_non_item_5.current(0)
                                    window_comb_enon_item_5 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_enon_item_5,tags=('nepcentry3'))
                                    comb_enon_item_5.delete(0,'end')
                                    comb_enon_item_5.insert(0, edit_pnon[14])

                                    label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel20'))

                                    sql = "select * from auth_user where username=%s"
                                    val = (nm_ent.get(),)
                                    fbcursor.execute(sql,val,)
                                    udtl = fbcursor.fetchone()

                                    sql = "select * from app1_company where id_id=%s"
                                    val = (udtl[0],)
                                    fbcursor.execute(sql,val,)
                                    cdtl = fbcursor.fetchone()

                                    sql = "select name from app1_accounts where acctype=%s and cid_id=%s"
                                    val = (14,cdtl[0],)
                                    fbcursor.execute(sql,val,)
                                    ex_ac_data = fbcursor.fetchall()
                                    ac_data_5 = ["Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities"]
                                    for i in ex_ac_data:
                                        ac_data_5.insert(-1,i[0])

                                    comb_enon_item_6 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                                    comb_enon_item_6['values'] = (ac_data_5)
                                    #comb_non_item_6.current(0)
                                    window_comb_enon_item_6 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_enon_item_6,tags=('nepcombo6'))
                                    comb_enon_item_6.delete(0,'end')
                                    comb_enon_item_6.insert(0, edit_pnon[13])


                                    label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel21'))

                                    def pr_e2(event):
                                        if edit_non_item_11.get()==edit_pnon[15]:
                                            edit_non_item_11.delete(0,END)
                                        else:
                                            pass

                                    edit_non_item_11=Entry(p_canvas_edit_2,width=50,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_non_item_11 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_11,tags=('nepentry11'))
                                    edit_non_item_11.insert(0,"0")
                                    edit_non_item_11.bind("<Button-1>",pr_e2)
                                    edit_non_item_11.delete(0,'end')
                                    edit_non_item_11.insert(0, edit_pnon[15])


                                    label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel22'))

                                    comb_enon_item_7 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                                    comb_enon_item_7['values'] = ("Select Supplier",)
                                    #comb_non_item_7.current(0)
                                    window_comb_enon_item_7 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_enon_item_7,tags=('nepcombo7'))
                                    comb_enon_item_7.delete(0,'end')
                                    comb_enon_item_7.insert(0, edit_pnon[16])
                                else:
                                    label_1 = Label(p_canvas_edit_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel18'),state=HIDDEN)

                                    edit_non_item_9=scrolledtext.ScrolledText(p_canvas_edit_2,width=145,background='#2f516f',foreground="white")
                                    window_edit_non_item_9 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=60,window=edit_non_item_9,tags=('nepentry10'),state=HIDDEN)
                                    edit_non_item_9.insert(1.0,edit_pnon[11])

                                    label_1 = Label(p_canvas_edit_2,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel9'),state=HIDDEN)

                                    def edit_non_tax_check_2():
                                        if comb_enon_item_5.get() == '28.0% GST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '28.0% IGST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '18.0% GST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '18.0% IGST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '15.0% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+15)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '14.5% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+14.5)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '14.00% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '14.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '12.36% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+12.36)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '12.0% GST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '12.0% IGST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '6.0% GST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '5.0% GST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            print(gst)
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '5.0% IGST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '5.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '4.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+4)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '3.0% GST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '3.0% IGST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '2.0% CST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+2)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '0.25% GST (O.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '0.25% IGST (0.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '0% GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == '0% IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == 'Exempt GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == 'Exempt IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_enon_item_5.get() == 'Out of Scope(0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_non_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_enon_item_2.get() == True:
                                                edit_non_item_10.delete(0,'end')
                                                edit_non_item_10.insert(0, np)
                                            else:
                                                pass
                                        else:
                                            pass
                                    
                                    edit_non_item_10=Entry(p_canvas_edit_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_non_item_10 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_10,tags=('nepcentry2'),state=HIDDEN)
                                    edit_non_item_10.delete(0,'end')
                                    edit_non_item_10.insert(0, edit_pnon[12])

                                    chk_str_enon_item_2 = BooleanVar()
                                    chkbtn_enon_item_2 = Checkbutton(p_canvas_edit_2, text = "Inclusive of purchase tax", variable = chk_str_enon_item_2, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=edit_non_tax_check_2)
                                    window_chkbtn_enon_item_2 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=chkbtn_enon_item_2,tags=('nepcbutton2'),state=HIDDEN)

                                    label_1 = Label(p_canvas_edit_2,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel10'),state=HIDDEN)

                                    comb_enon_item_5 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                                    comb_enon_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                                    #comb_non_item_5.current(0)
                                    window_comb_enon_item_5 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_enon_item_5,tags=('nepcentry3'),state=HIDDEN)
                                    comb_enon_item_5.delete(0,'end')
                                    comb_enon_item_5.insert(0, edit_pnon[14])

                                    label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel20'),state=HIDDEN)

                                    comb_enon_item_6 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                                    comb_enon_item_6['values'] = ("Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities",)
                                    #comb_non_item_6.current(0)
                                    window_comb_enon_item_6 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_enon_item_6,tags=('nepcombo6'),state=HIDDEN)
                                    comb_enon_item_6.delete(0,'end')
                                    comb_enon_item_6.insert(0, edit_pnon[13])


                                    label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel21'),state=HIDDEN)

                                    def pr_e2(event):
                                        if edit_non_item_11.get()==edit_pnon[15]:
                                            edit_non_item_11.delete(0,END)
                                        else:
                                            pass

                                    edit_non_item_11=Entry(p_canvas_edit_2,width=50,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_non_item_11 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_11,tags=('nepentry11'),state=HIDDEN)
                                    edit_non_item_11.insert(0,"0")
                                    edit_non_item_11.bind("<Button-1>",pr_e2)
                                    edit_non_item_11.delete(0,'end')
                                    edit_non_item_11.insert(0, edit_pnon[15])


                                    label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel22'),state=HIDDEN)

                                    comb_enon_item_7 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                                    comb_enon_item_7['values'] = ("Select Supplier",)
                                    #comb_non_item_7.current(0)
                                    window_comb_enon_item_7 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_enon_item_7,tags=('nepcombo7'),state=HIDDEN)
                                    comb_enon_item_7.delete(0,'end')
                                    comb_enon_item_7.insert(0, edit_pnon[16])

                                enon_sub_btn1=Button(p_canvas_edit_2,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=edit_new_pro_non)
                                window_enon_sub_btn1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=enon_sub_btn1,tags=('nepbutton5'))

                                def no_eback_1_():
                                    pro_frame_edit_2.grid_forget()
                                    pro_frame.grid(row=0,column=0,sticky='nsew')

                                bck_enbtn1=Button(p_canvas_edit_2,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=no_eback_1_)
                                window_bck_enbtn1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=bck_enbtn1,tags=('nepbuttn1'))
                            
                            elif pro_tree.item(pro_tree.focus())["values"][1] == 'Service':
                                pro_frame.grid_forget()
                                pro_frame_edit_3 = Frame(tab3_4)
                                pro_frame_edit_3.grid(row=0,column=0,sticky='nsew')

                                def pro_responsive_widgets_e4(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("sppoly1",x1 + r1,y1,
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

                                    dcanvas.coords("splabel1",dwidth/3,dheight/8.24)
                                    dcanvas.coords("sphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.29


                                    dcanvas.coords("sppoly2",x11 + r2,y11,
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

                                    r2 = 25
                                    x11 = dwidth/24
                                    x21 = dwidth/1.050
                                    y11 = dheight/2.1
                                    y21 = dheight/1.35


                                    dcanvas.coords("sppoly3",x11 + r2,y11,
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

                                    dcanvas.coords("seplabel2",dwidth/2.3,dheight/1.77)
                                    dcanvas.coords("sepbutton1",dwidth/1.8,dheight/1.77)

                                    dcanvas.coords("seplabel3",dwidth/23.2,dheight/1.23)
                                    dcanvas.coords("seplabel4",dwidth/23.3,dheight/1.02)
                                    dcanvas.coords("seplabel5",dwidth/1.9,dheight/1.02)
                                    dcanvas.coords("seplabel7",dwidth/27,dheight/0.865)
                                    dcanvas.coords("seplabel8",dwidth/1.915,dheight/0.865)
                                    dcanvas.coords("seplabel12",dwidth/26,dheight/0.675)
                                    dcanvas.coords("seplabel13",dwidth/26.8,dheight/0.606)
                                    dcanvas.coords("seplabel14",dwidth/28.3,dheight/0.538)
                                    dcanvas.coords("seplabel15",dwidth/1.9,dheight/0.538)
                                    dcanvas.coords("seplabel16",dwidth/28.4,dheight/0.485)
                                    dcanvas.coords("seplabel17",dwidth/50,dheight/0.438)
                                    dcanvas.coords("seplabel18",dwidth/26,dheight/0.420)
                                    dcanvas.coords("seplabel9",dwidth/23.2,dheight/0.392)
                                    dcanvas.coords("seplabel10",dwidth/1.9,dheight/0.392)
                                    dcanvas.coords("seplabel20",dwidth/28,dheight/0.368)
                                    dcanvas.coords("seplabel21",dwidth/2.6,dheight/0.368)
                                    dcanvas.coords("seplabel22",dwidth/1.5,dheight/0.368)

                                    dcanvas.coords("seplabel23",dwidth/2.6,dheight/0.485)

                                    dcanvas.coords("seplabel24",dwidth/1.53,dheight/0.485)
                                    

                                    dcanvas.coords("sepentry1",dwidth/23.2,dheight/1.165)
                                    dcanvas.coords("sepentry2",dwidth/23.2,dheight/0.975)
                                    dcanvas.coords("sepentry3",dwidth/1.9,dheight/0.975)
                                    dcanvas.coords("sepentry4",dwidth/1.9,dheight/0.83)
                                    dcanvas.coords("sepentry7",dwidth/23.2,dheight/0.59)
                                    dcanvas.coords("sepentry8",dwidth/23.2,dheight/0.525)
                                    dcanvas.coords("sepentry9",dwidth/23.2,dheight/0.43)
                                    dcanvas.coords("sepentry10",dwidth/23.2,dheight/0.412)
                                    dcanvas.coords("sepentry11",dwidth/2.6,dheight/0.362)

                                    dcanvas.coords("sepentry12",dwidth/2.6,dheight/0.474)

                                    dcanvas.coords("sepcentry2",dwidth/23.2,dheight/0.385)
                                    dcanvas.coords("sepcentry3",dwidth/1.9,dheight/0.385)

                                    dcanvas.coords("sepcombo1",dwidth/23.2,dheight/0.83)
                                    dcanvas.coords("sepcombo3",dwidth/1.9,dheight/0.525)
                                    dcanvas.coords("sepcombo4",dwidth/23.2,dheight/0.474)
                                    dcanvas.coords("sepcombo6",dwidth/23.2,dheight/0.362)
                                    dcanvas.coords("sepcombo7",dwidth/1.5,dheight/0.362)

                                    dcanvas.coords("sepcombo8",dwidth/1.5,dheight/0.474)

                                    dcanvas.coords("sepbutton2",dwidth/23.2,dheight/0.654)
                                    dcanvas.coords("sepbutton3",dwidth/3.37,dheight/0.474)
                                    dcanvas.coords("sepbutton4",dwidth/3.37,dheight/0.362)
                                    dcanvas.coords("sepbutton5",dwidth/2.38,dheight/0.345)

                                    dcanvas.coords("sepcbutton1",dwidth/23.2,dheight/0.51)
                                    dcanvas.coords("sepcbutton2",dwidth/23.2,dheight/0.378)

                                    dcanvas.coords("sepline1",dwidth/21,dheight/0.73,dwidth/1.055,dheight/0.73)

                                    dcanvas.coords("sephline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)
                                    dcanvas.coords("sepbuttn1",dwidth/23,dheight/3.415) 

                                    

                                p_canvas_edit_3=Canvas(pro_frame_edit_3, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                                pro_frame_edit_3.grid_columnconfigure(0,weight=1)
                                pro_frame_edit_3.grid_rowconfigure(0,weight=1)
                            
                                vertibar=Scrollbar(pro_frame_edit_3, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=p_canvas_edit_3.yview)

                                p_canvas_edit_3.bind("<Configure>", pro_responsive_widgets_e4)
                                p_canvas_edit_3.config(yscrollcommand=vertibar.set)
                                p_canvas_edit_3.grid(row=0,column=0,sticky='nsew')

                                ser_peditid = pro_tree.item(pro_tree.focus())["values"][2]
                                print(ser_peditid)

                                ser_peditid_1 = pro_tree.item(pro_tree.focus())["values"][3]
                                print(ser_peditid_1)

                                sql_pn="select * from auth_user where username=%s"
                                pn_val=(nm_ent.get(),)
                                fbcursor.execute(sql_pn,pn_val,)
                                pn_dtl=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pn_dtl[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dtln=fbcursor.fetchone()
                                print(cmp_dtln)

                                sql = 'select * from app1_service where name = %s and sku = %s and cid_id = %s'
                                val =  (ser_peditid,ser_peditid_1,cmp_dtln[0],)
                                fbcursor.execute(sql,val)
                                edit_pser = fbcursor.fetchone()

                                def edit_new_pro_ser():
                                    name = edit_ser_item_1.get()
                                    sku = edit_ser_iitem_2.get()
                                    sac = edit_ser_item_2.get()
                                    unit = comb_eser_item_1.get()
                                    categ = edit_ser_item_3.get()
                                    descr = edit_ser_item_7.get('1.0', 'end-1c')
                                    saleprice = edit_ser_item_s8.get()
                                    income = comb_eser_item_6.get()
                                    tax = comb_eser_item_3.get()
                                    abatement = edit_ser_iitem_11.get()
                                    sertype = comb_eser_iitem_7.get()
                                    purchasedescr = edit_ser_item_9.get('1.0', 'end-1c')
                                    cost = edit_ser_item_10.get()
                                    expenseaccount = comb_eser_item_e6.get()
                                    purchasetax = comb_eser_item_5.get()
                                    revcharge = edit_sser_item_11.get()
                                    presupplier = comb_eser_item_ps7.get()

                                    usrp2_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usrp2_val = (nm_ent.get(),)
                                    fbcursor.execute(usrp2_sql,usrp2_val)
                                    usrp2_data = fbcursor.fetchone()

                                    cmpp2_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmpp2_val = (usrp2_data[0],)
                                    fbcursor.execute(cmpp2_sql,cmpp2_val)
                                    cmpp2_data = fbcursor.fetchone()
                                    cid = cmpp2_data[0]

                                    s_p_sql = "UPDATE app1_service set name=%s,sku=%s,sac=%s,unit=%s,categ=%s,descr=%s,saleprice=%s,income=%s,tax=%s,abatement=%s,sertype=%s,purchasedescr=%s,cost=%s,expenseaccount=%s,purchasetax=%s,revcharge=%s,presupplier=%s,cid_id=%s where name=%s and sku = %s"
                                    s_p_val = (name,sku,sac,unit,categ,descr,saleprice,income,tax,abatement,sertype,purchasedescr,cost,expenseaccount,purchasetax,revcharge,presupplier,cid,ser_peditid,ser_peditid_1)
                                    fbcursor.execute(s_p_sql,s_p_val)
                                    finsysdb.commit()

                                    #_________Refresh insert tree________#

                                    for record in pro_tree.get_children():
                                        pro_tree.delete(record)

            
                                    sql_p="select * from auth_user where username=%s"
                                    sql_p_val=(nm_ent.get(),)
                                    fbcursor.execute(sql_p,sql_p_val,)
                                    pr_dt=fbcursor.fetchone()

                                    sql = "select * from app1_company where id_id=%s"
                                    val = (pr_dt[0],)
                                    fbcursor.execute(sql, val,)
                                    cmp_dt=fbcursor.fetchone()

                                    p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                    p_val_1 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_1,p_val_1,)
                                    p_data_1 = fbcursor.fetchall()
                                    
                                    count0 = 0
                                    for i in p_data_1:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                        else:
                                            pass
                                    count0 += 1

                                    p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                    p_val_2 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_2,p_val_2,)
                                    p_data_2 = fbcursor.fetchall()

                                    count1 = 0
                                    for i in p_data_2:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                        else:
                                            pass
                                    count1 += 1

                                    p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                    p_val_3 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_3,p_val_3,)
                                    p_data_3 = fbcursor.fetchall()
                                    

                                    count2 = 0
                                    for i in p_data_3:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                        else:
                                            pass
                                    count2 += 1

                                    p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                    p_val_4 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_4,p_val_4,)
                                    p_data_4 = fbcursor.fetchall()
                                    

                                    count3 = 0
                                    for i in p_data_4:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                        else:
                                            pass
                                    count3 += 1

                                    pro_frame_edit_3.destroy()
                                    pro_frame.grid(row=0,column=0,sticky='nsew')

                                p_canvas_edit_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sppoly1'))

                                label_1 = Label(p_canvas_edit_3,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel1'))

                                p_canvas_edit_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sphline'))

                                p_canvas_edit_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sppoly2'))

                                p_canvas_edit_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('sppoly3'))

                                label_1 = Label(p_canvas_edit_3,width=10,height=2,text="SERVICE", font=('arial 20'),background="#2f516f",fg="white") 
                                window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1, tags=('seplabel2'))

                                label_1 = Label(p_canvas_edit_3,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1, tags=('seplabel3'))

                                edit_ser_item_1=Entry(p_canvas_edit_3,width=200,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_ser_item_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_item_1, tags=('sepentry1'))
                                edit_ser_item_1.delete(0,'end')
                                edit_ser_item_1.insert(0, edit_pser[2])

                                label_1 = Label(p_canvas_edit_3,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1, tags=('seplabel4'))

                                def pse_3(event):
                                    if edit_ser_iitem_2.get()=="N41554":
                                        edit_ser_iitem_2.delete(0,END)
                                    else:
                                        pass

                                edit_ser_iitem_2=Entry(p_canvas_edit_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_ser_iitem_2 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_iitem_2, tags=('sepentry2'))
                                edit_ser_iitem_2.insert(0,"N41554")
                                edit_ser_iitem_2.bind("<Button-1>",pse_3)
                                edit_ser_iitem_2.delete(0,'end')
                                edit_ser_iitem_2.insert(0, edit_pser[3])

                                label_1 = Label(p_canvas_edit_3,width=9,height=1,text="SAC Code", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1, tags=('seplabel5'))

                                def p_sac_e1(event):
                                    if edit_ser_item_2.get()==edit_pser[4]:
                                        edit_ser_item_2.delete(0,END)
                                    else:
                                        pass
                                edit_ser_item_2=Entry(p_canvas_edit_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_ser_item_2 = p_canvas_edit_3.create_window(710, 630, anchor="nw", height=30,window=edit_ser_item_2, tags=('sepentry3'))
                                edit_ser_item_2.insert(0,"Eg: 998841-Coke and refined petroleum product manufacturing services")
                                edit_ser_item_2.bind("<Button-1>",p_sac_e1)
                                edit_ser_item_2.delete(0,'end')
                                edit_ser_item_2.insert(0, edit_pser[4])


                                label_1 = Label(p_canvas_edit_3,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1, tags=('seplabel7'))

                                comb_eser_item_1 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                comb_eser_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG-BAGS","BAL-BALE","BDL-BUNDLES","BKL-BUCKLES","BOX-BOX","BOU-BILLIONS OF UNITS","BTL-BOTTLES","BUN-BUNCHES","CAN-CANS","CBM-CUBIC METER","CMS-CENTIMETER","CCM-CUBIC CENTIMETER","CTN-CARTONS","DOZ-DOZEN","DRM-DRUM","GGR-GREAT GROSS","GMS-GRAMS","GRS-GROSS","GYD-GRODD YARDS","KGS-KILOGRAMS","KLR-KILOLITER","KME-KILOMETRE","MTS-METRIC TON","MLT-MILLILITRE","MTR-METERS","NOS-NUMBER","PAC-PACKS","PCS-PIECES","PRS-PAIRS","QTL-QUINTAL","ROL-ROLLS","SQF-SQUARE FEET","SET-SETS","SQM-SQUARE METERS","SQY-SQUARE YARDS","TBS-TABLETS","TGM-TEN GROSS","THD-THOUSAND","TON-TONNES","TUB-TUBES","UGS-US GALLONS","UNT-UNITS","YDS-YARDS","OTH-OTHERS",)
                                comb_eser_item_1.current(0)
                                window_comb_eser_item_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_eser_item_1, tags=('sepcombo1'))
                                comb_eser_item_1.delete(0,'end')
                                comb_eser_item_1.insert(0, edit_pser[5])

                                label_1 = Label(p_canvas_edit_3,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_3.create_window(705, 710, anchor="nw", window=label_1,tags=('seplabel8'))

                                edit_ser_item_3=Entry(p_canvas_edit_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_edit_ser_item_3 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_item_3,tags=('sepentry4'))
                                edit_ser_item_3.delete(0,'end')
                                edit_ser_item_3.insert(0, edit_pser[6])

                                p_canvas_edit_3.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('sepline1'))


                                label_1 = Label(p_canvas_edit_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel12'))

                                def d_eser_check():

                                    if chk_str_eser_item.get() == True:
                                        p_canvas_edit_3.itemconfig('seplabel13',state='normal')
                                        p_canvas_edit_3.itemconfig('sepentry7',state='normal')
                                        p_canvas_edit_3.itemconfig('seplabel14',state='normal')
                                        p_canvas_edit_3.itemconfig('sepentry8',state='normal')
                                        p_canvas_edit_3.itemconfig('sepcbutton1',state='normal')
                                        p_canvas_edit_3.itemconfig('seplabel15',state='normal')
                                        p_canvas_edit_3.itemconfig('sepcombo3',state='normal')
                                        p_canvas_edit_3.itemconfig('seplabel16',state='normal')
                                        p_canvas_edit_3.itemconfig('sepcombo4',state='normal')
                                        p_canvas_edit_3.itemconfig('sepbutton3',state='normal')
                                        p_canvas_edit_3.itemconfig('seplabel23',state='normal')
                                        p_canvas_edit_3.itemconfig('sepentry12',state='normal')
                                        p_canvas_edit_3.itemconfig('seplabel24',state='normal')
                                        p_canvas_edit_3.itemconfig('sepcombo8',state='normal')
                                    else:
                                        pass

                                chk_str_eser_item = BooleanVar()
                                chkbtn_eser_item = Checkbutton(p_canvas_edit_3, text = "I sell this product/service to my customers.", variable = chk_str_eser_item, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=d_eser_check)
                                if edit_pser[7] == None:
                                    chkbtn_eser_item.deselect()
                                else:
                                    chkbtn_eser_item.select()
                                window_chkbtn_eser_item = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=chkbtn_eser_item,tags=('sepbutton2'))
                                
                                if chk_str_eser_item.get() == True:
                                    label_d1 = Label(p_canvas_edit_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_d1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_d1,tags=('seplabel13'))

                                    edit_ser_item_7=scrolledtext.ScrolledText(p_canvas_edit_3,width=145,background='#2f516f',foreground="white")
                                    window_edit_ser_item_7 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=60,window=edit_ser_item_7,tags=('sepentry7'))
                                    edit_ser_item_7.insert(1.0,edit_pser[7])


                                    label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel14'))

                                    def edit_ser_tax_check_1():
                                        if comb_eser_item_3.get() == '28.0% GST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '28.0% IGST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '18.0% GST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '18.0% IGST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '15.0% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+15)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '14.5% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+14.5)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '14.00% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '14.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '12.36% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+12.36)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '12.0% GST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '12.0% IGST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '6.0% GST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '5.0% GST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            print(gst)
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '5.0% IGST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '5.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '4.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+4)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '3.0% GST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '3.0% IGST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '2.0% CST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+2)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '0.25% GST (O.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '0.25% IGST (0.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '0% GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '0% IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == 'Exempt GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == 'Exempt IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == 'Out of Scope(0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        else:
                                            pass
                                    
                                    edit_ser_item_s8=Entry(p_canvas_edit_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_ser_item_s8 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_item_s8,tags=('sepentry8'))
                                    edit_ser_item_s8.delete(0,'end')
                                    edit_ser_item_s8.insert(0, edit_pser[8])

                                    chk_str_eser_item_1 = BooleanVar()
                                    chkbtn_eser_item_1 = Checkbutton(p_canvas_edit_3, text = "Inclusive of tax", variable = chk_str_eser_item_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=edit_ser_tax_check_1)
                                    window_chkbtn_eser_item_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=chkbtn_eser_item_1,tags=('sepcbutton1'))

                                    label_1 = Label(p_canvas_edit_3,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel15'))

                                    comb_eser_item_3 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                    comb_eser_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                                    comb_eser_item_3.current(0)
                                    window_comb_eser_item_3 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_eser_item_3,tags=('sepcombo3'))
                                    comb_eser_item_3.delete(0,'end')
                                    comb_eser_item_3.insert(0, edit_pser[10])

                                    label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel16'))

                                    sql = "select * from auth_user where username=%s"
                                    val = (nm_ent.get(),)
                                    fbcursor.execute(sql,val,)
                                    udtl = fbcursor.fetchone()

                                    sql = "select * from app1_company where id_id=%s"
                                    val = (udtl[0],)
                                    fbcursor.execute(sql,val,)
                                    cdtl = fbcursor.fetchone()


                                    sql = "select name from app1_accounts where detype=%s and cid_id=%s"
                                    val = ('Account Receivable(Debtors)',cdtl[0],)
                                    fbcursor.execute(sql,val,)
                                    ser_in_ac_data = fbcursor.fetchall()
                                    ac_data_6 = ["Choose...","Billable Expense income","Product Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discounts","Sales of Product Income","Cost of sales","Equipment Rental for Jobs","Uncategorised Income","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Depreciation Expense","Dues and Subscriptions","Housekeeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Internet Expenses","Meals and Enetrtainments","Office Suppliers","Postage and Delivery","Printing and Reprooduction","Professional Fees","Purchases","Rent Expense","Repair and Maintananace","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities","Finance charge Income","Insurance Proceeds Received","Interest Income","Proceeds From Sale os Assets","Shipping and delivery Income","Ask My Accountant","CGST Write-off","GST Write-off","IGST Write-off","Miscellaneous Expense","Political Contributions","Reconcilation Discrepancies","SGST Write-off","Vehicles","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi kalyan Cess","Input Krishi kalyan Cess RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Krishi Kalyan Cess Payable","Input VAT 5%","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output SGST Tax RCM","Output Service Tax","Output Service Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","SGST Payable","Service Tax Payable","Srvice Tax Suspense","Swachh Barath Cess Payable","TDS Payable","VAT Payable","VAT Suspense","Deferred CGST","Deferred GST Input credit","Deferred IGST","Deferred SGST","Deferred Service Tax Input Credit","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Sevice Tax Refund","TDS Receivable","Uncategorised Asset","Undeposited Fund","Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and maintanance","Sales Discount","Sales of Product Income","Uncategorised Income","accumulated Depreciation","Building and Improvements","Furniture and Equipments","Land","Leasehold Improvements","Vehicles","Retained Earnings","Cost of Sales","Equipment Rental for Jobs","Freight and Shipping Costs","Merchant Account Fees","Purchases-Hardware for Resales","Purchases-Software for Resales","Subcontracted Services","Tools and Craft Suppliers"]
                                    for i in ser_in_ac_data:
                                        ac_data_6.insert(-1,i[0])

                                    
                                    comb_eser_item_6 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                    comb_eser_item_6['values'] = (ac_data_6)
                                    comb_eser_item_6.current(0)
                                    window_comb_eser_item_6 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_eser_item_6,tags=('sepcombo4'))
                                    comb_eser_item_6.delete(0,'end')
                                    comb_eser_item_6.insert(0, edit_pser[9])

                                    label_1 = Label(p_canvas_edit_3,width=10,height=1,text="Abatement %", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel23'))

                                    def pa_e1(event):
                                        if edit_ser_iitem_11.get()==edit_pser[11]:
                                            edit_ser_iitem_11.delete(0,END)
                                        else:
                                            pass

                                    edit_ser_iitem_11=Entry(p_canvas_edit_3,width=50,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_ser_iitem_11 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_iitem_11,tags=('sepentry12'))
                                    edit_ser_iitem_11.insert(0,"0")
                                    edit_ser_iitem_11.bind("<Button-1>",pa_e1)
                                    edit_ser_iitem_11.delete(0,'end')
                                    edit_ser_iitem_11.insert(0, edit_pser[11])

                                    label_1 = Label(p_canvas_edit_3,width=14,height=1,text="Service Type", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel24'))

                                    comb_eser_iitem_7 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                    comb_eser_iitem_7['values'] = ("Choose...","Stock Broking","Genral Insurance","Courier","Advertsing Agency","Consulting Engineer","Custom House Agent","Steamer Agent","Clearing and Forwarding","Man power Recruiting","Air Travel Agent","Tour operator","Rent a Cab","Architect","Interior Director","Management Consultment","Chartered Accountant","Cost Accountant","Company Scretary","Real Estate Agent","Security Agency","Credit Rating Agency","Market Research Agency","Underwriter","Beauty Parlor","Cargo Handling","Cable Operators","Dry Cleaning","Event Management","Fashion Designer","Life Insurance","Scientific and Technical Consultancy","Photography","Convention Services","Video Tape Production","Sound Recording","Broadcating","Insurance Auxilary Service","banking and Other Financial","Port Services","Authorised Service Station","Health Club and Fitness Centres","Rail Travel Agent","Storage and Warehousing","Business Auxilary","Commercial Coaching","Erection or Installation","Franchise Service","Internet Cafe","Maintanance or Repair","Technical Testing","Technical Inspection","Foreign Exchange Broking","Port","Airport Services","Air Transport","Business Exhibition","Goods Transport","Construction of Commerce Complex","Intellectual Property Service","Opinion Poll Service","Outdoor Catering","Television and Radio Program Production","Survey and Exploration of Minerals","Pandal and Shamiana","Travel Agent","Forward Contract Brokerage","Transport Through Pipeline","Site Preparation","Dredging","Survey and Map Making","Cleaning Service","Clubs and Association Service","Packaging Service","Mailing List Compilation","Residential Complex Construction","Share Transfer Agent","ATM Maintanance","Recovery Agent","Sale of Space for Advertisement","Sponsorship","International Air Travel","Containerised Rail Transport","Business Support Service","Action Service","Public Relation Management","Ship Management","Internet Telephony","Cruise Ship Tour","Credit Card","Telecommunication Service","Mining of Minerals, Oil or Gas","Recting Immovable Property","Works Contract","Development of Consent","Asset Management","Design Services","Information Technology Services","ULIP Management","Stock Exchange Service","Service for Transaction in Goods","Clearing House Services","Supply of Tangiable","Online Inforamtion Retrieval","Mandap keeper",)
                                    comb_eser_iitem_7.current(0)
                                    window_comb_eser_iitem_7 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_eser_iitem_7,tags=('sepcombo8'))
                                    comb_eser_iitem_7.delete(0,'end')
                                    comb_eser_iitem_7.insert(0, edit_pser[12])
                                else:
                                    label_d1 = Label(p_canvas_edit_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_d1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_d1,tags=('seplabel13'),state=HIDDEN)

                                    edit_ser_item_7=scrolledtext.ScrolledText(p_canvas_edit_3,width=145,background='#2f516f',foreground="white")
                                    window_edit_ser_item_7 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=60,window=edit_ser_item_7,tags=('sepentry7'),state=HIDDEN)
                                    edit_ser_item_7.insert(1.0,edit_pser[7])


                                    label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel14'),state=HIDDEN)

                                    def edit_ser_tax_check_1():
                                        if comb_eser_item_3.get() == '28.0% GST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '28.0% IGST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '18.0% GST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '18.0% IGST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '15.0% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+15)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '14.5% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+14.5)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '14.00% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '14.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '12.36% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+12.36)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '12.0% GST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '12.0% IGST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '6.0% GST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '5.0% GST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            print(gst)
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '5.0% IGST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '5.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '4.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+4)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '3.0% GST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '3.0% IGST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '2.0% CST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+2)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '0.25% GST (O.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '0.25% IGST (0.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '0% GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == '0% IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == 'Exempt GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == 'Exempt IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_3.get() == 'Out of Scope(0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_s8.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_eser_item_1.get() == True:
                                                edit_ser_item_s8.delete(0,'end')
                                                edit_ser_item_s8.insert(0, np)
                                            else:
                                                pass
                                        else:
                                            pass
                                    
                                    edit_ser_item_s8=Entry(p_canvas_edit_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_ser_item_s8 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_item_s8,tags=('sepentry8'),state=HIDDEN)
                                    edit_ser_item_s8.delete(0,'end')
                                    edit_ser_item_s8.insert(0, edit_pser[8])

                                    chk_str_eser_item_1 = BooleanVar()
                                    chkbtn_eser_item_1 = Checkbutton(p_canvas_edit_3, text = "Inclusive of tax", variable = chk_str_eser_item_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=edit_ser_tax_check_1)
                                    window_chkbtn_eser_item_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=chkbtn_eser_item_1,tags=('sepcbutton1'),state=HIDDEN)

                                    label_1 = Label(p_canvas_edit_3,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel15'),state=HIDDEN)

                                    comb_eser_item_3 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                    comb_eser_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                                    comb_eser_item_3.current(0)
                                    window_comb_eser_item_3 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_eser_item_3,tags=('sepcombo3'),state=HIDDEN)
                                    comb_eser_item_3.delete(0,'end')
                                    comb_eser_item_3.insert(0, edit_pser[10])

                                    label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel16'),state=HIDDEN)

                                    
                                    comb_eser_item_6 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                    comb_eser_item_6['values'] = ("Choose...","Billable Expense income","Product Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discounts","Sales of Product Income","Cost of sales","Equipment Rental for Jobs","Uncategorised Income","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Depreciation Expense","Dues and Subscriptions","Housekeeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Internet Expenses","Meals and Enetrtainments","Office Suppliers","Postage and Delivery","Printing and Reprooduction","Professional Fees","Purchases","Rent Expense","Repair and Maintananace","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities","Finance charge Income","Insurance Proceeds Received","Interest Income","Proceeds From Sale os Assets","Shipping and delivery Income","Ask My Accountant","CGST Write-off","GST Write-off","IGST Write-off","Miscellaneous Expense","Political Contributions","Reconcilation Discrepancies","SGST Write-off","Vehicles","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi kalyan Cess","Input Krishi kalyan Cess RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Krishi Kalyan Cess Payable","Input VAT 5%","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output SGST Tax RCM","Output Service Tax","Output Service Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","SGST Payable","Service Tax Payable","Srvice Tax Suspense","Swachh Barath Cess Payable","TDS Payable","VAT Payable","VAT Suspense","Deferred CGST","Deferred GST Input credit","Deferred IGST","Deferred SGST","Deferred Service Tax Input Credit","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Sevice Tax Refund","TDS Receivable","Uncategorised Asset","Undeposited Fund","Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and maintanance","Sales Discount","Sales of Product Income","Uncategorised Income","accumulated Depreciation","Building and Improvements","Furniture and Equipments","Land","Leasehold Improvements","Vehicles","Retained Earnings","Cost of Sales","Equipment Rental for Jobs","Freight and Shipping Costs","Merchant Account Fees","Purchases-Hardware for Resales","Purchases-Software for Resales","Subcontracted Services","Tools and Craft Suppliers",)
                                    comb_eser_item_6.current(0)
                                    window_comb_eser_item_6 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_eser_item_6,tags=('sepcombo4'),state=HIDDEN)
                                    comb_eser_item_6.delete(0,'end')
                                    comb_eser_item_6.insert(0, edit_pser[9])

                                    label_1 = Label(p_canvas_edit_3,width=10,height=1,text="Abatement %", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel23'),state=HIDDEN)

                                    def pa_e1(event):
                                        if edit_ser_iitem_11.get()==edit_pser[11]:
                                            edit_ser_iitem_11.delete(0,END)
                                        else:
                                            pass

                                    edit_ser_iitem_11=Entry(p_canvas_edit_3,width=50,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_ser_iitem_11 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_iitem_11,tags=('sepentry12'),state=HIDDEN)
                                    edit_ser_iitem_11.insert(0,"0")
                                    edit_ser_iitem_11.bind("<Button-1>",pa_e1)
                                    edit_ser_iitem_11.delete(0,'end')
                                    edit_ser_iitem_11.insert(0, edit_pser[11])

                                    label_1 = Label(p_canvas_edit_3,width=14,height=1,text="Service Type", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel24'),state=HIDDEN)

                                    comb_eser_iitem_7 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                    comb_eser_iitem_7['values'] = ("Choose...","Stock Broking","Genral Insurance","Courier","Advertsing Agency","Consulting Engineer","Custom House Agent","Steamer Agent","Clearing and Forwarding","Man power Recruiting","Air Travel Agent","Tour operator","Rent a Cab","Architect","Interior Director","Management Consultment","Chartered Accountant","Cost Accountant","Company Scretary","Real Estate Agent","Security Agency","Credit Rating Agency","Market Research Agency","Underwriter","Beauty Parlor","Cargo Handling","Cable Operators","Dry Cleaning","Event Management","Fashion Designer","Life Insurance","Scientific and Technical Consultancy","Photography","Convention Services","Video Tape Production","Sound Recording","Broadcating","Insurance Auxilary Service","banking and Other Financial","Port Services","Authorised Service Station","Health Club and Fitness Centres","Rail Travel Agent","Storage and Warehousing","Business Auxilary","Commercial Coaching","Erection or Installation","Franchise Service","Internet Cafe","Maintanance or Repair","Technical Testing","Technical Inspection","Foreign Exchange Broking","Port","Airport Services","Air Transport","Business Exhibition","Goods Transport","Construction of Commerce Complex","Intellectual Property Service","Opinion Poll Service","Outdoor Catering","Television and Radio Program Production","Survey and Exploration of Minerals","Pandal and Shamiana","Travel Agent","Forward Contract Brokerage","Transport Through Pipeline","Site Preparation","Dredging","Survey and Map Making","Cleaning Service","Clubs and Association Service","Packaging Service","Mailing List Compilation","Residential Complex Construction","Share Transfer Agent","ATM Maintanance","Recovery Agent","Sale of Space for Advertisement","Sponsorship","International Air Travel","Containerised Rail Transport","Business Support Service","Action Service","Public Relation Management","Ship Management","Internet Telephony","Cruise Ship Tour","Credit Card","Telecommunication Service","Mining of Minerals, Oil or Gas","Recting Immovable Property","Works Contract","Development of Consent","Asset Management","Design Services","Information Technology Services","ULIP Management","Stock Exchange Service","Service for Transaction in Goods","Clearing House Services","Supply of Tangiable","Online Inforamtion Retrieval","Mandap keeper",)
                                    comb_eser_iitem_7.current(0)
                                    window_comb_eser_iitem_7 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_eser_iitem_7,tags=('sepcombo8'),state=HIDDEN)
                                    comb_eser_iitem_7.delete(0,'end')
                                    comb_eser_iitem_7.insert(0, edit_pser[12])

                                p_canvas_edit_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sephline1'))

                                label_1 = Label(p_canvas_edit_3,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel17'))

                                def p_eser_check():

                                    if chk_str_eser_pitem.get() == True:
                                        p_canvas_edit_3.itemconfig('seplabel18',state='normal')
                                        p_canvas_edit_3.itemconfig('sepentry10',state='normal')
                                        p_canvas_edit_3.itemconfig('seplabel9',state='normal')
                                        p_canvas_edit_3.itemconfig('sepcentry2',state='normal')
                                        p_canvas_edit_3.itemconfig('sepcbutton2',state='normal')
                                        p_canvas_edit_3.itemconfig('seplabel10',state='normal')
                                        p_canvas_edit_3.itemconfig('sepcentry3',state='normal')
                                        p_canvas_edit_3.itemconfig('seplabel20',state='normal')
                                        p_canvas_edit_3.itemconfig('sepcombo6',state='normal')
                                        p_canvas_edit_3.itemconfig('sepbutton4',state='normal')
                                        p_canvas_edit_3.itemconfig('seplabel21',state='normal')
                                        p_canvas_edit_3.itemconfig('sepentry11',state='normal')
                                        p_canvas_edit_3.itemconfig('seplabel22',state='normal')
                                        p_canvas_edit_3.itemconfig('sepcombo7',state='normal')
                                    else:
                                        pass

                                chk_str_eser_pitem = BooleanVar()
                                chkbtn_eser_pitem = Checkbutton(p_canvas_edit_3, text = "I Purchase this product/service from Supplier.", variable = chk_str_eser_pitem, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=p_eser_check)
                                if edit_pser[13] == None:
                                    chkbtn_eser_pitem.deselect()
                                else:
                                    chkbtn_eser_pitem.select()
                                window_chkbtn_eser_pitem = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=chkbtn_eser_pitem,tags=('sepentry9'))

                                if chk_str_eser_pitem.get() == True:
                                    label_1 = Label(p_canvas_edit_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel18'))

                                    edit_ser_item_9=scrolledtext.ScrolledText(p_canvas_edit_3,width=145,background='#2f516f',foreground="white")
                                    window_edit_ser_item_9 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=60,window=edit_ser_item_9,tags=('sepentry10'))
                                    edit_ser_item_9.insert(1.0,edit_pser[13])

                                    label_1 = Label(p_canvas_edit_3,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel9'))

                                    def edit_ser_tax_check_2():
                                        if comb_eser_item_5.get() == '28.0% GST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '28.0% IGST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '18.0% GST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '18.0% IGST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '15.0% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+15)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '14.5% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+14.5)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '14.00% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '14.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '12.36% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+12.36)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '12.0% GST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '12.0% IGST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '6.0% GST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '5.0% GST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            print(gst)
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '5.0% IGST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '5.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '4.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+4)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '3.0% GST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '3.0% IGST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '2.0% CST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+2)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '0.25% GST (O.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '0.25% IGST (0.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '0% GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '0% IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == 'Exempt GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == 'Exempt IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == 'Out of Scope(0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        else:
                                            pass
                                    
                                    edit_ser_item_10=Entry(p_canvas_edit_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_ser_item_10 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_item_10,tags=('sepcentry2'))
                                    edit_ser_item_10.delete(0,'end')
                                    edit_ser_item_10.insert(0, edit_pser[14])

                                    chk_str_esser_item_2 = BooleanVar()
                                    chkbtn_esser_item_2 = Checkbutton(p_canvas_edit_3, text = "Inclusive of Tax", variable = chk_str_esser_item_2, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=edit_ser_tax_check_2)
                                    window_chkbtn_esser_item_2 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=chkbtn_esser_item_2,tags=('sepcbutton2'))

                                    label_1 = Label(p_canvas_edit_3,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel10'))

                                    comb_eser_item_5 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                    comb_eser_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                                    comb_eser_item_5.current(0)
                                    window_comb_eser_item_5 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_eser_item_5,tags=('sepcentry3'))
                                    comb_eser_item_5.delete(0,'end')
                                    comb_eser_item_5.insert(0, edit_pser[16])

                                    label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel20'))

                                    sql = "select * from auth_user where username=%s"
                                    val = (nm_ent.get(),)
                                    fbcursor.execute(sql,val,)
                                    udtl = fbcursor.fetchone()

                                    sql = "select * from app1_company where id_id=%s"
                                    val = (udtl[0],)
                                    fbcursor.execute(sql,val,)
                                    cdtl = fbcursor.fetchone()


                                    sql = "select name from app1_accounts where detype=%s and cid_id=%s"
                                    val = ('Account Receivable(Debtors)',cdtl[0],)
                                    fbcursor.execute(sql,val,)
                                    ser_ex_ac_data = fbcursor.fetchall()
                                    ac_data_7 = ["Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities"]
                                    for i in ser_ex_ac_data:
                                        ac_data_7.insert(-1,i[0])

                                    comb_eser_item_e6 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                    comb_eser_item_e6['values'] = (ac_data_7)
                                    comb_eser_item_e6.current(0)
                                    window_comb_eser_item_e6 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_eser_item_e6,tags=('sepcombo6'))
                                    comb_eser_item_e6.delete(0,'end')
                                    comb_eser_item_e6.insert(0, edit_pser[15])

                                    label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel21'))

                                    def pr_e3(event):
                                        if edit_sser_item_11.get()=="0":
                                            edit_sser_item_11.delete(0,END)
                                        else:
                                            pass

                                    edit_sser_item_11=Entry(p_canvas_edit_3,width=50,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_sser_item_11 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_sser_item_11,tags=('sepentry11'))
                                    edit_sser_item_11.insert(0,"0")
                                    edit_sser_item_11.bind("<Button-1>",pr_e3)
                                    edit_sser_item_11.delete(0,'end')
                                    edit_sser_item_11.insert(0, edit_pser[17])

                                    label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel22'))

                                    comb_eser_item_ps7 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                    comb_eser_item_ps7['values'] = ("Select Supplier",)
                                    comb_eser_item_ps7.current(0)
                                    window_comb_eser_item_ps7 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_eser_item_ps7,tags=('sepcombo7'))
                                    comb_eser_item_ps7.delete(0,'end')
                                    comb_eser_item_ps7.insert(0, edit_pser[18])

                                else:
                                    label_1 = Label(p_canvas_edit_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel18'),state=HIDDEN)

                                    edit_ser_item_9=scrolledtext.ScrolledText(p_canvas_edit_3,width=145,background='#2f516f',foreground="white")
                                    window_edit_ser_item_9 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=60,window=edit_ser_item_9,tags=('sepentry10'),state=HIDDEN)
                                    edit_ser_item_9.insert(1.0,edit_pser[13])

                                    label_1 = Label(p_canvas_edit_3,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel9'),state=HIDDEN)

                                    def edit_ser_tax_check_2():
                                        if comb_eser_item_5.get() == '28.0% GST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '28.0% IGST (28%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+28)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '18.0% GST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '18.0% IGST (18%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+18)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '15.0% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+15)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '14.5% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+14.5)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '14.00% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '14.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+14)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '12.36% ST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+12.36)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '12.0% GST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '12.0% IGST (12%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+12)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '6.0% GST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '6.0% IGST (6%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+6)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '5.0% GST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            print(gst)
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '5.0% IGST (5%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '5.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+5)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '4.0% VAT (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+4)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '3.0% GST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '3.0% IGST (3%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+3)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '2.0% CST (100%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+2)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '0.25% GST (O.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '0.25% IGST (0.25%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0.25)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '0% GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == '0% IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == 'Exempt GST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == 'Exempt IGST (0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        elif comb_eser_item_5.get() == 'Out of Scope(0%)':
                                            gst = 0.0
                                            np = 0.0
                                            n1 = float(edit_ser_item_10.get())
                                            gst = n1-(n1*(100/(100+0)))
                                            np = n1-gst
                                            if chk_str_esser_item_2.get() == True:
                                                edit_ser_item_10.delete(0,'end')
                                                edit_ser_item_10.insert(0, np)
                                            else:
                                                pass
                                        else:
                                            pass
                                    
                                    edit_ser_item_10=Entry(p_canvas_edit_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_ser_item_10 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_item_10,tags=('sepcentry2'),state=HIDDEN)
                                    edit_ser_item_10.delete(0,'end')
                                    edit_ser_item_10.insert(0, edit_pser[14])

                                    chk_str_esser_item_2 = BooleanVar()
                                    chkbtn_esser_item_2 = Checkbutton(p_canvas_edit_3, text = "Inclusive of Tax", variable = chk_str_esser_item_2, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=edit_ser_tax_check_2)
                                    window_chkbtn_esser_item_2 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=chkbtn_esser_item_2,tags=('sepcbutton2'),state=HIDDEN)

                                    label_1 = Label(p_canvas_edit_3,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel10'),state=HIDDEN)

                                    comb_eser_item_5 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                    comb_eser_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                                    comb_eser_item_5.current(0)
                                    window_comb_eser_item_5 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_eser_item_5,tags=('sepcentry3'),state=HIDDEN)
                                    comb_eser_item_5.delete(0,'end')
                                    comb_eser_item_5.insert(0, edit_pser[16])

                                    label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel20'),state=HIDDEN)

                                    comb_eser_item_e6 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                    comb_eser_item_e6['values'] = ("Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities",)
                                    comb_eser_item_e6.current(0)
                                    window_comb_eser_item_e6 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_eser_item_e6,tags=('sepcombo6'),state=HIDDEN)
                                    comb_eser_item_e6.delete(0,'end')
                                    comb_eser_item_e6.insert(0, edit_pser[15])

                                    label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel21'),state=HIDDEN)

                                    def pr_e3(event):
                                        if edit_sser_item_11.get()=="0":
                                            edit_sser_item_11.delete(0,END)
                                        else:
                                            pass

                                    edit_sser_item_11=Entry(p_canvas_edit_3,width=50,justify=LEFT,background='#2f516f',foreground="white")
                                    window_edit_sser_item_11 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_sser_item_11,tags=('sepentry11'),state=HIDDEN)
                                    edit_sser_item_11.insert(0,"0")
                                    edit_sser_item_11.bind("<Button-1>",pr_e3)
                                    edit_sser_item_11.delete(0,'end')
                                    edit_sser_item_11.insert(0, edit_pser[17])

                                    label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                                    window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel22'),state=HIDDEN)

                                    comb_eser_item_ps7 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                                    comb_eser_item_ps7['values'] = ("Select Supplier",)
                                    comb_eser_item_ps7.current(0)
                                    window_comb_eser_item_ps7 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_eser_item_ps7,tags=('sepcombo7'),state=HIDDEN)
                                    comb_eser_item_ps7.delete(0,'end')
                                    comb_eser_item_ps7.insert(0, edit_pser[18])

                                eser_sub_btn1=Button(p_canvas_edit_3,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=edit_new_pro_ser)
                                window_eser_sub_btn1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=eser_sub_btn1,tags=('sepbutton5'))

                                def s_eback_1_():
                                    pro_frame_edit_3.grid_forget()
                                    pro_frame.grid(row=0,column=0,sticky='nsew')

                                bck_esbtn1=Button(p_canvas_edit_3,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=s_eback_1_)
                                window_bck_esbtn1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=bck_esbtn1,tags=('sepbuttn1'))
                            elif pro_tree.item(pro_tree.focus())["values"][1] == 'Bundle':
                                pro_frame.grid_forget()
                                pro_frame_edit_4 = Frame(tab3_4)
                                pro_frame_edit_4.grid(row=0,column=0,sticky='nsew')

                                def pro_responsive_widgets_e5(event):
                                    dwidth = event.width
                                    dheight = event.height
                                    dcanvas = event.widget
                                
                                    r1 = 25
                                    x1 = dwidth/63
                                    x2 = dwidth/1.021
                                    y1 = dheight/14 
                                    y2 = dheight/3.505

                                    dcanvas.coords("beppoly1",x1 + r1,y1,
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

                                    dcanvas.coords("beplabel1",dwidth/3,dheight/8.24)
                                    dcanvas.coords("bephline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                    r2 = 25
                                    x11 = dwidth/63
                                    x21 = dwidth/1.021
                                    y11 = dheight/2.8
                                    y21 = dheight/0.45


                                    dcanvas.coords("beppoly2",x11 + r2,y11,
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

                                    r2 = 25
                                    x11 = dwidth/24
                                    x21 = dwidth/1.050
                                    y11 = dheight/2.1
                                    y21 = dheight/1.35


                                    dcanvas.coords("beppoly3",x11 + r2,y11,
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

                                    dcanvas.coords("beplabel2",dwidth/2.3,dheight/1.77)
                                    dcanvas.coords("bepbutton1",dwidth/1.8,dheight/1.77)

                                    dcanvas.coords("beplabel3",dwidth/23.2,dheight/1.23)
                                    dcanvas.coords("beplabel4",dwidth/1.9,dheight/1.23)
                                    dcanvas.coords("beplabel5",dwidth/25,dheight/1.02)
                                    dcanvas.coords("beplabel6",dwidth/22.7,dheight/0.8)


                                    dcanvas.coords("bepentry1",dwidth/23.2,dheight/1.165)
                                    dcanvas.coords("bepentry2",dwidth/1.9,dheight/1.165)
                                    dcanvas.coords("bepentry3",dwidth/23.2,dheight/0.97)

                                    #-----------------------------H Lines---------------------------------#
                                    dcanvas.coords("bepline1",dwidth/21.5,dheight/0.77,dwidth/1.075,dheight/0.77)
                                    dcanvas.coords("bepline2",dwidth/21.5,dheight/0.72,dwidth/1.075,dheight/0.72)
                                    dcanvas.coords("bepline3",dwidth/21.5,dheight/0.67,dwidth/1.075,dheight/0.67)
                                    dcanvas.coords("bepline4",dwidth/21.5,dheight/0.619,dwidth/1.075,dheight/0.619)
                                    dcanvas.coords("bepline5",dwidth/21.5,dheight/0.57,dwidth/1.075,dheight/0.57)
                                    dcanvas.coords("bepline6",dwidth/21.5,dheight/0.535,dwidth/1.075,dheight/0.535)
                                    #-----------------------------V Lines---------------------------------#
                                    dcanvas.coords("bepline7",dwidth/21.5,dheight/0.77,dwidth/21.5,dheight/0.535)
                                    dcanvas.coords("bepline8",dwidth/1.075,dheight/0.77,dwidth/1.075,dheight/0.535)
                                    dcanvas.coords("bepline9",dwidth/4.8,dheight/0.77,dwidth/4.8,dheight/0.535)
                                    dcanvas.coords("bepline10",dwidth/2.7,dheight/0.77,dwidth/2.7,dheight/0.535)
                                    dcanvas.coords("bepline11",dwidth/1.84,dheight/0.77,dwidth/1.84,dheight/0.535)
                                    dcanvas.coords("bepline12",dwidth/1.575,dheight/0.77,dwidth/1.575,dheight/0.535)
                                    dcanvas.coords("bepline13",dwidth/1.366,dheight/0.77,dwidth/1.366,dheight/0.535)
                                    dcanvas.coords("bepline14",dwidth/1.21,dheight/0.77,dwidth/1.21,dheight/0.535)

                                    dcanvas.coords("beplabel7",dwidth/13,dheight/0.754)
                                    dcanvas.coords("beplabel8",dwidth/3.85,dheight/0.754)
                                    dcanvas.coords("beplabel9",dwidth/2.35,dheight/0.754)
                                    dcanvas.coords("beplabel10",dwidth/1.75,dheight/0.754)
                                    dcanvas.coords("beplabel11",dwidth/1.515,dheight/0.754)
                                    dcanvas.coords("beplabel12",dwidth/1.325,dheight/0.754)
                                    dcanvas.coords("beplabel13",dwidth/1.17,dheight/0.754)

                                    dcanvas.coords("bepcombo1",dwidth/17,dheight/0.709)
                                    dcanvas.coords("bepcombo2",dwidth/17,dheight/0.651)
                                    dcanvas.coords("bepcombo3",dwidth/17,dheight/0.604)
                                    dcanvas.coords("bepcombo4",dwidth/17,dheight/0.56)

                                    dcanvas.coords("bepentry4",dwidth/4.6,dheight/0.709)
                                    dcanvas.coords("bepentry5",dwidth/4.6,dheight/0.651)
                                    dcanvas.coords("bepentry6",dwidth/4.6,dheight/0.604)
                                    dcanvas.coords("bepentry7",dwidth/4.6,dheight/0.56)

                                    dcanvas.coords("bepentry8",dwidth/2.6,dheight/0.709)
                                    dcanvas.coords("bepentry9",dwidth/2.6,dheight/0.651)
                                    dcanvas.coords("bepentry10",dwidth/2.6,dheight/0.604)
                                    dcanvas.coords("bepentry11",dwidth/2.6,dheight/0.56)

                                    dcanvas.coords("bepspin1",dwidth/1.81,dheight/0.709)
                                    dcanvas.coords("bepspin2",dwidth/1.81,dheight/0.651)
                                    dcanvas.coords("bepspin3",dwidth/1.81,dheight/0.604)
                                    dcanvas.coords("bepspin4",dwidth/1.81,dheight/0.56)

                                    dcanvas.coords("bepspin5",dwidth/1.56,dheight/0.709)
                                    dcanvas.coords("bepspin6",dwidth/1.56,dheight/0.651)
                                    dcanvas.coords("bepspin7",dwidth/1.56,dheight/0.604)
                                    dcanvas.coords("bepspin8",dwidth/1.56,dheight/0.56)

                                    dcanvas.coords("bepspin9",dwidth/1.351,dheight/0.709)
                                    dcanvas.coords("bepspin10",dwidth/1.351,dheight/0.651)
                                    dcanvas.coords("bepspin11",dwidth/1.351,dheight/0.604)
                                    dcanvas.coords("bepspin12",dwidth/1.351,dheight/0.56)

                                    dcanvas.coords("bepspin13",dwidth/1.195,dheight/0.709)
                                    dcanvas.coords("bepspin14",dwidth/1.195,dheight/0.651)
                                    dcanvas.coords("bepspin15",dwidth/1.195,dheight/0.604)
                                    dcanvas.coords("bepspin16",dwidth/1.195,dheight/0.56)

                                    dcanvas.coords("bepbutton2",dwidth/2.3,dheight/0.52)
                                    dcanvas.coords("bepbuttn1",dwidth/23,dheight/3.415) 




                                pro_canvas_edit_4=Canvas(pro_frame_edit_4, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                                pro_frame_edit_4.grid_columnconfigure(0,weight=1)
                                pro_frame_edit_4.grid_rowconfigure(0,weight=1)
                                
                                vertibar=Scrollbar(pro_frame_edit_4, orient=VERTICAL)
                                vertibar.grid(row=0,column=1,sticky='ns')
                                vertibar.config(command=pro_canvas_edit_4.yview)

                                pro_canvas_edit_4.bind("<Configure>", pro_responsive_widgets_e5)
                                pro_canvas_edit_4.config(yscrollcommand=vertibar.set)
                                pro_canvas_edit_4.grid(row=0,column=0,sticky='nsew')

                                bun_peditid = pro_tree.item(pro_tree.focus())["values"][2]

                                bun_peditid_1 = pro_tree.item(pro_tree.focus())["values"][3]

                                sql_pn="select * from auth_user where username=%s"
                                pn_val=(nm_ent.get(),)
                                fbcursor.execute(sql_pn,pn_val,)
                                pn_dtl=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pn_dtl[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dtln=fbcursor.fetchone()
                                print(cmp_dtln)

                                sql = 'select * from app1_bundle where name = %s and sku = %s and cid_id = %s'
                                val =  (bun_peditid,bun_peditid_1,cmp_dtln[0],)
                                fbcursor.execute(sql,val)
                                edit_pbun = fbcursor.fetchone()

                                def edit_new_pro_bun():

                                    name = entry_ebun_item_1.get()
                                    sku = entry_ebun_iitem_2.get()
                                    description = entry_ebun_item_7.get('1.0', 'end-1c')
                                    product1 = ebun_comb_1.get()
                                    product2 = ebun_comb_2.get()
                                    product3 = ebun_comb_3.get()
                                    product4 = ebun_comb_4.get()
                                    hsn1 = ebun_entry_1.get()
                                    hsn2 = ebun_entry_2.get()
                                    hsn3 = ebun_entry_3.get()
                                    hsn4 = ebun_entry_4.get()
                                    description1 = ebun_entry_5.get('1.0', 'end-1c')
                                    description2 = ebun_entry_6.get('1.0', 'end-1c')
                                    description3 = ebun_entry_7.get('1.0', 'end-1c')
                                    description4 = ebun_entry_8.get('1.0', 'end-1c')
                                    qty1 = ebun_entry_9.get()
                                    qty2 = ebun_entry_10.get()
                                    qty3 = ebun_entry_11.get()
                                    qty4 = ebun_entry_12.get()
                                    price1 = ebun_entry_13.get()
                                    price2 = ebun_entry_14.get()
                                    price3 = ebun_entry_15.get()
                                    price4 = ebun_entry_16.get()
                                    total1 = ebun_entry_17.get()
                                    total2 = ebun_entry_18.get()
                                    total3 = ebun_entry_19.get()
                                    total4 = ebun_entry_20.get()
                                    tax1 = ebun_entry_21.get()
                                    tax2 = ebun_entry_22.get()
                                    tax3 = ebun_entry_23.get()
                                    tax4 = ebun_entry_24.get()


                                    usrp3_sql = "SELECT id FROM auth_user WHERE username=%s"
                                    usrp3_val = (nm_ent.get(),)
                                    fbcursor.execute(usrp3_sql,usrp3_val)
                                    usrp3_data = fbcursor.fetchone()

                                    cmpp3_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                    cmpp3_val = (usrp3_data[0],)
                                    fbcursor.execute(cmpp3_sql,cmpp3_val)
                                    cmpp3_data = fbcursor.fetchone()
                                    cid = cmpp3_data[0]

                                    b_p_sql = "UPDATE app1_bundle set name=%s,sku=%s,description=%s,product1=%s,product2=%s,product3=%s,product4=%s,hsn1=%s,hsn2=%s,hsn3=%s,hsn4=%s,description1=%s,description2=%s,description3=%s,description4=%s,qty1=%s,qty2=%s,qty3=%s,qty4=%s,price1=%s,price2=%s,price3=%s,price4=%s,total1=%s,total2=%s,total3=%s,total4=%s,tax1=%s,tax2=%s,tax3=%s,tax4=%s,cid_id=%s where name=%s and sku = %s"
                                    b_p_val = (name,sku,description,product1,product2,product3,product4,hsn1,hsn2,hsn3,hsn4,description1,description2,description3,description4,qty1,qty2,qty3,qty4,price1,price2,price3,price4,total1,total2,total3,total4,tax1,tax2,tax3,tax4,cid,bun_peditid,bun_peditid_1)
                                    fbcursor.execute(b_p_sql,b_p_val)
                                    finsysdb.commit()

                                    #_________Refresh insert tree________#

                                    for record in pro_tree.get_children():
                                        pro_tree.delete(record)

            
                                    sql_p="select * from auth_user where username=%s"
                                    sql_p_val=(nm_ent.get(),)
                                    fbcursor.execute(sql_p,sql_p_val,)
                                    pr_dt=fbcursor.fetchone()

                                    sql = "select * from app1_company where id_id=%s"
                                    val = (pr_dt[0],)
                                    fbcursor.execute(sql, val,)
                                    cmp_dt=fbcursor.fetchone()

                                    p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                    p_val_1 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_1,p_val_1,)
                                    p_data_1 = fbcursor.fetchall()
                                    
                                    count0 = 0
                                    for i in p_data_1:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                        else:
                                            pass
                                    count0 += 1

                                    p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                    p_val_2 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_2,p_val_2,)
                                    p_data_2 = fbcursor.fetchall()

                                    count1 = 0
                                    for i in p_data_2:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                        else:
                                            pass
                                    count1 += 1

                                    p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                    p_val_3 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_3,p_val_3,)
                                    p_data_3 = fbcursor.fetchall()
                                    

                                    count2 = 0
                                    for i in p_data_3:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                        else:
                                            pass
                                    count2 += 1

                                    p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                    p_val_4 = (cmp_dt[0],)
                                    fbcursor.execute(p_sql_4,p_val_4,)
                                    p_data_4 = fbcursor.fetchall()
                                    

                                    count3 = 0
                                    for i in p_data_4:
                                        if True:
                                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                        else:
                                            pass
                                    count3 += 1

                                    pro_frame_edit_4.destroy()
                                    pro_frame.grid(row=0,column=0,sticky='nsew')


                                pro_canvas_edit_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('beppoly1'))

                                label_1 = Label(pro_canvas_edit_4,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                                window_label_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_1, tags=('beplabel1'))

                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('bephline'))

                                pro_canvas_edit_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('beppoly2'))

                                pro_canvas_edit_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('beppoly3'))
                                
                                label_1 = Label(pro_canvas_edit_4,width=15,height=2,text="BUNDLE", font=('arial 20'),background="#2f516f",fg="white") 
                                window_label_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_1, tags=('beplabel2'))

                                label_1 = Label(pro_canvas_edit_4,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_1, tags=('beplabel3'))

                                entry_ebun_item_1=Entry(pro_canvas_edit_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_ebun_item_1 = pro_canvas_edit_4.create_window(55, 530, anchor="nw", height=30,window=entry_ebun_item_1, tags=('bepentry1'))
                                entry_ebun_item_1.delete(0,'end')
                                entry_ebun_item_1.insert(0, edit_pbun[2])


                                label_1 = Label(pro_canvas_edit_4,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_1, tags=('beplabel4'))

                                def ps_e4(event):
                                    if entry_ebun_iitem_2.get()==edit_pbun[3]:
                                        entry_ebun_iitem_2.delete(0,END)
                                    else:
                                        pass

                                entry_ebun_iitem_2=Entry(pro_canvas_edit_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                                window_entry_ebun_iitem_2 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30,window=entry_ebun_iitem_2, tags=('bepentry2'))
                                entry_ebun_iitem_2.delete(0,'end')
                                entry_ebun_iitem_2.insert(0, edit_pbun[3])
                                entry_ebun_iitem_2.bind("<Button-1>",ps_e4)


                                label_1 = Label(pro_canvas_edit_4,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_1, tags=('beplabel5'))

                                entry_ebun_item_7=scrolledtext.ScrolledText(pro_canvas_edit_4,width=146,background='#2f516f',foreground="white")
                                window_entry_ebun_item_7 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=60,window=entry_ebun_item_7, tags=('bepentry3'))
                                entry_ebun_item_7.insert(1.0,edit_pbun[4])

                                label_1 = Label(pro_canvas_edit_4,width=30,height=1,text="Products/services included in the bundle", font=('arial 12'),background="#1b3857",fg="white") 
                                window_label_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_1, tags=('beplabel6'))

                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline1'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline2'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline3'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline4'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline5'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline6'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline7'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline8'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline9'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline10'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline11'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline12'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline13'))
                                pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline14'))
                                

                                label_3 = Label(pro_canvas_edit_4,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
                                window_label_3 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_3,tags=('beplabel7'))

                                label_4 = Label(pro_canvas_edit_4,width=10,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
                                window_label_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_4,tags=('beplabel8'))

                                label_4 = Label(pro_canvas_edit_4,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
                                window_label_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_4,tags=('beplabel9'))

                                label_4 = Label(pro_canvas_edit_4,width=5,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
                                window_label_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_4,tags=('beplabel10'))

                                label_4 = Label(pro_canvas_edit_4,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
                                window_label_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_4,tags=('beplabel11'))

                                label_4 = Label(pro_canvas_edit_4,width=8,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
                                window_label_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_4,tags=('beplabel12'))

                                label_4 = Label(pro_canvas_edit_4,width=8,height=1,text="TAX", font=('arial 10'),background="#1b3857",fg="white") 
                                window_label_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_4,tags=('beplabel13'))

                                def bun_details_e1(event):
                                    ebun_to_str_1 = ebun_comb_1.get()
                                    try:
                                        sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                        val = (ebun_to_str_1,cmp_dtli[0],)
                                        fbcursor.execute(sql,val)
                                        ebun_sel_1 = fbcursor.fetchone()
                                        ebun_entry_1.delete(0,END)
                                        ebun_entry_1.insert(0,ebun_sel_1[4])
                                        ebun_entry_5.delete('1.0',END)
                                        ebun_entry_5.insert('1.0',ebun_sel_1[11])
                                        ebun_entry_13.delete(0,END)
                                        ebun_entry_13.insert(0,ebun_sel_1[12])
                                        ebun_entry_21.delete(0,END)
                                        ebun_entry_21.insert(0,ebun_sel_1[14])
                                    except:
                                        sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                        val = (ebun_to_str_1,cmp_dtli[0],)
                                        fbcursor.execute(sql,val)
                                        ebun_sel_1 = fbcursor.fetchone()
                                        ebun_entry_1.delete(0,END)
                                        ebun_entry_1.insert(0,ebun_sel_1[4])
                                        ebun_entry_5.delete('1.0',END)
                                        ebun_entry_5.insert('1.0',ebun_sel_1[7])
                                        ebun_entry_13.delete(0,END)
                                        ebun_entry_13.insert(0,ebun_sel_1[8])
                                        ebun_entry_21.delete(0,END)
                                        ebun_entry_21.insert(0,ebun_sel_1[10])

                                def bun_details_e2(event):
                                    ebun_to_str_2 = ebun_comb_2.get()
                                    try:
                                        sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                        val = (ebun_to_str_2,cmp_dtli[0],)
                                        fbcursor.execute(sql,val)
                                        ebun_sel_2 = fbcursor.fetchone()
                                        ebun_entry_2.delete(0,END)
                                        ebun_entry_2.insert(0,ebun_sel_2[4])
                                        ebun_entry_6.delete('1.0',END)
                                        ebun_entry_6.insert('1.0',ebun_sel_2[11])
                                        ebun_entry_14.delete(0,END)
                                        ebun_entry_14.insert(0,ebun_sel_2[12])
                                        ebun_entry_22.delete(0,END)
                                        ebun_entry_22.insert(0,ebun_sel_2[14])
                                    except:
                                        sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                        val = (ebun_to_str_2,cmp_dtli[0],)
                                        fbcursor.execute(sql,val)
                                        ebun_sel_2 = fbcursor.fetchone()
                                        ebun_entry_2.delete(0,END)
                                        ebun_entry_2.insert(0,ebun_sel_2[4])
                                        ebun_entry_6.delete('1.0',END)
                                        ebun_entry_6.insert('1.0',ebun_sel_2[7])
                                        ebun_entry_14.delete(0,END)
                                        ebun_entry_14.insert(0,ebun_sel_2[8])
                                        ebun_entry_22.delete(0,END)
                                        ebun_entry_22.insert(0,ebun_sel_2[10])

                                def bun_details_e3(event):
                                    ebun_to_str_3 = ebun_comb_3.get()
                                    try:
                                        sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                        val = (ebun_to_str_3,cmp_dtli[0],)
                                        fbcursor.execute(sql,val)
                                        ebun_sel_3 = fbcursor.fetchone()
                                        ebun_entry_3.delete(0,END)
                                        ebun_entry_3.insert(0,ebun_sel_3[4])
                                        ebun_entry_7.delete('1.0',END)
                                        ebun_entry_7.insert('1.0',ebun_sel_3[11])
                                        ebun_entry_15.delete(0,END)
                                        ebun_entry_15.insert(0,ebun_sel_3[12])
                                        ebun_entry_23.delete(0,END)
                                        ebun_entry_23.insert(0,ebun_sel_3[14])
                                    except:
                                        sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                        val = (ebun_to_str_3,cmp_dtli[0],)
                                        fbcursor.execute(sql,val)
                                        ebun_sel_3 = fbcursor.fetchone()
                                        ebun_entry_3.delete(0,END)
                                        ebun_entry_3.insert(0,ebun_sel_3[4])
                                        ebun_entry_7.delete('1.0',END)
                                        ebun_entry_7.insert('1.0',ebun_sel_3[7])
                                        ebun_entry_15.delete(0,END)
                                        ebun_entry_15.insert(0,ebun_sel_3[8])
                                        ebun_entry_23.delete(0,END)
                                        ebun_entry_23.insert(0,ebun_sel_3[10])

                                def bun_details_e4(event):
                                    ebun_to_str_4 = ebun_comb_4.get()
                                    try:
                                        sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                        val = (ebun_to_str_4,cmp_dtli[0],)
                                        fbcursor.execute(sql,val)
                                        ebun_sel_4 = fbcursor.fetchone()
                                        ebun_entry_4.delete(0,END)
                                        ebun_entry_4.insert(0,ebun_sel_4[4])
                                        ebun_entry_8.delete('1.0',END)
                                        ebun_entry_8.insert('1.0',ebun_sel_4[11])
                                        ebun_entry_16.delete(0,END)
                                        ebun_entry_16.insert(0,ebun_sel_4[12])
                                        ebun_entry_24.delete(0,END)
                                        ebun_entry_24.insert(0,ebun_sel_4[14])
                                    except:
                                        sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                        val = (ebun_to_str_4,cmp_dtli[0],)
                                        fbcursor.execute(sql,val)
                                        ebun_sel_4 = fbcursor.fetchone()
                                        ebun_entry_4.delete(0,END)
                                        ebun_entry_4.insert(0,ebun_sel_4[4])
                                        ebun_entry_8.delete('1.0',END)
                                        ebun_entry_8.insert('1.0',ebun_sel_4[7])
                                        ebun_entry_16.delete(0,END)
                                        ebun_entry_16.insert(0,ebun_sel_4[8])
                                        ebun_entry_24.delete(0,END)
                                        ebun_entry_24.insert(0,ebun_sel_4[10])
                                    

                                sql_pi="select * from auth_user where username=%s"
                                pi_val=(nm_ent.get(),)
                                fbcursor.execute(sql_pi,pi_val,)
                                pi_dtl=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pi_dtl[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dtli=fbcursor.fetchone()
                                print(cmp_dtli)

                                ebi_sql = "SELECT name FROM app1_inventory where cid_id=%s"
                                ebi_val = (cmp_dtli[0],)
                                fbcursor.execute(ebi_sql,ebi_val)
                                ebi_data = fbcursor.fetchall()
                            
                                ebii_sql = "SELECT name FROM app1_noninventory where cid_id=%s"
                                ebii_val = (cmp_dtli[0],)
                                fbcursor.execute(ebii_sql,ebii_val)
                                ebii_data = fbcursor.fetchall()

                                eb_data = []   
                                
                                for i in ebi_data:
                                    eb_data.append(i[0])
                                for i in ebii_data:
                                    eb_data.append(i[0])            


                                ebun_comb_1 = ttk.Combobox(pro_canvas_edit_4, font=('arial 10'),values=eb_data)
                                # bun_comb_1['values'] = ("Choose",b_data,)
                                ebun_comb_1.bind("<<ComboboxSelected>>",bun_details_e1)
                                window_ebun_comb_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", width=180, height=30,window=ebun_comb_1,tags=('bepcombo1'))
                                ebun_comb_1.delete(0,'end')
                                ebun_comb_1.insert(0, edit_pbun[5])

                                ebun_comb_2 = ttk.Combobox(pro_canvas_edit_4, font=('arial 10'),values=eb_data)
                                # bun_comb_2['values'] = ("Choose",b_data,)
                                ebun_comb_2.bind("<<ComboboxSelected>>",bun_details_e2)
                                window_ebun_comb_2 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", width=180, height=30,window=ebun_comb_2,tags=('bepcombo2'))
                                ebun_comb_2.delete(0,'end')
                                ebun_comb_2.insert(0, edit_pbun[6])

                                ebun_comb_3 = ttk.Combobox(pro_canvas_edit_4, font=('arial 10'),values=eb_data)
                                # bun_comb_3['values'] = ("Choose",b_data,)
                                ebun_comb_3.bind("<<ComboboxSelected>>",bun_details_e3)
                                window_ebun_comb_3 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", width=180, height=30,window=ebun_comb_3,tags=('bepcombo3'))
                                ebun_comb_3.delete(0,'end')
                                ebun_comb_3.insert(0, edit_pbun[7])

                                ebun_comb_4 = ttk.Combobox(pro_canvas_edit_4, font=('arial 10'),values=eb_data)
                                # bun_comb_4['values'] = ("Choose",b_data,)
                                ebun_comb_4.bind("<<ComboboxSelected>>",bun_details_e4)
                                window_ebun_comb_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", width=180, height=30,window=ebun_comb_4,tags=('bepcombo4'))
                                ebun_comb_4.delete(0,'end')
                                ebun_comb_4.insert(0, edit_pbun[8])
                            

                                ebun_entry_1=Entry(pro_canvas_edit_4,width=30,justify=LEFT,background='#2f516f',foreground="white")
                                window_ebun_entry_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_1,tags=('bepentry4'))
                                ebun_entry_1.delete(0,'end')
                                ebun_entry_1.insert(0, edit_pbun[9])
                                
                                ebun_entry_2=Entry(pro_canvas_edit_4,width=30,justify=LEFT,background='#2f516f',foreground="white")
                                window_ebun_entry_2 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_2,tags=('bepentry5'))
                                ebun_entry_2.delete(0,'end')
                                ebun_entry_2.insert(0, edit_pbun[10])

                                ebun_entry_3=Entry(pro_canvas_edit_4,width=30,justify=LEFT,background='#2f516f',foreground="white")
                                window_ebun_entry_3 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_3,tags=('bepentry6'))
                                ebun_entry_3.delete(0,'end')
                                ebun_entry_3.insert(0, edit_pbun[11])
                                
                                ebun_entry_4=Entry(pro_canvas_edit_4,width=30,justify=LEFT,background='#2f516f',foreground="white")
                                window_ebun_entry_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_4,tags=('bepentry7'))
                                ebun_entry_4.delete(0,'end')
                                ebun_entry_4.insert(0, edit_pbun[12])


                                ebun_entry_5=scrolledtext.ScrolledText(pro_canvas_edit_4,width=23,background='#2f516f',foreground="white")
                                window_ebun_entry_5 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_5,tags=('bepentry8'))
                                ebun_entry_5.insert(1.0,edit_pbun[13])

                                ebun_entry_6=scrolledtext.ScrolledText(pro_canvas_edit_4,width=23,background='#2f516f',foreground="white")
                                window_ebun_entry_6 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_6,tags=('bepentry9'))
                                ebun_entry_6.insert(1.0,edit_pbun[14])

                                ebun_entry_7=scrolledtext.ScrolledText(pro_canvas_edit_4,width=23,background='#2f516f',foreground="white")
                                window_ebun_entry_7 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_7,tags=('bepentry10'))
                                ebun_entry_7.insert(1.0,edit_pbun[15])

                                ebun_entry_8=scrolledtext.ScrolledText(pro_canvas_edit_4,width=23,background='#2f516f',foreground="white")
                                window_ebun_entry_8 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_8,tags=('bepentry11'))
                                ebun_entry_8.insert(1.0,edit_pbun[16])


                                ebun_entry_9=Spinbox(pro_canvas_edit_4,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_9 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_9,tags=('bepspin1'))
                                ebun_entry_9.delete(0, END)
                                ebun_entry_9.insert(0, edit_pbun[17])

                                ebun_entry_10=Spinbox(pro_canvas_edit_4,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_10 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_10,tags=('bepspin2'))
                                ebun_entry_10.delete(0, END)
                                ebun_entry_10.insert(0, edit_pbun[18])

                                ebun_entry_11=Spinbox(pro_canvas_edit_4,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_11 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_11,tags=('bepspin3'))
                                ebun_entry_11.delete(0, END)
                                ebun_entry_11.insert(0, edit_pbun[19])

                                ebun_entry_12=Spinbox(pro_canvas_edit_4,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_12 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_12,tags=('bepspin4'))
                                ebun_entry_12.delete(0, END)
                                ebun_entry_12.insert(0, edit_pbun[20])

                                
                                ebun_entry_13=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_13 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_13,tags=('bepspin5'))
                                ebun_entry_13.delete(0, END)
                                ebun_entry_13.insert(0, edit_pbun[21])
                                
                                ebun_entry_14=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_14 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_14,tags=('bepspin6'))
                                ebun_entry_14.delete(0, END)
                                ebun_entry_14.insert(0, edit_pbun[22])

                                ebun_entry_15=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_15 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_15,tags=('bepspin7'))
                                ebun_entry_15.delete(0, END)
                                ebun_entry_15.insert(0, edit_pbun[23])

                                ebun_entry_16=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_16 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_16,tags=('bepspin8'))
                                ebun_entry_16.delete(0, END)
                                ebun_entry_16.insert(0, edit_pbun[24])

                                def multiply_num_e1(event):
                                    num1= float(ebun_entry_9.get())
                                    num2= float(ebun_entry_13.get())
                                    mul= round(num1 * num2)
                                    ebun_entry_17.delete(0, END)
                                    ebun_entry_17.insert(0,mul)
                                
                                ebun_entry_17=Entry(pro_canvas_edit_4,width=16,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_17 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_17,tags=('bepspin9'))
                                ebun_entry_17.bind("<Button-1>",multiply_num_e1)
                                ebun_entry_17.delete(0, END)
                                ebun_entry_17.insert(0, edit_pbun[25])

                                def multiply_num_e2(event):
                                    num1= float(ebun_entry_10.get())
                                    num2= float(ebun_entry_14.get())
                                    mul= round(num1 * num2)
                                    ebun_entry_18.delete(0, END)
                                    ebun_entry_18.insert(0,mul)
                            
                                
                                ebun_entry_18=Entry(pro_canvas_edit_4,width=16,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_18 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_18,tags=('bepspin10'))
                                ebun_entry_18.bind("<Button-1>",multiply_num_e2)
                                ebun_entry_18.delete(0, END)
                                ebun_entry_18.insert(0, edit_pbun[26])

                                def multiply_num_e3(event):
                                    num1= float(ebun_entry_11.get())
                                    num2= float(ebun_entry_15.get())
                                    mul= round(num1 * num2)
                                    ebun_entry_19.delete(0, END)
                                    ebun_entry_19.insert(0,mul)
                                
                                ebun_entry_19=Entry(pro_canvas_edit_4,width=16,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_19 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_19,tags=('bepspin11'))
                                ebun_entry_19.bind("<Button-1>",multiply_num_e3)
                                ebun_entry_19.delete(0, END)
                                ebun_entry_19.insert(0, edit_pbun[27])

                                def multiply_num_e4(event):
                                    num1= float(ebun_entry_12.get())
                                    num2= float(ebun_entry_16.get())
                                    mul= round(num1 * num2)
                                    ebun_entry_20.delete(0, END)
                                    ebun_entry_20.insert(0,mul)
                            
                                ebun_entry_20=Entry(pro_canvas_edit_4,width=16,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_20 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_20,tags=('bepspin12'))
                                ebun_entry_20.bind("<Button-1>",multiply_num_e4)
                                ebun_entry_20.delete(0, END)
                                ebun_entry_20.insert(0, edit_pbun[28])
                                
                                ebun_entry_21=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_21 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_21,tags=('bepspin13'))
                                ebun_entry_21.delete(0, END)
                                ebun_entry_21.insert(0, edit_pbun[29])

                                ebun_entry_22=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_22 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_22,tags=('bepspin14'))
                                ebun_entry_22.delete(0, END)
                                ebun_entry_22.insert(0, edit_pbun[30])

                                ebun_entry_23=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_23 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_23,tags=('bepspin15'))
                                ebun_entry_23.delete(0, END)
                                ebun_entry_23.insert(0, edit_pbun[31])

                                ebun_entry_24=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                                window_ebun_entry_24 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_24,tags=('bepspin16'))
                                ebun_entry_24.delete(0, END)
                                ebun_entry_24.insert(0, edit_pbun[32])

                                ebun_sub_btn1=Button(pro_canvas_edit_4,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=edit_new_pro_bun)
                                window_ebun_sub_btn1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=ebun_sub_btn1,tags=('bepbutton2'))

                                def b_eback_1_():
                                    pro_frame_edit_4.grid_forget()
                                    pro_frame.grid(row=0,column=0,sticky='nsew')

                                bck_ebbtn1=Button(pro_canvas_edit_4,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=b_eback_1_)
                                window_bck_ebbtn1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=bck_ebbtn1,tags=('bepbuttn1'))
                            else:
                                pass
                        
                        elif pro_comb_1.get() == 'Delete':
                            pro_del = messagebox.askyesno("Delete Customer","Are you sure to delete this customer?")

                            if pro_del == True:
                                if pro_tree.item(pro_tree.focus())["values"][1] == 'Inventory':
                                    inv_peditid = pro_tree.item(pro_tree.focus())["values"][2]
                                    inv_peditid_1 = pro_tree.item(pro_tree.focus())["values"][3]

                                    sql_u = 'select * from auth_user where username=%s'
                                    val_u = (nm_ent.get(),)
                                    fbcursor.execute(sql_u,val_u)
                                    u_dtl = fbcursor.fetchone()

                                    sql_c = 'select * from app1_company where id_id=%s'
                                    val_c = (u_dtl[0],)
                                    fbcursor.execute(sql_c,val_c)
                                    c_dtl = fbcursor.fetchone()

                                    sql = 'delete from app1_inventory where name=%s and sku=%s and cid_id=%s'
                                    val = (inv_peditid,inv_peditid_1,c_dtl[0],)
                                    fbcursor.execute(sql,val)
                                    finsysdb.commit()

                                elif pro_tree.item(pro_tree.focus())["values"][1] == 'Noninventory':

                                    non_peditid = pro_tree.item(pro_tree.focus())["values"][2]
                            
                                    non_peditid_1 = pro_tree.item(pro_tree.focus())["values"][3]

                                    sql_u = 'select * from auth_user where username=%s'
                                    val_u = (nm_ent.get(),)
                                    fbcursor.execute(sql_u,val_u)
                                    u_dtl = fbcursor.fetchone()

                                    sql_c = 'select * from app1_company where id_id=%s'
                                    val_c = (u_dtl[0],)
                                    fbcursor.execute(sql_c,val_c)
                                    c_dtl = fbcursor.fetchone()

                                    sql = 'delete from app1_noninventory where name=%s and sku=%s and cid_id=%s'
                                    val = (non_peditid,non_peditid_1,c_dtl[0],)
                                    fbcursor.execute(sql,val)
                                    finsysdb.commit()
                                elif pro_tree.item(pro_tree.focus())["values"][1] == 'Service':

                                    ser_peditid = pro_tree.item(pro_tree.focus())["values"][2]

                                    ser_peditid_1 = pro_tree.item(pro_tree.focus())["values"][3]

                                    sql_u = 'select * from auth_user where username=%s'
                                    val_u = (nm_ent.get(),)
                                    fbcursor.execute(sql_u,val_u)
                                    u_dtl = fbcursor.fetchone()

                                    sql_c = 'select * from app1_company where id_id=%s'
                                    val_c = (u_dtl[0],)
                                    fbcursor.execute(sql_c,val_c)
                                    c_dtl = fbcursor.fetchone()

                                    sql = 'delete from app1_service where name=%s and sku=%s and cid_id=%s'
                                    val = (ser_peditid,ser_peditid_1,c_dtl[0],)
                                    fbcursor.execute(sql,val)
                                    finsysdb.commit()
                            
                                elif pro_tree.item(pro_tree.focus())["values"][1] == 'Bundle':

                                    bun_peditid = pro_tree.item(pro_tree.focus())["values"][2]

                                    bun_peditid_1 = pro_tree.item(pro_tree.focus())["values"][3]

                                    sql_u = 'select * from auth_user where username=%s'
                                    val_u = (nm_ent.get(),)
                                    fbcursor.execute(sql_u,val_u)
                                    u_dtl = fbcursor.fetchone()

                                    sql_c = 'select * from app1_company where id_id=%s'
                                    val_c = (u_dtl[0],)
                                    fbcursor.execute(sql_c,val_c)
                                    c_dtl = fbcursor.fetchone()

                                    sql = 'delete from app1_bundle where name=%s and sku=%s and cid_id=%s'
                                    val = (ser_peditid,ser_peditid_1,c_dtl[0],)
                                    fbcursor.execute(sql,val)
                                    finsysdb.commit()

                                

                                #_________Refresh insert tree________#

                                for record in pro_tree.get_children():
                                    pro_tree.delete(record)

        
                                sql_p="select * from auth_user where username=%s"
                                sql_p_val=(nm_ent.get(),)
                                fbcursor.execute(sql_p,sql_p_val,)
                                pr_dt=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dt[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dt=fbcursor.fetchone()

                                p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                p_val_1 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_1,p_val_1,)
                                p_data_1 = fbcursor.fetchall()
                                
                                count0 = 0
                                for i in p_data_1:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                    else:
                                        pass
                                count0 += 1

                                p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                p_val_2 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_2,p_val_2,)
                                p_data_2 = fbcursor.fetchall()

                                count1 = 0
                                for i in p_data_2:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count1 += 1

                                p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                p_val_3 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_3,p_val_3,)
                                p_data_3 = fbcursor.fetchall()
                                

                                count2 = 0
                                for i in p_data_3:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count2 += 1

                                p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                p_val_4 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_4,p_val_4,)
                                p_data_4 = fbcursor.fetchall()
                                

                                count3 = 0
                                for i in p_data_4:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                    else:
                                        pass
                                count3 += 1


                            else:
                                pass
                        else:  
                            pass



                    # pebtn1=Button(pro_canvas,text='Edit', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=pro_edit_item)
                    # window_pebtn1 = pro_canvas.create_window(0, 0, anchor="nw", window=pebtn1,tags=('pbutton2'))

                    pro_comb_1 = ttk.Combobox(pro_canvas,font=('arial 10'))
                    pro_comb_1['values'] = ("Actions","Edit","Delete")
                    pro_comb_1.current(0)
                    window_pro_comb_1 = pro_canvas.create_window(0, 0, anchor="nw", width=110,height=30,window=pro_comb_1,tags=('pbutton3'))
                    pro_comb_1.bind("<<ComboboxSelected>>",pro_edit_item)

                    # pdbtn1=Button(pro_canvas,text='Delete', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                    # window_pdbtn1 = pro_canvas.create_window(0, 0, anchor="nw", window=pdbtn1,tags=('pbutton3'))

                    fgth = ttk.Style()
                    fgth.theme_use("default")
                    fgth.configure("Treeview", background="#2f516f", foreground="white",fieldbackground="#2f516f",rowheight=25,font=(None,11))
                    fgth.configure("Treeview.Heading",background="#1b3857",activeforeground="black",foreground="white",font=(None,11)) 

                    pro_scrollbar = Scrollbar(pro_frame,orient="vertical") 

                    pro_tree = ttk.Treeview(pro_canvas, columns = (1,2,3,4,5,6),show = "headings",yscrollcommand=pro_scrollbar.set)
                    pro_tree.heading(1)
                    pro_tree.heading(2, text="TYPE")
                    pro_tree.heading(3, text="NAME")
                    pro_tree.heading(4, text="SKU")
                    pro_tree.heading(5, text="HSN/SAC")
                    pro_tree.heading(6, text="QUANTITY")
                    
                    pro_tree.column(1, width = 50)
                    pro_tree.column(2, width = 250)
                    pro_tree.column(3, width = 300)
                    pro_tree.column(4, width = 150)
                    pro_tree.column(5, width = 200)
                    pro_tree.column(6, width = 150)
                    window_label_4 = pro_canvas.create_window(0, 0, anchor="nw", window=pro_tree,tags=('ptree1'))

                    pro_scrollbar.config(command=pro_tree.yview)
                    pro_scrollbar.grid(row=0,column=2,sticky='ns')

                    sql_p="select * from auth_user where username=%s"
                    sql_p_val=(nm_ent.get(),)
                    fbcursor.execute(sql_p,sql_p_val,)
                    pr_dt=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (pr_dt[0],)
                    fbcursor.execute(sql, val,)
                    cmp_dt=fbcursor.fetchone()

                    p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                    p_val_1 = (cmp_dt[0],)
                    fbcursor.execute(p_sql_1,p_val_1,)
                    p_data_1 = fbcursor.fetchall()
                    
                    count0 = 0
                    for i in p_data_1:
                        if True:
                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                        else:
                            pass
                    count0 += 1

                    p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                    p_val_2 = (cmp_dt[0],)
                    fbcursor.execute(p_sql_2,p_val_2,)
                    p_data_2 = fbcursor.fetchall()

                    count1 = 0
                    for i in p_data_2:
                        if True:
                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                        else:
                            pass
                    count1 += 1

                    p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                    p_val_3 = (cmp_dt[0],)
                    fbcursor.execute(p_sql_3,p_val_3,)
                    p_data_3 = fbcursor.fetchall()
                    

                    count2 = 0
                    for i in p_data_3:
                        if True:
                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                        else:
                            pass
                    count2 += 1

                    p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                    p_val_4 = (cmp_dt[0],)
                    fbcursor.execute(p_sql_4,p_val_4,)
                    p_data_4 = fbcursor.fetchall()
                    

                    count3 = 0
                    for i in p_data_4:
                        if True:
                            pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                        else:
                            pass
                    count3 += 1