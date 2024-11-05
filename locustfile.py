from locust import HttpUser, TaskSet, task, between

class LinkExtractorRubyBehavior(TaskSet):
    @task(10)
    def extract_links(self):
        urls = [
            "http://localhost:4567/extract?url=https://www.google.com",
            "http://localhost:4567/extract?url=https://www.wikipedia.org",
            "http://localhost:4567/extract?url=https://www.github.com",
            "http://localhost:4567/extract?url=https://www.stackoverflow.com",
            "http://localhost:4567/extract?url=https://www.medium.com",
            "http://localhost:4567/extract?url=https://www.reddit.com",
            "http://localhost:4567/extract?url=https://www.bbc.com",
            "http://localhost:4567/extract?url=https://www.cnn.com",
            "http://localhost:4567/extract?url=https://www.nytimes.com",
            "http://localhost:4567/extract?url=https://www.linkedin.com"
        ]
        for url in urls:
            self.client.get(url)


class LinkExtractorPythonBehavior(TaskSet):
    @task(10)
    def extract_links(self):
        urls = [
            "http://localhost:5000/extract?url=https://www.google.com",
            "http://localhost:5000/extract?url=https://www.wikipedia.org",
            "http://localhost:5000/extract?url=https://www.github.com",
            "http://localhost:5000/extract?url=https://www.stackoverflow.com",
            "http://localhost:5000/extract?url=https://www.medium.com",
            "http://localhost:5000/extract?url=https://www.reddit.com",
            "http://localhost:5000/extract?url=https://www.bbc.com",
            "http://localhost:5000/extract?url=https://www.cnn.com",
            "http://localhost:5000/extract?url=https://www.nytimes.com",
            "http://localhost:5000/extract?url=https://www.linkedin.com"
        ]
        for url in urls:
            self.client.get(url)


class LinkExtractorRubyUser(HttpUser):
    tasks = [LinkExtractorRubyBehavior]
    wait_time = between(1, 2)
    host = "http://localhost:4567"


class LinkExtractorPythonUser(HttpUser):
    tasks = [LinkExtractorPythonBehavior]
    wait_time = between(1, 2)
    host = "http://localhost:5000"
