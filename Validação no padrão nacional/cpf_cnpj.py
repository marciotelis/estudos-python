from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documentos = str(documento)
        if self.tipo_documento == "cpf":
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!!")
        elif self.tipo_documento == "cnpj":
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CPF inválido!!")
        else:
            raise ValueError("Documento inválido!")

    def __str__(self):
        return self.format_cpf()

    def cpf_eh_valido(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
        
    def cnpj_e_valido(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)
