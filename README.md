
Este é um Sistema de envio de documentos para impressão.

#FUNCIONAMENTO BÁSICO
===============================================================================================
Os utilizadores criam contas e, com estas contas, estes podem fazer uploads de documentos. Depois de fazer o upload dos documentos, os utilizadores podem os enviar para serem impressos em um determinado local de impressão.
Os locais de impressão neste caso são os agentes.
Os agentes acedem os documentos e podem fazer o download dos mesmos ou imprimir utilizando o proprio navegador.
NOTA: PARA OS AGENTES, RECOMENDA-SE QUE UTILIZEM O NAVEGAR FIREFOX

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
* sudo docker volume create autoprintvolume
* sudo docker build -t postgresautoprint .
* sudo docker run --name postgresautoprint --restart always -e POSTGRES_PASSWORD=mysecretpassword -v autoprintvolume:/var/lib/postgresql/data -d postgresautoprint

  NOTA:  AJUSTE O UTILIZADOR E A SENHA DO DOCKERFILE de acordo com as suas preferências
   Após isso, substitua as configurações no ficheiro settings.py de acordo com a sua base de dados.
  ===============
   
 4. Instalar as dependencias do Django, migrar a base de dados e iniciar o servidor
    -->> Navegue até Autoprint/ e digite *pip install -r requirements.txt* para instalar as dependêcias
    * python3 manage.py makemigrations (Fazer as migrações)
    * python3 manage.py migrate (inicializar a base de dados)
    * python3 manage.py runserver (inicializar o servidor)
    Se tudo estiver bem, o servidor estará acessivel em http://localhost:8000

CAPTURAS DE TELA
==============================
* Página Inicial
![Screenshot from 2023-12-15 14-23-55](https://github.com/magiccode4Dim/autoprint/assets/128492329/09535651-9dba-429a-bc6f-e085f26f75cf)
* Fazer upload de documentos
![Screenshot from 2023-12-15 14-24-21](https://github.com/magiccode4Dim/autoprint/assets/128492329/45dc123e-1a55-4162-8646-8a22d37b00ad)
* Documentos carregados
![Screenshot from 2023-12-15 14-29-22](https://github.com/magiccode4Dim/autoprint/assets/128492329/bb015881-5f84-472c-88fc-23b340a2f7eb)
* Fazer pedido de impressão
![Screenshot from 2023-12-15 14-29-50](https://github.com/magiccode4Dim/autoprint/assets/128492329/eaf89ee5-6494-4f27-bf5c-15aa90ddcf3a)
* O agente confirmando o pedido apartir do CCC
![Screenshot from 2023-12-15 14-25-13](https://github.com/magiccode4Dim/autoprint/assets/128492329/0234f696-3d3f-4b30-b9a8-3e034ea6dda2)
* O agente acedendo o documento
![Screenshot from 2023-12-15 14-26-14](https://github.com/magiccode4Dim/autoprint/assets/128492329/7adc3372-41b4-4a9a-bd56-89122571542b)

    
    
 
