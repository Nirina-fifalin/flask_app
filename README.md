Voici les commandes utiles pour présenter le TP de façon claire et progressive :

---

## 1. Montrer que tout tourne dans Kubernetes

```powershell
# Voir tous les pods
kubectl get pods -n jenkins

# Voir les services
kubectl get service -n jenkins

# Voir les déploiements
kubectl get deployment -n jenkins
```

---

## 2. Montrer le pipeline Jenkins

```powershell
# Ouvrir Jenkins dans le navigateur
minikube service jenkins -n jenkins
```

Montrez dans l'interface :
- Le pipeline `flask_app`
- Les stages : **Test** OK → **Build** OK → **Deploy** OK
- Les logs de chaque stage

---

## 3. Montrer l'application déployée

```powershell
# Accéder à l'application Flask
minikube service pythontest -n jenkins
```

Montrez dans le navigateur :
- `http://127.0.0.1:XXXXX` → `Hello World!`
- `http://127.0.0.1:XXXXX/hello/` → `Hello World!`
- `http://127.0.0.1:XXXXX/hello/VotreNom` → `Hello VotreNom!`

---

## 4. Montrer le déclenchement automatique (pollSCM)

```powershell
# Faites une modification dans app.py ou test.py
# puis poussez
git add .
git commit -m "Test declenchement automatique"
git push
```

Attendez 1 minute et montrez que Jenkins lance automatiquement un nouveau build.

---

## 5. Montrer l'image dans le registry local

```powershell
# Lister les images dans le registry
curl http://192.168.49.1:4000/v2/_catalog

# Voir les tags de l'image
curl http://192.168.49.1:4000/v2/pythontest/tags/list
```

---

## 6. Montrer les détails du pod déployé

```powershell
# Détails du pod pythontest
kubectl describe pod -l app=pythontest -n jenkins

# Logs de l'application
kubectl logs -l app=pythontest -n jenkins
```

---

## Ordre conseillé pour la présentation

```
1. Expliquez l'architecture (GitHub → Jenkins → Docker → Kubernetes)
2. Montrez les codes (Jenkinsfile, app.py, test.py, Dockerfile)
3. Montrez Jenkins et le pipeline SUCCESS
4. Montrez l'application qui tourne dans le navigateur
5. Faites un push en live et montrez le déclenchement automatique
```
