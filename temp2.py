import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# root window
root = tk.Tk()
root.title('Controller Detector')
root.geometry('400x300')
root.resizable(False, False)

# frame
frame = ttk.Frame(root)


# field options
options = {'padx': 5, 'pady': 5}

# Target ip address label
target_label = ttk.Label(frame, text='Target IP address')
target_label.grid(column=0, row=0, sticky='W', **options)

# # port label
# port_label = ttk.Label(frame, text='Port number')
# port_label.grid(column=0, row=1, sticky='W', **options)


# target_ip entry
target_ip = tk.StringVar()
target_ip_entry = ttk.Entry(frame, textvariable=target_ip)
target_ip_entry.grid(column=1, row=0, **options)
target_ip_entry.focus()

# # port entry
# port = tk.StringVar()
# port_entry = ttk.Entry(frame, textvariable=port)
# port_entry.grid(column=1, row=1, **options)
# port_entry.focus()

# submit  button


def submit_button_clicked():
    """  Handle submit button click event
    """
    try:
        t = str(target_ip.get())
        # po = str(port.get())
        result = f'The target ip address {t} '  #and the port number is  {p} '
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)


submit_button = ttk.Button(frame, text='submit')
submit_button.grid(column=2, row=1, sticky='W', **options)
submit_button.configure(command=submit_button_clicked)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)

#check the controller 

def Checkcontroller(t,po):
 # defaultGuiPorts = {"Floodlight & OpenDayLight": 8080, "OpenDayLight (DLUX Standalone)": 9000, "OpenDayLight (DLUX w/t Karaf) & ONOS": 8181}
 defaultGuiURLs = {"Floodlight": "/ui/index.html", "OpenDayLight (DLUX)": "/dlux/index.html", "OpenDayLight (Hydrogen)": "/index.html", "ONOS": "/onos/ui/login.html"}
 guiIdentifiers = {}
 verbose = False
 
 target = t # 
 target_message = f"Testing visibility of northbound interface on host{target} "
 tm_label.config(text=target_message)

 for u in defaultGuiURLs:
        try:
            conn = httpc.HTTPConnection(target)
            conn.request("GET", defaultGuiURLs[u])
            res = conn.getresponse()
            reqStatus = res.status
            if(reqStatus >= 200 and reqStatus < 400):
              rs_message = "Got {reqStatus} for {defaultGuiURLs[u]}"
              rs_label.config(text=rs_message) 
              ug_message = "URL associated with {u} GUI interface"
              ug_label.config(text=ug_message) 
            else:
              if(verbose == True):
                sg_message=(f'Got sheet{reqStatus}for URL {u}')
                sg_label.config(text=sg_message)
        except Exception as e:
              if(verbose == True):
                error_message=(f'Error testing URL: {e}')
                error_label.config(text=error_message)
 print("")
           




# start the app
root.mainloop()