from locust import HttpUser, task

class BookEndpoint(HttpUser):
    @task
    def load_test_book_endpoint(self):
        self.client.get("/book/")