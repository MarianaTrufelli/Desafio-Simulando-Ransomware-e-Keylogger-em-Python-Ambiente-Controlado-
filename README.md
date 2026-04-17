📁 Estrutura do Projeto
/ransomware/: Simulação de ransomware, arquivos de teste e descriptografia.
/keylogger/: Keylogger simples e seu registro.
/defesa/: Reflexão sobre defesa, prevenção e boas práticas.
/images/: Prints do funcionamento.
Como Utilizar
1. Clonar o repositório

git clone https://github.com/SEU_USUARIO/NOME-DO-REPOSITORIO.git
cd NOME-DO-REPOSITORIO
Ransomware Simulado
Criptografa todos os arquivos .txt na pasta /test_data/;
Gera chave e mensagem de resgate;
Permite descriptografia com a chave correta.
Como executar:
pip install cryptography
cd ransomware
python3 ransomware_simulado.py encrypt

# Para descriptografar depois:
python3 ransomware_simulado.py decrypt <coloque_sua_chave_aqui>
Keylogger Simulado
Captura teclas pressionadas através da biblioteca pynput;
Salva tudo em log.txt;
Pode ser adaptado para enviar logs por email (comentado para segurança).
Como executar:
pip install pynput
cd keylogger
python3 keylogger_simulado.py
Defesa e Prevenção
Veja /defesa/reflexao_defesa.md para estratégias detalhadas:

Antivírus
Firewall
Sandboxing
Educação do usuário
Restrições de permissão
ATENÇÃO: NÃO execute scripts deste tipo fora de ambientes de teste/laboratório. Não use para fins maliciosos.
Todos scripts foram implementados apenas para fins educacionais.
