import linkedin_api as ld
import pandas as pd

# Abrindo o Execel.
def LerExcel():
    try:
        UsuariosDf = pd.read_excel(
            "CaminhoArquivo/arquivo.xlsx"
        )
        return UsuariosDf
    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo:", e)

#Função para conectar no Linkedin.
def ConectarLinkedin(Usuario, senha):
    try:
        linkedin = ld.Linkedin(Usuario, senha, authenticate=True)
        return linkedin
    except Exception as e:
        print("Erro ao conectar no linkedin:", e)

#Armazenando os dados do Excel em uma variavel e fazendo o tratamento de dados para pesquisa no Linkedin
def UsandoExecel():
    try:
        usuarios = LerExcel()
        nomes_perfis = []  # Inicializa a lista de nomes de perfis
        for indice, url in enumerate(usuarios["Linkedin"]):
            partes = url.split("https://www.linkedin.com/in/")
            if len(partes) > 1:  # Verifica se há partes na URL
                nome_perfil = partes[1].split("/")[0]
                nomes_perfis.append(nome_perfil)  # Adiciona o nome do perfil à lista
        return nomes_perfis
    except Exception as e:
        print("Erro ao ler o arquivo Excel:", e)
# Executando a automação de pesquisa.
def ExecutandoAutomacao():
    linkedin = ConectarLinkedin("UserProfile", "Password")
    Nomes= UsandoExecel()
    df = LerExcel()
    dados = []
    for nome in Nomes:
        try:
            perfil = linkedin.get_profile(public_id=nome)
            for experiencia in perfil["experience"]:
                empresa = experiencia["companyName"]
                titulo = experiencia["title"]
                dados.append({'Empresa': empresa, 'Cargo': titulo})                
        except Exception as e:
            print(f"Erro ao ler os Dados do usuário {nome}:", e)
            continue
      # Criar um DataFrame a partir dos dados
    novos_dados_df = pd.DataFrame(dados)

    # Adicionar os novos dados ao DataFrame original
    df['Cargo'] = novos_dados_df['Cargo']
    df['Empresa'] = novos_dados_df['Empresa']

    # Salvar o DataFrame de volta no arquivo Excel
    df.to_excel('arquivo_modificado.xlsx', index=False)

# Chamando a função para executar a automação
ExecutandoAutomacao()