from pydantic import BaseModel,EmailStr,field_validator,model_validator
from typing_extensions import Self


class UtilisateurSchema(BaseModel):
    nom:str
    prenom : str
    email : EmailStr
    password: str
    confirm_password : str


    @field_validator("nom",mode="after")
    @classmethod
    def transform_nom(cls,nom:str):
        return nom.upper()
    
    @field_validator("prenom",mode="after")
    def transform_prenom(prenom:str):
        return prenom.upper()
    
    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self

class UtilisateurResponse(BaseModel):
    id: int
    nom:str
    prenom : str
    email : EmailStr
    password: str
