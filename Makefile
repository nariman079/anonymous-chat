up:
	docker compose -f docker-compose.develop.yml up -d


down:
	docker compose -f docker-compose.develop.yml down && docker network prune --force