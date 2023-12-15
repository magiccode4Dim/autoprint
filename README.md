Este é um Sistema de envio de documentos para impressão.

#FUNCIONAMENTO BÁSICO
===============================================================================================
Os utilizadores criam contas e, com estas contas, estes podem fazer uploads de documentos. Depois de fazer o upload dos documentos, os utilizadores podem os enviar para serem impressos em um determinado local de impressão.
Os locais de impressão neste caso são os agentes.
Os agentes acedem os documentos e podem fazer o download dos mesmos ou imprimir utilizando o proprio navegador

#SOBRE O APLICAÇÃO
===============================================================================================
O projecto foi desenvolvida em Django e, deve utilizar uma base de dados relacional MYSQL ou POSTGRES (recomendo).
Foi desenvolvido como uma iniciativa para eliminar a necessidade de envio de documentos ou transporte de dispositivos de armazenamento como flashs para o local de impressão.

#DEPENDÊNCIAS DA APLICAÇÃO
==============================================================================================
* Python >= 3.8 (Estou usando 3.10.12);
* Mysql ou Postgres (É só depois substituir as credências de base de dados de acordo com o caso)
* Docker ( É Opcional mas, é necessário caso queria fazer com que a base de dados seja um container) 

#COMO INSTALAR?
===============================================================================================
1. Baixe o projecto
   *git clone https://github.com/magiccode4Dim/autoprint.git*
   
2. Instale o container de base de dados com Suporte a Postgres Replication (Opcional)
       No directorio Raiz do projecto digite *cd DatabaseImage/*
       Em seguida corra os comando:
         *---> sudo docker volume create autoprintvolume
           --> sudo docker build -t postgresautoprint .
           --> sudo docker run --name postgresautoprint --restart always -e POSTGRES_PASSWORD=mysecretpassword -v autoprintvolume:/var/lib/postgresql/data -d postgresautoprint*
   NOTA:  AJUSTE O UTILIZADOR E A SENHA DO DOCKERFILE de acordo com as suas preferências
   Após isso, substitua as configurações no ficheiro settings.py de acordo com a sua base de dados.
   
 3. Instalar as dependencias do Django, migrar a base de dados e iniciar o servidor
    -->> Navegue até Autoprint/ e digite *pip install -r requirements.txt*
    -->> python3 manage.py makemigrations (Fazer as migrações)
    -->> python3 manage.py migrate (inicializar a base de dados)
    -->> python3 manage.py runserver (inicializar o servidor)
    Se tudo estiver bem, o servidor estará acessivel em http://localhost:8000
    
    
    
 
