from locust import HttpUser, task, between

class LinkExtractorUser(HttpUser):
    wait_time = between(1, 2)  # Tempo de espera entre as requisições 

    @task
    def extract_links(self):
        url = "http://localhost:5000/extract?url=http://example.com"  # Endereço do serviço Link Extractor
        self.client.get(url)
