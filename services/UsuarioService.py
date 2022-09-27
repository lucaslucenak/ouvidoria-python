from repositories import UsuarioRepository


class UsuarioService:
    usuarioRepository = UsuarioRepository.UsuarioRepository()

    # def __init__(self) -> None:
    #     super().__init__()

    def __int__(self):
        pass

    def findAllUsuarios(self):
        usuarios = self.usuarioRepository.findAllUsuarios()
        # self.usuarioRepository.closeCursorAndConnection()
        self.usuarioRepository.commit()
        return usuarios

    def findUsuarioById(self, id):
        usuario = self.usuarioRepository.findUsuarioById(id=id)
        # self.usuarioRepository.closeCursorAndConnection()
        self.usuarioRepository.commit()
        return usuario

    def saveUsuario(self, nome, usuario, senha):
        self.usuarioRepository.saveUsuario(nome=nome, usuario=usuario, senha=senha)
        # self.usuarioRepository.closeCursorAndConnection()
        self.usuarioRepository.commit()

    def deleteUsuarioById(self, id):
        self.usuarioRepository.deleteUsuarioById(id=id)
        # self.usuarioRepository.closeCursorAndConnection()
        self.usuarioRepository.commit()

    def deleteAllUsuarios(self):
        self.usuarioRepository.deleteAllUsuarios()
        # self.usuarioRepository.closeCursorAndConnection()
        self.usuarioRepository.commit()
