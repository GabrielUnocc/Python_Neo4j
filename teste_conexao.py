from neo4j import GraphDatabase

# Configure a URI e as credenciais. A senha deve corresponder ao seu Neo4j!
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "unochapeco"))

# Verifica conectividade
print("Verificando conexão...")
driver.verify_connectivity()
print("Conexão bem-sucedida!")

# Abre sessão e executa query
with driver.session(database="neo4j") as session:
    print("Executando query...")
    # NOTE: Este código assume que você já tem Pessoas com o label Pessoa e propriedade nome no seu DB.
    # Se o banco estiver vazio, o resultado será vazio.
    result = session.run("MATCH (p:Pessoa) RETURN p.nome AS nome")

    for record in result:
        print(f"Nome encontrado: {record['nome']}")

# Fecha conexão
driver.close()
print("Conexão fechada.")