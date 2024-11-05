from locust import HttpUser, TaskSet, task, between

class LinkExtractorRubyBehavior(TaskSet):
    @task(10)
    def extract_links(self):
        urls = [
            # "http://localhost/?url=https%3A%2F%2Fwww.google.com",
            "http://localhost/?url=https%3A%2F%2Fwww.wikipedia.org",
            "http://localhost/?url=https%3A%2F%2Fwww.github.com",
            "http://localhost/?url=https%3A%2F%2Fwww.stackoverflow.com",
            "http://localhost/?url=https%3A%2F%2Fwww.medium.com",
            "http://localhost/?url=https%3A%2F%2Fwww.reddit.com",
            "http://localhost/?url=https%3A%2F%2Fwww.bbc.com",
            "http://localhost/?url=https%3A%2F%2Fwww.cnn.com",
            "http://localhost/?url=https%3A%2F%2Fwww.nytimes.com",
            "http://localhost/?url=https%3A%2F%2Fwww.linkedin.com"
        ]
        for url in urls:
            self.client.get(url)


# class LinkExtractorPythonBehavior(TaskSet):
#     @task(10)
#     def extract_links(self):
#         urls = [
#             "http://localhost/?url=https%3A%2F%2Fwww.google.com",
#             "http://localhost/?url=https%3A%2F%2Fwww.wikipedia.org",
#             "http://localhost/?url=https%3A%2F%2Fwww.github.com",
#             "http://localhost/?url=https%3A%2F%2Fwww.stackoverflow.com",
#             "http://localhost/?url=https%3A%2F%2Fwww.medium.com",
#             "http://localhost/?url=https%3A%2F%2Fwww.reddit.com",
#             "http://localhost/?url=https%3A%2F%2Fwww.bbc.com",
#             "http://localhost/?url=https%3A%2F%2Fwww.cnn.com",
#             "http://localhost/?url=https%3A%2F%2Fwww.nytimes.com",
#             "http://localhost/?url=https%3A%2F%2Fwww.linkedin.com"
#         ]
#         for url in urls:
#             self.client.get(url)


class LinkExtractorRubyUser(HttpUser):
    tasks = [LinkExtractorRubyBehavior]
    wait_time = between(1, 2)
    host = "http://localhost:4567"


# class LinkExtractorPythonUser(HttpUser):
#     tasks = [LinkExtractorPythonBehavior]
#     wait_time = between(1, 2)
#     host = "http://localhost:5000"
