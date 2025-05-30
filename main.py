from fastapi import FastAPI,Depends
from database.connexion import initialisation,get_db
from schema.utilisateur_schema import UtilisateurSchema,UtilisateurResponse

initialisation()

app = FastAPI()




@app.post("/utilisateurs",response_model=UtilisateurResponse)
def create_utilisateur(utilisateurs:UtilisateurSchema,db=Depends(get_db)):
    db.execute("INSERT INTO UTILISATEUR (nom,prenom,email,password) values (%s,%s,%s,%s) returning *",(utilisateurs.nom,utilisateurs.prenom,utilisateurs.email,utilisateurs.password))
    user = db.fetchone()
    return UtilisateurResponse(**user)

    



@app.get("/hello")
def hello_word():
    return "Hello word"

