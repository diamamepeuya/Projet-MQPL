from typing import List
from abc import ABC, abstractmethod
import unittest
from datetime import date


# Création des classes
class Membre:
    # Initialisation d'un membre
    def __init__(self, nom: str, role: str):
        self.nom = nom
        self.role = role


class Equipe:
    # Initialisation d'une équipe
    def __init__(self):
        self.membres = []


   # Creation de la fonction ajoutMembre qui permet d'ajouter un membre sur une équipe
    def ajoutMembre(self, membre: Membre):
        self.membres.append(membre)


class Tache:
    # Initialisation d'une tache
    def __init__(
        self,
        nom: str,
        description: str,
        date_debut:date,
        date_fin:date,
        responsable: Membre,
        statut: str,
        dependances: List["Tache"],):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsable = responsable
        self.statut = statut
        self.dependances = dependances


class Jalon:
    #Initialisation d'un jalon
    def __init__(self, nom: str, date: date):
        self.nom = nom
        self.date = date


class Risque:
    #Initialisation d'un risque
    def __init__(self, description: str, probabilite:float, impact: str):
        self.description = description
        self.probabilite = probabilite
        self.impact = impact


class Changement:
    #Initialisation d'un changement
    def __init__(self, description: str, version:float, date: date):
        self.description = description
        self.version = version
        self.date = date


# Gestion des Notifications

# Creation de classes abstraites
class NotificationStrategy(ABC):
    # Creation de methode abstraite
    @abstractmethod
    def envoyer(self, message: str, membre: Membre):
        pass


# Création des classes EmailNotificationStrategy et SMSNotificationStrategy
# pour envouyer des notifications aux menmbres
class EmailNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, membre: Membre):
        print(f"Notification envoyée à {membre.nom} par email: {message}")


class SMSNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, membre: Membre):
        print(f"Notification envoyée à {membre.nom} par SMS: {message}")


class NotificationContext:
    def __init__(self, strategie: NotificationStrategy):
        self._strategie = strategie


    def changer_strategie(self, strategie: NotificationStrategy):
        self._strategie = strategie


    def notifier(self, message: str, membre: Membre):
        self._strategie.envoyer(message, membre)


# Intégration des notifications dans la classe Projet

class Projet:
    # Initialisation de Projet
    def __init__(self, nom: str, description: str, date_debut: date, date_fin: date, budget: float):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.budget = budget
        self.taches = []
        self.equipe = Equipe()
        self.risques = []
        self.jalons = []
        self.changements = []
        self.notification = NotificationContext(EmailNotificationStrategy())


   # Fonction qui permet d'ajouter des taches
    def ajoutTache(self, tache: Tache):
        self.taches.append(tache)
        for membre in self.equipe.membres:
            self.notification.notifier(f"Nouvelle tâche ajoutée: {tache.nom}", membre)


  #Fonction qui permet d'ajouter un membre
    def ajoutMembre(self, membre: Membre):
        self.equipe.ajoutMembre(membre)
        self.notification.notifier(f"{membre.nom} a été ajouté à l'équipe", membre)


    # Fonction qui permet d'ajouter un membre
    def ajoutRisque(self, risque: Risque):
        self.risques.append(risque)
        for membre in self.equipe.membres:
            self.notification.notifier(
                f"Nouveau risque ajouté: {risque.description}", membre
            )


    # Fonction qui permet d'ajouter un jalon
    def ajoutJalon(self, jalon: Jalon):
        self.jalons.append(jalon)
        for membre in self.equipe.membres:
            self.notification.notifier(f"Nouveau jalon ajouté: {jalon.nom}", membre)


    # Fonction qui permet d'enregistrer un changement
    def enregistrerChangement(self, changement: Changement):
        self.changements.append(changement)
        for membre in self.equipe.membres:
            self.notification.notifier(
                f"Changement enregistré: {changement.description} "
                f"(version {changement.version})",
                membre,
            )

    # Fonction qui permet de generer un rapport
    def genererRapport(self):
        rapport = f"Rapport d'activités du Projet '{self.nom}' :\n"
        rapport += (
            f"Version: {self.changements[-1].version if self.changements else 1}\n"
        )
        rapport += f"Dates: {self.date_debut} à {self.date_fin}\n"
        rapport += f"Budget: {self.budget} Unité Monétaire\n"
        rapport += "Équipe:\n"
        for membre in self.equipe.membres:
            rapport += f"* {membre.nom} ({membre.role})\n"
        rapport += "Tâches:\n"
        for tache in self.taches:
            rapport += (f"- {tache.nom} ({tache.date_debut} à {tache.date_fin}), "
                        f"Responsable: {tache.responsable.nom}, Statut: {tache.statut}\n")
        rapport += "Jalons:\n"
        for jalon in self.jalons:
            rapport += f"- {jalon.nom} ({jalon.date})\n"
        rapport += "Risques:\n"
        for risque in self.risques:
            rapport += (f"- {risque.description} (Probabilité: {risque.probabilite}, "
                        f"Impact: {risque.impact})\n")

        return rapport





