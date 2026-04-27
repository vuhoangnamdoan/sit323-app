# SIT323 7.2HD - Scenario 3 (Two-Tier Microservices App)

This project implements a **Cloud-Native Task Monitor** with:
- **Frontend tier**: Nginx + HTML/JS
- **Backend tier**: Python Flask API
- **Service discovery**: frontend reaches backend via Kubernetes service name `backend-service`

---

## 1) What to update first

Replace `DOCKERHUB_USERNAME` in:
- `cloudbuild.yaml`
- `k8s/backend-deployment.yaml`
- `k8s/frontend-deployment.yaml`

---

## 2) Backend API (local check)

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Test endpoint:

```bash
curl http://localhost:5000/tasks
```

---

## 3) Build and push images to Docker Hub manually (fallback when GAR blocked)

```bash
docker login
docker build -t DOCKERHUB_USERNAME/cloud-task-backend:latest ./backend
docker build -t DOCKERHUB_USERNAME/cloud-task-frontend:latest ./frontend
docker push DOCKERHUB_USERNAME/cloud-task-backend:latest
docker push DOCKERHUB_USERNAME/cloud-task-frontend:latest
```

---

## 4) Cloud Build pipeline (push to Docker Hub)

Run from project root:

```bash
gcloud builds submit --config cloudbuild.yaml .
```

If push fails due permissions in Deakin environment, keep logs/screenshots as evidence and continue with manual Docker Hub push.

---

## 5) Deploy to GKE

```bash
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml
```

Check resources:

```bash
kubectl get pods
kubectl get svc
```

Get external IP of `frontend-service`, then open it in browser.
Click **Fetch System Tasks** to verify frontend-backend communication.

---

## 6) What to capture for 7.2HD submission

- Architecture diagram (frontend -> backend-service -> backend pod)
- Docker Hub repositories showing both images
- `kubectl get pods` and `kubectl get svc` screenshots
- Frontend browser screenshot showing returned JSON task list
- Cloud Build logs (success or permission-failure evidence + explanation)
