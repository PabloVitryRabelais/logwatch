| n° | date | symptôme observé
| fonction suspectée | état |

| B1 | 2026-09-30 | test_d1_somme_egale_total_lines rouge : attendu 6, reçu 3
| d1_requetes_par_ip | ouvert |

| B2 | 2026-09-30 | test_d3_ignore_url_legitime rouge : attendu [], reçu [{'ip': '10.0...': 'moyenne'}] == []
| d3_scan | ouvert |

| B4 | 2026-10-14 | test_d4_aucune_alerte_de_depassement_seuil_requete : pas d'alerte quand le trafic depasse le seuil sur une fenetre de cinq minutes
| d4_pic_trafic | ouvert |

## B1 - <P2 Q3>

Test en échec : test_d1_somme_egale_total_lines
Attendu / reçu : 6 / 3
Fonction visée : d1_requetes_par_ip, ligne 116
Cause racine : "if e["statut"] < 400:" ligne 120
Correction prévue : supression de la ligne
(étape 6) Correctif : commit <hash>, <auteur>, le AAAA-MM-JJ
Vérifié par : <nom>, sur <le cas éprouvé, différent de celui du
test>

## B2 - <P2 Q3>

Test en échec : test_d3_ignore_url_legitime
Attendu / reçu : [] / [{'ip': '10.0...': 'moyenne'}] == []
Fonction visée : d3_scan, ligne 142
Cause racine : "admin" dans MOTIFS_SCAN ligne 47
Correction prévue : supression/modification de la valeure
(étape 6) Correctif : commit <hash>, <auteur>, le AAAA-MM-JJ
Vérifié par : <nom>, sur <le cas éprouvé, différent de celui du
test>

## B3 - sample-log.log <P2 Q5>

| ligne 121 | 2026-09-30 | ligne tronquée après le code HTTP 200 : il manque la taille, le referer et l’agent | ouvert
| ligne 301 | 2026-09-30 | message : "<<< rotation du journal 03/Sep/2026 >>>" pas une entrée Apache | ouvert
| ligne 521 | 2026-09-30 | date invalide, elle cotient un x | ouvert

## B4 - <P4 Q3>

Test en échec : test_d4_aucune_alerte_de_depassement_seuil_requete
Attendu / recu : ["alerte"] = True / ["alerte] = False
Fonction visée : d4_pic_trafic, ligne 161, ligne 164
Cause racine : le parametre fenetre_minutes n'est pas utilisé
