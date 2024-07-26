Oque é o controle versão?
O Controle de versão é praticamente uma ferramenta de software que ajuda as equipes a trabalhar mais rapidamente. Também é preciso ter muito cuidado para não cometer erros, pois erros podem ter um impacto significativo e até mesmo serem fatais para o progresso de toda a equipe. É essencial seguir boas práticas e garantir que as alterações sejam bem gerenciadas para evitar problemas. É também O controle de versão permite acompanhar mudanças em arquivos de muito tempo, incluindo a criação e exclusão de arquivos antigos. E também podemos rever versões anteriores e até reverter mudanças feitas no passado.

Vantagens:1. Histórico de Alterações
2. Trabalho em Equipe
3. Backup e Recuperação
4. Rastreamento e Auditoria
5. Gestão de Releases

Exemplo:1:Git
2:Apache Subversion (SVN)
3:Mercurial

Oque é programação orientada?
Programação Orientada a Objetos é um paradigma de linguagem de programação que pode ser usado com várias linguagens, como Java, Python, C#, entre outras. Esse paradigma facilita muito o dia a dia de quem o utiliza.caracteristicas desse programação é que ele faça que o programador possa pensar em várias coisas de forma distintas

HTTP é um protocolo (protocol) que permite a obtenção de recursos, como documentos HTML. É a base de qualquer troca de dados na Web e um protocolo cliente-servidor, o que significa que as requisições são iniciadas pelo destinatário, geralmente um navegador da Web. Um documento completo é reconstruído a partir dos diferentes sub-documentos obtidos, como por exemplo texto, descrição do layout, imagens, vídeos, scripts e muito.
REST é um estilo de arquitetura web muito importante no desenvolvimento e gerenciamento de sistemas na internet. Com esse recurso, tanto o servidor quanto os clientes têm acesso a um procedimento mais rápido e fácil de conduzir.A relação entre Web API e REST (Representational State Transfer) é que REST é um dos estilos arquitetônicos mais comuns para a construção de Web APIs. As APIs RESTful seguem princípios específicos que permitem uma comunicação eficiente e escalável entre cliente e servidor.

1:get
2:POST
3:put
4:patch
5:DELETE
6:HEAD
7:OPTIONS 

 (Entidade): A camada de entidade representa os objetos do domínio do sistema, ou seja, os dados e seus atributos que são persistidos no banco de dados. Essas classes geralmente correspondem às tabelas do banco de dados e são mapeadas utilizando frameworks de ORM (Object-Relational Mapping). Elas contêm apenas os atributos e, ocasionalmente, algumas validações simples dos dados.

Controller (Controlador): A camada de controlador é responsável por receber as requisições HTTP, processar os dados de entrada, chamar os serviços apropriados e devolver uma resposta adequada ao cliente. Os controladores atuam como intermediários entre as camadas de apresentação (interface do usuário) e a lógica de negócios, convertendo os dados de entrada em chamadas de métodos de serviço e formatando os resultados para a saída

Repository (Repositório): A camada de repositório é responsável pela interação direta com o banco de dados. Ela abstrai os detalhes de acesso a dados, fornecendo métodos para realizar operações de CRUD (Create, Read, Update, Delete). Essa camada permite que a lógica de negócios e os controladores interajam com os dados de maneira mais abstrata e desacoplada dos detalhes do banco de dados subjacente.

Service (Serviço): A camada de serviço contém a lógica de negócios da aplicação. Ela é responsável por orquestrar as operações, aplicar regras de negócio, validar dados e coordenar a interação entre a camada de repositório e a camada de controlador. Essa camada pode chamar múltiplos repositórios e outros serviços para realizar operações complexas, garantindo que todas as regras de negócio sejam aplicadas corretamente.Entity

○ que é um padrão de projeto e porque utilizamos? 

Um padrão de projeto é uma solução reutilizável para problemas comuns que surgem no design de software. Eles fornecem uma abordagem testada e comprovada para resolver determinados problemas de maneira eficiente, facilitando a manutenção e evolução do código. Utilizamos padrões de projeto para promover boas práticas de desenvolvimento, melhorar a comunicação entre desenvolvedores e aumentar a produtividade. Esses padrões também ajudam a criar sistemas mais robustos e flexíveis, pois são baseados em experiências acumuladas e aplicadas em diversas situações. Adotar padrões de projeto contribui para a criação de um código mais organizado e facil de entender.

Explique o conceito de arquitetura de software e seus propósitos?

A arquitetura de software refere-se à estrutura fundamental de um sistema de software, incluindo seus componentes, a relação entre esses componentes e as diretrizes que orientam seu design e evolução. Os principais propósitos da arquitetura de software são:

Organização e Estrutura: Define como os componentes do sistema são organizados e como interagem entre si, facilitando a compreensão e manutenção do sistema.

Qualidade do Sistema: Influencia diretamente atributos de qualidade, como desempenho, escalabilidade, segurança, e confiabilidade.

Tomada de Decisões: Fornece uma base para decisões de design, ajudando a identificar e mitigar riscos técnicos precocemente.

Comunicação: Serve como um meio de comunicação entre as partes interessadas, incluindo desenvolvedores, arquitetos, e clientes, garantindo que todos tenham uma visão comum do sistema.

Reuso e Mantenabilidade: Facilita o reuso de componentes e a manutenção do sistema ao longo do tempo, promovendo uma estrutura modular e coesa.

Evolução: Suporta a evolução do sistema, permitindo que ele se adapte a novas necessidades e tecnologias sem uma reescrita completa.

○ que signiica a sigla SOLID e quais seus princípios?

A sigla SOLID representa cinco princípios de design de software destinados a melhorar a qualidade e a manutenção do código. Esses princípios foram introduzidos por Robert C. Martin, também conhecido como "Uncle Bob". Aqui estão os princípios do SOLID:

Single Responsibility Principle (SRP):

Princípio da Responsabilidade Única: Uma classe deve ter apenas uma razão para mudar, ou seja, deve ter apenas uma responsabilidade. Isso significa que cada classe deve ser responsável por uma única parte da funcionalidade fornecida pelo software e essa responsabilidade deve ser completamente encapsulada pela classe.
Open/Closed Principle (OCP):

Princípio do Aberto/Fechado: Entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão, mas fechadas para modificação. Isso significa que o comportamento de uma classe deve poder ser estendido sem alterar seu código-fonte.
Liskov Substitution Principle (LSP):

Princípio da Substituição de Liskov: Objetos de uma classe base devem poder ser substituídos por objetos de uma classe derivada sem alterar o correto funcionamento do programa. Em outras palavras, se S é uma subclasse de T, então os objetos do tipo T no programa podem ser substituídos por objetos do tipo S sem que o programa altere seu comportamento desejado.
Interface Segregation Principle (ISP):

Princípio da Segregação de Interfaces: Uma classe não deve ser forçada a depender de interfaces que não utiliza. Isso significa que é melhor criar interfaces específicas e pequenas, em vez de interfaces grandes e abrangentes.
Dependency Inversion Principle (DIP):

Princípio da Inversão de Dependência: Dependa de abstrações, não de concretudes. Este princípio sugere que módulos de alto nível não devem depender de módulos de baixo nível; ambos devem depender de abstrações (interfaces). Além disso, abstrações não devem depender de detalhes. Detalhes devem depender de abstrações.