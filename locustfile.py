from locust import HttpUser, task, between, LoadTestShape


class DemoUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def get_posts(self):
        self.client.get("/posts", name="GET /posts")

    @task(1)
    def get_single_post(self):
        self.client.get("/posts/1", name="GET /posts/1")

    @task(1)
    def create_post(self):
        payload = {"title": "foo", "body": "bar", "userId": 1}
        self.client.post("/posts", json=payload, name="POST /posts")


# Custom load shape: gradual ramp-up, steady load, then ramp-down
class StagedLoadShape(LoadTestShape):
    stages = [
        {"duration": 30, "users": 5, "spawn_rate": 1},  # ramp up to 5 users
        {"duration": 60, "users": 10, "spawn_rate": 2},  # ramp up to 10 users
        {"duration": 90, "users": 10, "spawn_rate": 0},  # hold steady
        {"duration": 120, "users": 0, "spawn_rate": 2},  # ramp down
    ]

    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                return stage["users"], stage["spawn_rate"]
        return None
