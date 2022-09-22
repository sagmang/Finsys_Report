#------------------------------------Profit & Loss---------------------------------#
                    tab6_1.grid_columnconfigure(0,weight=1)
                    tab6_1.grid_rowconfigure(0,weight=1)

                    profit_frame = Frame(tab6_1)
                    profit_frame.grid(row=0,column=0,sticky='nsew')

                    def profit_responsive_widgets(event):
                        try:
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget

                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("plpoly1",x1 + r1,y1,
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

                            dcanvas.coords("plhline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                            dcanvas.coords("pllabel1",dwidth/2.5,dheight/8.00)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/3
                            y21 = dheight/1.4


                            dcanvas.coords("plpoly2",x11 + r2,y11,
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
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/1.3
                            y21 = dheight/0.195


                            dcanvas.coords("plpoly3",x11 + r2,y11,
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

                            dcanvas.coords("pllabel2",dwidth/30,dheight/2.65)
                            dcanvas.coords("pllabel3",dwidth/3.4,dheight/2.65)
                            dcanvas.coords("pllabel4",dwidth/1.98,dheight/2.65)
                            dcanvas.coords("plcombo1",dwidth/20,dheight/2.3)
                            dcanvas.coords("plbutton1",dwidth/1.9,dheight/1.8)
                            dcanvas.coords("plbutton2",dwidth/1.45,dheight/1.8)

                            r2 = 25
                            x11 = dwidth/16
                            x21 = dwidth/1.07
                            y11 = dheight/1.15
                            y21 = dheight/0.2


                            dcanvas.coords("plpoly4",x11 + r2,y11,
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
                            x11 = dwidth/10
                            x21 = dwidth/1.12
                            y11 = dheight/1.05
                            y21 = dheight/0.8

                            dcanvas.coords("plpoly5",x11 + r2,y11,
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

                            dcanvas.coords("pllabel5",dwidth/4,dheight/0.87)
                            dcanvas.coords("plimage1",dwidth/6.5,dheight/0.88)
                            dcanvas.coords("plhline1",dwidth/10,dheight/0.7,dwidth/1.12,dheight/0.7)
                            dcanvas.coords("plhline2",dwidth/10,dheight/0.66,dwidth/1.12,dheight/0.66)
                            dcanvas.coords("pllabel6",dwidth/1.3,dheight/0.685)
                            dcanvas.coords("pllabel7",dwidth/8,dheight/0.645)
                            dcanvas.coords("plhline3",dwidth/10,dheight/0.52,dwidth/1.12,dheight/0.52)
                            dcanvas.coords("pllabel8",dwidth/6.5,dheight/0.515)
                            dcanvas.coords("plhline4",dwidth/10,dheight/0.5,dwidth/1.12,dheight/0.5)
                            dcanvas.coords("plhline5",dwidth/10,dheight/0.492,dwidth/1.12,dheight/0.492)
                            dcanvas.coords("pllabel9",dwidth/9,dheight/0.486)
                            dcanvas.coords("plhline6",dwidth/10,dheight/0.415,dwidth/1.12,dheight/0.415)
                            dcanvas.coords("pllabel10",dwidth/6.5,dheight/0.412)
                            dcanvas.coords("pllabel11",dwidth/8,dheight/0.40)
                            dcanvas.coords("plhline7",dwidth/10,dheight/0.405,dwidth/1.12,dheight/0.405)
                            dcanvas.coords("plhline8",dwidth/10,dheight/0.35,dwidth/1.12,dheight/0.35)
                            dcanvas.coords("pllabel12",dwidth/8,dheight/0.347)
                            dcanvas.coords("plhline9",dwidth/10,dheight/0.31,dwidth/1.12,dheight/0.31)
                            dcanvas.coords("pllabel13",dwidth/8,dheight/0.308)
                            dcanvas.coords("plhline10",dwidth/10,dheight/0.278,dwidth/1.12,dheight/0.278)
                            dcanvas.coords("pllabel14",dwidth/6.5,dheight/0.277)
                            dcanvas.coords("plhline11",dwidth/10,dheight/0.273,dwidth/1.12,dheight/0.273)
                            dcanvas.coords("pllabel15",dwidth/10,dheight/0.27)

                            dcanvas.coords("pltree1",dwidth/6.6,dheight/0.62)
                            dcanvas.coords("pllabel16",dwidth/1.3,dheight/0.515)
                            dcanvas.coords("pltree2",dwidth/6.6,dheight/0.475)
                            dcanvas.coords("pllabel17",dwidth/1.3,dheight/0.412)
                            dcanvas.coords("pltree3",dwidth/6.6,dheight/0.392)
                            dcanvas.coords("pltree4",dwidth/6.6,dheight/0.341)
                            dcanvas.coords("pltree5",dwidth/6.6,dheight/0.303)
                            dcanvas.coords("pllabel18",dwidth/1.3,dheight/0.27)
                            dcanvas.coords("pllabel19",dwidth/1.3,dheight/0.277)
                        except:
                            pass
                        try:
                            dcanvas.coords("pldate1",dwidth/3.4,dheight/2.3)
                            dcanvas.coords("pldate2",dwidth/1.97,dheight/2.3)
                        except:
                            pass


                    pl_canvas=Canvas(profit_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,3000))

                    profit_frame.grid_rowconfigure(0,weight=1)
                    profit_frame.grid_columnconfigure(0,weight=1)

                    vertibar=Scrollbar(profit_frame, orient=VERTICAL)
                    vertibar.grid(row=0,column=1,sticky='ns')
                    vertibar.config(command=pl_canvas.yview)
                    
                    pl_canvas.bind("<Configure>", profit_responsive_widgets)
                    pl_canvas.config(yscrollcommand=vertibar.set)
                    pl_canvas.grid(row=0,column=0,sticky='nsew')

                    
                    pl_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("plpoly1"))

                    label_1 = Label(pl_canvas,width=16,height=1,text="PROFIT AND LOSS", font=('arial 25'),background="#1b3857",fg="white") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel1"))

                    pl_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("plhline"))

                    pl_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("plpoly2"))

                    pl_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("plpoly3"))

                    label_1 = Label(pl_canvas,width=16,height=1,text="Report period", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel2"))

                    def custom_date_1(event):
                        if pl_comb_1.get() == 'Custom':
                            pl_canvas.itemconfig('pldate1',state='normal')
                            pl_canvas.itemconfig('pldate2',state='normal')
                            pl_canvas.itemconfig('pllabel3',state='normal')
                            pl_canvas.itemconfig('pllabel4',state='normal')
                        else:
                            pl_canvas.itemconfig('pldate1',state='hidden')
                            pl_canvas.itemconfig('pldate2',state='hidden')
                            pl_canvas.itemconfig('pllabel3',state='hidden')
                            pl_canvas.itemconfig('pllabel4',state='hidden')

                     #--------Filter By Date------------#
                    def filterby_date_2():

                        if pl_comb_1.get() == 'All dates':

                            s_date = '2000-01-01'
                            e_date = '2050-01-01'

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (s_date,e_date,'Income',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_1 = fbcursor.fetchall()

                            for record in pl_tree.get_children():
                                pl_tree.delete(record)

                            countd = 0
                            for i in pl_date_data_1:
                                pl_tree.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                in_result_1['text'] = '{}'.format(total)
                            except:
                                in_result_1['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (s_date,e_date,'Cost of Goods Sold',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_2 = fbcursor.fetchall()

                            for record in pl_tree_1.get_children():
                                pl_tree_1.delete(record)

                            countd = 0
                            for i in pl_date_data_2:
                                pl_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                total_1 = 0.0
                                total_2 = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                for child in pl_tree_1.get_children():
                                    total_1 += float(pl_tree_1.item(child, 'values')[1])
                                total_2 = total-total_1
                                in_result_2['text'] = '{}'.format(total_2)
                            except:
                                in_result_2['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (s_date,e_date,'Other Income',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_3 = fbcursor.fetchall()

                            for record in pl_tree_2.get_children():
                                pl_tree_2.delete(record)

                            countd = 0
                            for i in pl_date_data_3:
                                pl_tree_2.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))  
                            countd += 1  

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (s_date,e_date,'Expenses',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_4 = fbcursor.fetchall()

                            for record in pl_tree_3.get_children():
                                pl_tree_3.delete(record)

                            countd = 0
                            for i in pl_date_data_4:
                                pl_tree_3.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))  
                            countd += 1  

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (s_date,e_date,'Other Expenses',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_5 = fbcursor.fetchall()

                            for record in pl_tree_4.get_children():
                                pl_tree_4.delete(record)

                            countd = 0
                            for i in pl_date_data_5:
                                pl_tree_4.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))
                            countd += 1  
                            try:
                                total_5 = 0.0
                                for child in pl_tree_4.get_children():
                                    total_5 += float(pl_tree_4.item(child, 'values')[1])
                                in_result_3['text'] = '{}'.format(total_5)
                            except:
                                in_result_3['text'] = '{}'.format(0)
                            try:
                                total = 0.0
                                total_1 = 0.0
                                total_3 = 0.0
                                total_4 = 0.0
                                total_5 = 0.0
                                total_6 = 0.0
                                total_7 = 0.0
                                total_8 = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                for child in pl_tree_1.get_children():
                                    total_1 += float(pl_tree_1.item(child, 'values')[1])
                                total_2 = total-total_1
                                for child in pl_tree_2.get_children():
                                    total_3 += float(pl_tree_2.item(child, 'values')[1])
                                for child in pl_tree_3.get_children():
                                    total_4 += float(pl_tree_3.item(child, 'values')[1])
                                for child in pl_tree_4.get_children():
                                    total_5 += float(pl_tree_4.item(child, 'values')[1])
                                total_6 = total_2+total_3
                                total_7 = total_6-total_4
                                total_8 = total_7-total_5
                                in_result_4['text'] = '{}'.format(total_8)
                            except:
                                in_result_4['text'] = '{}'.format(0)


                        elif pl_comb_1.get() == 'Custom':

                            start_date = pl_date_1.get_date()
                            end_date = pl_date_2.get_date()

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (start_date,end_date,'Income',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_1 = fbcursor.fetchall()

                            for record in pl_tree.get_children():
                                pl_tree.delete(record)

                            countd = 0
                            for i in pl_date_data_1:
                                pl_tree.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                in_result_1['text'] = '{}'.format(total)
                            except:
                                in_result_1['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (start_date,end_date,'Cost of Goods Sold',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_2 = fbcursor.fetchall()

                            for record in pl_tree_1.get_children():
                                pl_tree_1.delete(record)

                            countd = 0
                            for i in pl_date_data_2:
                                pl_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                total_1 = 0.0
                                total_2 = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                for child in pl_tree_1.get_children():
                                    total_1 += float(pl_tree_1.item(child, 'values')[1])
                                total_2 = total-total_1
                                in_result_2['text'] = '{}'.format(total_2)
                            except:
                                in_result_2['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (start_date,end_date,'Other Income',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_3 = fbcursor.fetchall()

                            for record in pl_tree_2.get_children():
                                pl_tree_2.delete(record)

                            countd = 0
                            for i in pl_date_data_3:
                                pl_tree_2.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))  
                            countd += 1  

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (start_date,end_date,'Expenses',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_4 = fbcursor.fetchall()

                            for record in pl_tree_3.get_children():
                                pl_tree_3.delete(record)

                            countd = 0
                            for i in pl_date_data_4:
                                pl_tree_3.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))  
                            countd += 1  

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (start_date,end_date,'Other Expenses',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_5 = fbcursor.fetchall()

                            for record in pl_tree_4.get_children():
                                pl_tree_4.delete(record)

                            countd = 0
                            for i in pl_date_data_5:
                                pl_tree_4.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))
                            countd += 1  
                            try:
                                total_5 = 0.0
                                for child in pl_tree_4.get_children():
                                    total_5 += float(pl_tree_4.item(child, 'values')[1])
                                in_result_3['text'] = '{}'.format(total_5)
                            except:
                                in_result_3['text'] = '{}'.format(0)
                            try:
                                total = 0.0
                                total_1 = 0.0
                                total_3 = 0.0
                                total_4 = 0.0
                                total_5 = 0.0
                                total_6 = 0.0
                                total_7 = 0.0
                                total_8 = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                for child in pl_tree_1.get_children():
                                    total_1 += float(pl_tree_1.item(child, 'values')[1])
                                total_2 = total-total_1
                                for child in pl_tree_2.get_children():
                                    total_3 += float(pl_tree_2.item(child, 'values')[1])
                                for child in pl_tree_3.get_children():
                                    total_4 += float(pl_tree_3.item(child, 'values')[1])
                                for child in pl_tree_4.get_children():
                                    total_5 += float(pl_tree_4.item(child, 'values')[1])
                                total_6 = total_2+total_3
                                total_7 = total_6-total_4
                                total_8 = total_7-total_5
                                in_result_4['text'] = '{}'.format(total_8)
                            except:
                                in_result_4['text'] = '{}'.format(0)

                        elif pl_comb_1.get() == 'Today':

                            today1 = date.today()
                            print("Today is: ", today1)

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof=%s AND acctype=%s and cid_id=%s"
                            date_val = (date.today(),'Income',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_1 = fbcursor.fetchall()

                            for record in pl_tree.get_children():
                                pl_tree.delete(record)

                            countd = 0
                            for i in pl_date_data_1:
                                pl_tree.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                in_result_1['text'] = '{}'.format(total)
                            except:
                                in_result_1['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof=%s AND acctype=%s and cid_id=%s"
                            date_val = (date.today(),'Cost of Goods Sold',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_2 = fbcursor.fetchall()

                            for record in pl_tree_1.get_children():
                                pl_tree_1.delete(record)

                            countd = 0
                            for i in pl_date_data_2:
                                pl_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                total_1 = 0.0
                                total_2 = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                for child in pl_tree_1.get_children():
                                    total_1 += float(pl_tree_1.item(child, 'values')[1])
                                total_2 = total-total_1
                                in_result_2['text'] = '{}'.format(total_2)
                            except:
                                in_result_2['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof=%s AND acctype=%s and cid_id=%s"
                            date_val = (date.today(),'Other Income',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_3 = fbcursor.fetchall()

                            for record in pl_tree_2.get_children():
                                pl_tree_2.delete(record)

                            countd = 0
                            for i in pl_date_data_3:
                                pl_tree_2.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))  
                            countd += 1  

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof=%s AND acctype=%s and cid_id=%s"
                            date_val = (date.today(),'Expenses',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_4 = fbcursor.fetchall()

                            for record in pl_tree_3.get_children():
                                pl_tree_3.delete(record)

                            countd = 0
                            for i in pl_date_data_4:
                                pl_tree_3.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))  
                            countd += 1  

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof=%s AND acctype=%s and cid_id=%s"
                            date_val = (date.today(),'Other Expenses',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_5 = fbcursor.fetchall()

                            for record in pl_tree_4.get_children():
                                pl_tree_4.delete(record)

                            countd = 0
                            for i in pl_date_data_5:
                                pl_tree_4.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))
                            countd += 1  
                            try:
                                total_5 = 0.0
                                for child in pl_tree_4.get_children():
                                    total_5 += float(pl_tree_4.item(child, 'values')[1])
                                in_result_3['text'] = '{}'.format(total_5)
                            except:
                                in_result_3['text'] = '{}'.format(0)
                            try:
                                total = 0.0
                                total_1 = 0.0
                                total_3 = 0.0
                                total_4 = 0.0
                                total_5 = 0.0
                                total_6 = 0.0
                                total_7 = 0.0
                                total_8 = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                for child in pl_tree_1.get_children():
                                    total_1 += float(pl_tree_1.item(child, 'values')[1])
                                total_2 = total-total_1
                                for child in pl_tree_2.get_children():
                                    total_3 += float(pl_tree_2.item(child, 'values')[1])
                                for child in pl_tree_3.get_children():
                                    total_4 += float(pl_tree_3.item(child, 'values')[1])
                                for child in pl_tree_4.get_children():
                                    total_5 += float(pl_tree_4.item(child, 'values')[1])
                                total_6 = total_2+total_3
                                total_7 = total_6-total_4
                                total_8 = total_7-total_5
                                in_result_4['text'] = '{}'.format(total_8)
                            except:
                                in_result_4['text'] = '{}'.format(0)

                        elif pl_comb_1.get() == 'This month':

                            today_gt2 = date.today()
                            firsty_gt2= today_gt2.replace(day=1)
                            last_monthy_gt2 = firsty_gt2 -relativedelta(day=1)

                            end_todayy_gt2 = last_monthy_gt2
                            end_firsty_gt2 = end_todayy_gt2.replace(day=1)
                            end_monthy_gt2 = end_firsty_gt2 -relativedelta(days=1)+relativedelta(months=1)

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (last_monthy_gt2,end_monthy_gt2,'Income',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_1 = fbcursor.fetchall()

                            for record in pl_tree.get_children():
                                pl_tree.delete(record)

                            countd = 0
                            for i in pl_date_data_1:
                                pl_tree.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                in_result_1['text'] = '{}'.format(total)
                            except:
                                in_result_1['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (last_monthy_gt2,end_monthy_gt2,'Cost of Goods Sold',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_2 = fbcursor.fetchall()

                            for record in pl_tree_1.get_children():
                                pl_tree_1.delete(record)

                            countd = 0
                            for i in pl_date_data_2:
                                pl_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                total_1 = 0.0
                                total_2 = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                for child in pl_tree_1.get_children():
                                    total_1 += float(pl_tree_1.item(child, 'values')[1])
                                total_2 = total-total_1
                                in_result_2['text'] = '{}'.format(total_2)
                            except:
                                in_result_2['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (last_monthy_gt2,end_monthy_gt2,'Other Income',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_3 = fbcursor.fetchall()

                            for record in pl_tree_2.get_children():
                                pl_tree_2.delete(record)

                            countd = 0
                            for i in pl_date_data_3:
                                pl_tree_2.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))  
                            countd += 1  

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (last_monthy_gt2,end_monthy_gt2,'Expenses',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_4 = fbcursor.fetchall()

                            for record in pl_tree_3.get_children():
                                pl_tree_3.delete(record)

                            countd = 0
                            for i in pl_date_data_4:
                                pl_tree_3.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))  
                            countd += 1  

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (last_monthy_gt2,end_monthy_gt2,'Other Expenses',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_5 = fbcursor.fetchall()

                            for record in pl_tree_4.get_children():
                                pl_tree_4.delete(record)

                            countd = 0
                            for i in pl_date_data_5:
                                pl_tree_4.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))
                            countd += 1  
                            try:
                                total_5 = 0.0
                                for child in pl_tree_4.get_children():
                                    total_5 += float(pl_tree_4.item(child, 'values')[1])
                                in_result_3['text'] = '{}'.format(total_5)
                            except:
                                in_result_3['text'] = '{}'.format(0)
                            try:
                                total = 0.0
                                total_1 = 0.0
                                total_3 = 0.0
                                total_4 = 0.0
                                total_5 = 0.0
                                total_6 = 0.0
                                total_7 = 0.0
                                total_8 = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                for child in pl_tree_1.get_children():
                                    total_1 += float(pl_tree_1.item(child, 'values')[1])
                                total_2 = total-total_1
                                for child in pl_tree_2.get_children():
                                    total_3 += float(pl_tree_2.item(child, 'values')[1])
                                for child in pl_tree_3.get_children():
                                    total_4 += float(pl_tree_3.item(child, 'values')[1])
                                for child in pl_tree_4.get_children():
                                    total_5 += float(pl_tree_4.item(child, 'values')[1])
                                total_6 = total_2+total_3
                                total_7 = total_6-total_4
                                total_8 = total_7-total_5
                                in_result_4['text'] = '{}'.format(total_8)
                            except:
                                in_result_4['text'] = '{}'.format(0)

                        elif pl_comb_1.get() == 'This financial year':

                            fiscalyear.setup_fiscal_calendar(start_month=4)

                            first_fiscal_year = date.today().year + 1
                            print(first_fiscal_year)
                            current_fiscal_year = FiscalDate.today().fiscal_year

                            for x in range(0, 1):
                                fy = FiscalYear(first_fiscal_year + x)
                                fystart = fy.start.strftime("%Y-%m-%d")
                                fyend = fy.end.strftime("%Y-%m-%d")
                                print(fystart)
                                print(fyend)

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (fystart,fyend,'Income',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_1 = fbcursor.fetchall()

                            for record in pl_tree.get_children():
                                pl_tree.delete(record)

                            countd = 0
                            for i in pl_date_data_1:
                                pl_tree.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                in_result_1['text'] = '{}'.format(total)
                            except:
                                in_result_1['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (fystart,fyend,'Cost of Goods Sold',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_2 = fbcursor.fetchall()

                            for record in pl_tree_1.get_children():
                                pl_tree_1.delete(record)

                            countd = 0
                            for i in pl_date_data_2:
                                pl_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                total_1 = 0.0
                                total_2 = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                for child in pl_tree_1.get_children():
                                    total_1 += float(pl_tree_1.item(child, 'values')[1])
                                total_2 = total-total_1
                                in_result_2['text'] = '{}'.format(total_2)
                            except:
                                in_result_2['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (fystart,fyend,'Other Income',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_3 = fbcursor.fetchall()

                            for record in pl_tree_2.get_children():
                                pl_tree_2.delete(record)

                            countd = 0
                            for i in pl_date_data_3:
                                pl_tree_2.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))  
                            countd += 1  

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (fystart,fyend,'Expenses',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_4 = fbcursor.fetchall()

                            for record in pl_tree_3.get_children():
                                pl_tree_3.delete(record)

                            countd = 0
                            for i in pl_date_data_4:
                                pl_tree_3.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))  
                            countd += 1  

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (fystart,fyend,'Other Expenses',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            pl_date_data_5 = fbcursor.fetchall()

                            for record in pl_tree_4.get_children():
                                pl_tree_4.delete(record)

                            countd = 0
                            for i in pl_date_data_5:
                                pl_tree_4.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7]))
                            countd += 1  
                            try:
                                total_5 = 0.0
                                for child in pl_tree_4.get_children():
                                    total_5 += float(pl_tree_4.item(child, 'values')[1])
                                in_result_3['text'] = '{}'.format(total_5)
                            except:
                                in_result_3['text'] = '{}'.format(0)
                            try:
                                total = 0.0
                                total_1 = 0.0
                                total_3 = 0.0
                                total_4 = 0.0
                                total_5 = 0.0
                                total_6 = 0.0
                                total_7 = 0.0
                                total_8 = 0.0
                                for child in pl_tree.get_children():
                                    total += float(pl_tree.item(child, 'values')[1])
                                for child in pl_tree_1.get_children():
                                    total_1 += float(pl_tree_1.item(child, 'values')[1])
                                total_2 = total-total_1
                                for child in pl_tree_2.get_children():
                                    total_3 += float(pl_tree_2.item(child, 'values')[1])
                                for child in pl_tree_3.get_children():
                                    total_4 += float(pl_tree_3.item(child, 'values')[1])
                                for child in pl_tree_4.get_children():
                                    total_5 += float(pl_tree_4.item(child, 'values')[1])
                                total_6 = total_2+total_3
                                total_7 = total_6-total_4
                                total_8 = total_7-total_5
                                in_result_4['text'] = '{}'.format(total_8)
                            except:
                                in_result_4['text'] = '{}'.format(0)
                        else:
                            pass

                    pl_comb_1 = ttk.Combobox(pl_canvas,font=('arial 10'))
                    pl_comb_1['values'] = ("All dates","Custom","Today","This month","This financial year",)
                    pl_comb_1.current(0)
                    window_pl_comb_1 = pl_canvas.create_window(0, 0, anchor="nw", width=300,height=30,window=pl_comb_1,tags=('plcombo1'))
                    pl_comb_1.bind("<<ComboboxSelected>>",custom_date_1)

                    pl_btn_1=Button(pl_canvas,text='Run Report', width=20,height=1,foreground="white",background="#1b3857",font='arial 12',command=filterby_date_2)
                    window_pl_btn_1 = pl_canvas.create_window(0, 0, anchor="nw", window=pl_btn_1,tags=('plbutton2'))

                    pl_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="white",tags=("plpoly4"))

                    pl_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#0d6e9e",tags=("plpoly5"))

                    usr_sql = "SELECT * FROM auth_user WHERE username=%s"
                    usr_val = (nm_ent.get(),)
                    fbcursor.execute(usr_sql,usr_val)
                    usr_data = fbcursor.fetchone()

                    cmp_sql = "SELECT * FROM app1_company WHERE id_id=%s"
                    cmp_val = (usr_data[0],)
                    fbcursor.execute(cmp_sql,cmp_val)
                    cmp_data = fbcursor.fetchone()

                    label_1 = Label(pl_canvas,width=14,height=1,text=cmp_data[1], font=('arial 18 bold'),background="#0d6e9e",fg="white") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel5"))


                    pl_image_1=Label(pl_canvas,  image = prof_pics,bg="#213b52",width=150,height=150,  anchor="center",font=('Calibri 14 bold'))
                    win_pl_image_1 = pl_canvas.create_window(0, 0, anchor="nw", window=pl_image_1,tags=("plimage1"))

                    label_1 = Label(pl_canvas,width=5,height=1,text="From", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel3"),state=HIDDEN)

                    label_1 = Label(pl_canvas,width=3,height=1,text="To", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel4"),state=HIDDEN)

                    pl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("plhline1"))
                    pl_canvas.create_line(0,0,0,0,fill='#2f516f',width=2,tags=("plhline2"))

                    label_1 = Label(pl_canvas,width=6,height=1,text="TOTAL", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel6"))

                    label_1 = Label(pl_canvas,width=12,height=1,text='Income', font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel7"))


                    fgthdi = ttk.Style()
                    fgthdi.theme_use("default")
                    fgthdi.configure('mystyle108.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                    fgthdi.configure('mystyle108.Treeview.Heading', background='white',State='DISABLE',foreground='black')

                    pl_scrollbar = Scrollbar(profit_frame,orient="vertical")
                    
                    pl_tree = ttk.Treeview(pl_canvas, columns = (1,2), height = 6, show = "headings",style='mystyle108.Treeview',yscrollcommand=pl_scrollbar.set)
                    
                    pl_tree.column(1, width = 820)
                    pl_tree.column(2, width = 170)

                    window_label_4 = pl_canvas.create_window(0, 0, anchor="nw", window=pl_tree,tags=('pltree1'))

                    pl_scrollbar.config(command=pl_tree.yview)
                    pl_scrollbar.grid(row=0,column=2,sticky='ns')

                    inv_sql="select * from auth_user where username=%s"
                    inv_val=(nm_ent.get(),)
                    fbcursor.execute(inv_sql,inv_val,)
                    inv_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (inv_dtl[0],)
                    fbcursor.execute(sql, val,)
                    inv_dtls=fbcursor.fetchone()

                    c_sql_i1 = "SELECT * FROM app1_accounts1 where acctype=%s and cid_id=%s"
                    c_val_i1 = ('Income',inv_dtls[0],)
                    fbcursor.execute(c_sql_i1,c_val_i1,)
                    in_data = fbcursor.fetchall()

                    count0 = 0
                    for i in in_data:
                        if True:
                            pl_tree.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                        else:
                            pass
                    count0 += 1


                    pl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("plhline3"))

                    label_1 = Label(pl_canvas,width=12,height=1,text="Total Income", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel8"))

                    in_result_1 = Label(pl_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_in_result_1 = pl_canvas.create_window(0, 0, anchor="nw", window=in_result_1, tags=("pllabel16"))

                    total = 0.0
                    for child in pl_tree.get_children():
                        total += float(pl_tree.item(child, 'values')[1])
                    in_result_1['text'] = '{}'.format(total)
                    

                    pl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("plhline4"))
                    pl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("plhline5"))

                    label_1 = Label(pl_canvas,width=20,height=1,text="Cost of Goods Sold", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel9"))

                    fgthdi = ttk.Style()
                    fgthdi.theme_use("default")
                    fgthdi.configure('mystyle109.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                    fgthdi.configure('mystyle109.Treeview.Heading', background='white',State='DISABLE',foreground='black')

                    pl_scrollbar_1 = Scrollbar(profit_frame,orient="vertical")
                    
                    pl_tree_1 = ttk.Treeview(pl_canvas, columns = (1,2), height = 6, show = "headings",style='mystyle109.Treeview',yscrollcommand=pl_scrollbar_1.set)
                    
                    pl_tree_1.column(1, width = 820)
                    pl_tree_1.column(2, width = 170)

                    window_label_4 = pl_canvas.create_window(0, 0, anchor="nw", window=pl_tree_1,tags=('pltree2'))

                    pl_scrollbar_1.config(command=pl_tree_1.yview)
                    pl_scrollbar_1.grid(row=0,column=2,sticky='ns')

                    inv_sql="select * from auth_user where username=%s"
                    inv_val=(nm_ent.get(),)
                    fbcursor.execute(inv_sql,inv_val,)
                    inv_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (inv_dtl[0],)
                    fbcursor.execute(sql, val,)
                    inv_dtls=fbcursor.fetchone()

                    c_sql_i1 = "SELECT * FROM app1_accounts1 where acctype=%s and cid_id=%s"
                    c_val_i1 = ('Cost of Goods Sold',inv_dtls[0],)
                    fbcursor.execute(c_sql_i1,c_val_i1,)
                    in_data_1 = fbcursor.fetchall()

                    count0 = 0
                    for i in in_data_1:
                        if True:
                            pl_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                        else:
                            pass
                    count0 += 1

                    pl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("plhline6"))

                    label_1 = Label(pl_canvas,width=12,height=1,text="Gross Profit", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel10"))

                    in_result_2 = Label(pl_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_in_result_2 = pl_canvas.create_window(0, 0, anchor="nw", window=in_result_2, tags=("pllabel17"))

                    total = 0.0
                    total_1 = 0.0
                    total_2 = 0.0
                    for child in pl_tree.get_children():
                        total += float(pl_tree.item(child, 'values')[1])
                    for child in pl_tree_1.get_children():
                        total_1 += float(pl_tree_1.item(child, 'values')[1])
                    total_2 = total-total_1
                    in_result_2['text'] = '{}'.format(total_2)

                    pl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("plhline7"))

                    label_1 = Label(pl_canvas,width=12,height=1,text="Other Income", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel11"))

                    fgthdi = ttk.Style()
                    fgthdi.theme_use("default")
                    fgthdi.configure('mystyle110.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                    fgthdi.configure('mystyle110.Treeview.Heading', background='white',State='DISABLE',foreground='black')

                    pl_scrollbar_2 = Scrollbar(profit_frame,orient="vertical")
                    
                    pl_tree_2 = ttk.Treeview(pl_canvas, columns = (1,2), height = 6, show = "headings",style='mystyle110.Treeview',yscrollcommand=pl_scrollbar_2.set)
                    
                    pl_tree_2.column(1, width = 820)
                    pl_tree_2.column(2, width = 170)

                    window_label_4 = pl_canvas.create_window(0, 0, anchor="nw", window=pl_tree_2,tags=('pltree3'))

                    pl_scrollbar_2.config(command=pl_tree_2.yview)
                    pl_scrollbar_2.grid(row=0,column=2,sticky='ns')

                    inv_sql="select * from auth_user where username=%s"
                    inv_val=(nm_ent.get(),)
                    fbcursor.execute(inv_sql,inv_val,)
                    inv_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (inv_dtl[0],)
                    fbcursor.execute(sql, val,)
                    inv_dtls=fbcursor.fetchone()

                    c_sql_i1 = "SELECT * FROM app1_accounts1 where acctype=%s and cid_id=%s"
                    c_val_i1 = ('Other Income',inv_dtls[0],)
                    fbcursor.execute(c_sql_i1,c_val_i1,)
                    in_data_2 = fbcursor.fetchall()

                    count0 = 0
                    for i in in_data_2:
                        if True:
                            pl_tree_2.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                        else:
                            pass
                    count0 += 1

                    pl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("plhline8"))

                    label_1 = Label(pl_canvas,width=9,height=1,text="Expenses", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel12"))

                    fgthdi = ttk.Style()
                    fgthdi.theme_use("default")
                    fgthdi.configure('mystyle111.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                    fgthdi.configure('mystyle111.Treeview.Heading', background='white',State='DISABLE',foreground='black')

                    pl_scrollbar_3 = Scrollbar(profit_frame,orient="vertical")
                    
                    pl_tree_3 = ttk.Treeview(pl_canvas, columns = (1,2), height = 6, show = "headings",style='mystyle111.Treeview',yscrollcommand=pl_scrollbar_3.set)
                    
                    pl_tree_3.column(1, width = 820)
                    pl_tree_3.column(2, width = 170)

                    window_label_4 = pl_canvas.create_window(0, 0, anchor="nw", window=pl_tree_3,tags=('pltree4'))

                    pl_scrollbar_3.config(command=pl_tree_3.yview)
                    pl_scrollbar_3.grid(row=0,column=2,sticky='ns')

                    inv_sql="select * from auth_user where username=%s"
                    inv_val=(nm_ent.get(),)
                    fbcursor.execute(inv_sql,inv_val,)
                    inv_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (inv_dtl[0],)
                    fbcursor.execute(sql, val,)
                    inv_dtls=fbcursor.fetchone()

                    c_sql_i1 = "SELECT * FROM app1_accounts1 where acctype=%s and cid_id=%s"
                    c_val_i1 = ('Expenses',inv_dtls[0],)
                    fbcursor.execute(c_sql_i1,c_val_i1,)
                    in_data_3 = fbcursor.fetchall()

                    count0 = 0
                    for i in in_data_3:
                        if True:
                            pl_tree_3.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                        else:
                            pass
                    count0 += 1

                    pl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("plhline9"))

                    label_1 = Label(pl_canvas,width=14,height=1,text="Other Expenses", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel13"))

                    fgthdi = ttk.Style()
                    fgthdi.theme_use("default")
                    fgthdi.configure('mystyle112.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                    fgthdi.configure('mystyle112.Treeview.Heading', background='white',State='DISABLE',foreground='black')

                    pl_scrollbar_4 = Scrollbar(profit_frame,orient="vertical")
                    
                    pl_tree_4 = ttk.Treeview(pl_canvas, columns = (1,2), height = 6, show = "headings",style='mystyle112.Treeview',yscrollcommand=pl_scrollbar_4.set)
                    
                    pl_tree_4.column(1, width = 820)
                    pl_tree_4.column(2, width = 170)

                    window_label_4 = pl_canvas.create_window(0, 0, anchor="nw", window=pl_tree_4,tags=('pltree5'))

                    pl_scrollbar_4.config(command=pl_tree_4.yview)
                    pl_scrollbar_4.grid(row=0,column=2,sticky='ns')

                    inv_sql="select * from auth_user where username=%s"
                    inv_val=(nm_ent.get(),)
                    fbcursor.execute(inv_sql,inv_val,)
                    inv_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (inv_dtl[0],)
                    fbcursor.execute(sql, val,)
                    inv_dtls=fbcursor.fetchone()

                    c_sql_i1 = "SELECT * FROM app1_accounts1 where acctype=%s and cid_id=%s"
                    c_val_i1 = ('Other Expenses',inv_dtls[0],)
                    fbcursor.execute(c_sql_i1,c_val_i1,)
                    in_data_4 = fbcursor.fetchall()

                    count0 = 0
                    for i in in_data_4:
                        if True:
                            pl_tree_4.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                        else:
                            pass
                    count0 += 1

                    pl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("plhline10"))

                    label_1 = Label(pl_canvas,width=12,height=1,text="Total Expense", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel14"))

                    in_result_3 = Label(pl_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_in_result_3 = pl_canvas.create_window(0, 0, anchor="nw", window=in_result_3, tags=("pllabel19"))

                    
                    total_5 = 0.0
                    for child in pl_tree_4.get_children():
                        total_5 += float(pl_tree_4.item(child, 'values')[1])
                    in_result_3['text'] = '{}'.format(total_5)

                    pl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("plhline11"))

                    label_1 = Label(pl_canvas,width=14,height=1,text="PROFIT OR LOSS", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = pl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("pllabel15"))

                    in_result_4 = Label(pl_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_in_result_4 = pl_canvas.create_window(0, 0, anchor="nw", window=in_result_4, tags=("pllabel18"))

                    total = 0.0
                    total_1 = 0.0
                    total_3 = 0.0
                    total_4 = 0.0
                    total_5 = 0.0
                    total_6 = 0.0
                    total_7 = 0.0
                    total_8 = 0.0
                    for child in pl_tree.get_children():
                        total += float(pl_tree.item(child, 'values')[1])
                    for child in pl_tree_1.get_children():
                        total_1 += float(pl_tree_1.item(child, 'values')[1])
                    total_2 = total-total_1
                    for child in pl_tree_2.get_children():
                        total_3 += float(pl_tree_2.item(child, 'values')[1])
                    for child in pl_tree_3.get_children():
                        total_4 += float(pl_tree_3.item(child, 'values')[1])
                    for child in pl_tree_4.get_children():
                        total_5 += float(pl_tree_4.item(child, 'values')[1])
                    total_6 = total_2+total_3
                    total_7 = total_6-total_4
                    total_8 = total_7-total_5
                    in_result_4['text'] = '{}'.format(total_8)

                    pl_date_1=DateEntry(pl_canvas,width=40,justify=LEFT,foreground='white')
                    window_pl_date_1 = pl_canvas.create_window(0, 0, anchor="nw", height=30, window=pl_date_1,tags=('pldate1'),state=HIDDEN)

                    pl_date_2=DateEntry(pl_canvas,width=40,justify=LEFT,foreground='white')
                    window_pl_date_2 = pl_canvas.create_window(0, 0, anchor="nw", height=30, window=pl_date_2,tags=('pldate2'),state=HIDDEN)

                    #------------------------------------Balance Sheet---------------------------------#
                    tab6_2.grid_columnconfigure(0,weight=1)
                    tab6_2.grid_rowconfigure(0,weight=1)

                    balance_frame = Frame(tab6_2)
                    balance_frame.grid(row=0,column=0,sticky='nsew')

                    def balance_responsive_widgets(event):
                        try:
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget

                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("blpoly1",x1 + r1,y1,
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

                            dcanvas.coords("blhline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                            dcanvas.coords("bllabel1",dwidth/2.5,dheight/8.00)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/3
                            y21 = dheight/1.4


                            dcanvas.coords("blpoly2",x11 + r2,y11,
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
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/1.3
                            y21 = dheight/0.195


                            dcanvas.coords("blpoly3",x11 + r2,y11,
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

                            dcanvas.coords("bllabel2",dwidth/30,dheight/2.65)
                            dcanvas.coords("bllabel3",dwidth/3.4,dheight/2.65)
                            dcanvas.coords("bllabel4",dwidth/1.98,dheight/2.65)
                            dcanvas.coords("blcombo1",dwidth/20,dheight/2.3)
                            dcanvas.coords("blbutton1",dwidth/1.9,dheight/1.8)
                            dcanvas.coords("blbutton2",dwidth/1.45,dheight/1.8)

                            r2 = 25
                            x11 = dwidth/16
                            x21 = dwidth/1.07
                            y11 = dheight/1.15
                            y21 = dheight/0.2


                            dcanvas.coords("blpoly4",x11 + r2,y11,
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
                            x11 = dwidth/10
                            x21 = dwidth/1.12
                            y11 = dheight/1.05
                            y21 = dheight/0.8

                            dcanvas.coords("blpoly5",x11 + r2,y11,
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

                            dcanvas.coords("bllabel5",dwidth/4,dheight/0.87)
                            dcanvas.coords("blimage1",dwidth/6.5,dheight/0.88)
                            dcanvas.coords("blhline1",dwidth/10,dheight/0.7,dwidth/1.12,dheight/0.7)
                            dcanvas.coords("blhline2",dwidth/10,dheight/0.66,dwidth/1.12,dheight/0.66)
                            dcanvas.coords("bllabel6",dwidth/1.3,dheight/0.685)
                            dcanvas.coords("bllabel7",dwidth/8,dheight/0.645)
                            dcanvas.coords("bllabel8",dwidth/6.5,dheight/0.415)
                            dcanvas.coords("blhline4",dwidth/10,dheight/0.418,dwidth/1.12,dheight/0.418)
                            dcanvas.coords("blhline5",dwidth/10,dheight/0.405,dwidth/1.12,dheight/0.405)
                            dcanvas.coords("bllabel9",dwidth/7,dheight/0.63)
                            dcanvas.coords("bllabel10",dwidth/6,dheight/0.493)
                            dcanvas.coords("bllabel11",dwidth/7,dheight/0.512)
                            dcanvas.coords("blhline3",dwidth/10,dheight/0.52,dwidth/1.12,dheight/0.52)
                            dcanvas.coords("blhline6",dwidth/10,dheight/0.50,dwidth/1.12,dheight/0.50)
                            dcanvas.coords("bllabel12",dwidth/8,dheight/0.401)
                            dcanvas.coords("blhline7",dwidth/10,dheight/0.393,dwidth/1.12,dheight/0.393)
                            dcanvas.coords("blhline8",dwidth/10,dheight/0.388,dwidth/1.12,dheight/0.388)
                            dcanvas.coords("bllabel13",dwidth/9,dheight/0.383)
                            dcanvas.coords("bllabel14",dwidth/7,dheight/0.376)
                            dcanvas.coords("bllabel15",dwidth/6,dheight/0.317)
                            dcanvas.coords("blhline9",dwidth/10,dheight/0.329,dwidth/1.12,dheight/0.329)
                            dcanvas.coords("bllabel16",dwidth/6.5,dheight/0.281)
                            dcanvas.coords("blhline10",dwidth/10,dheight/0.321,dwidth/1.12,dheight/0.321)
                            dcanvas.coords("bllabel17",dwidth/8,dheight/0.326)
                            dcanvas.coords("blhline11",dwidth/10,dheight/0.283,dwidth/1.12,dheight/0.283)
                            dcanvas.coords("blhline12",dwidth/10,dheight/0.277,dwidth/1.12,dheight/0.277)
                            dcanvas.coords("bllabel18",dwidth/7,dheight/0.274)
                            dcanvas.coords("blhline13",dwidth/10,dheight/0.248,dwidth/1.12,dheight/0.248)
                            dcanvas.coords("blhline14",dwidth/10,dheight/0.243,dwidth/1.12,dheight/0.243)
                            dcanvas.coords("bllabel19",dwidth/7,dheight/0.2462)
                            dcanvas.coords("bllabel20",dwidth/10,dheight/0.242)

                            dcanvas.coords("bltree1",dwidth/6.5,dheight/0.613)
                            dcanvas.coords("bltree2",dwidth/5.7,dheight/0.482)
                            dcanvas.coords("bltree3",dwidth/5.8,dheight/0.368)
                            dcanvas.coords("bltree4",dwidth/5.7,dheight/0.31)
                            dcanvas.coords("bltree5",dwidth/6.5,dheight/0.269)

                            dcanvas.coords("bpllabel16",dwidth/1.3,dheight/0.512)
                            dcanvas.coords("bpllabel17",dwidth/1.3,dheight/0.415)
                            dcanvas.coords("bpllabel18",dwidth/1.3,dheight/0.401)
                            dcanvas.coords("bpllabel19",dwidth/1.3,dheight/0.326)
                            dcanvas.coords("bpllabel20",dwidth/1.3,dheight/0.281)
                            dcanvas.coords("bpllabel21",dwidth/1.3,dheight/0.2462)
                            dcanvas.coords("bpllabel22",dwidth/1.3,dheight/0.242)
                        except:
                            pass
                        try:
                            dcanvas.coords("bldate1",dwidth/3.4,dheight/2.3)
                            dcanvas.coords("bldate2",dwidth/1.97,dheight/2.3)
                        except:
                            pass


                    bl_canvas=Canvas(balance_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,3000))

                    balance_frame.grid_rowconfigure(0,weight=1)
                    balance_frame.grid_columnconfigure(0,weight=1)

                    vertibar=Scrollbar(balance_frame, orient=VERTICAL)
                    vertibar.grid(row=0,column=1,sticky='ns')
                    vertibar.config(command=bl_canvas.yview)
                    
                    bl_canvas.bind("<Configure>", balance_responsive_widgets)
                    bl_canvas.config(yscrollcommand=vertibar.set)
                    bl_canvas.grid(row=0,column=0,sticky='nsew')

                    
                    bl_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("blpoly1"))

                    label_1 = Label(bl_canvas,width=17,height=1,text="BALANCE SHEET", font=('arial 25'),background="#1b3857",fg="white") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel1"))

                    bl_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("blhline"))

                    bl_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("blpoly2"))

                    bl_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("blpoly3"))

                    label_1 = Label(bl_canvas,width=16,height=1,text="Report period", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel2"))

                    def custom_date_2(event):
                        if bl_comb_1.get() == 'Custom':
                            bl_canvas.itemconfig('bldate1',state='normal')
                            bl_canvas.itemconfig('bldate2',state='normal')
                            bl_canvas.itemconfig('bllabel3',state='normal')
                            bl_canvas.itemconfig('bllabel4',state='normal')
                        else:
                            bl_canvas.itemconfig('bldate1',state='hidden')
                            bl_canvas.itemconfig('bldate2',state='hidden')
                            bl_canvas.itemconfig('bllabel3',state='hidden')
                            bl_canvas.itemconfig('bllabel4',state='hidden')
                    
                    #--------Filter By Date------------#
                    def filterby_date_3():

                        if bl_comb_1.get() == 'All dates':

                            s_date = '2000-01-01'
                            e_date = '2050-01-01'

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (s_date,e_date,'Current Assets',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_1 = fbcursor.fetchall()

                            for record in bl_tree.get_children():
                                bl_tree.delete(record)

                            countd = 0
                            for i in bl_date_data_1:
                                bl_tree.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                for child in bl_tree.get_children():
                                    total += float(bl_tree.item(child, 'values')[1])
                                bl_result_1['text'] = '{}'.format(total)
                            except:
                                bl_result_1['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (s_date,e_date,'Account Receivable(Debtors)',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_2 = fbcursor.fetchall()

                            for record in bl_tree_1.get_children():
                                bl_tree_1.delete(record)

                            countd = 0
                            for i in bl_date_data_2:
                                bl_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total_1 = 0.0
                                for child in bl_tree_1.get_children():
                                    total_1 += float(bl_tree_1.item(child, 'values')[1])
                                bl_result_2['text'] = '{}'.format(total_1)
                            except:
                                bl_result_2['text'] = '{}'.format(0)

                            try:
                                total = 0.0
                                total_2 = 0.0
                                for child in bl_tree.get_children():
                                    total += float(bl_tree.item(child, 'values')[1])
                                total_1 = 0.0
                                for child in bl_tree_1.get_children():
                                    total_1 += float(bl_tree_1.item(child, 'values')[1])
                                total_2 = total+total_1
                                bl_result_3['text'] = '{}'.format(total_2)
                            except:
                                bl_result_3['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (s_date,e_date,'Current Liabilities',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_3 = fbcursor.fetchall()

                            for record in bl_tree_2.get_children():
                                bl_tree_2.delete(record)

                            countd = 0
                            for i in bl_date_data_3:
                                bl_tree_2.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_3 = 0.0
                                for child in bl_tree_2.get_children():
                                    total_3 += float(bl_tree_2.item(child, 'values')[1])
                                bl_result_4['text'] = '{}'.format(total_3)
                            except:
                                bl_result_4['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (s_date,e_date,'Accounts Payable(Creditors)',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_4 = fbcursor.fetchall()

                            for record in bl_tree_3.get_children():
                                bl_tree_3.delete(record)

                            countd = 0
                            for i in bl_date_data_4:
                                bl_tree_3.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_4 = 0.0
                                for child in bl_tree_3.get_children():
                                    total_4 += float(bl_tree_3.item(child, 'values')[1])
                                bl_result_5['text'] = '{}'.format(total_4)
                            except:
                                bl_result_5['text'] = '{}'.format(0)
                            
                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (s_date,e_date,'Equity',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_5 = fbcursor.fetchall()

                            for record in bl_tree_4.get_children():
                                bl_tree_4.delete(record)

                            countd = 0
                            for i in bl_date_data_5:
                                bl_tree_4.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_5 = 0.0
                                for child in bl_tree_4.get_children():
                                    total_5 += float(bl_tree_4.item(child, 'values')[1])
                                bl_result_6['text'] = '{}'.format(total_5)
                            except:
                                bl_result_6['text'] = '{}'.format(0)

                            try:
                                total_6 = 0.0
                                total_3 = 0.0
                                for child in bl_tree_2.get_children():
                                    total_3 += float(bl_tree_2.item(child, 'values')[1])
                                total_4 = 0.0
                                for child in bl_tree_3.get_children():
                                    total_4 += float(bl_tree_3.item(child, 'values')[1])
                                total_5 = 0.0
                                for child in bl_tree_4.get_children():
                                    total_5 += float(bl_tree_4.item(child, 'values')[1])
                                total_6 = total_3+total_4+total_5
                                bl_result_7['text'] = '{}'.format(total_6)
                            except:
                                bl_result_7['text'] = '{}'.format(0)

                        elif bl_comb_1.get() == 'Custom':

                            start_date = bl_date_1.get_date()
                            end_date = bl_date_2.get_date()

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (start_date,end_date,'Current Assets',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_1 = fbcursor.fetchall()

                            for record in bl_tree.get_children():
                                bl_tree.delete(record)

                            countd = 0
                            for i in bl_date_data_1:
                                bl_tree.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                for child in bl_tree.get_children():
                                    total += float(bl_tree.item(child, 'values')[1])
                                bl_result_1['text'] = '{}'.format(total)
                            except:
                                bl_result_1['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (start_date,end_date,'Account Receivable(Debtors)',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_2 = fbcursor.fetchall()

                            for record in bl_tree_1.get_children():
                                bl_tree_1.delete(record)

                            countd = 0
                            for i in bl_date_data_2:
                                bl_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total_1 = 0.0
                                for child in bl_tree_1.get_children():
                                    total_1 += float(bl_tree_1.item(child, 'values')[1])
                                bl_result_2['text'] = '{}'.format(total_1)
                            except:
                                bl_result_2['text'] = '{}'.format(0)

                            try:
                                total = 0.0
                                total_2 = 0.0
                                for child in bl_tree.get_children():
                                    total += float(bl_tree.item(child, 'values')[1])
                                total_1 = 0.0
                                for child in bl_tree_1.get_children():
                                    total_1 += float(bl_tree_1.item(child, 'values')[1])
                                total_2 = total+total_1
                                bl_result_3['text'] = '{}'.format(total_2)
                            except:
                                bl_result_3['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (start_date,end_date,'Current Liabilities',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_3 = fbcursor.fetchall()

                            for record in bl_tree_2.get_children():
                                bl_tree_2.delete(record)

                            countd = 0
                            for i in bl_date_data_3:
                                bl_tree_2.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_3 = 0.0
                                for child in bl_tree_2.get_children():
                                    total_3 += float(bl_tree_2.item(child, 'values')[1])
                                bl_result_4['text'] = '{}'.format(total_3)
                            except:
                                bl_result_4['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (start_date,end_date,'Accounts Payable(Creditors)',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_4 = fbcursor.fetchall()

                            for record in bl_tree_3.get_children():
                                bl_tree_3.delete(record)

                            countd = 0
                            for i in bl_date_data_4:
                                bl_tree_3.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_4 = 0.0
                                for child in bl_tree_3.get_children():
                                    total_4 += float(bl_tree_3.item(child, 'values')[1])
                                bl_result_5['text'] = '{}'.format(total_4)
                            except:
                                bl_result_5['text'] = '{}'.format(0)
                            
                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (start_date,end_date,'Equity',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_5 = fbcursor.fetchall()

                            for record in bl_tree_4.get_children():
                                bl_tree_4.delete(record)

                            countd = 0
                            for i in bl_date_data_5:
                                bl_tree_4.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_5 = 0.0
                                for child in bl_tree_4.get_children():
                                    total_5 += float(bl_tree_4.item(child, 'values')[1])
                                bl_result_6['text'] = '{}'.format(total_5)
                            except:
                                bl_result_6['text'] = '{}'.format(0)

                            try:
                                total_6 = 0.0
                                total_3 = 0.0
                                for child in bl_tree_2.get_children():
                                    total_3 += float(bl_tree_2.item(child, 'values')[1])
                                total_4 = 0.0
                                for child in bl_tree_3.get_children():
                                    total_4 += float(bl_tree_3.item(child, 'values')[1])
                                total_5 = 0.0
                                for child in bl_tree_4.get_children():
                                    total_5 += float(bl_tree_4.item(child, 'values')[1])
                                total_6 = total_3+total_4+total_5
                                bl_result_7['text'] = '{}'.format(total_6)
                            except:
                                bl_result_7['text'] = '{}'.format(0)

                        elif bl_comb_1.get() == 'Today':

                            today1 = date.today()
                            print("Today is: ", today1)

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof=%s AND acctype=%s and cid_id=%s"
                            date_val = (date.today(),'Current Assets',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_1 = fbcursor.fetchall()

                            for record in bl_tree.get_children():
                                bl_tree.delete(record)

                            countd = 0
                            for i in bl_date_data_1:
                                bl_tree.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                for child in bl_tree.get_children():
                                    total += float(bl_tree.item(child, 'values')[1])
                                bl_result_1['text'] = '{}'.format(total)
                            except:
                                bl_result_1['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof=%s AND acctype=%s and cid_id=%s"
                            date_val = (date.today(),'Account Receivable(Debtors)',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_2 = fbcursor.fetchall()

                            for record in bl_tree_1.get_children():
                                bl_tree_1.delete(record)

                            countd = 0
                            for i in bl_date_data_2:
                                bl_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total_1 = 0.0
                                for child in bl_tree_1.get_children():
                                    total_1 += float(bl_tree_1.item(child, 'values')[1])
                                bl_result_2['text'] = '{}'.format(total_1)
                            except:
                                bl_result_2['text'] = '{}'.format(0)

                            try:
                                total = 0.0
                                total_2 = 0.0
                                for child in bl_tree.get_children():
                                    total += float(bl_tree.item(child, 'values')[1])
                                total_1 = 0.0
                                for child in bl_tree_1.get_children():
                                    total_1 += float(bl_tree_1.item(child, 'values')[1])
                                total_2 = total+total_1
                                bl_result_3['text'] = '{}'.format(total_2)
                            except:
                                bl_result_3['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof=%s AND acctype=%s and cid_id=%s"
                            date_val = (date.today(),'Current Liabilities',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_3 = fbcursor.fetchall()

                            for record in bl_tree_2.get_children():
                                bl_tree_2.delete(record)

                            countd = 0
                            for i in bl_date_data_3:
                                bl_tree_2.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_3 = 0.0
                                for child in bl_tree_2.get_children():
                                    total_3 += float(bl_tree_2.item(child, 'values')[1])
                                bl_result_4['text'] = '{}'.format(total_3)
                            except:
                                bl_result_4['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof=%s AND acctype=%s and cid_id=%s"
                            date_val = (date.today(),'Accounts Payable(Creditors)',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_4 = fbcursor.fetchall()

                            for record in bl_tree_3.get_children():
                                bl_tree_3.delete(record)

                            countd = 0
                            for i in bl_date_data_4:
                                bl_tree_3.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_4 = 0.0
                                for child in bl_tree_3.get_children():
                                    total_4 += float(bl_tree_3.item(child, 'values')[1])
                                bl_result_5['text'] = '{}'.format(total_4)
                            except:
                                bl_result_5['text'] = '{}'.format(0)
                            
                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof=%s AND acctype=%s and cid_id=%s"
                            date_val = (date.today(),'Equity',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_5 = fbcursor.fetchall()

                            for record in bl_tree_4.get_children():
                                bl_tree_4.delete(record)

                            countd = 0
                            for i in bl_date_data_5:
                                bl_tree_4.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_5 = 0.0
                                for child in bl_tree_4.get_children():
                                    total_5 += float(bl_tree_4.item(child, 'values')[1])
                                bl_result_6['text'] = '{}'.format(total_5)
                            except:
                                bl_result_6['text'] = '{}'.format(0)

                            try:
                                total_6 = 0.0
                                total_3 = 0.0
                                for child in bl_tree_2.get_children():
                                    total_3 += float(bl_tree_2.item(child, 'values')[1])
                                total_4 = 0.0
                                for child in bl_tree_3.get_children():
                                    total_4 += float(bl_tree_3.item(child, 'values')[1])
                                total_5 = 0.0
                                for child in bl_tree_4.get_children():
                                    total_5 += float(bl_tree_4.item(child, 'values')[1])
                                total_6 = total_3+total_4+total_5
                                bl_result_7['text'] = '{}'.format(total_6)
                            except:
                                bl_result_7['text'] = '{}'.format(0)
                        
                        elif bl_comb_1.get() == 'This month':

                            today_gt2 = date.today()
                            firsty_gt2= today_gt2.replace(day=1)
                            last_monthy_gt2 = firsty_gt2 -relativedelta(day=1)

                            end_todayy_gt2 = last_monthy_gt2
                            end_firsty_gt2 = end_todayy_gt2.replace(day=1)
                            end_monthy_gt2 = end_firsty_gt2 -relativedelta(days=1)+relativedelta(months=1)

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (last_monthy_gt2,end_monthy_gt2,'Current Assets',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_1 = fbcursor.fetchall()

                            for record in bl_tree.get_children():
                                bl_tree.delete(record)

                            countd = 0
                            for i in bl_date_data_1:
                                bl_tree.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                for child in bl_tree.get_children():
                                    total += float(bl_tree.item(child, 'values')[1])
                                bl_result_1['text'] = '{}'.format(total)
                            except:
                                bl_result_1['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (last_monthy_gt2,end_monthy_gt2,'Account Receivable(Debtors)',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_2 = fbcursor.fetchall()

                            for record in bl_tree_1.get_children():
                                bl_tree_1.delete(record)

                            countd = 0
                            for i in bl_date_data_2:
                                bl_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total_1 = 0.0
                                for child in bl_tree_1.get_children():
                                    total_1 += float(bl_tree_1.item(child, 'values')[1])
                                bl_result_2['text'] = '{}'.format(total_1)
                            except:
                                bl_result_2['text'] = '{}'.format(0)

                            try:
                                total = 0.0
                                total_2 = 0.0
                                for child in bl_tree.get_children():
                                    total += float(bl_tree.item(child, 'values')[1])
                                total_1 = 0.0
                                for child in bl_tree_1.get_children():
                                    total_1 += float(bl_tree_1.item(child, 'values')[1])
                                total_2 = total+total_1
                                bl_result_3['text'] = '{}'.format(total_2)
                            except:
                                bl_result_3['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (last_monthy_gt2,end_monthy_gt2,'Current Liabilities',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_3 = fbcursor.fetchall()

                            for record in bl_tree_2.get_children():
                                bl_tree_2.delete(record)

                            countd = 0
                            for i in bl_date_data_3:
                                bl_tree_2.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_3 = 0.0
                                for child in bl_tree_2.get_children():
                                    total_3 += float(bl_tree_2.item(child, 'values')[1])
                                bl_result_4['text'] = '{}'.format(total_3)
                            except:
                                bl_result_4['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (last_monthy_gt2,end_monthy_gt2,'Accounts Payable(Creditors)',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_4 = fbcursor.fetchall()

                            for record in bl_tree_3.get_children():
                                bl_tree_3.delete(record)

                            countd = 0
                            for i in bl_date_data_4:
                                bl_tree_3.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_4 = 0.0
                                for child in bl_tree_3.get_children():
                                    total_4 += float(bl_tree_3.item(child, 'values')[1])
                                bl_result_5['text'] = '{}'.format(total_4)
                            except:
                                bl_result_5['text'] = '{}'.format(0)
                            
                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (last_monthy_gt2,end_monthy_gt2,'Equity',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_5 = fbcursor.fetchall()

                            for record in bl_tree_4.get_children():
                                bl_tree_4.delete(record)

                            countd = 0
                            for i in bl_date_data_5:
                                bl_tree_4.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_5 = 0.0
                                for child in bl_tree_4.get_children():
                                    total_5 += float(bl_tree_4.item(child, 'values')[1])
                                bl_result_6['text'] = '{}'.format(total_5)
                            except:
                                bl_result_6['text'] = '{}'.format(0)

                            try:
                                total_6 = 0.0
                                total_3 = 0.0
                                for child in bl_tree_2.get_children():
                                    total_3 += float(bl_tree_2.item(child, 'values')[1])
                                total_4 = 0.0
                                for child in bl_tree_3.get_children():
                                    total_4 += float(bl_tree_3.item(child, 'values')[1])
                                total_5 = 0.0
                                for child in bl_tree_4.get_children():
                                    total_5 += float(bl_tree_4.item(child, 'values')[1])
                                total_6 = total_3+total_4+total_5
                                bl_result_7['text'] = '{}'.format(total_6)
                            except:
                                bl_result_7['text'] = '{}'.format(0)

                        elif bl_comb_1.get() == 'This financial year':

                            fiscalyear.setup_fiscal_calendar(start_month=4)

                            first_fiscal_year = date.today().year + 1
                            print(first_fiscal_year)
                            current_fiscal_year = FiscalDate.today().fiscal_year

                            for x in range(0, 1):
                                fy = FiscalYear(first_fiscal_year + x)
                                fystart = fy.start.strftime("%Y-%m-%d")
                                fyend = fy.end.strftime("%Y-%m-%d")
                                print(fystart)
                                print(fyend)
                            
                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (fystart,fyend,'Current Assets',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_1 = fbcursor.fetchall()

                            for record in bl_tree.get_children():
                                bl_tree.delete(record)

                            countd = 0
                            for i in bl_date_data_1:
                                bl_tree.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total = 0.0
                                for child in bl_tree.get_children():
                                    total += float(bl_tree.item(child, 'values')[1])
                                bl_result_1['text'] = '{}'.format(total)
                            except:
                                bl_result_1['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (fystart,fyend,'Account Receivable(Debtors)',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_2 = fbcursor.fetchall()

                            for record in bl_tree_1.get_children():
                                bl_tree_1.delete(record)

                            countd = 0
                            for i in bl_date_data_2:
                                bl_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1  
                            try:
                                total_1 = 0.0
                                for child in bl_tree_1.get_children():
                                    total_1 += float(bl_tree_1.item(child, 'values')[1])
                                bl_result_2['text'] = '{}'.format(total_1)
                            except:
                                bl_result_2['text'] = '{}'.format(0)

                            try:
                                total = 0.0
                                total_2 = 0.0
                                for child in bl_tree.get_children():
                                    total += float(bl_tree.item(child, 'values')[1])
                                total_1 = 0.0
                                for child in bl_tree_1.get_children():
                                    total_1 += float(bl_tree_1.item(child, 'values')[1])
                                total_2 = total+total_1
                                bl_result_3['text'] = '{}'.format(total_2)
                            except:
                                bl_result_3['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (fystart,fyend,'Current Liabilities',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_3 = fbcursor.fetchall()

                            for record in bl_tree_2.get_children():
                                bl_tree_2.delete(record)

                            countd = 0
                            for i in bl_date_data_3:
                                bl_tree_2.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_3 = 0.0
                                for child in bl_tree_2.get_children():
                                    total_3 += float(bl_tree_2.item(child, 'values')[1])
                                bl_result_4['text'] = '{}'.format(total_3)
                            except:
                                bl_result_4['text'] = '{}'.format(0)

                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (fystart,fyend,'Accounts Payable(Creditors)',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_4 = fbcursor.fetchall()

                            for record in bl_tree_3.get_children():
                                bl_tree_3.delete(record)

                            countd = 0
                            for i in bl_date_data_4:
                                bl_tree_3.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_4 = 0.0
                                for child in bl_tree_3.get_children():
                                    total_4 += float(bl_tree_3.item(child, 'values')[1])
                                bl_result_5['text'] = '{}'.format(total_4)
                            except:
                                bl_result_5['text'] = '{}'.format(0)
                            
                            date_sql = "SELECT * FROM app1_accounts1 WHERE asof BETWEEN %s AND %s AND acctype=%s and cid_id=%s"
                            date_val = (fystart,fyend,'Equity',inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            bl_date_data_5 = fbcursor.fetchall()

                            for record in bl_tree_4.get_children():
                                bl_tree_4.delete(record)

                            countd = 0
                            for i in bl_date_data_5:
                                bl_tree_4.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                            countd += 1 
                            try:
                                total_5 = 0.0
                                for child in bl_tree_4.get_children():
                                    total_5 += float(bl_tree_4.item(child, 'values')[1])
                                bl_result_6['text'] = '{}'.format(total_5)
                            except:
                                bl_result_6['text'] = '{}'.format(0)

                            try:
                                total_6 = 0.0
                                total_3 = 0.0
                                for child in bl_tree_2.get_children():
                                    total_3 += float(bl_tree_2.item(child, 'values')[1])
                                total_4 = 0.0
                                for child in bl_tree_3.get_children():
                                    total_4 += float(bl_tree_3.item(child, 'values')[1])
                                total_5 = 0.0
                                for child in bl_tree_4.get_children():
                                    total_5 += float(bl_tree_4.item(child, 'values')[1])
                                total_6 = total_3+total_4+total_5
                                bl_result_7['text'] = '{}'.format(total_6)
                            except:
                                bl_result_7['text'] = '{}'.format(0)

                        else:
                            pass


                    bl_comb_1 = ttk.Combobox(bl_canvas,font=('arial 10'))
                    bl_comb_1['values'] = ("All dates","Custom","Today","This month","This financial year",)
                    bl_comb_1.current(0)
                    window_bl_comb_1 = bl_canvas.create_window(0, 0, anchor="nw", width=300,height=30,window=bl_comb_1,tags=('blcombo1'))
                    bl_comb_1.bind("<<ComboboxSelected>>",custom_date_2)

                    bl_btn_1=Button(bl_canvas,text='Run Report', width=20,height=1,foreground="white",background="#1b3857",font='arial 12',command=filterby_date_3)
                    window_bl_btn_1 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_btn_1,tags=('blbutton2'))

                    bl_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="white",tags=("blpoly4"))

                    bl_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#0d6e9e",tags=("blpoly5"))

                    usr_sql = "SELECT * FROM auth_user WHERE username=%s"
                    usr_val = (nm_ent.get(),)
                    fbcursor.execute(usr_sql,usr_val)
                    usr_data = fbcursor.fetchone()

                    cmp_sql = "SELECT * FROM app1_company WHERE id_id=%s"
                    cmp_val = (usr_data[0],)
                    fbcursor.execute(cmp_sql,cmp_val)
                    cmp_data = fbcursor.fetchone()

                    label_1 = Label(bl_canvas,width=14,height=1,text=cmp_data[1], font=('arial 18 bold'),background="#0d6e9e",fg="white") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel5"))

                    bl_image_1=Label(bl_canvas,  image = prof_pics,bg="#213b52",width=150,height=150,  anchor="center",font=('Calibri 14 bold'))
                    win_bl_image_1 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_image_1,tags=("blimage1"))

                    label_1 = Label(bl_canvas,width=5,height=1,text="From", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel3"),state=HIDDEN)

                    label_1 = Label(bl_canvas,width=3,height=1,text="To", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel4"),state=HIDDEN)

                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline1"))
                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=2,tags=("blhline2"))

                    label_1 = Label(bl_canvas,width=6,height=1,text="TOTAL", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel6"))

                    label_1 = Label(bl_canvas,width=6,height=1,text="Assets", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel7"))

                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("bl_canvas"))

                    label_1 = Label(bl_canvas,width=32,height=1,text="Total Account Receivable(Debtors)", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel8"))


                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline4"))
                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline5"))

                    label_1 = Label(bl_canvas,width=15,height=1,text="Current Assets", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel9"))

                    fgthdi = ttk.Style()
                    fgthdi.theme_use("default")
                    fgthdi.configure('mystyle113.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                    fgthdi.configure('mystyle113.Treeview.Heading', background='white',State='DISABLE',foreground='black')

                    bl_scrollbar = Scrollbar(balance_frame,orient="vertical")
                    
                    bl_tree = ttk.Treeview(bl_canvas, columns = (1,2), height = 5, show = "headings",style='mystyle113.Treeview',yscrollcommand=bl_scrollbar.set)
                    
                    bl_tree.column(1, width = 810)
                    bl_tree.column(2, width = 170)

                    window_label_4 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_tree,tags=('bltree1'))

                    bl_scrollbar.config(command=bl_tree.yview)
                    bl_scrollbar.grid(row=0,column=2,sticky='ns')

                    inv_sql="select * from auth_user where username=%s"
                    inv_val=(nm_ent.get(),)
                    fbcursor.execute(inv_sql,inv_val,)
                    inv_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (inv_dtl[0],)
                    fbcursor.execute(sql, val,)
                    inv_dtls=fbcursor.fetchone()

                    c_sql_i1 = "SELECT * FROM app1_accounts1 where acctype=%s and cid_id=%s"
                    c_val_i1 = ('Current Assets',inv_dtls[0],)
                    fbcursor.execute(c_sql_i1,c_val_i1,)
                    in_data_5 = fbcursor.fetchall()

                    count0 = 0
                    for i in in_data_5:
                        if True:
                            bl_tree.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                        else:
                            pass
                    count0 += 1


                    label_1 = Label(bl_canvas,width=25,height=1,text="Account Receivable(Debtors)", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel10"))

                    fgthdi = ttk.Style()
                    fgthdi.theme_use("default")
                    fgthdi.configure('mystyle114.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                    fgthdi.configure('mystyle114.Treeview.Heading', background='white',State='DISABLE',foreground='black')

                    bl_scrollbar_1 = Scrollbar(balance_frame,orient="vertical")
                    
                    bl_tree_1 = ttk.Treeview(bl_canvas, columns = (1,2), height = 6, show = "headings",style='mystyle114.Treeview',yscrollcommand=bl_scrollbar_1.set)
                    
                    bl_tree_1.column(1, width = 785)
                    bl_tree_1.column(2, width = 170)

                    window_label_4 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_tree_1,tags=('bltree2'))

                    bl_scrollbar_1.config(command=bl_tree_1.yview)
                    bl_scrollbar_1.grid(row=0,column=2,sticky='ns')

                    inv_sql="select * from auth_user where username=%s"
                    inv_val=(nm_ent.get(),)
                    fbcursor.execute(inv_sql,inv_val,)
                    inv_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (inv_dtl[0],)
                    fbcursor.execute(sql, val,)
                    inv_dtls=fbcursor.fetchone()

                    c_sql_i1 = "SELECT * FROM app1_accounts1 where acctype=%s and cid_id=%s"
                    c_val_i1 = ('Account Receivable(Debtors)',inv_dtls[0],)
                    fbcursor.execute(c_sql_i1,c_val_i1,)
                    in_data_5 = fbcursor.fetchall()

                    count0 = 0
                    for i in in_data_5:
                        if True:
                            bl_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                        else:
                            pass
                    count0 += 1

                    bl_result_2 = Label(bl_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_bl_result_2 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_result_2, tags=("bpllabel17"))

                    total_1 = 0.0
                    for child in bl_tree_1.get_children():
                        total_1 += float(bl_tree_1.item(child, 'values')[1])
                    bl_result_2['text'] = '{}'.format(total_1)

                    label_1 = Label(bl_canvas,width=20,height=1,text="Total Current Assets", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel11"))

                    bl_result_1 = Label(bl_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_bl_result_1 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_result_1, tags=("bpllabel16"))

                    total = 0.0
                    for child in bl_tree.get_children():
                        total += float(bl_tree.item(child, 'values')[1])
                    bl_result_1['text'] = '{}'.format(total)

                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline3"))
                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline6"))

                    label_1 = Label(bl_canvas,width=12,height=1,text="Total Assets", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel12"))

                    bl_result_3 = Label(bl_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_bl_result_3 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_result_3, tags=("bpllabel18"))

                    total = 0.0
                    total_2 = 0.0
                    for child in bl_tree.get_children():
                        total += float(bl_tree.item(child, 'values')[1])
                    total_1 = 0.0
                    for child in bl_tree_1.get_children():
                        total_1 += float(bl_tree_1.item(child, 'values')[1])
                    total_2 = total+total_1
                    bl_result_3['text'] = '{}'.format(total_2)

                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline7"))
                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline8"))

                    label_1 = Label(bl_canvas,width=22,height=1,text="Liabilities and Equity", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel13"))

                    label_1 = Label(bl_canvas,width=20,height=1,text="Current Liabilities", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel14"))

                    fgthdi = ttk.Style()
                    fgthdi.theme_use("default")
                    fgthdi.configure('mystyle115.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                    fgthdi.configure('mystyle115.Treeview.Heading', background='white',State='DISABLE',foreground='black')

                    bl_scrollbar_2 = Scrollbar(balance_frame,orient="vertical")
                    
                    bl_tree_2 = ttk.Treeview(bl_canvas, columns = (1,2), height = 6, show = "headings",style='mystyle115.Treeview',yscrollcommand=bl_scrollbar_2.set)
                    
                    bl_tree_2.column(1, width = 785)
                    bl_tree_2.column(2, width = 170)

                    window_label_4 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_tree_2,tags=('bltree3'))

                    bl_scrollbar_2.config(command=bl_tree_2.yview)
                    bl_scrollbar_2.grid(row=0,column=2,sticky='ns')

                    inv_sql="select * from auth_user where username=%s"
                    inv_val=(nm_ent.get(),)
                    fbcursor.execute(inv_sql,inv_val,)
                    inv_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (inv_dtl[0],)
                    fbcursor.execute(sql, val,)
                    inv_dtls=fbcursor.fetchone()

                    c_sql_i1 = "SELECT * FROM app1_accounts1 where acctype=%s and cid_id=%s"
                    c_val_i1 = ('Current Liabilities',inv_dtls[0],)
                    fbcursor.execute(c_sql_i1,c_val_i1,)
                    ap_data_5 = fbcursor.fetchall()

                    count0 = 0
                    for i in ap_data_5:
                        if True:
                            bl_tree_2.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                        else:
                            pass
                    count0 += 1

                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline9"))

                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline10"))

                    label_1 = Label(bl_canvas,width=27,height=1,text="Total Current Liabilities", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel17"))

                    bl_result_4 = Label(bl_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_bl_result_4 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_result_4, tags=("bpllabel19"))
 
                    total_3 = 0.0
                    for child in bl_tree_2.get_children():
                        total_3 += float(bl_tree_2.item(child, 'values')[1])
                    bl_result_4['text'] = '{}'.format(total_3)

                    label_1 = Label(bl_canvas,width=25,height=1,text="Account Payable(Creditors)", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel15"))

                    fgthdi = ttk.Style()
                    fgthdi.theme_use("default")
                    fgthdi.configure('mystyle116.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                    fgthdi.configure('mystyle116.Treeview.Heading', background='white',State='DISABLE',foreground='black')

                    bl_scrollbar_3 = Scrollbar(balance_frame,orient="vertical")
                    
                    bl_tree_3 = ttk.Treeview(bl_canvas, columns = (1,2), height = 6, show = "headings",style='mystyle116.Treeview',yscrollcommand=bl_scrollbar_3.set)
                    
                    bl_tree_3.column(1, width = 785)
                    bl_tree_3.column(2, width = 170)

                    window_label_4 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_tree_3,tags=('bltree4'))

                    bl_scrollbar_3.config(command=bl_tree_3.yview)
                    bl_scrollbar_3.grid(row=0,column=2,sticky='ns')

                    inv_sql="select * from auth_user where username=%s"
                    inv_val=(nm_ent.get(),)
                    fbcursor.execute(inv_sql,inv_val,)
                    inv_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (inv_dtl[0],)
                    fbcursor.execute(sql, val,)
                    inv_dtls=fbcursor.fetchone()

                    c_sql_i1 = "SELECT * FROM app1_accounts1 where acctype=%s and cid_id=%s"
                    c_val_i1 = ('Accounts Payable(Creditors)',inv_dtls[0],)
                    fbcursor.execute(c_sql_i1,c_val_i1,)
                    ap_data_6 = fbcursor.fetchall()

                    count0 = 0
                    for i in ap_data_6:
                        if True:
                            bl_tree_3.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                        else:
                            pass
                    count0 += 1  

                    label_1 = Label(bl_canvas,width=32,height=1,text="Total Account Payable(Creditors)", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel16"))

                    bl_result_5 = Label(bl_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_bl_result_5 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_result_5, tags=("bpllabel20"))
 
                    total_4 = 0.0
                    for child in bl_tree_3.get_children():
                        total_4 += float(bl_tree_3.item(child, 'values')[1])
                    bl_result_5['text'] = '{}'.format(total_4)

                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline11"))
                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline12"))

                    label_1 = Label(bl_canvas,width=8,height=1,text="Equity", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel18"))

                    fgthdi = ttk.Style()
                    fgthdi.theme_use("default")
                    fgthdi.configure('mystyle117.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                    fgthdi.configure('mystyle117.Treeview.Heading', background='white',State='DISABLE',foreground='black')

                    bl_scrollbar_4 = Scrollbar(balance_frame,orient="vertical")
                    
                    bl_tree_4 = ttk.Treeview(bl_canvas, columns = (1,2), height = 6, show = "headings",style='mystyle117.Treeview',yscrollcommand=bl_scrollbar_4.set)
                    
                    bl_tree_4.column(1, width = 805)
                    bl_tree_4.column(2, width = 170)

                    window_label_4 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_tree_4,tags=('bltree5'))

                    bl_scrollbar_4.config(command=bl_tree_4.yview)
                    bl_scrollbar_4.grid(row=0,column=2,sticky='ns')

                    inv_sql="select * from auth_user where username=%s"
                    inv_val=(nm_ent.get(),)
                    fbcursor.execute(inv_sql,inv_val,)
                    inv_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (inv_dtl[0],)
                    fbcursor.execute(sql, val,)
                    inv_dtls=fbcursor.fetchone()

                    c_sql_i1 = "SELECT * FROM app1_accounts1 where acctype=%s and cid_id=%s"
                    c_val_i1 = ('Equity',inv_dtls[0],)
                    fbcursor.execute(c_sql_i1,c_val_i1,)
                    ap_data_7 = fbcursor.fetchall()

                    count0 = 0
                    for i in ap_data_7:
                        if True:
                            bl_tree_4.insert(parent='',index='end',iid=i,text='',values=(i[3],i[7])) 
                        else:
                            pass
                    count0 += 1  

                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline13"))
                    bl_canvas.create_line(0,0,0,0,fill='#2f516f',width=1,tags=("blhline14"))

                    label_1 = Label(bl_canvas,width=13,height=1,text="Total Equity", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel19"))

                    bl_result_6 = Label(bl_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_bl_result_6 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_result_6, tags=("bpllabel21"))
 
                    total_5 = 0.0
                    for child in bl_tree_4.get_children():
                        total_5 += float(bl_tree_4.item(child, 'values')[1])
                    bl_result_6['text'] = '{}'.format(total_5)

                    label_1 = Label(bl_canvas,width=29,height=1,text="Total Liabilities and Equity", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = bl_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("bllabel20"))

                    bl_result_7 = Label(bl_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_bl_result_7 = bl_canvas.create_window(0, 0, anchor="nw", window=bl_result_7, tags=("bpllabel22"))

                    total_6 = 0.0
                    total_3 = 0.0
                    for child in bl_tree_2.get_children():
                        total_3 += float(bl_tree_2.item(child, 'values')[1])
                    total_4 = 0.0
                    for child in bl_tree_3.get_children():
                        total_4 += float(bl_tree_3.item(child, 'values')[1])
                    total_5 = 0.0
                    for child in bl_tree_4.get_children():
                        total_5 += float(bl_tree_4.item(child, 'values')[1])
                    total_6 = total_3+total_4+total_5
                    bl_result_7['text'] = '{}'.format(total_6)

                    bl_date_1=DateEntry(bl_canvas,width=40,justify=LEFT,foreground='white')
                    window_bl_date_1 = bl_canvas.create_window(0, 0, anchor="nw", height=30, window=bl_date_1,tags=('bldate1'),state=HIDDEN)

                    bl_date_2=DateEntry(bl_canvas,width=40,justify=LEFT,foreground='white')
                    window_bl_date_2 = bl_canvas.create_window(0, 0, anchor="nw", height=30, window=bl_date_2,tags=('bldate2'),state=HIDDEN)

                    #-----------------------------Accounts Receivables---------------------------------#
                    tab6_3.grid_columnconfigure(0,weight=1)
                    tab6_3.grid_rowconfigure(0,weight=1)

                    accountre_frame = Frame(tab6_3)
                    accountre_frame.grid(row=0,column=0,sticky='nsew')

                    def accountre_responsive_widgets(event):
                        try:
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget

                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("arpoly1",x1 + r1,y1,
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

                            dcanvas.coords("arhline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                            dcanvas.coords("arlabel1",dwidth/2.9,dheight/8.00)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/3
                            y21 = dheight/1.4


                            dcanvas.coords("arpoly2",x11 + r2,y11,
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
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/1.3
                            y21 = dheight/0.29


                            dcanvas.coords("arpoly3",x11 + r2,y11,
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

                            dcanvas.coords("arlabel2",dwidth/30,dheight/2.65)
                            dcanvas.coords("arlabel3",dwidth/3.4,dheight/2.65)
                            dcanvas.coords("arlabel4",dwidth/1.98,dheight/2.65)
                            dcanvas.coords("arcombo1",dwidth/20,dheight/2.3)
                            dcanvas.coords("arbutton1",dwidth/1.9,dheight/1.8)
                            dcanvas.coords("arbutton2",dwidth/1.45,dheight/1.8)

                            r2 = 25
                            x11 = dwidth/16
                            x21 = dwidth/1.07
                            y11 = dheight/1.15
                            y21 = dheight/0.3


                            dcanvas.coords("arpoly4",x11 + r2,y11,
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
                            x11 = dwidth/10
                            x21 = dwidth/1.12
                            y11 = dheight/1.05
                            y21 = dheight/0.8

                            dcanvas.coords("arpoly5",x11 + r2,y11,
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

                            dcanvas.coords("arlabel5",dwidth/4,dheight/0.87)
                            dcanvas.coords("arimage1",dwidth/6.5,dheight/0.88)
                            dcanvas.coords("artree1",dwidth/12,dheight/0.65)
                            dcanvas.coords("arhline1",dwidth/12,dheight/0.5,dwidth/1.09,dheight/0.5)
                            dcanvas.coords("arhline2",dwidth/12,dheight/0.48,dwidth/1.09,dheight/0.48)
                            dcanvas.coords("arlabel6",dwidth/10,dheight/0.493)
                            dcanvas.coords("arlabel7",dwidth/3.2,dheight/0.493)
                            dcanvas.coords("arlabel8",dwidth/1.24,dheight/0.493)
                        except:
                            pass
                        try:
                            dcanvas.coords("ardate1",dwidth/3.4,dheight/2.3)
                            dcanvas.coords("ardate2",dwidth/1.97,dheight/2.3)
                        except:
                            pass


                    ar_canvas=Canvas(accountre_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,2000))

                    accountre_frame.grid_rowconfigure(0,weight=1)
                    accountre_frame.grid_columnconfigure(0,weight=1)

                    vertibar=Scrollbar(accountre_frame, orient=VERTICAL)
                    vertibar.grid(row=0,column=1,sticky='ns')
                    vertibar.config(command=ar_canvas.yview)
                    
                    ar_canvas.bind("<Configure>", accountre_responsive_widgets)
                    ar_canvas.config(yscrollcommand=vertibar.set)
                    ar_canvas.grid(row=0,column=0,sticky='nsew')

                    
                    ar_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("arpoly1"))

                    label_1 = Label(ar_canvas,width=28,height=1,text="A/R AGEING SUMMARY REPORT", font=('arial 25'),background="#1b3857",fg="white") 
                    window_label_1 = ar_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("arlabel1"))

                    ar_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("arhline"))

                    ar_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("arpoly2"))

                    ar_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("arpoly3"))

                    label_1 = Label(ar_canvas,width=16,height=1,text="Report period", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_1 = ar_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("arlabel2"))

                    def custom_date_3(event):
                        if ar_comb_1.get() == 'Custom':
                            ar_canvas.itemconfig('ardate1',state='normal')
                            ar_canvas.itemconfig('ardate2',state='normal')
                            ar_canvas.itemconfig('arlabel3',state='normal')
                            ar_canvas.itemconfig('arlabel4',state='normal')    
                        else:
                            ar_canvas.itemconfig('ardate1',state='hidden')
                            ar_canvas.itemconfig('ardate2',state='hidden')
                            ar_canvas.itemconfig('arlabel3',state='hidden')
                            ar_canvas.itemconfig('arlabel4',state='hidden')

                    #--------Filter By Date------------#
                    def filterby_date():
                        if ar_comb_1.get() == 'All dates':

                            s_date = '2000-01-01'
                            e_date = '2050-01-01'

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_invoice WHERE invoicedate BETWEEN %s AND %s AND cid_id=%s"
                            date_val = (s_date,e_date,inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            date_data_2 = fbcursor.fetchall()

                            for record in ac_tree.get_children():
                                ac_tree.delete(record)

                            countd = 0
                            for i in date_data_2:
                                ac_tree.insert(parent='',index='end',iid=i,text='',values=(i[1],'Invoice Balance Due',i[41],'','','','',i[41]))
                            countd += 1  

                            try:
                                total = 0.0
                                for child in ac_tree.get_children():
                                    total += float(ac_tree.item(child, 'values')[7])
                                result_1['text'] = '{}'.format(total)
                                result_2['text'] = '{}'.format(total)
                            except:
                                result_1['text'] = '{}'.format(0)
                                result_2['text'] = '{}'.format(0)

                        elif ar_comb_1.get() == 'Custom':

                            start_date = ar_date_1.get_date()
                            end_date = ar_date_2.get_date()

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_invoice WHERE invoicedate BETWEEN %s AND %s AND cid_id=%s"
                            date_val = (start_date,end_date,inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            date_data = fbcursor.fetchall()

                            for record in ac_tree.get_children():
                                ac_tree.delete(record)

                            countd = 0
                            for i in date_data:
                                ac_tree.insert(parent='',index='end',iid=i,text='',values=(i[1],'Invoice Balance Due',i[41],'','','','',i[41]))
                            countd += 1  
                            try:
                                total = 0.0
                                for child in ac_tree.get_children():
                                    total += float(ac_tree.item(child, 'values')[7])
                                result_1['text'] = '{}'.format(total)
                                result_2['text'] = '{}'.format(total)
                            except:
                                result_1['text'] = '{}'.format(0)
                                result_2['text'] = '{}'.format(0)

                        elif ar_comb_1.get() == 'Today':

                            today1 = date.today()
                            print("Today is: ", today1)

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_invoice WHERE invoicedate=%s and cid_id=%s"
                            date_val = (date.today(),inv_dtls[0],)
                            fbcursor.execute(date_sql,date_val)
                            date_data_1 = fbcursor.fetchall()


                            for record in ac_tree.get_children():
                                ac_tree.delete(record)

                            countd = 0
                            for i in date_data_1:
                                ac_tree.insert(parent='',index='end',iid=i,text='',values=(i[1],'Invoice Balance Due',i[41],'','','','',i[41]))
                            countd += 1  

                            try:
                                total = 0.0
                                for child in ac_tree.get_children():
                                    total += float(ac_tree.item(child, 'values')[7])
                                result_1['text'] = '{}'.format(total)
                                result_2['text'] = '{}'.format(total)
                            except:
                                result_1['text'] = '{}'.format(0)
                                result_2['text'] = '{}'.format(0)

                        elif ar_comb_1.get() == 'This month':

                            today_gt2 = date.today()
                            firsty_gt2= today_gt2.replace(day=1)
                            last_monthy_gt2 = firsty_gt2 -relativedelta(day=1)

                            end_todayy_gt2 = last_monthy_gt2
                            end_firsty_gt2 = end_todayy_gt2.replace(day=1)
                            end_monthy_gt2 = end_firsty_gt2 -relativedelta(days=1)+relativedelta(months=1)

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_invoice WHERE invoicedate BETWEEN %s AND %s and cid_id=%s"
                            date_val = (last_monthy_gt2,end_monthy_gt2,inv_dtls[0],)
                            fbcursor.execute(date_sql,date_val)
                            date_data_3 = fbcursor.fetchall()


                            for record in ac_tree.get_children():
                                ac_tree.delete(record)

                            countd = 0
                            for i in date_data_3:
                                ac_tree.insert(parent='',index='end',iid=i,text='',values=(i[1],'Invoice Balance Due',i[41],'','','','',i[41]))
                            countd += 1  

                            try:
                                total = 0.0
                                for child in ac_tree.get_children():
                                    total += float(ac_tree.item(child, 'values')[7])
                                result_1['text'] = '{}'.format(total)
                                result_2['text'] = '{}'.format(total)
                            except:
                                result_1['text'] = '{}'.format(0)
                                result_2['text'] = '{}'.format(0)

                        elif ar_comb_1.get() == 'This financial year':

                            fiscalyear.setup_fiscal_calendar(start_month=4)

                            first_fiscal_year = date.today().year + 1
                            print(first_fiscal_year)
                            current_fiscal_year = FiscalDate.today().fiscal_year

                            for x in range(0, 1):
                                fy = FiscalYear(first_fiscal_year + x)
                                fystart = fy.start.strftime("%Y-%m-%d")
                                fyend = fy.end.strftime("%Y-%m-%d")
                                print(fystart)
                                print(fyend)

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_invoice WHERE invoicedate BETWEEN %s AND %s and cid_id=%s"
                            date_val = (fystart,fyend,inv_dtls[0],)
                            fbcursor.execute(date_sql,date_val)
                            date_data_3 = fbcursor.fetchall()


                            for record in ac_tree.get_children():
                                ac_tree.delete(record)

                            countd = 0
                            for i in date_data_3:
                                ac_tree.insert(parent='',index='end',iid=i,text='',values=(i[1],'Invoice Balance Due',i[41],'','','','',i[41]))
                            countd += 1  

                            try:
                                total = 0.0
                                for child in ac_tree.get_children():
                                    total += float(ac_tree.item(child, 'values')[7])
                                result_1['text'] = '{}'.format(total)
                                result_2['text'] = '{}'.format(total)
                            except:
                                result_1['text'] = '{}'.format(0)
                                result_2['text'] = '{}'.format(0)

                            
                        else:
                            pass

                    ar_comb_1 = ttk.Combobox(ar_canvas,font=('arial 10'))
                    ar_comb_1['values'] = ("All dates","Custom","Today","This month","This financial year",)
                    ar_comb_1.current(0)
                    window_ar_comb_1 = ar_canvas.create_window(0, 0, anchor="nw", width=300,height=30,window=ar_comb_1,tags=('arcombo1'))
                    ar_comb_1.bind("<<ComboboxSelected>>",custom_date_3)

                    ar_btn_1=Button(ar_canvas,text='Run Report', width=20,height=1,foreground="white",background="#1b3857",font='arial 12',command=filterby_date)
                    window_ar_btn_1 = ar_canvas.create_window(0, 0, anchor="nw", window=ar_btn_1,tags=('arbutton2'))

                    ar_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="white",tags=("arpoly4"))

                    ar_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#0d6e9e",tags=("arpoly5"))

                    usr_sql = "SELECT * FROM auth_user WHERE username=%s"
                    usr_val = (nm_ent.get(),)
                    fbcursor.execute(usr_sql,usr_val)
                    usr_data = fbcursor.fetchone()

                    cmp_sql = "SELECT * FROM app1_company WHERE id_id=%s"
                    cmp_val = (usr_data[0],)
                    fbcursor.execute(cmp_sql,cmp_val)
                    cmp_data = fbcursor.fetchone()

                    label_1 = Label(ar_canvas,width=14,height=1,text=cmp_data[1], font=('arial 18 bold'),background="#0d6e9e",fg="white") 
                    window_label_1 = ar_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("arlabel5"))

                    ar_image_1=Label(ar_canvas,  image = prof_pics,bg="#213b52",width=150,height=150,  anchor="center",font=('Calibri 14 bold'))
                    win_ar_image_1 = ar_canvas.create_window(0, 0, anchor="nw", window=ar_image_1,tags=("arimage1"))

                    label_1 = Label(ar_canvas,width=5,height=1,text="From", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_1 = ar_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("arlabel3"),state=HIDDEN)

                    label_1 = Label(ar_canvas,width=3,height=1,text="To", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_1 = ar_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("arlabel4"),state=HIDDEN)

                    fgthdi = ttk.Style()
                    fgthdi.theme_use("default")
                    fgthdi.configure('mystyle106.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                    fgthdi.configure('mystyle106.Treeview.Heading', background='white',State='DISABLE',foreground='black')

                    ar_scrollbar = Scrollbar(accountre_frame,orient="vertical")
                    
                    ac_tree = ttk.Treeview(ar_canvas, columns = (1,2,3,4,5,6,7,8), height = 10, show = "headings",style='mystyle106.Treeview',yscrollcommand=ar_scrollbar.set)
                    ac_tree.heading(1, text="CUSTOMER NAME")
                    ac_tree.heading(2, text="TRANSACTION TYPE")
                    ac_tree.heading(3, text="CURRENT")
                    ac_tree.heading(4, text="0-30")
                    ac_tree.heading(5, text="30-60")
                    ac_tree.heading(6, text="60-90")
                    ac_tree.heading(7, text="90 AND OVER")
                    ac_tree.heading(8, text="TOTAL")
                    
                    ac_tree.column(1, width = 150)
                    ac_tree.column(2, width = 150)
                    ac_tree.column(3, width = 150)
                    ac_tree.column(4, width = 130)
                    ac_tree.column(5, width = 130)
                    ac_tree.column(6, width = 130)
                    ac_tree.column(7, width = 130)
                    ac_tree.column(8, width = 130)

                    window_label_4 = ar_canvas.create_window(0, 0, anchor="nw", window=ac_tree,tags=('artree1'))

                    ar_scrollbar.config(command=ac_tree.yview)
                    ar_scrollbar.grid(row=0,column=2,sticky='ns')

                    inv_sql="select * from auth_user where username=%s"
                    inv_val=(nm_ent.get(),)
                    fbcursor.execute(inv_sql,inv_val,)
                    inv_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (inv_dtl[0],)
                    fbcursor.execute(sql, val,)
                    inv_dtls=fbcursor.fetchone()

                    c_sql_i1 = "SELECT * FROM app1_invoice where cid_id=%s"
                    c_val_i1 = (inv_dtls[0],)
                    fbcursor.execute(c_sql_i1,c_val_i1,)
                    c_data_i2 = fbcursor.fetchall()

                    count0 = 0
                    for i in c_data_i2:
                        if True:
                            ac_tree.insert(parent='',index='end',iid=i,text='',values=(i[1],'Invoice Balance Due',i[41],'','','','',i[41])) 
                        else:
                            pass
                    count0 += 1

                    ar_canvas.create_line(0,0,0,0,fill='black',width=1,tags=("arhline1"))
                    ar_canvas.create_line(0,0,0,0,fill='black',width=1,tags=("arhline2"))

                    label_1 = Label(ar_canvas,width=6,height=1,text="TOTAL", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = ar_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("arlabel6"))


                    result_1 = Label(ar_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_result_1 = ar_canvas.create_window(0, 0, anchor="nw", window=result_1, tags=("arlabel7"))

                    result_2 = Label(ar_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_result_2 = ar_canvas.create_window(0, 0, anchor="nw", window=result_2, tags=("arlabel8"))

                    total = 0.0
                    for child in ac_tree.get_children():
                        total += float(ac_tree.item(child, 'values')[7])
                    result_1['text'] = '{}'.format(total)
                    result_2['text'] = '{}'.format(total)

                    ar_date_1=DateEntry(ar_canvas,width=40,justify=LEFT,foreground='white')
                    window_ar_date_1 = ar_canvas.create_window(0, 0, anchor="nw", height=30, window=ar_date_1,tags=('ardate1'),state=HIDDEN)

                    ar_date_2=DateEntry(ar_canvas,width=40,justify=LEFT,foreground='white')
                    window_ar_date_2 = ar_canvas.create_window(0, 0, anchor="nw", height=30, window=ar_date_2,tags=('ardate2'),state=HIDDEN)

                    #-------------------------------Accounts Payables---------------------------------#
                    tab6_4.grid_columnconfigure(0,weight=1)
                    tab6_4.grid_rowconfigure(0,weight=1)

                    accountpay_frame = Frame(tab6_4)
                    accountpay_frame.grid(row=0,column=0,sticky='nsew')

                    def accountpay_responsive_widgets(event):
                        try:
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget

                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("aypoly1",x1 + r1,y1,
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

                            dcanvas.coords("ayhline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                            dcanvas.coords("aylabel1",dwidth/2.9,dheight/8.00)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/3
                            y21 = dheight/1.4


                            dcanvas.coords("aypoly2",x11 + r2,y11,
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
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/1.3
                            y21 = dheight/0.29


                            dcanvas.coords("aypoly3",x11 + r2,y11,
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

                            dcanvas.coords("aylabel2",dwidth/30,dheight/2.65)
                            dcanvas.coords("aylabel3",dwidth/3.4,dheight/2.65)
                            dcanvas.coords("aylabel4",dwidth/1.98,dheight/2.65)
                            dcanvas.coords("aycombo1",dwidth/20,dheight/2.3)
                            dcanvas.coords("aybutton1",dwidth/1.9,dheight/1.8)
                            dcanvas.coords("aybutton2",dwidth/1.45,dheight/1.8)

                            r2 = 25
                            x11 = dwidth/16
                            x21 = dwidth/1.07
                            y11 = dheight/1.15
                            y21 = dheight/0.3


                            dcanvas.coords("aypoly4",x11 + r2,y11,
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
                            x11 = dwidth/10
                            x21 = dwidth/1.12
                            y11 = dheight/1.05
                            y21 = dheight/0.8

                            dcanvas.coords("aypoly5",x11 + r2,y11,
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

                            dcanvas.coords("aylabel5",dwidth/4,dheight/0.87)
                            dcanvas.coords("ayimage1",dwidth/6.5,dheight/0.88)
                            dcanvas.coords("aytree1",dwidth/12,dheight/0.65)
                            dcanvas.coords("ayhline1",dwidth/12,dheight/0.495,dwidth/1.095,dheight/0.495)
                            dcanvas.coords("ayhline2",dwidth/12,dheight/0.479,dwidth/1.095,dheight/0.479)
                            dcanvas.coords("aylabel6",dwidth/10,dheight/0.49)
                            dcanvas.coords("aylabel7",dwidth/3.2,dheight/0.49)
                            dcanvas.coords("aylabel8",dwidth/1.24,dheight/0.49)
                        except:
                            pass
                        try:
                            dcanvas.coords("aydate1",dwidth/3.4,dheight/2.3)
                            dcanvas.coords("aydate2",dwidth/1.97,dheight/2.3)
                        except:
                            pass


                    ap_canvas=Canvas(accountpay_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,2000))

                    accountpay_frame.grid_rowconfigure(0,weight=1)
                    accountpay_frame.grid_columnconfigure(0,weight=1)

                    vertibar=Scrollbar(accountpay_frame, orient=VERTICAL)
                    vertibar.grid(row=0,column=1,sticky='ns')
                    vertibar.config(command=ap_canvas.yview)
                    
                    ap_canvas.bind("<Configure>", accountpay_responsive_widgets)
                    ap_canvas.config(yscrollcommand=vertibar.set)
                    ap_canvas.grid(row=0,column=0,sticky='nsew')

                    
                    ap_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aypoly1"))

                    label_1 = Label(ap_canvas,width=28,height=1,text="A/P AGEING SUMMARY REPORT", font=('arial 25'),background="#1b3857",fg="white") 
                    window_label_1 = ap_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("aylabel1"))

                    ap_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("ayhline"))

                    ap_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aypoly2"))

                    ap_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aypoly3"))

                    label_1 = Label(ap_canvas,width=16,height=1,text="Report period", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_1 = ap_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("aylabel2"))

                    def custom_date_4(event):
                        if ap_comb_1.get() == 'Custom':
                            ap_canvas.itemconfig('aydate1',state='normal')
                            ap_canvas.itemconfig('aydate2',state='normal')
                            ap_canvas.itemconfig('aylabel3',state='normal')
                            ap_canvas.itemconfig('aylabel4',state='normal')
                        else:
                            ap_canvas.itemconfig('aydate1',state='hidden')
                            ap_canvas.itemconfig('aydate2',state='hidden')
                            ap_canvas.itemconfig('aylabel3',state='hidden')
                            ap_canvas.itemconfig('aylabel4',state='hidden')

                    #--------Filter By Date------------#
                    def filterby_date_1():
                        if ap_comb_1.get() == 'All dates':

                            s_date = '2000-01-01'
                            e_date = '2050-01-01'

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_supplier WHERE effectivedate BETWEEN %s AND %s AND cid_id=%s"
                            date_val = (s_date,e_date,inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            ap_date_data_2 = fbcursor.fetchall()

                            for record in ap_tree.get_children():
                                ap_tree.delete(record)

                            count0 = 0
                            for i in ap_date_data_2:
                                
                                ap_tree.insert(parent='',index='end',iid=i,text='',values=(i[2]+" "+i[3],'Opening Balance',i[11],'','','','',i[11])) 
                                
                            count0 += 1 

                            try:
                                total = 0.0
                                for child in ap_tree.get_children():
                                    total += float(ap_tree.item(child, 'values')[7])
                                ap_result_1['text'] = '{}'.format(total)
                                ap_result_2['text'] = '{}'.format(total)
                            except:
                                ap_result_1['text'] = '{}'.format(0)
                                ap_result_2['text'] = '{}'.format(0)

                        elif ap_comb_1.get() == 'Custom':

                            start_date = ap_date_1.get_date()
                            end_date = ap_date_2.get_date()

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_supplier WHERE effectivedate BETWEEN %s AND %s AND cid_id=%s"
                            date_val = (start_date,end_date,inv_dtls[0])
                            fbcursor.execute(date_sql,date_val)
                            ap_date_data = fbcursor.fetchall()

                            for record in ap_tree.get_children():
                                ap_tree.delete(record)

                            countd = 0
                            for i in ap_date_data:
                                ap_tree.insert(parent='',index='end',iid=i,text='',values=(i[2]+" "+i[3],'Opening Balance',i[11],'','','','',i[11])) 
                            countd += 1  
                            try:
                                total = 0.0
                                for child in ap_tree.get_children():
                                    total += float(ap_tree.item(child, 'values')[7])
                                ap_result_1['text'] = '{}'.format(total)
                                ap_result_2['text'] = '{}'.format(total)
                            except:
                                ap_result_1['text'] = '{}'.format(0)
                                ap_result_2['text'] = '{}'.format(0)

                        elif ap_comb_1.get() == 'Today':

                            today1 = date.today()
                            print("Today is: ", today1)

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_supplier WHERE effectivedate=%s and cid_id=%s"
                            date_val = (date.today(),inv_dtls[0],)
                            fbcursor.execute(date_sql,date_val)
                            ap_date_data_1 = fbcursor.fetchall()


                            for record in ap_tree.get_children():
                                ap_tree.delete(record)

                            countd = 0
                            for i in ap_date_data_1:
                                ap_tree.insert(parent='',index='end',iid=i,text='',values=(i[2]+" "+i[3],'Opening Balance',i[11],'','','','',i[11])) 
                            countd += 1  

                            try:
                                total = 0.0
                                for child in ap_tree.get_children():
                                    total += float(ap_tree.item(child, 'values')[7])
                                ap_result_1['text'] = '{}'.format(total)
                                ap_result_2['text'] = '{}'.format(total)
                            except:
                                ap_result_1['text'] = '{}'.format(0)
                                ap_result_2['text'] = '{}'.format(0)
                        
                        elif ap_comb_1.get() == 'This month':

                            today_gt2 = date.today()
                            firsty_gt2= today_gt2.replace(day=1)
                            last_monthy_gt2 = firsty_gt2 -relativedelta(day=1)

                            end_todayy_gt2 = last_monthy_gt2
                            end_firsty_gt2 = end_todayy_gt2.replace(day=1)
                            end_monthy_gt2 = end_firsty_gt2 -relativedelta(days=1)+relativedelta(months=1)

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_supplier WHERE effectivedate BETWEEN %s AND %s and cid_id=%s"
                            date_val = (last_monthy_gt2,end_monthy_gt2,inv_dtls[0],)
                            fbcursor.execute(date_sql,date_val)
                            ap_date_data_3 = fbcursor.fetchall()

                            for record in ap_tree.get_children():
                                ap_tree.delete(record)

                            countd = 0
                            for i in ap_date_data_3:
                                ap_tree.insert(parent='',index='end',iid=i,text='',values=(i[2]+" "+i[3],'Opening Balance',i[11],'','','','',i[11]))
                            countd += 1  

                            try:
                                total = 0.0
                                for child in ap_tree.get_children():
                                    total += float(ap_tree.item(child, 'values')[7])
                                ap_result_1['text'] = '{}'.format(total)
                                ap_result_2['text'] = '{}'.format(total)
                            except:
                                ap_result_1['text'] = '{}'.format(0)
                                ap_result_2['text'] = '{}'.format(0)
                        elif ap_comb_1.get() == 'This financial year':

                            fiscalyear.setup_fiscal_calendar(start_month=4)

                            first_fiscal_year = date.today().year + 1
                            print(first_fiscal_year)
                            current_fiscal_year = FiscalDate.today().fiscal_year

                            for x in range(0, 1):
                                fy = FiscalYear(first_fiscal_year + x)
                                fystart = fy.start.strftime("%Y-%m-%d")
                                fyend = fy.end.strftime("%Y-%m-%d")
                                print(fystart)
                                print(fyend)

                            inv_sql="select * from auth_user where username=%s"
                            inv_val=(nm_ent.get(),)
                            fbcursor.execute(inv_sql,inv_val,)
                            inv_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (inv_dtl[0],)
                            fbcursor.execute(sql, val,)
                            inv_dtls=fbcursor.fetchone()

                            date_sql = "SELECT * FROM app1_supplier WHERE effectivedate BETWEEN %s AND %s and cid_id=%s"
                            date_val = (fystart,fyend,inv_dtls[0],)
                            fbcursor.execute(date_sql,date_val)
                            ap_date_data_3 = fbcursor.fetchall()

                            for record in ap_tree.get_children():
                                ap_tree.delete(record)

                            countd = 0
                            for i in ap_date_data_3:
                                ap_tree.insert(parent='',index='end',iid=i,text='',values=(i[2]+" "+i[3],'Opening Balance',i[11],'','','','',i[11]))
                            countd += 1  

                            try:
                                total = 0.0
                                for child in ap_tree.get_children():
                                    total += float(ap_tree.item(child, 'values')[7])
                                ap_result_1['text'] = '{}'.format(total)
                                ap_result_2['text'] = '{}'.format(total)
                            except:
                                ap_result_1['text'] = '{}'.format(0)
                                ap_result_2['text'] = '{}'.format(0)
 
                        else:
                            pass

                    ap_comb_1 = ttk.Combobox(ap_canvas,font=('arial 10'))
                    ap_comb_1['values'] = ("All dates","Custom","Today","This month","This financial year",)
                    ap_comb_1.current(0)
                    window_ap_comb_1 = ap_canvas.create_window(0, 0, anchor="nw", width=300,height=30,window=ap_comb_1,tags=('aycombo1'))
                    ap_comb_1.bind("<<ComboboxSelected>>",custom_date_4)

                    ay_btn_1=Button(ap_canvas,text='Run Report', width=20,height=1,foreground="white",background="#1b3857",font='arial 12',command=filterby_date_1)
                    window_ay_btn_1 = ap_canvas.create_window(0, 0, anchor="nw", window=ay_btn_1,tags=('aybutton2'))

                    ap_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="white",tags=("aypoly4"))

                    ap_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#0d6e9e",tags=("aypoly5"))

                    usr_sql = "SELECT * FROM auth_user WHERE username=%s"
                    usr_val = (nm_ent.get(),)
                    fbcursor.execute(usr_sql,usr_val)
                    usr_data = fbcursor.fetchone()

                    cmp_sql = "SELECT * FROM app1_company WHERE id_id=%s"
                    cmp_val = (usr_data[0],)
                    fbcursor.execute(cmp_sql,cmp_val)
                    cmp_data = fbcursor.fetchone()

                    label_1 = Label(ap_canvas,width=14,height=1,text=cmp_data[1], font=('arial 18 bold'),background="#0d6e9e",fg="white") 
                    window_label_1 = ap_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("aylabel5"))

                    ap_image_1=Label(ap_canvas,  image = prof_pics,bg="#213b52",width=150,height=150,  anchor="center",font=('Calibri 14 bold'))
                    win_ap_image_1 = ap_canvas.create_window(0, 0, anchor="nw", window=ap_image_1,tags=("ayimage1"))

                    label_1 = Label(ap_canvas,width=5,height=1,text="From", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_1 = ap_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("aylabel3"),state=HIDDEN)

                    label_1 = Label(ap_canvas,width=3,height=1,text="To", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_1 = ap_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("aylabel4"),state=HIDDEN)

                    fgthdi = ttk.Style()
                    fgthdi.theme_use("default")
                    fgthdi.configure('mystyle107.Treeview', background='white',State='DISABLE',foreground='black',fieldbackground='white',font=(None,11))
                    fgthdi.configure('mystyle107.Treeview.Heading', background='white',State='DISABLE',foreground='black')

                    ap_scrollbar = Scrollbar(accountpay_frame,orient="vertical")
                    
                    ap_tree = ttk.Treeview(ap_canvas, columns = (1,2,3,4,5,6,7,8), height = 10, show = "headings",style='mystyle107.Treeview',yscrollcommand=ap_scrollbar.set)
                    ap_tree.heading(1, text="CUSTOMER NAME")
                    ap_tree.heading(2, text="TRANSACTION TYPE")
                    ap_tree.heading(3, text="CURRENT")
                    ap_tree.heading(4, text="0-30")
                    ap_tree.heading(5, text="30-60")
                    ap_tree.heading(6, text="60-90")
                    ap_tree.heading(7, text="90 AND OVER")
                    ap_tree.heading(8, text="TOTAL")
                    
                    ap_tree.column(1, width = 150)
                    ap_tree.column(2, width = 150)
                    ap_tree.column(3, width = 150)
                    ap_tree.column(4, width = 130)
                    ap_tree.column(5, width = 130)
                    ap_tree.column(6, width = 130)
                    ap_tree.column(7, width = 130)
                    ap_tree.column(8, width = 135)

                    window_label_4 = ap_canvas.create_window(0, 0, anchor="nw", window=ap_tree,tags=('aytree1'))

                    ap_scrollbar.config(command=ap_tree.yview)
                    ap_scrollbar.grid(row=0,column=2,sticky='ns')

                    inv_sql="select * from auth_user where username=%s"
                    inv_val=(nm_ent.get(),)
                    fbcursor.execute(inv_sql,inv_val,)
                    inv_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (inv_dtl[0],)
                    fbcursor.execute(sql, val,)
                    inv_dtls=fbcursor.fetchone()

                    c_sql_i1 = "SELECT * FROM app1_supplier where cid_id=%s"
                    c_val_i1 = (inv_dtls[0],)
                    fbcursor.execute(c_sql_i1,c_val_i1,)
                    c_data_i3 = fbcursor.fetchall()

                    count0 = 0
                    for i in c_data_i3:
                        if True:
                            ap_tree.insert(parent='',index='end',iid=i,text='',values=(i[2]+" "+i[3],'Opening Balance',i[11],'','','','',i[11])) 
                        else:
                            pass
                    count0 += 1

                    
                    ap_canvas.create_line(0,0,0,0,fill='black',width=1,tags=("ayhline1"))
                    ap_canvas.create_line(0,0,0,0,fill='black',width=1,tags=("ayhline2"))

                    label_1 = Label(ap_canvas,width=6,height=1,text="TOTAL", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = ap_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("aylabel6"))

                    ap_result_1 = Label(ap_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_ap_result_1 = ap_canvas.create_window(0, 0, anchor="nw", window=ap_result_1, tags=("aylabel7"))

                    ap_result_2 = Label(ap_canvas, text='0',font=('arial 12 bold'),background="white",fg="black")
                    window_ap_result_2 = ap_canvas.create_window(0, 0, anchor="nw", window=ap_result_2, tags=("aylabel8"))

                    total = 0.0
                    for child in ap_tree.get_children():
                        total += float(ap_tree.item(child, 'values')[7])
                    ap_result_1['text'] = '{}'.format(total)
                    ap_result_2['text'] = '{}'.format(total)

                    ap_date_1=DateEntry(ap_canvas,width=40,justify=LEFT,foreground='white')
                    window_ap_date_1 = ap_canvas.create_window(0, 0, anchor="nw", height=30, window=ap_date_1,tags=('aydate1'),state=HIDDEN)

                    ap_date_2=DateEntry(ap_canvas,width=40,justify=LEFT,foreground='white')
                    window_ap_date_2 = ap_canvas.create_window(0, 0, anchor="nw", height=30, window=ap_date_2,tags=('aydate2'),state=HIDDEN)

