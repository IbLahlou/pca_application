## Partie Technique 

PyQt5 est utilisé pour créer une interface graphique pour une application de bureau qui utilise l'ACP pour réduire la dimensionnalité des données en utilisant des widgets tels que QMainWindow, QPushButton, QLabel et QGraphicsView. Pandas est utilisé pour lire et stocker les données dans un DataFrame, et Matplotlib est utilisé pour créer un nuage de points des données après l'analyse PCA. L'ACP est utilisée pour faciliter la visualisation et l'analyse des données, ainsi que réduire le coût de calcul des algorithmes d'apprentissage automatique.


## Partie Théorique

Pour comprendre mieux le processus du PCA en white-box 

 1.  calculer la matrice de covariance 

    - On peut aussi extraire le coefficient de correlation pour savoir comment les données se corrèle entre eux
    - On pourra calculer l'inertie total pour optimiser le modèle afin d'avoir une projection compatible avec la réalité

$$cov(\hat{X^{i},X^{j}})=/frac{<x^{i},x^{j}>}{\norm{X^{i}}\norm{X^{j}}}$$

2. Calculer les vecteurs et les valeurs propres
    - Avec la réduction de la matrice covariance on trouvera des indicateurs qui nous fourniront des informations sur les axes et la directions des données .

3. Trier les vecteurs et les valeurs propres en ordre décroissant

    - On obtiendra par la suite un visuel pour avoir en tête ce qu'on est préviligier a reduire pour garder un bon pourcentage de conservation d'information 

4. Stocker les n premières composantes principales

    -Aprés avoir trouver les composantes principal on pourra donc
5. Stocker les variances expliquées par chaque composante principale
6. Stocker les pourcentages de variances expliquées par chaque composante principale

> Remarque :
> La réduction de dimension est d’autant plus forte que les variables de départ sont plus corrélées

7. Projeter les données sur les composantes principales

- Comme ça nous interpretant de mieux la façon comment les données se convergent et ainsi pouvoir prendre la bonne décision selon différentes hypothèses


