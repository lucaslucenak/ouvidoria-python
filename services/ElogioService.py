from repositories import ElogioRepository


class UsuarioService:
    elogioRepository = ElogioRepository.ElogioRepository()

    # def __init__(self) -> None:
    #     super().__init__()

    def __int__(self):
        pass

    def findAllElogios(self):
        usuarios = self.elogioRepository.findAllElogios()
        # self.usuarioRepository.closeCursorAndConnection()
        self.elogioRepository.commit()
        return usuarios

    def findUsuarioById(self, id):
        usuario = self.elogioRepository.findElogioById(id=id)
        # self.usuarioRepository.closeCursorAndConnection()
        self.elogioRepository.commit()
        return usuario

    def saveUsuario(self, elogio):
        self.elogioRepository.saveElogio(elogio=elogio)
        # self.usuarioRepository.closeCursorAndConnection()
        self.elogioRepository.commit()

    def deleteUsuarioById(self, id):
        self.elogioRepository.deleteElogioById(id=id)
        # self.usuarioRepository.closeCursorAndConnection()
        self.elogioRepository.commit()

    def deleteAllUsuarios(self):
        self.elogioRepository.deleteAllElogios()
        # self.usuarioRepository.closeCursorAndConnection()
        self.elogioRepository.commit()
