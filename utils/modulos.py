from tkinter import *
from pathlib import Path
base_dir = Path(__file__).resolve().parent.parent
from time import localtime, sleep
from tkcalendar import Calendar
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from random import randint
from models.banco import *
from models.calendario import Calendario
from models.principal import Principal
from models.add_advogado import AddAdvogado
from models.ocorrencias import Ocorrencias
from models.pesquisar import Pesquisar
from models.consultas import Consultas
from models.processos import Processos
