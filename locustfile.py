from locust import HttpUser, task, between


class DemoUser(HttpUser):
    wait_time = between(1, 3)  # seconds between tasks

    @task(2)
    def get_posts(self):
        # Example public API endpoint
        self.client.get("/posts", name="GET /posts")

    @task(1)
    def get_single_post(self):
        # Get a single resource
        self.client.get("/posts/1", name="GET /posts/1")

    @task(1)
    def create_post(self):
        payload = {"title": "foo", "body": "bar", "userId": 1}
        self.client.post("/posts", json=payload, name="POST /posts")
