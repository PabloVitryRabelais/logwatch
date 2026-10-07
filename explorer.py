
from pathlib import Path
from logwatch import lire_log


def main():
    chemin_log = Path(__file__).with_name("sample-logs.log")
    entrees, ignorees = lire_log(chemin_log)
    print(f"Requetes lues : {len(entrees)}")
    print(f"Lignes ignorees : {ignorees}")

    requetes_par_famille = {"2xx": 0, "3xx": 0, "4xx": 0, "5xx": 0}
    requetes_par_ip = {}
    echecs_par_ip = {}

    for entree in entrees:
        famille = f"{entree['statut'] // 100}xx"
        if famille in requetes_par_famille:
            requetes_par_famille[famille] += 1

        if entree["ip"] not in requetes_par_ip:
            requetes_par_ip[entree["ip"]] = 0
        requetes_par_ip[entree["ip"]] += 1

        if entree["statut"] >= 400 and entree["url"] == "/login":
            if entree["ip"] not in echecs_par_ip:
                echecs_par_ip[entree["ip"]] = 0
            echecs_par_ip[entree["ip"]] += 1

    print(f"Requetes par famille : {requetes_par_famille}")
    print(f"Somme des quatre familles : {sum(requetes_par_famille.values())}")

    print(f"Requetes par IP : {requetes_par_ip}")   
    
    print(f"Echecs par IP : {echecs_par_ip}")

if __name__ == "__main__":
    main()
