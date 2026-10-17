class User:

    def __init__(self, idDocument, name, email):
        self.set_idDocument(idDocument)
        self.name = name
        self.set_email(email)                                                           

    def get_idDocument(self):
        return self._idDocument

    def set_idDocument(self, idDocument):
        if(idDocument > 0):
            self._idDocument = idDocument
        else:
            raise ValueError("El documento no es valido")

    def get_email(self):
        return self._email

    def set_email(self, email):
        if(email != ""):
            self._email = email
        else:
            raise ValueError("El correo no puede estar vacío")

    def show_info(self):
        return f"Documento: {self.get_idDocument()} - Nombre: {self.name} - Correo: {self.get_email()}"