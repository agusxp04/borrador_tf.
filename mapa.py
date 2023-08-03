#Mapa y planificador de rutas
import tkinter
from tkintermapview from TkinterMapView
import tkintermapview as mapa
import customtkinter as ctk

class VistaMapa(ctk.CTkFrame):
  def __init__(self, master=None, controlador=None):
    super().__init__(master)
    self.master = master
    self.controlador = controlador
    self.ubicaciones = ()

    #ventana mapa
    self.mapa = mapa.TkinterMapView(self, width=800, height=600, corner_radius=15)
    self.mapa.pack (pady=10, padx=10)
    map_widget.pack(fill="both", espand=True)

    self.mapa.set_position(-24.7859, -65.41166, marker= True) #Salta, Argentina
    self.mapa.set_zoom(15)

 def crear_mapa (self):
   evento_seleccionado = self.controlador.ubicación_seleccionadada
   self.mapa.set_position (evento_seleccionado.latitud, evento_seleccionado.longitud)
   sel.mapa.set.marker (evento_seleccionado.latitud, evento_seleccionado.longitud)

    ubicaciones = ctk.CTkButton(
        self,
        text="Volver a Ubicaciones",
        corner_radius=15)
        .pack (pady=10, padx=10)
        
    add = ctk.CTkButton(
        self,
        text="Añadir ubicación",
        corner_radius=15)
        .pack(pady=10, padx=10)
    

  

