.all: dev

.PHONY: dev-setup
dev-setup:
	kubectl config set-context minikube; kubectl apply -f k8s/initial;

.PHONY: dev
dev:
	skaffold dev -p local;

.PHONY: dev-front
dev-front:
	docker build -t dev-watcher ./app/frontend;
	docker run -v `pwd`/app/frontend:/app dev-watcher

.PHONY: dev-full
dev-full:
	bash echo `minikube ip`;

.PHONY: dev-flower
dev-flower:
	minikube service flower-app;