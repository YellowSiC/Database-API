import typing as t
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship
from contextlib import asynccontextmanager
import datetime
from pydantic import BaseModel  # Import Pydantic's BaseModel



class Edukt(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    hersteller: str
    menge: float
    daten_blatt: bytes  
    vorhandene_menge: float
    kauf_datum: t.Optional[datetime.date]  
    # the implementation your columns of the database must be here




    




    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    sicquelle_id: t.Optional[int] = Field(default=None, foreign_key="sicquelle.id")
    sicquelles: t.Optional['Sicquelle'] = Relationship(back_populates="edukts")
    cquelle_id: t.Optional[int] = Field(default=None, foreign_key="cquelle.id")
    cquelle: t.Optional['Cquelle'] = Relationship(back_populates="edukts")
    zusatzsoff_id: t.Optional[int] = Field(default=None, foreign_key="zusatzsoff.id")
    zusatzsoff: t.Optional['Zusatzsoff'] = Relationship(back_populates="edukts")
    herstellprozesss: t.List['Herstellprozess'] = Relationship(back_populates="edukts")






class Sicquelle(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    eduks: t.List[Edukt] = Relationship(back_populates="sicquelle")



class Cquelle(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    edukts: t.List[Edukt] = Relationship(back_populates="cquelle")




class Zusatzsoff(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here





    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    edukts: t.List[Edukt] = Relationship(back_populates="zusatzsoff")




class Apparatur(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    herstellprozesss: t.List['Herstellprozess'] = Relationship(back_populates="apparaturs")




class Zwischenprecursor(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    verarbeitung_id: t.Optional[int] = Field(default=None, foreign_key="verarbeitung.id")
    verarbeitung: t.Optional['Verarbeitung'] = Relationship(back_populates="zwischenprecursors")
    herstellprozesss: t.List['Herstellprozess'] = Relationship(back_populates="zwischenprecursors")



class Verarbeitung(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    precursor_id: t.Optional[int] = Field(default=None, foreign_key="precursor.id")
    precursor: t.Optional['Precursor'] = Relationship(back_populates="verarbeitungs")
    zwischenprecursors: t.List[Zwischenprecursor] = Relationship(back_populates="verarbeitung")



class Precursor(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    analyse_id: t.Optional[int] = Field(default=None, foreign_key="analyse.id")
    analyses: t.Optional['Analyse'] = Relationship(back_populates="precursors")
    herstellprozesssic_id: t.Optional[int] = Field(default=None, foreign_key="herstellprozesssic.id")
    herstellprozesssics: t.Optional['Herstellprozesssic'] = Relationship(back_populates="precursors")

     


class Analyse(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here









    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    csi02bestimmung_id: t.Optional[int] = Field(default=None, foreign_key="csi02bestimmung.id")
    csi02bestimmungs: t.Optional['Csi02bestimmung'] = Relationship(back_populates="analyses")
    iga_id: t.Optional[int] = Field(default=None, foreign_key="iga.id")
    igas: t.Optional['Iga'] = Relationship(back_populates="analyses")
    mikroskopie_id: t.Optional[int] = Field(default=None, foreign_key="mikroskopie.id")
    mikroskopies: t.Optional['Mikroskopie'] = Relationship(back_populates="analyses")
    gdms_id: t.Optional[int] = Field(default=None, foreign_key="gdms.id")
    gdms: t.Optional['Gdms'] = Relationship(back_populates="analyses")
    raman_id: t.Optional[int] = Field(default=None, foreign_key="raman.id")
    ramans: t.Optional['Raman'] = Relationship(back_populates="analyses")
    pxrd_id: t.Optional[int] = Field(default=None, foreign_key="pxrd.id")
    pxrds: t.Optional['Pxrd'] = Relationship(back_populates="analyses")
    rem_id: t.Optional[int] = Field(default=None, foreign_key="rem.id")
    rems: t.Optional['Rem'] = Relationship(back_populates="analyses")
    laserbeugung_id: t.Optional[int] = Field(default=None, foreign_key="laserbeugung.id")
    laserbeugungs: t.Optional['Laserbeugung'] = Relationship(back_populates="analyses")
    bet_id: t.Optional[int] = Field(default=None, foreign_key="bet.id")
    bets: t.Optional['Bet'] = Relationship(back_populates="analyses")
    precursors: t.List[Precursor] = Relationship(back_populates="analyses")
    sicsubstrats: t.List['Sicsubstrat'] = Relationship(back_populates="analyses")
    sics: t.List['Sic'] = Relationship(back_populates="analyses")





class Csi02bestimmung(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    analyses: t.List[Analyse] = Relationship(back_populates="csi02bestimmungs")




class Iga(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    analyses: t.List[Analyse] = Relationship(back_populates="igas")







class Mikroskopie(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    analyses: t.List[Analyse] = Relationship(back_populates="mikroskopies")






class Gdms(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    analyses: t.List[Analyse] = Relationship(back_populates="gdms")







class Raman(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    analyses: t.List[Analyse] = Relationship(back_populates="ramans")







class Pxrd(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    analyses: t.List[Analyse] = Relationship(back_populates="pxrds")







class Sicsubstrat(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here





    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    analyse_id: t.Optional[int] = Field(default=None, foreign_key="analyse.id")
    analyse: t.Optional['Analyse'] = Relationship(back_populates="sicsubstrats")
    herstellprozesssics: t.List['Herstellprozesssic'] = Relationship(back_populates="sicsubstrats")







class Sic(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here

    



    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    analyse_id: t.Optional[int] = Field(default=None, foreign_key="analyse.id")
    analyse: t.Optional['Analyse'] = Relationship(back_populates="sics")
    herstellprozesssics: t.List['Herstellprozesssic'] = Relationship(back_populates="sics")

    






class Rem(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    analyses: t.List[Zwischenprecursor] = Relationship(back_populates="rems")







class Laserbeugung(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    analyses: t.List[Zwischenprecursor] = Relationship(back_populates="laserbeugungs")






class Bet(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    analyses: t.List[Zwischenprecursor] = Relationship(back_populates="bets")



class Reaktor(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here










    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    herstellprozesssics: t.List['Herstellprozesssic'] = Relationship(back_populates="reaktors")




class Tiegel(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    herstellprozesssics: t.List['Herstellprozesssic'] = Relationship(back_populates="tiegels")



class Substrat(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    herstellprozesssics: t.List['Herstellprozesssic'] = Relationship(back_populates="substrats")





class Inertags(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    herstellprozesssics: t.List['Herstellprozesssic'] = Relationship(back_populates="inertags")




class Herstellprozesssic(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    reaktor_id: t.Optional[int] = Field(default=None, foreign_key="reaktor.id")
    reaktors: t.Optional['Reaktor'] = Relationship(back_populates="herstellprozesssics")
    tiegel_id: t.Optional[int] = Field(default=None, foreign_key="tiegel.id")
    tiegels: t.Optional['Tiegel'] = Relationship(back_populates="herstellprozesssics")
    substrat_id: t.Optional[int] = Field(default=None, foreign_key="substrat.id")
    substrats: t.Optional['Substrat'] = Relationship(back_populates="herstellprozesssics")
    inertags_id: t.Optional[int] = Field(default=None, foreign_key="inertags.id")
    inertags: t.Optional['Inertags'] = Relationship(back_populates="herstellprozesssics")
    sic_id: t.Optional[int] = Field(default=None, foreign_key="sic.id")
    sics: t.Optional['Sic'] = Relationship(back_populates="herstellprozesssics")
    sicsubstrat_id: t.Optional[int] = Field(default=None, foreign_key="sicsubstrat.id")
    sicsubstrats: t.Optional['Sicsubstrat'] = Relationship(back_populates="herstellprozesssics")
    
    


class Herstellprozess(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    user: t.Optional[str]
    datum: t.Optional[datetime.date]  
    ausbeute: float
    endtemperatur: float
    edukt_sic_quelle_soll: float
    edukt_sic_quelle_ist: float
    edukt_c_quelle_soll: float
    edukt_c_quelle_ist: float
    rezept_anleitung: bytes 
    auffälligkeiten: str
    # the implementation your columns of the database must be here







    


    """ Attention: everything that is written below Do not change anything, otherwise the relationship between the tables will not work......!!!!!!!"""
    edukt_id: t.Optional[int] = Field(default=None, foreign_key="edukt.id")
    edukts: t.Optional['Edukt'] = Relationship(back_populates="herstellprozesss")
    zwischenprecursor_id: t.Optional[int] = Field(default=None, foreign_key="zwischenprecursor.id")
    zwischenprecursors: t.Optional['Zwischenprecursor'] = Relationship(back_populates="herstellprozesss")
    apparatur_id: t.Optional[int] = Field(default=None, foreign_key="apparatur.id")
    apparaturs: t.Optional['Apparatur'] = Relationship(back_populates="herstellprozesss")

    



sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)
