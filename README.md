# USP-SEL0456 Trabalho 3

Sua equipe está desenvolvendo uma aplicação de automação residencial que exige a entrada de senha para execução de determinada rotina crítica. Você ficou responsável por desenvolver um script em Python que prove o conceito de verificar se uma senha fornecida pelo usuário coincide com a senha armazenada de forma criptografada. Os requisitos para a prova de conceito são:
- A senha é fornecida pelo usuário via arquivo de texto;
- A senha encriptada também está salva em arquivo de texto;
- Utilizar dois branches com funcionalidade específicas:
> - Branch 1: o programa deve apresentar ao usuário a senha presente no arquivo de texto e informar se a senha é correta;
> - Branch 2: o programa deve realizar o teste de comparação apenas internamente, sem apresentar informações ao usuário.
- Utilizar o GitHub Actions para automatizar a verificação. Para a branch 1, usar o teste com o comando `python`; para o branch 2, usar o teste com o `pytest`.

**Bônus:** usar arquivos criptografados para armazenar as senhas.
