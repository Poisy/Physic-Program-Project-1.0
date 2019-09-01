#------------------------------------------Imports------------------------------------------------------
from bin.Settings import *
import tkinter
import bin.f_elec


#---------------------------------------Functions------------------------------------------------------
def calculation():
    return root2.set(bin.f_elec.ohm_law(u_entry.get(), i_entry.get(), r_entry.get()))

def reset():
    return root2.set(''), r_entry.delete(0, tkinter.END), u_entry.delete(0, tkinter.END), i_entry.delete(0, tkinter.END)


#---------------------------------------The Window---------------------------------------------------
root = tkinter.Tk()
root.title(window_title)
root.configure(bg=window_background_color)
root.geometry("723x400+%d+%d" % ((root.winfo_screenwidth()/2-723/2), root.winfo_screenheight()/2-400/2))
root.resizable(width=False, height=False)

root2 = tkinter.StringVar()


#----------------------------------------The Frames---------------------------------------------------



#---------------------------------------The Objects---------------------------------------------------
#Main Label
main_label = tkinter.Label(root,
                           text=main_label_text,
                           fg=main_label_color, bg=default_bg,
                           font=main_label_font,
                           height=main_label_height,
                           )


#Result Label
result_label = tkinter.Label(root,
                       fg=default_fg, bg=default_bg,
                       font=result_label_font,
                       textvariable=root2,
                       )


#U Label
u_label = tkinter.Label(root,
                       text=u_label_text,
                       fg=default_fg, bg=default_bg,
                       font=u_i_r_font,
                       )


#I Label
i_label = tkinter.Label(root,
                        text=i_label_text,
                        fg=default_fg, bg=default_bg,
                        font=u_i_r_font,
                        )


#R Label
r_label = tkinter.Label(root,
                        text=r_label_text,
                        fg=default_fg, bg=default_bg,
                        font=u_i_r_font,
                        )


#Button Start
start_button = tkinter.Button(root,
                         text=start_button_text,
                         fg=default_fg, bg=button_bg,
                         bd=button_bd, relief=button_relief,
                         font=button_font,
                         width=button_width,
                         command=calculation,
                              )


#Button Reset
reset_button = tkinter.Button(root,
                              text=reset_button_text,
                              fg=default_fg, bg=button_bg,
                              bd=button_bd, relief=button_relief,
                              font=button_font,
                              width=button_width,
                              command=reset,
                              )


#U Entry
u_entry = tkinter.Entry(root,
                       )


#I Entry
i_entry = tkinter.Entry(root,
                       )


#R Entry
r_entry = tkinter.Entry(root,
                        )

#-------------------------------------------Place--------------------------------------------------------
#Main Label
main_label.place(x=main_label_place[0],
                 y=main_label_place[1],
                 )

#Result Label
result_label.place(x=result_label_place[0],
             y=result_label_place[1],
             anchor=tkinter.CENTER
                   )

#U Label
u_label.place(x=u_label_place[0],
             y=u_label_place[1],
             )

#I Label
i_label.place(x=i_label_place[0],
              y=i_label_place[1],
              )

#R Label
r_label.place(x=r_label_place[0],
              y=r_label_place[1],
              )

#Button Start
start_button.place(x=start_button_place[0],
                   y=start_button_place[1],
                   )

#Button Reset
reset_button.place(x=reset_button_place[0],
                   y=reset_button_place[1],
                   )

#U Entry
u_entry.place(x=u_entry_place[0],
              y=u_entry_place[1],
              )

#I Entry
i_entry.place(x=i_entry_place[0],
              y=i_entry_place[1],
              )

#R Entry
r_entry.place(x=r_entry_place[0],
              y=r_entry_place[1],
              )

#-----------------------------------------The end------------------------------------------------------
root.mainloop()
