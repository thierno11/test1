

USER="""
    CREATE TABLE IF NOT EXISTS UTILISATEUR(
        id SERIAL PRIMARY KEY,
        nom VARCHAR(50),
        prenom VARCHAR(100),
        email VARCHAR(100) UNIQUE ,
        password VARCHAR(10)
    )
"""