from gi.repository import Gtk, Gdk
from UI.MatrixMethods.view.table_j_s import Tree_View_J_S
from UI.MatrixMethods.view.matrix_view import Matrix_View
from UI.MatrixMethods.view.matrixTable import TreeView2
from UI.MatrixMethods.view.e1_view import Matrix_View2
from UI.MatrixMethods.Functions.GaussSeidel import GaussSeidel
from UI.MatrixMethods.Functions.Doolittle import Doolittle
from UI.MatrixMethods.Functions.Cholesky import Cholesky
from UI.MatrixMethods.Functions.Pivoteo import Pivoteo
from UI.MatrixMethods.Functions.Jacobi import Jacobi
from UI.MatrixMethods.Functions.Gauss import Gauss
from UI.MatrixMethods.Functions.Crout import Crout
from UI.MatrixMethods.Messages.errors import Errors
from UI.MatrixMethods.Messages.help import Help

#Importación de excepciones
from UI.MatrixMethods.Messages.errors import ZeroDeterminantException
from UI.MatrixMethods.Messages.errors import InvalidIterException
from UI.MatrixMethods.Messages.errors import InvalidToleranceException
from UI.MatrixMethods.Messages.errors import InvalidLambdaException
from UI.MatrixMethods.Messages.errors import NegativeRoot
from UI.MatrixMethods.Messages.errors import InvalidMatrix

import numpy as np
import gi
gi.require_version('Gtk', '3.0')


class Linear_Control:
    def __init__(self, parameters2):
        self.parameters2 = parameters2
        self.errors = Errors()
        self.help = Help()

    def matrix_generate_view(self):
        rows = self.parameters2[0].get_text()
        try:
            rows = int(rows)
            columns = rows + 1
            tree = TreeView2(rows, columns)
            tree.connect("destroy", Gtk.main_quit)
            tree.show_all()
            Gtk.main()
            self.matrixTable = tree.returnTable()
            self.matrixTable = self.matrixTable.to_numpy()
            self.matrixTable = self.matrixTable.astype(np.float)
        except:
            list_error = []
            if rows == '':
                list_error[0] = 1
            self.errors.lineal_errors(list_error)

    def initial_values_view(self):
        columns = int(self.parameters2[2].get_text())
        rows = 1
        tree = TreeView2(rows, columns)
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()
        self.initialValuesTable = tree.returnTable()
        self.initialValuesTable = self.initialValuesTable.to_numpy()
        self.initialValuesTable = self.initialValuesTable.astype(np.float)

    def evaluate_gauss(self):
        try:
            #Method
            etapa_index = 0
            matrixSize = self.matrixTable.shape[0]
            gauss = Gauss(self.matrixTable, matrixSize)
            answer = gauss.evaluate()
            x_result = gauss.x
            etapas = gauss.etapas

            #View
            matrix_gui = Matrix_View(x_result, etapas, self.matrixTable)
            Gtk.main()
        except ZeroDivisionError:
            self.errors.div_0()

    def evaluate_pivot_parcial(self):
        try:
            #Method
            etapa_index = 0
            matrixSize = int(self.parameters2[0].get_text())
            pivot = Pivoteo(self.matrixTable, matrixSize)
            x_result, etapas = pivot.evaluate_parcial()
            etapas = pivot.etapas

            #View
            matrix_gui = Matrix_View(x_result, etapas, self.matrixTable)
            Gtk.main()
        except ZeroDivisionError:
            self.errors.div_0()

    def evaluate_pivot_total(self):
        try:
            #Method
            etapa_index = 0
            matrixSize = int(self.parameters2[0].get_text())
            pivot = Pivoteo(self.matrixTable, matrixSize)
            x_result, etapas = pivot.evaluate_total()

            #View
            matrix_gui = Matrix_View(x_result, etapas, self.matrixTable)
            Gtk.main()
        except ZeroDivisionError:
            self.errors.div_0()

    def evaluate_crout(self):
        try:
            #Method
            etapa_index = 0
            matrixSize = int(self.parameters2[0].get_text())
            matrix = self.matrixTable[:, :(matrixSize)]
            indp = self.matrixTable[:, -1]
            crout = Crout(matrix, matrixSize, indp)
            x_result, etapas = crout.evaluate()
            matrix_u = crout.U
            matrix_l = crout.L
            vector_z = crout.z

            #View
            matrix_gui2 = Matrix_View2(matrix_l, matrix_u, vector_z, x_result)
            Gtk.main()
        except(ZeroDeterminantException):
            self.errors.determinante_0()

    def evaluate_doolittle(self):
        try:
            #Method
            etapa_index = 0
            matrixSize = int(self.parameters2[0].get_text())
            matrix = self.matrixTable[:, :(matrixSize)]
            indp = self.matrixTable[:, -1]
            doo = Doolittle(matrix, matrixSize, indp)
            matrix_l, matrix_u, vector_z, x_result = doo.evaluate()

            #View
            matrix_gui2 = Matrix_View2(matrix_l, matrix_u, vector_z, x_result)
            Gtk.main()
        except(ZeroDivisionError):
            self.errors.div_0()
        except(ZeroDeterminantException):
            self.errors.determinante_0()

    def evaluate_cholesky(self):
        try:
            #Method
            etapa_index = 0
            matrixSize = int(self.parameters2[0].get_text())
            matrix = self.matrixTable[:, :(matrixSize)]
            indp = self.matrixTable[:, -1]
            chol = Cholesky(matrix, matrixSize, indp)
            matrix_l, matrix_u, vector_z, x_result = chol.evaluate()

            #View
            matrix_gui2 = Matrix_View2(matrix_l, matrix_u, vector_z, x_result)
            Gtk.main()
        except(ZeroDivisionError):
            self.errors.div_0()
        except(ZeroDeterminantException):
            self.errors.determinante_0()
        except(NegativeRoot):
            self.errors.negativeRoot()

    def evaluate_jacobi(self):
        try:
            #Method
            matrixSize = int(self.parameters2[0].get_text())
            tol = float(self.parameters2[5].get_text())
            itera = int(self.parameters2[6].get_text())
            lamb = float(self.parameters2[7].get_text())
            initialValues = self.initialValuesTable
            matrix = self.matrixTable[:, :(matrixSize)]
            indp = self.matrixTable[:, -1]
            jacobi = Jacobi(matrix, matrixSize, indp, initialValues)
            message = jacobi.evaluate(tol, itera, lamb)
            table_values = jacobi.tabla_values()
            self.parameters2[8].set_text(str(message))
            cont = [int(table_values[x][0]) for x in range(len(table_values))]
            values = [list(table_values[x][1]) for x in range(len(table_values))]
            error = [float(table_values[x][2]) for x in range(len(table_values))]
            final_result = []
            for i in range(len(table_values)):
                temp_values = values[i]
                temp_array = []
                temp_array.append(cont[i])
                for j in range(len(temp_values)):
                    temp_array.append(temp_values[j])
                temp_array.append(error[i])
                final_result.append(temp_array)

            #View
            tree = Tree_View_J_S(final_result)
            tree.connect("destroy", Gtk.main_quit)
            tree.show_all()
            Gtk.main()

        except(ZeroDivisionError):
            self.errors.div_0()
        except(InvalidToleranceException):
            self.errors.invalidTol()
        except(InvalidLambdaException):
            self.errors.invalidLambda
        except(InvalidIterException):
            self.erros.invalidIter()
        except(InvalidMatrix):
            self.errors.invalidMatrix()

    def evaluate_gauss_seidel(self):
        try:
            #Method
            matrixSize = int(self.parameters2[0].get_text())
            tol = float(self.parameters2[5].get_text())
            itera = float(self.parameters2[6].get_text())
            lamb = float(self.parameters2[7].get_text())
            initialValues = self.initialValuesTable
            matrix = self.matrixTable[:, :(matrixSize)]
            indp = self.matrixTable[:, -1]
            seidel = GaussSeidel(matrix, matrixSize, indp, initialValues)
            message = seidel.evaluate(tol, itera, lamb)
            table_values = seidel.table_values()
            self.parameters2[8].set_text(str(message))

            cont = [int(table_values[x][0]) for x in range(len(table_values))]
            values = [list(table_values[x][1])for x in range(len(table_values))]
            error = [float(table_values[x][2])for x in range(len(table_values))]
            final_result = []
            for i in range(len(table_values)):
                temp_values = values[i]
                temp_array = []
                temp_array.append(cont[i])
                for j in range(len(temp_values)):
                    temp_array.append(temp_values[j])
                temp_array.append(error[i])
                final_result.append(temp_array)

            #View
            tree = Tree_View_J_S(final_result)
            tree.connect("destroy", Gtk.main_quit)
            tree.show_all()
            Gtk.main()
            

        except(ZeroDivisionError):
            self.errors.div_0()
        except(InvalidToleranceException):
            self.errors.invalidTol()
        except(InvalidLambdaException):
            self.errors.invalidLambda
        except(InvalidIterException):
            self.errors.invalidIter()
        except(InvalidMatrix):
            self.errors.invalidMatrix()

    def helpMatrix_view(self):
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
