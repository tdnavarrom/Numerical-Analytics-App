from .MatrixMethods.view.matrix_view import Matrix_View
from .MatrixMethods.Gauss import Gauss
from .MatrixMethods.Pivoteo import Pivoteo
from .MatrixMethods.Pivoteo import Pivoteo
from .MatrixMethods.Crout import Crout
from .MatrixMethods.Doolittle import Doolittle
from .MatrixMethods.Cholesky import Cholesky
from .MatrixMethods.GaussSeidel import GaussSeidel
from .Messages.help import Help
from .Messages.errors import Errors
from .matrixTable import *

class EquationSystemHandler:

    def __init__(self, parameters):
        self.parameters = parameters
        self.help = Help()
        self.errors = Errors()

    def matrix_generate(self):
        rows = int(self.parameters2[0].get_text())
        columns = rows + 1
        tree = TreeView2(rows ,columns)
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()
        self.matrixTable = tree.returnTable()
        print(self.matrixTable.dtypes)
        self.matrixTable = self.matrixTable.to_numpy()
        self.matrixTable = self.matrixTable.astype(np.float)
        print(self.matrixTable)

    def initialValues_generate(self):
        columns = int(self.parameters2[2].get_text())
        rows = 1
        tree = TreeView2(rows ,columns)
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()
        self.initialValuesTable = tree.returnTable()
        print(self.initialValuesTable.dtypes)
        self.initialValuesTable = self.initialValuesTable.to_numpy()
        self.initialValuesTable = self.initialValuesTable.astype(np.float)
        print(self.initialValuesTable)


    def evaluate_gauss(self):
        self.etapa_index = 0

        print(f"Matriz\n{self.matrixTable}")
        matrixSize = self.matrixTable.shape[0]
        gauss = Gauss(self.matrixTable, matrixSize)
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

        print(self.x_result)
        print(self.etapas)

    def evaluate_pivot_parcial(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())
        pivot = Pivoteo(self.matrixTable,matrixSize)
        self.x_text,self.etapas = pivot.evaluate_parcial()

    def evaluate_pivot_total(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())

        pivot = Pivoteo(self.matrixTable,matrixSize)
        self.x_text,self.etapas = pivot.evaluate_total()

    def evaluate_crout(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        crout = Crout(matrix,matrixSize,indp)
        self.x_text,self.etapas = crout.evaluate()

    def evaluate_doolittle(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        doo = Doolittle(matrix,matrixSize,indp)
        self.L, self.U, self.Z, self.X = doo.evaluate()

    def evaluate_cholesky(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        chol = Cholesky(matrix,matrixSize,indp)
        self.L, self.U, self.Z, self.X = chol.evaluate()

    def evaluate_jacobi(self):
        matrixSize = int(self.parameters2[0].get_text())

        tol = float(self.parameters2[5].get_text())
        iter = int(self.parameters2[6].get_text())
        lamb = float(self.parameters2[7].get_text())

        initialValues = self.initialValuesTable
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        print(f"Indp: {indp}")
        seidel = GaussSeidel(matrix,matrixSize,indp,initialValues)
        seidel.evaluate(tol,iter,lamb)

    def evaluate_gauss_seidel(self):
        matrixSize = int(self.parameters2[0].get_text())

        tol = float(self.parameters2[5].get_text())
        iter = int(self.parameters2[6].get_text())
        lamb = float(self.parameters2[7].get_text())

        initialValues = self.initialValuesTable
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        print(f"Indp: {indp}")
        seidel = GaussSeidel(matrix,matrixSize,indp,initialValues)
        seidel.evaluate(tol,iter,lamb)
    
    def helpMatrix_pressed(self):
        method = self.parameters2[4].get_active()

        if method == 0:
            self.help.linear_equations_help("Simple Gaussian")
        elif method == 1:
            self.help.linear_equations_help("Parcial Pivot")
        elif method == 2:
            self.help.linear_equations_help("Total Pivot")
        elif method == 3:
            self.help.linear_equations_help("Crout")
        elif method == 4:
            self.help.linear_equations_help("Doolittle")
        elif method == 5:
            self.help.linear_equations_help("Cholesky")
        elif method == 6:
            self.help.linear_equations_help("Jacobi")
        elif method == 7:
            self.help.linear_equations_help("Gauss-Seidel")
