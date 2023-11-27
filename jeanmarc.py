import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QMessageBox 
from bd_tp import Ui_MainWindow

cnx = mysql.connector.connect(
            user='player', 
            password='qwerty',
            host='localhost',
            database='bd_tp')

class MainWindow(QMainWindow, Ui_MainWindow):
    id_personnage = 1
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        
        
        self.populate_combobox()
        self.populate_combobox_usager()

        self.creersauvgarde.clicked.connect(self.create_save)
        self.pushButton_2.clicked.connect(self.delete_save)
        self.pushButton_3.clicked.connect(self.initiate_save)
        self.btn_creation_utilisateur.clicked.connect(self.nouveau_usager)

    def populate_combobox(self):
        cursor = cnx.cursor()
        
        self.comboBox_11.clear()
        query_select = "SELECT id_sauvegarde, nom_sauvegarde FROM Sauvegarde"
        cursor.execute(query_select)
        saves_data = cursor.fetchall()

        for save in saves_data:
            self.comboBox_11.addItem(str(save[0]) + "- " + str(save[1]))
    def populate_combobox_usager(self):
        cursor = cnx.cursor()
        
        self.comboBox_2.clear()
        query_select = "SELECT nom FROM Utilisateur"
        cursor.execute(query_select)
        saves_data = cursor.fetchall()

        for save in saves_data:
            self.comboBox_2.addItem(str(save[0]))

    def create_save(self):
        cursor = cnx.cursor()

        query_insert = "INSERT INTO Sauvegarde (id_personnage,id_chapitre,nom_sauvegarde) VALUES (%s,%s,%s)"
        data = (1,1,self.lineEdit_2.text())
        cursor.execute(query_insert, data)

        cnx.commit()
        QMessageBox.information(self, "Partie sauvegarder", "Partie sauvegarder.")

        self.populate_combobox()

    def delete_save(self):
            cursor = cnx.cursor()
            selected_index = int(self.comboBox_11.currentText().split("-")[0])
            if selected_index == -1:
                return 

            query_delete = "DELETE FROM Sauvegarde WHERE id_sauvegarde = %s"
            data = (selected_index,)
            cursor.execute(query_delete, data)
            cnx.commit()

            self.comboBox_11.clear()
            self.populate_combobox()

            QMessageBox.information(self, "Sauvegarde effacer", "reussie.")

    def initiate_save(self):
        try:
            # Get the selected save ID from the combo box
            selected_index = self.comboBox_11.currentIndex()
            if selected_index == -1:
                return  # No save selected

            selected_save_id = self.comboBox_11.itemData(selected_index)

            # Insert the selected save into the "Progression" table
            query_insert_progression = "INSERT INTO Progression (id_sauvegarde) VALUES (%s)"
            data_progression = (selected_save_id,)
            self.cursor.execute(query_insert_progression, data_progression)
            self.cnx.commit()

            QMessageBox.information(self, "Initiate Save", "Save initiated in the Progression table.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def nouveau_usager(self):
        cursor = cnx.cursor()

        query_insert = "INSERT INTO Utilisateur (nom) VALUES (%s)"
        data = (self.lineEdit.text(),)
        cursor.execute(query_insert, data)

        cnx.commit()
        self.id_personnage = cursor.lastrowid
        self.populate_combobox_usager()
        QMessageBox.information(self, "Sauvegarde Usager réussie", "Sauvegarde Usager réussie.")

    

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()