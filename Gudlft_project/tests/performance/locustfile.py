from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def index(self):
        self.client.get("/")
    
    @task
    def showSummary(self):
        self.client.post("/showSummary", {"email": "locutusclan@locutusclan.com"})
    
    @task
    def pointsDisplay(self):
        self.client.get("/pointsDisplay")
    
    @task
    def purchasePlaces(self):
        self.client.post("/purchasePlaces", {
            "club": "locutus clan",
            "competition": "Borg clash",
            "places": "5"
        })