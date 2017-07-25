# MEPLA

Ce document considère pour acquis les points suivants : 

* Vous possédez une Raspberry Pi 3 sur laquelle est installée la version 16.04 de Ubuntu
* Vous possédez une connexion internet pour aller chercher les paquets 
* Vous avez cloné la gconf sur la raspberry (`git clone /media/STORE\ N\ GO/Git-repo/ROS-MEPLA-2 ROS-WS-MEPLA-2`)

### Installation
Dans le cas où le script d'installation ne fonctionne pas, voici la marche à suivre. 
Vous pouvez aussi lire le script effectuer les étapes vous-même

1. Installer `ros-kinetic-desktop`
2. Installer les packages ros nécéssaires
```
ros-kinetic-pid
ros-kinetic-nmea-navsat-drivers
```
3. Installer pyqtgraph
4. Initialiser le workspace ROS en se plaçant dans src et en tapant la commande `catkin_init_workspace`
5. Afin de faciliter l'utilisation, créer un alias dans le fichier `.bashrc` en y ajoutant cette ligne
`alias ros_make="catkin_make && chmod -R u+x . && source devel/setup.bash"`

### Utilisation

###### En local sur la raspberry
Afin de tester avec un écran, un clavier et une souris sur la raspberry

1. Se déplacer dans le workspace ROS de MEPLA (habituellement `cd ~/ROS-WS-MEPLA-2`)
2. lancer `ros_make` ou `source devel/setup.bash` afin d'initialiser les variables système
3. lancer `roslaunch mepla_ai mepla_1.launch`

###### Par une connexion ssh 

1. Connecter la Rasperry et un pc distant sur le même réseau (wifi ou Ethernet)
2. Récupérer l'adresse ip de la raspberry sur ce réseau (habituellement avec la commande `ifconfig`)
3. Se connecter par ssh
Sous Windows on peut utiliser l'utilitaire putty en y indiquant l'adresse ip de la raspberry
Sous Linux on utilise une fenêtre de commande. Lancer `ssh usv@$adresseipdelaraspberry`.
4. Un mot de passe est alors demandé. C'est "drome07"
5. Répéter les étapes de l'utilisation en local.

###### Les différentes configurations de lancement
ROS utilise un fichier xml pour la configuration des agents lancés au démarrage. 
Pour lancer : 

 - uniquement les drivers : `roslaunch kayakmepla_hardware_drivers drivers.launch`
 - uniquement la simulation : `roslaunch kayakmepla_hardware_drivers simu.launch`
 - tout le package hardware : `roslaunch kayakmepla_hardware_drivers kayakmepla_hardware.launch`
 - uniquement une node (ou agent) : `rosrun packagename nodename`

Pour modifier : 
 - les pid : utiliser la reconfiguration dynamique avec `rosrun dynamic_reconfigure dynamic_reconfigure` ou modifier les valeurs au démarage dans core.launch
 - si on lance la simulation ou pas : modifier kayak_hardware.launch en commentant ou décommentant la ligne qui 'include' le simu.launch

### Debug
Pour debugger on utilise habituellement `rqt` sur la raspberry ou sur un ordi distant connecté au même réseau.
Pour le faire sur un pc distant il suffit d'ajouter en variable système l'url du serveur http de ros comme ceci : `ROS_MASTER_URI=http://adresseip:11311`; et de lancer `rqt`. Cet ordi doit avoir ros installé, donc c'est forcément un pc linux.

RQT est une interface graphique qui possède de nombreux plugins. Les plus utiles sont : 

 - __node_graph__ : trace un diagramme des interactions entre les nodes. Peut se lancer indépendemment par la commande `rqt_graph`
 - __topic monitor__ : permet de savoir quelles sont les informations qui transitenten temps réel
 - __rqt_plot__ : permet de tracer une donnée numérique du système en fonction du temps. Il est aussi possible de le lancer indépendamment en lançant la commande `rqt_plot`
 - __message publisher__ : pour injecter des données manuellement dans le système. Il suffit de spécifier le topic et la donnée.
