up:
	sudo docker compose -f docker-compose.develop.yml up -d


down:
	sudo docker compose -f docker-compose.develop.yml down && docker network prune --force