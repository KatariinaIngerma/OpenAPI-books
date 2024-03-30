import connexion
from typing import Dict
from typing import Tuple
from typing import Union
import requests
import os
from flask import send_file


from raamatu_teenus.models.raamatu_lisamine201_response import RaamatuLisamine201Response  # noqa: E501
from raamatu_teenus.models.raamatu_loomise_sisend import RaamatuLoomiseSisend  # noqa: E501
from raamatu_teenus.models.raamatu_nimekiri200_response import RaamatuNimekiri200Response  # noqa: E501
from raamatu_teenus.models.raamatu_otsingu_sisend import RaamatuOtsinguSisend  # noqa: E501
from raamatu_teenus.models.raamatust_sone_otsimine201_response import RaamatustSoneOtsimine201Response  # noqa: E501
from raamatu_teenus import util

raamatute_kaust = "C:\\Users\\katar\\OneDrive\\\Desktop\\\VeebiHajus24\\Praks5-OpenAPI\\raamatud"

def raamatu_allatombamine(book_id):  # noqa: E501
    """Raamatu allatombamine

     # noqa: E501

    :param book_id: allalaetava raamatu id
    :type book_id: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    faili_nimi = book_id + ".txt"
    faili_path = os.path.join(raamatute_kaust, faili_nimi)
    
    if os.path.exists(faili_path):
        return send_file(faili_path, mimetype='text/plain'), 200
    else:
        return {}, 404


def raamatu_kustutamine(book_id):  # noqa: E501
    """Raamatu kustutamine

     # noqa: E501

    :param book_id: kustutatava raamatu id
    :type book_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    faili_nimi = book_id + ".txt"
    faili_path = os.path.join(raamatute_kaust, faili_nimi)
    
    if os.path.exists(faili_path) and book_id.isnumeric():
        os.remove(faili_path)
        return {}, 204
    else:
        return {}, 404


def raamatu_lisamine(raamatu_loomise_sisend=None):  # noqa: E501
    """Raamatu loomine

     # noqa: E501

    :param raamatu_loomise_sisend: 
    :type raamatu_loomise_sisend: dict | bytes

    :rtype: Union[RaamatuLisamine201Response, Tuple[RaamatuLisamine201Response, int], Tuple[RaamatuLisamine201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        raamatu_loomise_sisend = RaamatuLoomiseSisend.from_dict(connexion.request.get_json())  # noqa: E501
    
    
    raamatu_id = raamatu_loomise_sisend.raamatu_id

    book_address = "https://www.gutenberg.org/cache/epub/"+ str(raamatu_id) +"/pg"+ str(raamatu_id) +".txt"
    response = requests.get(book_address)
    if response.status_code == 200:
         content= response.text
         filename = os.path.join(raamatute_kaust, f"{raamatu_id}.txt")

         with open(filename, 'w+', encoding="utf-8") as f:
            f.write(content)

            return {"tulemus": "Raamatu loomine õnnestus",
                "raamatu_id": str(raamatu_id) }, 201
    else:
        return {"tulemus": "Raamatu laadimine ebaõnnestus"}, 400
    



def raamatu_nimekiri():  # noqa: E501
    """Raamatute

     # noqa: E501


    :rtype: Union[RaamatuNimekiri200Response, Tuple[RaamatuNimekiri200Response, int], Tuple[RaamatuNimekiri200Response, int, Dict[str, str]]
    """

    raamatud = []
    
    failid = os.listdir(raamatute_kaust)
    for fail in failid:
        if fail.endswith('.txt'):
            raamatud.append(fail.split('.')[0])
    return ({"raamatud": raamatud}, 200 )


def raamatust_sone_otsimine(raamatu_otsingu_sisend=None):  # noqa: E501
    """Alla tõmmatud raamtust sõne otsimine

     # noqa: E501

    :param raamatu_otsingu_sisend: 
    :type raamatu_otsingu_sisend: dict | bytes

    :rtype: Union[RaamatustSoneOtsimine201Response, Tuple[RaamatustSoneOtsimine201Response, int], Tuple[RaamatustSoneOtsimine201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        raamatu_otsingu_sisend = RaamatuOtsinguSisend.from_dict(connexion.request.get_json())  # noqa: E501
    
    sone = raamatu_otsingu_sisend.sone
    raamatu_id =  raamatu_otsingu_sisend.raamatu_id
    
    faili_nimi = str(raamatu_id) + ".txt"
    faili_path = os.path.join(raamatute_kaust, faili_nimi)
    
    
    if os.path.exists(faili_path):
        summa = 0
        with open(faili_path, 'r', encoding='utf-8') as f:
            content = f.read().lower() 
            summa = content.split().count(sone.lower()) 
        return {"raamatu_id": raamatu_id, "sone" : sone, "leitud": summa}, 200
    else:
        return {}, 404
    
    
