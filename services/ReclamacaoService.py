from repositories import ReclamacaoRepository


class ReclamacaoService:
    reclamacaoRepository = ReclamacaoRepository.ReclamacaoRepository()

    # def __init__(self) -> None:
    #     super().__init__()

    def __int__(self):
        pass

    def findAllElogios(self):
        usuarios = self.reclamacaoRepository.findAllReclamacoes()
        # self.usuarioRepository.closeCursorAndConnection()
        self.reclamacaoRepository.commit()
        return usuarios

    def findUsuarioById(self, id):
        usuario = self.reclamacaoRepository.findReclamacaoById(id=id)
        # self.usuarioRepository.closeCursorAndConnection()
        self.reclamacaoRepository.commit()
        return usuario

    def saveUsuario(self, reclamacao, idUsuario):
        self.reclamacaoRepository.saveReclamacao(reclamacao=reclamacao, idUsuario=idUsuario)
        # self.usuarioRepository.closeCursorAndConnection()
        self.reclamacaoRepository.commit()

    def deleteUsuarioById(self, id):
        self.reclamacaoRepository.deleteReclamacaoById(id=id)
        # self.usuarioRepository.closeCursorAndConnection()
        self.reclamacaoRepository.commit()

    def deleteAllUsuarios(self):
        self.reclamacaoRepository.deleteAllReclamacoes()
        # self.usuarioRepository.closeCursorAndConnection()
        self.reclamacaoRepository.commit()
