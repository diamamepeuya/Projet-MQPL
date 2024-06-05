import unittest
from datetime import date
from main import Projet, Membre, Tache, Risque, Jalon, Changement

# Cette partie nous permet de faire des tests et voir la performance de notre code
class Test(unittest.TestCase):
    # Créer des instances
    def setUp(self):
        self.projet = Projet(
            "Nouveau Produit",
            "Description du projet",
            date(2024, 1, 1),
            date(2024, 12, 31),
            50000,
        )
        self.membre1 = Membre("Modou", "Chef de projet")
        self.membre2 = Membre("Christian", "Développeur")
        self.projet.ajoutMembre(self.membre1)
        self.projet.ajoutMembre(self.membre2)
        self.tache1 = Tache(
            "Analyse des besoins",
            "Description",
            date(2024, 1, 1),
            date(2024, 1, 31),
            self.membre1,
            "Terminée",
            [],
        )
        self.tache2 = Tache(
            "Développement",
            "Description",
            date(2024, 2, 1),
            date(2024, 6, 30),
            self.membre2,
            "Non démarrée",
            [self.tache1],
        )
        self.projet.ajoutTache(self.tache1)
        self.projet.ajoutTache(self.tache2)
        self.jalon1 = Jalon("Phase 1 terminée", date(2024, 1, 31))
        self.projet.ajoutJalon(self.jalon1)
        self.risque1 = Risque("Retard de Livraison", 0.3, "Élevé")
        self.projet.ajoutRisque(self.risque1)
        self.changement1 = Changement(
            "Changement de la portée du projet", 2, date(2024, 2, 15)
        )
        self.projet.enregistrerChangement(self.changement1)


    #Test de la fonction AjoutMembre
    def testAjouterMembre(self):
        self.assertEqual(len(self.projet.equipe.membres), 2)

    # Test de la fonction AjoutTache
    def testAjouterTache(self):
        self.assertEqual(len(self.projet.taches), 2)

    # Test de la fonction AjoutRisque
    def testAjouterRisque(self):
        self.assertEqual(len(self.projet.risques), 1)

    # Test de la fonction AjoutJalon
    def testAjouterJalon(self):
        self.assertEqual(len(self.projet.jalons), 1)

    # Test de la fonction EnregistrerChangement
    def testEnregistrerChangement(self):
        self.assertEqual(len(self.projet.changements), 1)

    # Test de la fonction GenererRapport
    def testGenererRapport(self):
        rapport = self.projet.genererRapport()
        self.assertIn("Rapport d'activités du Projet 'Nouveau Produit'", rapport)
        print(rapport)


if __name__ == "__main__":
    unittest.main()
