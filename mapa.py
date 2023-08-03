#Mapa y planificador de rutas
import tkinter
from tkintermapview from TkinterMapView
import tkintermapview as mapa
import customtkinter as ctk

root_tk = tkinter.Tk()
root_tk.geometry("800x600")
root_tk.tittle("Google Maps")

map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
map_widget.pack(fill="both", espand=True)

map_widget.set_position(-24.7859, -65.41166) #Salta, Argentina
map_widget.set_zoom(15)

map_widget.set_address("Capital, Salta, Argentina")

map_widget.set_tile_server(

root_tk.mainloop()
