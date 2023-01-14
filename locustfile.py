from locust import HttpUser, task

class BookEndpoint(HttpUser):
    @task
    def spring_test(self):
        self.client.get("/book/")