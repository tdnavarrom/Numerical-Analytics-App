import gi
import numpy as np
from .methods.Gauss import Gauss
from .methods.Pivoteo import Pivoteo
from .methods.Crout import Crout
from .methods.Cholesky import Cholesky
from .methods.Doolittle import Doolittle
from .methods.GaussSeidel import GaussSeidel
from .methods.Jacobi import Jacobi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SysEqMenu(Gtk.Notebook):

    def __init__(self):
        """ Grid that contains basic UI Components for all System Equations"""
        self.grid = Gtk.Grid()
        self.grid.props.row_spacing = 15
        self.type_error = 1
        #self.matrix_grid = Gtk.Grid()
        self.etapa_index = 0
        self.m = 0
        self.entrygrid = Gtk.Grid()
        self.indp_grid = Gtk.Grid()
        self.vect_grid = Gtk.Grid()
        self.params_grid = Gtk.Grid()
        self.vect_box = Gtk.Box()
        self.entrybox = Gtk.Box()
        self.answerbox = Gtk.Box()
        self.etapabox = Gtk.Box()
        self.params_box = Gtk.Box()
        self.ui = self.create_ui()

    def m_entry(self):
        """
        Function Label and Entry at the bottom, with Evaluate Button.

        Returns:
            grid
            vbox
        """
        #grid = Gtk.Grid()
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.m_entry = Gtk.Entry()
        self.m_entry.set_placeholder_text("m")
        self.vbox.pack_start(self.m_entry, True, True, 0)
        self.grid.attach(self.vbox, 0, 0, 1, 1)
        self.grid.attach_next_to(self.entrybox,self.vbox,Gtk.PositionType.BOTTOM,10,10)
        self.grid.attach_next_to(self.vect_box,self.entrybox,Gtk.PositionType.BOTTOM,10,1)
        self.grid.attach_next_to(self.params_box,self.vect_box,Gtk.PositionType.BOTTOM,3,1)



    def gen_matrix_button(self):
        self.vbox2 = Gtk.Box(spacing=8)
        self.matrix_gen_button = Gtk.Button(label="Generar matriz")
        self.matrix_gen_button.connect('clicked', self.matrix_fields)
        self.vbox2.pack_start(self.matrix_gen_button, True, True, 0)

        self.grid.attach_next_to(self.vbox2, self.vbox, Gtk.PositionType.RIGHT, 1, 1)

    
    def matrix_fields(self, widget):
        self.entrygrid.destroy()
        self.indp_grid.destroy()
        self.vect_grid.destroy()
        self.params_grid.destroy()
        self.indp_grid = Gtk.Grid()
        self.entrygrid = Gtk.Grid()
        self.vect_grid = Gtk.Grid()
        #self.params_grid = Gtk.Grid()

       
        self.tol = Gtk.Entry()
        self.itera = Gtk.Entry()
        self.lamb = Gtk.Entry()
        self.tol.set_placeholder_text("Tolerancia")
        self.itera.set_placeholder_text("Iteraciones")
        self.lamb.set_placeholder_text("Lambda")
        self.params_grid.attach(self.tol,0,0,1,1)
        self.params_grid.attach(self.itera,1,0,1,1)
        self.params_grid.attach(self.lamb,2,0,1,1)
        self.params_box.pack_start(self.params_grid,True,True,0)


        for i in range(int(self.m_entry.get_text())):
            indp = Gtk.Entry()
            indp.set_placeholder_text(f"B{i}")
            self.indp_grid.attach(indp,0,i,1,1)

            vect = Gtk.Entry()
            vect.set_placeholder_text(f"V{i}")
            self.vect_grid.attach(vect,i,0,1,1)

            for j in range(int(self.m_entry.get_text())):
                entry = Gtk.Entry()
                entry.set_placeholder_text(f"x{j}")
                self.entrygrid.attach(entry,j,i,1,1)
        self.vect_box.pack_start(self.vect_grid,True,True,0)
        self.entrybox.pack_start(self.entrygrid, True, True, 0)
        self.entrybox.pack_start(self.indp_grid,True,True,0)

        self.entrybox.show_all()
        self.grid.show_all()
    
 
    def gen_matrix(self,widget):
        #self.entrygrid.hide()
        m = self.m_entry.get_text()

        for i in range(10):
            self.indp_grid.get_child_at(0,i).hide()
            for j in range(10):
                self.entrygrid.get_child_at(i,j).hide()

        for i in range(int(m)):
            self.indp_grid.get_child_at(0,i).show()
            for j in range(int(m)):
                self.entrygrid.get_child_at(i,j).show()
                

    
    def button_box(self):
        '''
        Box that contains all Buttons.
        '''
        self.buttonbox = Gtk.Box(spacing=8)
        self.Gaussbutton = Gtk.Button(label="Gauss method")
        self.Gaussbutton.connect('clicked', self.Eval_gauss)
        self.buttonbox.pack_start(self.Gaussbutton, True, True, 0)

        self.Pivotbutton = Gtk.Button(label="Total Pivot method")
        self.Pivotbutton.connect('clicked', self.Eval_pivot_total)
        self.buttonbox.pack_start(self.Pivotbutton, True, True, 0)

        self.Pivotparcialbutton = Gtk.Button(label="Partial Pivot method")
        self.Pivotparcialbutton.connect('clicked', self.Eval_pivot_parcial)
        self.buttonbox.pack_start(self.Pivotparcialbutton, True, True, 0)
        
        self.Croutbutton = Gtk.Button(label="Crout method")
        self.Croutbutton.connect('clicked', self.Eval_crout)
        self.buttonbox.pack_start(self.Croutbutton, True, True, 0)

        self.Cholbutton = Gtk.Button(label="Cholesky method")
        self.Cholbutton.connect('clicked', self.Eval_chol)
        self.buttonbox.pack_start(self.Cholbutton, True, True, 0)

        self.Doobutton = Gtk.Button(label="Doolittle method")
        self.Doobutton.connect('clicked', self.Eval_doo)
        self.buttonbox.pack_start(self.Doobutton, True, True, 0)

        self.Seidelbutton = Gtk.Button(label="Gauss Seidel method")
        self.Seidelbutton.connect('clicked', self.Eval_seidel)
        self.buttonbox.pack_start(self.Seidelbutton, True, True, 0)

        self.Jacobibutton = Gtk.Button(label="Jacobi method")
        self.Jacobibutton.connect('clicked', self.Eval_jacobi)
        self.buttonbox.pack_start(self.Jacobibutton, True, True, 0)

        self.grid.attach_next_to(self.buttonbox, self.params_box, Gtk.PositionType.BOTTOM, 7, 1)



    def answer_box(self):
        
        self.result = Gtk.TextView()
        self.resultbuffer = self.result.get_buffer()
        self.result.editable = False
        # self.scrolledwindow.add(self.textview)

        self.answerbox.pack_start(self.result, True, True, 0)

        self.grid.attach_next_to(self.answerbox, self.buttonbox, Gtk.PositionType.BOTTOM, 1, 1)


    def etapa_buttonbox(self):
        self.Etapabutton = Gtk.Button(label="Next Phase")
        self.Etapabutton.connect('clicked', self.next_etapa)
        self.etapabox.pack_start(self.Etapabutton, True, True, 0)

        self.grid.attach_next_to(self.etapabox, self.answerbox, Gtk.PositionType.BOTTOM, 1, 1)

    def next_etapa(self,widget):
        
        self.resultbuffer.set_text(self.x_text+f"\nEtapa {self.etapa_index +1}:\n{str(self.etapas[self.etapa_index])}")
        
        if self.etapa_index == len(self.etapas)-1:
            self.etapa_index = 0
        else:
            self.etapa_index+=1





    def Eval_gauss(self,widget):
        self.etapa_index = 0
        m = int(self.m_entry.get_text())
        matrix = np.empty([m,m+1])
        
        for i in range(m):
            matrix[i,m] = self.indp_grid.get_child_at(0,i).get_text()
            for j in range(m):
                matrix[i][j] = self.entrygrid.get_child_at(j,i).get_text()
    
        print(f"Matriz\n{matrix}")
        gauss = Gauss(matrix,m)
        self.x_result, self.etapas =gauss.evaluate()

        #CODIGO POPUP
        # self.etapas_text = ""
        # for i in range(len(x)-1):
        #     etapas_text+= f"Etapa {i}:\n {str(self.etapas[i])}\n\n"

        # etapas_popover = Gtk.Popover()
        # etapas_label = Gtk.Label(etapas_text)
        # etapas_popover.add(etapas_label)

        # etapas_popover.set_relative_to(self.Gaussbutton)
        # etapas_popover.show_all()
        # etapas_popover.popup()

        self.x_text = ""
        for i in range(len(self.x_result)):
            self.x_text+= f"X{i}: {self.x_result[i]}\n"

        self.resultbuffer.set_text(self.x_text)

    def Eval_pivot_total(self,widget):
        self.etapa_index = 0
        m = int(self.m_entry.get_text())
        matrix = np.empty([m,m+1])
        
        for i in range(m):
            matrix[i,m] = self.indp_grid.get_child_at(0,i).get_text()
            for j in range(m):
                matrix[i][j] = self.entrygrid.get_child_at(j,i).get_text()
        pivot = Pivoteo(matrix,m)
        self.x_text,self.etapas = pivot.evaluate_total()
        self.resultbuffer.set_text(self.x_text)


    def Eval_pivot_parcial(self,widget):
        self.etapa_index = 0
        m = int(self.m_entry.get_text())
        matrix = np.empty([m,m+1])
        
        for i in range(m):
            matrix[i,m] = self.indp_grid.get_child_at(0,i).get_text()
            for j in range(m):
                matrix[i][j] = self.entrygrid.get_child_at(j,i).get_text()
        pivot = Pivoteo(matrix,m)
        self.x_text,self.etapas = pivot.evaluate_parcial()
        self.resultbuffer.set_text(self.x_text)



    def Eval_crout(self,widget):
        self.etapa_index = 0
        m = int(self.m_entry.get_text())
        matrix = np.empty([m,m])
        indp = np.empty(m) 
        for i in range(m):
            indp[i] = self.indp_grid.get_child_at(0,i).get_text()
            for j in range(m):
                matrix[i][j] = self.entrygrid.get_child_at(j,i).get_text()

        print(f"matrix:\n {matrix}\n\nindp:\n{indp}")

        crout = Crout(matrix,m,indp)
        self.x_text,self.etapas = crout.evaluate()
        self.resultbuffer.set_text(self.x_text)

    def Eval_chol(self,widget):
        m = int(self.m_entry.get_text())
        matrix = np.empty([m,m])
        indp = np.empty(m) 
        for i in range(m):
            indp[i] = self.indp_grid.get_child_at(0,i).get_text()
            for j in range(m):
                matrix[i][j] = self.entrygrid.get_child_at(j,i).get_text()

        chol = Cholesky(matrix,m,indp)
        chol.evaluate()


    def Eval_doo(self,widget):
        m = int(self.m_entry.get_text())
        matrix = np.empty([m,m])
        indp = np.empty(m) 
        for i in range(m):
            indp[i] = self.indp_grid.get_child_at(0,i).get_text()
            for j in range(m):
                matrix[i][j] = self.entrygrid.get_child_at(j,i).get_text()

        doo = Doolittle(matrix,m,indp)
        doo.evaluate()
   

    def Eval_seidel(self,widget):
        m = int(self.m_entry.get_text())
        tol = float(self.tol.get_text())
        itera = int(self.itera.get_text())
        lamb = float(self.lamb.get_text())

        x0 = np.empty(m)

        for i in range(m):
            x0[i] = float(self.vect_grid.get_child_at(i,0).get_text())

        print("vector: "+str(x0))

        print(f"tol = {tol}")
       


        matrix = np.empty([m,m])
        indp = np.empty(m) 
        for i in range(m):
            indp[i] = self.indp_grid.get_child_at(0,i).get_text()
            for j in range(m):
                matrix[i][j] = self.entrygrid.get_child_at(j,i).get_text()

        print(f"Indp: {indp}")
        seidel = GaussSeidel(matrix,m,indp,x0)
        seidel.evaluate(tol,itera,lamb)

    def Eval_jacobi(self,widget):
        m = int(self.m_entry.get_text())
        tol = float(self.tol.get_text())
        itera = int(self.itera.get_text())
        lamb = float(self.lamb.get_text())

        x0 = np.empty(m)

        for i in range(m):
            x0[i] = float(self.vect_grid.get_child_at(i,0).get_text())

        print("vector: "+str(x0))

        print(f"tol = {tol}")


        matrix = np.empty([m,m])
        indp = np.empty(m) 
        for i in range(m):
            indp[i] = self.indp_grid.get_child_at(0,i).get_text()
            for j in range(m):
                matrix[i][j] = self.entrygrid.get_child_at(j,i).get_text()

        print(f"Indp: {indp}")
        seidel = GaussSeidel(matrix,m,indp,x0)
        seidel.evaluate(tol,itera,lamb)


    def create_ui(self):
        # entrybox = self.entrybox
        self.m_entry()
        self.gen_matrix_button()
        self.button_box()
        self.answer_box()
        self.etapa_buttonbox()
        
        return self.grid