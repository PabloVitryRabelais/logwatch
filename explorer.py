
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
    par_minute = {}
    fenetre_minutes = {}

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

        minute = entree["date"][:17]
        if minute not in par_minute:
            par_minute[minute] = 0
        par_minute[minute] += 1

    minute_pic = None
    max_par_minute = 0
    for minute, nombre in par_minute.items():
        if nombre > max_par_minute:
            minute_pic = minute
            max_par_minute = nombre
        if minute[:15] + str(int(minute[-2:]) - ((int(minute[-2:]) % 5))) not in fenetre_minutes:
            fenetre_minutes[minute[:15] + str(int(minute[-2:]) - ((int(minute[-2:]) % 5)))] = 0
        fenetre_minutes[minute[:15] + str(int(minute[-2:]) - ((int(minute[-2:]) % 5)))] += nombre  

    fenetre_pic = None
    max_par_fenetre = 0
    for fenetre, nombre in fenetre_minutes.items():
        if nombre > max_par_fenetre:
            fenetre_pic = fenetre
            max_par_fenetre = nombre


    print(f"Requetes par famille : {requetes_par_famille}")
    print(f"Somme des quatre familles : {sum(requetes_par_famille.values())}")

    print(f"Requetes par IP : {requetes_par_ip}")   
    
    print(f"Echecs par IP : {echecs_par_ip}")
    print(f"Requetes par minute : {par_minute}")
    if minute_pic is None:
        print("Minute la plus chargee : aucune (0 requete)")
    else:
        print(f"Minute la plus chargee : {minute_pic} ({max_par_minute} requetes)")
    if fenetre_pic is None:
        print("Fenetre la plus chargee : aucune (0 requete)")
    else:
        print(f"Fenetre la plus chargee : {fenetre_pic} ({max_par_fenetre} requetes)")


if __name__ == "__main__":
    main()
