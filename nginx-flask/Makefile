.PHONY: app web
apply: app web
	@kubectl apply -f kubernetes
	@echo ""
	@echo "\033[32mhttp://localhost:3000/movies\033[0m"
delete:
	@kubectl delete -f kubernetes
app:
	@docker image build -t app:latest app
web:
	@docker image build -t web:latest web
