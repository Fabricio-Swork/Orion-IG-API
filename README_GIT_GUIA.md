
# 🧠 Guia Git & GitHub - Início e Sincronização de Projeto

Este guia é um checklist prático para iniciar e sincronizar projetos com Git e GitHub via linha de comando e VS Code.

---

## ✅ Iniciar um Repositório Local e Enviar para o GitHub

```bash
# 1. Acesse a pasta do seu projeto local
cd nome-da-pasta-do-projeto

# 2. Inicie o repositório Git
git init

# 3. Adicione todos os arquivos
git add .

# 4. Faça o primeiro commit
git commit -m "Primeiro commit"

# 5. Crie um repositório no GitHub (sem README/.gitignore)

# 6. Adicione o repositório remoto
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git

# 7. Envie para o GitHub
git branch -M main
git push -u origin main
```

---

## ✅ Clonar um Repositório em Nova Máquina e Sincronizar com VS Code

```bash
# 1. Instale o Git: https://git-scm.com/downloads

# 2. Configure o usuário (apenas uma vez)
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

# 3. Clone o repositório
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git

# 4. Acesse a pasta do projeto
cd NOME_DO_REPOSITORIO

# 5. (Opcional) Abra com o VS Code
code .

# 6. Verifique o remoto
git remote -v

# 7. Trabalhe normalmente: add, commit, push
git add .
git commit -m "Atualizações"
git push
```

---

## 🔁 Comandos Úteis para Gestão do Repositório

### 📌 Salvar atualizações locais e enviar para GitHub

```bash
git add .                      # Adiciona todas as mudanças
git commit -m "Mensagem"       # Cria um commit
git push                       # Envia para o GitHub
```

### ⬇️ Baixar alterações do GitHub para sua máquina

```bash
git pull                       # Atualiza seu código local com o que está no GitHub
```

---

## 🌿 Trabalhando com Branches (Funcionalidades/Testes)

###  Criar branch para nova funcionalidade e depois aplicar na branch "main"

```bash
# Verifique que voce esta na branch main
# A branch atual estará marcada com *
git branch

# Se não estiver na branch main, troque com: 
git checkout main

# crie e mude para uma nova branch
git checkout -b branch-nova-funcionalidade        

# Faça alterações...
...

# Adicione os arquivos modificados ao controle de versao
git add .

# Faça o comite das alterações
git commit -m "Funcionalidade nova"

# Volte para branch main
git checkout main

# Aplique as alterações da nova branch à main (MERGE)
# Isso incorpora as mudanças da "branch-nova-funcionalidade" na "main"
git merge branch-nova-funcionalidade


git push -u origin nome-da-branch     # Envia a nova branch ao GitHub
```

### colaborador cria nova funcionalidade e você integra na sua

```bash
# Verifique as branches disponíveis no repositório remoto (GitHub)
# Isso atualiza a lista de branches remotas do repositório no seu Git local.
git fetch

# Veja as branches remotas disponíveis
git branch -r

# Procure por algo como:
origin/nova-feature-colaborador

# Baixe e crie uma branch local a partir da branch do colaborador
# Isso cria uma cópia local da branch remota e te coloca nela.
git checkout -b nova-feature-colaborador origin/nova-feature-colaborador

# Testar a branch...
...

# Se aprovado, mude para a branch principal (main)
git checkout main

# Aplique o merge da branch do colaborador à sua main
git merge nova-feature-colaborador

# Envie sua branch main atualizada para o GitHub
git push origin main


```

### 🔄 Alternar entre branches

```bash
git checkout nome-da-branch
```

### 🚀 Enviar alterações em uma branch existente

```bash
git push                              # Já estando na branch desejada
```

---

## 📦 Sincronizar Pacotes (Dependências do Projeto)

### Enviar lista de pacotes da sua máquina para o GitHub

Python:
```bash
pip freeze > requirements.txt         # Salva pacotes do virtualenv
git add requirements.txt
git commit -m "Adiciona dependências"
git push
```

Node.js:
```bash
npm install nome-pacote               # Instala um pacote
git add package.json package-lock.json
git commit -m "Atualiza dependências"
git push
```

### Baixar dependências em outra máquina

Python:
```bash
pip install -r requirements.txt
```

Node.js:
```bash
npm install
```

---

## 👥 Baixar e trabalhar com branches de outros colaboradores

```bash
# Ver branches remotas
git fetch                            # Atualiza lista de branches
git branch -r

# Baixar uma branch remota e criar localmente
git checkout -b nome-local origin/nome-remoto

# Enviar alterações para uma branch de outro colaborador
git push origin nome-da-branch
```

---

🛠️ **Dica**: sempre verifique se você está na branch correta com:

```bash
git branch
```

## Arquivo .Gitignore

``` bash 
 Crie o arquivo na raiz do projet

# Comandos 

*.extensão	        # Ignora todos os arquivos com essa extensão

/pasta/	            # Ignora uma pasta (e seu conteúdo) na raiz

nome-do-arquivo.ext	# Ignora um arquivo específico

**/nome.ext	        # Ignora arquivos com esse nome em qualquer pasta

!arquivo.ext	    # Inclui um arquivo mesmo que uma regra geral o ignore

EXEMPLOS COMUNS 

# Ignorar arquivos Python compilados
__pycache__/
*.py[cod]

# Ignorar ambientes virtuais
venv/
.env/

# Ignorar arquivos de log
*.log

# Ignorar dependências do Node.js
node_modules/

# Ignorar arquivos temporários do VS Code
.vscode/
*.swp

# Ignorar arquivos de banco local
*.sqlite3
*.db

# Ignorar arquivos de configuração locais e senhas
.env
secrets.json

# Ignorar arquivos do sistema
.DS_Store
Thumbs.db

```
###  Importante:

Se um arquivo já foi adicionado ao Git antes de você criar o .gitignore, ele ainda será rastreado. Para parar de rastrear, use:

> git rm --cached nome-do-arquivo

Você pode usar modelos prontos de .gitignore no site:

🔗 https://www.toptal.com/developers/gitignore


```


---

📌 Esse guia pode ser usado como referência rápida no seu projeto para manter seu fluxo de trabalho com Git organizado e consistente.
